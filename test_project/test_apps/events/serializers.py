from rest_framework import serializers
from .models import Event
from ..users.serializers import UserSerializer


class BaseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'time_created', 'date_created')


class EventListSerializer(BaseEventSerializer):
    organizer = UserSerializer(read_only=True)

    class Meta(BaseEventSerializer.Meta):
        fields = BaseEventSerializer.Meta.fields + ('organizer', )


class EventRetrieveSerializer(EventListSerializer):
    guests = UserSerializer(many=True, read_only=True)

    class Meta(EventListSerializer.Meta):
        fields = EventListSerializer.Meta.fields + ("guests", )
