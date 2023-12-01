from django.urls import path

from payment.apps import PaymentConfig
from payment.views import *

app_name = PaymentConfig.name
urlpatterns = [
    path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_detail'),
    path('update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),

]
