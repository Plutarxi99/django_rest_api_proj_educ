from django.contrib import admin

from education.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', )

