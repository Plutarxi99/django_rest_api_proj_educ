from rest_framework import serializers

from education.models import Payment
from users.models import User
from users.serializer import UserSerializer, UserPaymentDetailSerializer


class PaymentSerializer(serializers.ModelSerializer):
    # lesson_count = serializers.SerializerMethodField()
    user_pay = serializers.SerializerMethodField(read_only=True)

    # user_payment = UserSerializer(source='lesson_set.all', read_only=True, many=True)

    def get_user_pay(self, obj):
        return UserPaymentDetailSerializer(User.objects.filter(email=obj.user), many=True).data

    class Meta:
        model = Payment
        fields = '__all__'


