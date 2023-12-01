from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Lesson, Course
from education.validators import LinkInVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkInVideoValidator(field='link_to_video')]


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
