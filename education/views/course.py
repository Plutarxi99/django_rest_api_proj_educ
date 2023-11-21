from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from education.models import Course
from education.serializers.course import *


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    # serializer_class = CourseSerializer
    default_serializer = CourseSerializer
    serializer = {
        "list": CourseListSerializer,
        "retrieve": CourseDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(count_lesson=Count("lesson"))
        return super().list(request, *args, **kwargs)
