from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson
from education.serializers.lesson import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    count_lesson = serializers.IntegerField(source='lesson.all.count', read_only=True)

    class Meta:
        model = Course
        # fields = '__all__'
        exclude = ('picture', 'id', 'description',)


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_this_course = SerializerMethodField()

    # def get_lesson_this_course(self, course):
    #     return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_lesson_this_course(self, course):
        return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'
