from datetime import timedelta

from celery import shared_task

from education.models import Course
from education.services.tasks import back_send_mail


@shared_task
def send_mail_update_course():
    """
    Функция проходит по всем курсам
    Если курс обновлялся менее, чем 4 часа, то рассылка не начнется
    Иначе, рассылка начинается и устанавливаем флаг, что отправка успешно отправлена
    @return:
    """
    time_diff = timedelta(hours=4)
    # получение списка объекта курса
    for obj in Course.objects.all():
        # Получаем разницу во времени обновлении
        diff_time_update = obj.update_at - obj.update_the_last_one
        # Если разница больше 4 часов и флаг, что сообщение не отправлялось,
        # то начинается рассылка
        if diff_time_update > time_diff and not obj.is_send_update:
            # отправка сообщение об обновлении
            bsm = back_send_mail(obj)
            # Если отправилось, то устанавливаем флаг, что отправилось
            if bsm:
                # Устанавливаем флаг True, что отправилось и сохраняем объект
                obj.is_send_update = True
                obj.save()
            else:
                pass
        else:
            pass


@shared_task
def check_update_subs(instance: int):
    """
    Создание отложенной задача, при обновлении курса
    идёт запись в переодическую задачу, через 4 часа после обновлении курса
    если ещё раз обновлеся курс, то идёт пересохранения даты отправка
    @param instance:
    @return:
    """
    # получение списка объекта курса
    obj = tuple(Course.objects.filter(pk=instance).values())[0]
    obj['is_send_update'] = False
    obj.save()
