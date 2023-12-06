from education.services.views import send_mail_subs_users
from subscription.models import Subscription
from users.models import User

from django_celery_beat.models import PeriodicTask, ClockedSchedule


def back_send_mail(obj):
    """
    Отправка сообщений
    @param obj: словарь значений курса
    @return:
    """
    # Названмия курса
    name_course = obj['name']
    # Получаем <QuerySet [1, 2, 4]> список pk подписок и узнаем в подписках user
    subs = tuple(
        Subscription.course.through.objects.values().filter(course_id=2).values_list('subscription_id', flat=True))
    # Кортеж пользователей (pk), которые подписаны на данный курс
    user_id = tuple(Subscription.objects.filter(id__in=[*subs]).values_list('user', flat=True))
    # Кортеж пользователей (email), которые подписаны на данный курс
    tuple_email = tuple(User.objects.filter(id__in=[*user_id]).values_list('email', flat=True))

    send_mail_subs_users(
        mailing_message_topic=f"Вы подписаны на курс(ы) {name_course}",
        mailing_message_body=f"Успей первым узнать, что изменилось",
        tuple_email=tuple_email,
    )


def time_set(target_time, name_task):
    """
    Создание или обновление переодической задачи для отправки сообщения об обнорвлении курса
    @param target_time: дата отправки
    @param name_task: названия задачи
    @return:
    """
    if not PeriodicTask.objects.filter(name=name_task):
        clocked_schedule = ClockedSchedule.objects.create(clocked_time=target_time)

        PeriodicTask.objects.create(
            clocked=clocked_schedule,
            name=name_task,
            description="Если после обновления курса прошло более 4 часов. Идёт отправка сообщений",
            one_off=True,
            task="education.tasks.send_mail_update_course.add",
        )
    else:
        per_task = PeriodicTask.objects.get(name=name_task) # получения объекта переодической задача
        clocked_schedule = ClockedSchedule.objects.create(clocked_time=target_time) # создания нового объекта модели ClockedSchedule
        per_task.clocked = clocked_schedule # переопределяем новое значения для объекта PeriodicTask
        per_task.save()

