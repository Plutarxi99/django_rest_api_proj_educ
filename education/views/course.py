from datetime import timedelta

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from education.paginators import CoursePaginator
from education.permissions import ModeratorOrOwnerCourse
from education.serializers.course import *
from education.services.views import send_mail_subs_users
from education.tasks import check_update_subs


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
        """Для отображения списка всех курсов"""
        self.queryset = self.queryset.annotate(count_lesson=Count("lesson"))
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Для создания курсов"""
        request.data['owner'] = self.request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        """Для отображения одного курса и его состояние подписки, а также уроки"""
        return super().retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        #
        check_update_subs.delay(instance=instance.pk)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def get_queryset(self):
        """
        Определяет, если модератор, то выводит список всех курсов, иначе только принадлежащие владельцу
        """
        # Возвращает значения в соотвествии с его группой или он суперюзер, то показывает все курсы
        # иначе, только те курсы, которым он принадлежит
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_one_of_groups('moderator') or user.is_superuser:
            return queryset
        else:
            return queryset.filter(owner=user.pk)
