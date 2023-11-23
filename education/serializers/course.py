from django.db.models import Count
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson, Payment
from education.serializers.lesson import LessonListSerializer, LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonListSerializer(source='lesson', read_only=True, many=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonListSerializer(source='lesson', read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'
