from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/', UserListAPIView.as_view(), name='user_list'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]
