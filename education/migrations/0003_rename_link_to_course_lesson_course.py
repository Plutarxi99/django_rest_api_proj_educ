# Generated by Django 4.2.7 on 2023-11-20 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_lesson_link_to_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='link_to_course',
            new_name='course',
        ),
    ]
