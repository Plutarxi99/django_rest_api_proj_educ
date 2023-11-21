from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views.course import *
from education.views.lesson import *
from education.views.payment import *

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
                  path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  # payment
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
                  path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
                  path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_detail'),
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
                  path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_delete'),
              ] + router.urls
