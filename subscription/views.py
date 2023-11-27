from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from subscription.models import Subscription
from subscription.serializers import SubsSerializer


class SubsCreateAPIView(CreateAPIView):
    serializer_class = SubsSerializer


class SubsListAPIView(ListAPIView):
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsUpdateAPIView(UpdateAPIView):
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsRetrieveAPIView(RetrieveAPIView):
    serializer_class = SubsSerializer
    queryset = Subscription.objects.all()


class SubsDestroyAPIView(DestroyAPIView):
    queryset = Subscription.objects.all()
