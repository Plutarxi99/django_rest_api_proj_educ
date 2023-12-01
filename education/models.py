from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    picture = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    amount = models.PositiveIntegerField(default=0, verbose_name='цена курса')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner',
                              verbose_name='создатель курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    link_to_video = models.URLField(max_length=200, **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='lesson', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        # order_with_respect_to = "course"


# class Payment(models.Model):
#     CARD = 'card'
#     TRANSLATION = 'translation'
#
#     WAY = [
#         (CARD, 'card'),
#         (TRANSLATION, 'translation'),
#     ]
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
#                              verbose_name='покупатель')
#     date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='купил курс', related_name='payment',
#                                **NULLABLE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='купил урок', related_name='payment',
#                                **NULLABLE)
#     sum_of_pay = models.PositiveIntegerField(verbose_name='сумма оплаты')
#     way_of_pay = models.CharField(choices=WAY, verbose_name='способ оплаты', **NULLABLE)
