# Generated by Django 4.2.7 on 2023-12-04 20:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0012_course_update_at_lesson_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='update_the_last_one',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время прошлого изменения'),
            preserve_default=False,
        ),
    ]