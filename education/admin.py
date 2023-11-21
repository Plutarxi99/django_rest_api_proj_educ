from django.contrib import admin

from education.models import Course, Lesson, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', )
