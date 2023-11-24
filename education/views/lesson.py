from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from education.models import Lesson, Course
from education.permissions import InModeratorOrOwnerLesson, InModeratorLesson
from education.serializers.course import CourseListSerializer
from education.serializers.lesson import LessonSerializer, LessonListSerializer
from education.services.views import MixinQueryset


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorLesson]


class LessonListAPIView(MixinQueryset, ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(MixinQueryset, RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]


class LessonUpdateAPIView(MixinQueryset, UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, InModeratorOrOwnerLesson]
