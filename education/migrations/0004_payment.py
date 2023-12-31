# Generated by Django 4.2.7 on 2023-11-20 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0003_rename_link_to_course_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('what_pay', models.CharField(blank=True, choices=[('course', 'course'), ('lesson', 'lesson')], null=True, verbose_name='что купил')),
                ('sum_of_pay', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('way_of_pay', models.CharField(blank=True, choices=[('card', 'card'), ('translation', 'translation')], null=True, verbose_name='способ оплаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель рассылки')),
            ],
        ),
    ]
