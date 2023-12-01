from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from subscription.models import Subscription
from subscription.serializers import SubsSerializer


class SubsCreateAPIView(CreateAPIView):
    """Создание подписки"""
    serializer_class = SubsSerializer


class SubsListAPIView(ListAPIView):
    """Список подписок"""
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsUpdateAPIView(UpdateAPIView):
    """Обновление подписки"""
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsRetrieveAPIView(RetrieveAPIView):
    """Детали подписки"""
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsDestroyAPIView(DestroyAPIView):
    """Удаление подписки"""
    queryset = Subscription.objects.all()
