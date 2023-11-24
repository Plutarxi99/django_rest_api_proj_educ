from django.urls import path

from users.apps import UsersConfig
from users.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
