from django.conf import settings
from django.db import models

from config.settings import NULLABLE
from education.models import Course


class Subscription(models.Model):
    course = models.ManyToManyField(Course, related_name='course', verbose_name='подписан на курсы', symmetrical=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                             related_name='user')

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

