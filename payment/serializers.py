from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from payment.models import Payment
from payment.services.serializers import create_sessions, create_price, create_product
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    # lesson_count = serializers.SerializerMethodField()
    # user_pay = serializers.SerializerMethodField(read_only=True)

    # user_payment = UserSerializer(source='lesson_set.all', read_only=True, many=True)

    # def get_user_pay(self, obj):
    # return UserPaymentDetailSerializer(User.objects.filter(email=obj.user), many=True).data

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):
    """Создание платежа и отправка ссылки на оплату"""
    url_stripe = serializers.SerializerMethodField()

    def get_url_stripe(self, obj):
        id_product = create_product(obj)
        price = create_price(amount=obj.course.amount, id_product=id_product)
        return create_sessions(price)

    class Meta:
        model = Payment
        fields = ('id', 'sum_of_pay', 'way_of_pay', 'course', 'user', 'url_stripe',)


class PaymentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentUserSerializer(serializers.ModelSerializer):
    # user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
