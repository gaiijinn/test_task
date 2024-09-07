from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'event'

router = routers.DefaultRouter()
router.register('events', views.EventViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
