from rest_framework.viewsets import ModelViewSet

from education.models import Course
from education.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
