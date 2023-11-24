from rest_framework.views import APIView

from education.models import Course


class MixinQueryset(APIView):
    def get_queryset(self):
        """
        Определяет, если модератор, то выводит список всех курсов, иначе только принадлежащие владельцу
        """
        queryset = super().get_queryset()
        user = self.request.user
        if user.has_one_of_groups('moderator') or user.is_superuser:
            return queryset
        else:
            id_course = Course.objects.filter(owner=user).values_list('pk', flat=True)
            return queryset.filter(course__in=id_course)