from education.services.views import send_mail_subs_users
from subscription.models import Subscription
from users.models import User


def back_send_mail(obj):
    """
    Отправка сообщений
    @param obj: словарь значений курса
    @return:
    """
    # Названмия курса
    name_course = obj.name
    # Получаем <QuerySet [1, 2, 4]> список pk подписок и узнаем в подписках user
    subs = tuple(
        Subscription.course.through.objects.values().filter(course_id=obj.pk).values_list('subscription_id', flat=True))
    # Кортеж пользователей (pk), которые подписаны на данный курс
    user_id = tuple(Subscription.objects.filter(id__in=[*subs]).values_list('user', flat=True))
    # Кортеж пользователей (email), которые подписаны на данный курс
    tuple_email = tuple(User.objects.filter(id__in=[*user_id]).values_list('email', flat=True))

    smsu = send_mail_subs_users(
        mailing_message_topic=f"Вы подписаны на курс(ы) {name_course}",
        mailing_message_body=f"Успей первым узнать, что изменилось",
        tuple_email=tuple_email,
    )
    return smsu['status']
