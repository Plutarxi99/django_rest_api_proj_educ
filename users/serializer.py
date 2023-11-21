from rest_framework import serializers

from education.models import Payment
from education.serializers.payment import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRetrieveSerializer(serializers.ModelSerializer):
    payment_user = serializers.SerializerMethodField(read_only=True)

    # def get_payment_user(self, payment):
    #     return [payment.date for payment in Payment.objects.filter(user=5)]
    # def get_lesson_this_course(self, course):
    #     return [lesson.name for lesson in Lesson.objects.filter(course=course)]
    # def get_lesson_this_course(self, course):
    #     return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data
    def get_payment_user(self, payment):
        return PaymentSerializer(Payment.objects.filter(user=payment), many=True).data
    class Meta:
        model = User
        fields = '__all__'
