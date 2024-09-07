from django.contrib.auth import get_user_model
from rest_framework import viewsets
from . import serializers

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all().order_by('-id')
