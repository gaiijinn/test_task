from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

app_name = 'users'

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
