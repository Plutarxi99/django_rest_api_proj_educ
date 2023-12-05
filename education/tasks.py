from datetime import timedelta

from celery import shared_task
from celery.app import task

from education.models import Course
from education.services.tasks import back_send_mail


# from education.services.views import send_mail_subs_users
# from subscription.models import Subscription
# from users.models import User

@shared_task
def check_update_subs(instance: int):
    # получение списка объекта курса
    obj = tuple(Course.objects.filter(pk=instance).values())[0]
    # получение разниц дат обновление курса
    delta = obj['update_at'] - obj['update_the_last_one']
    # Если курс изменился менее, чем на 4 часа, то отсылка не отправляется
    if delta > timedelta(hours=4):
        back_send_mail(obj)
        print('Время настало')
    else:
        print('Время не настало')


def check_condition():
    for obj in Course.objects.all():
        # получение списка объекта курса
        obj = tuple(Course.objects.filter(pk=obj.pk).values())[0]
        # получение разниц дат обновление курса
        delta = obj['update_at'] - obj['update_the_last_one']
        # Если курс изменился менее, чем на 4 часа, то отсылка не отправляется
        if delta > timedelta(hours=4):
            back_send_mail(obj)
            print('Время настало')
        else:
            print('Время не настало')

