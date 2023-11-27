from django.urls import path

from subscription.apps import SubscriptionConfig
from subscription.views import SubsCreateAPIView, SubsDestroyAPIView, SubsUpdateAPIView, SubsRetrieveAPIView, \
    SubsListAPIView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('', SubsListAPIView.as_view(), name='subs_list'),
    path('create/', SubsCreateAPIView.as_view(), name='subs_create'),
    path('update/<int:pk>/', SubsUpdateAPIView.as_view(), name='subs_update'),
    path('detail/<int:pk>/', SubsRetrieveAPIView.as_view(), name='subs_detail'),
    path('delete/<int:pk>/', SubsDestroyAPIView.as_view(), name='subs_delete'),
]
