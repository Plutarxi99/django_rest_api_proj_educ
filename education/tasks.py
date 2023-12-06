from datetime import timedelta

from celery import shared_task

from education.models import Course
from education.services.tasks import back_send_mail, time_set


@shared_task
def send_mail_update_course():
    """
    Массовая рассылка для подписантов этого курса
    и отправка сообщений
    @return:
    """
    for obj in Course.objects.all():
        # получение списка объекта курса
        obj = tuple(Course.objects.filter(pk=obj.pk).values())[0]
        back_send_mail(obj)
        print('Время настало')


@shared_task
def check_update_subs(instance: int):
    """
    Создание отложенной задача, при обновлении курса
    идёт запись в переодическую задачу, через 4 часа после обновлении курса
    если ещё раз обновлеся курс, то идёт пересохранения даты отправка
    @param instance:
    @return:
    """
    time_diff = timedelta(hours=4)
    # получение списка объекта курса
    obj = tuple(Course.objects.filter(pk=instance).values())[0]
    # Время отправки сообщений
    target_time = obj['update_at'] + time_diff
    # делается переодическая задача на отправку сообщений через 4 часа
    time_set(target_time=target_time, name_task="send-mail-update-course")

