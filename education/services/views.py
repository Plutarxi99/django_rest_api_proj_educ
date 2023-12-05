from config.settings import SERVER_EMAIL
from django.core.mail import send_mass_mail
from rest_framework.views import APIView

from education.models import Course


def send_mail_subs_users(
        mailing_message_topic: str,
        mailing_message_body: str,
        tuple_email: tuple
) -> dict:
    """
    Функция для отправки писем
    @param mailing_message_topic: тема сообщения
    @param mailing_message_body: тело сообщения
    @param tuple_email: кортеж клиентов, которым отправятся рассылка
    """
    message = (
        mailing_message_topic,
        mailing_message_body,
        SERVER_EMAIL,
        tuple_email,
    )
    try:
        send_mass_mail((message,), fail_silently=False)
        return {'status': True, 'response': "Сервер отработал как надо"}
    except BaseException as error:
        return {'status': False, 'response': error}


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
