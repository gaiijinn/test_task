from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers
from . import permissions

# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all().select_related('organizer').prefetch_related('guests').order_by('-id')
    serializer_class = serializers.EventListSerializer
    permission_classes = (permissions.CustomEventPermission, )

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

    @action(detail=True, methods=['post'])
    def add_user_as_guest(self, request, pk=None):
        event = self.get_object()

        if event.organizer != self.request.user and self.request.user not in event.guests.all():
            event.guests.add(request.user)
            event.save()

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response({'detail': 'User is either the organizer or a guest'},
                            status=status.HTTP_400_BAD_REQUEST)
