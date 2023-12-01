from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentCreateSerializer, PaymentUpdateSerializer
from rest_framework import status



class PaymentCreateAPIView(CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentListAPIView(ListAPIView):
    """Список платежей"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'way_of_pay']
    ordering_fields = ['date']
    permission_classes = [IsAuthenticated]


class PaymentRetrieveAPIView(RetrieveAPIView):
    """Детали платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentUpdateAPIView(UpdateAPIView):
    """Изменение деталей платежа"""
    queryset = Payment.objects.all()
    serializer_class = PaymentUpdateSerializer
    permission_classes = [IsAuthenticated]


class PaymentDestroyAPIView(DestroyAPIView):
    """Удаление платежа"""
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


