from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    picture = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)

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

    link_to_course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
