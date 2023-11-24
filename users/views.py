from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializer import UserSerializer, UserRetrieveSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsAuthenticated]
    default_serializer = UserRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user = self.request.user
        if user == instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(instance)
            email = serializer.data['email']
            last_name = serializer.data['last_name']
            return Response(email, last_name)


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
