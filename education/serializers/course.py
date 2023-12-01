from django.db.models import Count
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson
from payment.models import Payment
from education.serializers.lesson import LessonListSerializer, LessonSerializer
from subscription.models import Subscription
from subscription.serializers import SubsSerializer
from users.services import MixinGetUser


class CourseSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор для вывода всех курсов """
    class Meta:
        model = Course
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    """ Сериализатор для вывода списка курсов """
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonListSerializer(source='lesson', read_only=True, many=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    class Meta:
        model = Course
        fields = '__all__'



class CourseDetailSerializer(MixinGetUser, serializers.ModelSerializer):
    lessons = LessonListSerializer(source='lesson', read_only=True, many=True)
    is_subs = serializers.SerializerMethodField()

    def get_is_subs(self, obj):
        """
        Получение курсов из подписки и если есть курсы в подписке, то в поле подписки выводится подписан
        """
        user = self._user()['pk']
        list_subs_course = list(Subscription.objects.filter(user=user).values_list('course', flat=True))
        if obj.pk in list_subs_course:
            return 'Подписан'
        else:
            return 'Не подписан'

    class Meta:
        model = Course
        fields = '__all__'
