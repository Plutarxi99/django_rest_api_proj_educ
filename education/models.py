from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    picture = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    amount = models.PositiveIntegerField(default=0, verbose_name='цена курса')
    update_the_last_one = models.DateTimeField(verbose_name='время прошлого изменения', **NULLABLE)
    update_at = models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner',
                              verbose_name='создатель курса')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Если объект модели изменяется, то идет запись изменения
        update_the_last_one: это поле обновление записывает предпоследнюю дату изменeния курса
        update_at: это поле последнего изменения
        """
        self.update_the_last_one = self.update_at
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    picture = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    link_to_video = models.URLField(max_length=200, **NULLABLE)
    update_at = models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='lesson', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        # order_with_respect_to = "course"
