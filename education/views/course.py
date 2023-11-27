from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from education.models import Course
from education.paginators import CoursePaginator
from education.permissions import ModeratorOrOwnerCourse
from education.serializers.course import *


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    serializer = {
        "list": CourseListSerializer,
        "retrieve": CourseDetailSerializer,
    }
    permission_classes = [IsAuthenticated, ModeratorOrOwnerCourse]
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        return self.serializer.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(count_lesson=Count("lesson"))
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = self.request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        """
        Определяет, если модератор, то выводит список всех курсов, иначе только принадлежащие владельцу
        """
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_one_of_groups('moderator') or user.is_superuser:
            return queryset
        else:
            return queryset.filter(owner=user.pk)


