from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from events.models import Event
from events.selectors import EventsFilter
from events.serializers import EventDetailSerializer, EventListSerializer
from events.services import create_event


class EventViewSet(ViewSet, GenericAPIView):

    queryset = Event.objects.all()
    filter_backends = (EventsFilter,)

    def get_serializer_class(self):
        if self.action in ('retrieve', 'create', 'update'):
            return EventDetailSerializer
        if self.action in ('list',):
            return EventListSerializer

    def list(self, request):
        data = request.data
        serializer = self.get_serializer_class()
        events = self.filter_queryset(self.get_queryset())
        serializer = serializer(events, many=True)
        return Response(data=serializer.data, status=200)

    def create(self, request):
        data = request.data
        event_author = request.user
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        val_data = serializer.validated_data

        event = create_event(event_author=event_author, **val_data)
        return Response(serializer.data, status=201)

