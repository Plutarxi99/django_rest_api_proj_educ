from rest_framework import serializers

from education.models import Payment
from education.serializers.payment import PaymentUserSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRetrieveSerializer(serializers.ModelSerializer):
    user_pay = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        # Не передавайте аргумент 'fields' в суперкласс
        fields = kwargs.pop('fields', None)

        # Создайте экземпляр суперкласса обычным образом
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Удалите все поля, которые не указаны в аргументе `fields`.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def get_user_pay(self, obj):
        return PaymentUserSerializer(Payment.objects.filter(user=obj.id), many=True).data

    def _user(self):
        """
        Получение авторизированного пользователя, который делает запрос
        """
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return user

    def to_representation(self, instance):
        """Если пользователь обращается к своему профилю, то информация ограничивается"""
        ret = super().to_representation(instance)
        if self._user() == instance:
            return ret
        else:
            ret.pop('password')
            ret.pop('last_name')
            ret.pop('user_pay')
            return ret

    class Meta:
        model = User
        fields = '__all__'

# class UserPaymentDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
