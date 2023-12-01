from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from education.models import Lesson, Course
from education.paginators import LessonPaginator
from education.permissions import InModeratorOrOwnerLesson, InModeratorLesson
from education.serializers.course import CourseListSerializer
from education.serializers.lesson import LessonSerializer, LessonListSerializer
from education.services.views import MixinQueryset


class LessonCreateAPIView(CreateAPIView):
    """ Создание урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorLesson]



class LessonListAPIView(MixinQueryset, ListAPIView):
    """ Отображение списка уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(MixinQueryset, RetrieveAPIView):
    """ Отображение одного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]


class LessonUpdateAPIView(MixinQueryset, UpdateAPIView):
    """ Обновление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]


class LessonDestroyAPIView(DestroyAPIView):
    """ Удаление урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]
