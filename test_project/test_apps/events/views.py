from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all().select_related('organizer').prefetch_related('guests').order_by('-id')
    serializer_class = serializers.EventListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.EventRetrieveSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=False)
    def get_created_event(self, request):
        self.serializer_class = serializers.BaseEventSerializer

        events = self.queryset.filter(organizer=request.user)

        serializer = self.serializer_class(events, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def get_pinned_events(self, request):
        self.serializer_class = serializers.BaseEventSerializer

        events = self.queryset.filter(guests=request.user)
        serializer = self.serializer_class(events, many=True)
        return Response(serializer.data)
