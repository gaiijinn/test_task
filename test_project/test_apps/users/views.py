from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions
from . import serializers

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class UserCreating(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserCreatingSerializer
    permission_classes = (permissions.AllowAny, )
