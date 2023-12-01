from django.db import models

from config import settings
from config.settings import NULLABLE
from education.models import Course, Lesson


class Payment(models.Model):
    CARD = 'card'
    TRANSLATION = 'translation'

    WAY = [
        (CARD, 'card'),
        (TRANSLATION, 'translation'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='покупатель')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='купил курс', related_name='payment',
                               **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='купил урок', related_name='payment',
                               **NULLABLE)
    sum_of_pay = models.PositiveIntegerField(default=1, verbose_name='сумма оплаты')
    way_of_pay = models.CharField(choices=WAY, verbose_name='способ оплаты', **NULLABLE)

    def save(self, *args, **kwargs):
        """Сохраняет сумму платежа, которую надо внести пользователю"""
        try:
            pay = self.course.amount
        except AttributeError:
            return 'Нельзя' # потом доделать
        self.sum_of_pay = pay
        super(Payment, self).save(*args, **kwargs)