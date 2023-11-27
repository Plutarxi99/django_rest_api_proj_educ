from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator
from subscription.models import Subscription


class SubsSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        validators = [UniqueTogetherValidator(fields=['user'], queryset=Subscription.objects.all())]
