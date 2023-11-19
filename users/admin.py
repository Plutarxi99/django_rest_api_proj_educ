from django.contrib import admin

from users.models import User


@admin.register(User)
class AdminManager(admin.ModelAdmin):
    list_display = ['email', ]
