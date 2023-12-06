from datetime import timedelta

from celery import shared_task
from celery.app import task

from users.models import User
from django.utils import timezone
import calendar
from django.utils.timezone import now


@shared_task
def check_last_login():
    """
    Если пользователь не заходил больше месяца, то его блокируют
    @return:
    """
    end_date = timezone.now()
    # Получение дней в месяце
    days_in_month = calendar.monthrange(
        year=now().year, month=now().month
    )[1]
    start_date = end_date - timedelta(days=days_in_month)
    # users = User.objects.filter(last_login__range=(start_date, end_date)).values_list('pk', flat=True)
    users = User.objects.filter(last_login__date__lte=start_date)
    for user in users:
        user.is_active = False
        print(user.is_active)
        user.save()
    return 'Пользователи, которые заходили больше месяца назад. Успешно заблокированы'