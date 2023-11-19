from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


from users.models import User
from users.serializer import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        self.object = super().get_object()
        self.object = self.request.user
        return self.object


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
