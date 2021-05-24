from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django_filters import rest_framework as filters
from events.models import Event, Topic
from events.selectors import EventsFilter
from events.serializers import EventDetailSerializer, EventListSerializer, TopicSerializer, EventCreateSerializer, \
    TopicDetailSerializer
from events.services import create_event, create_topic, update_event, update_topic


class EventViewSet(ViewSet, GenericAPIView):

    queryset = Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventsFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return EventCreateSerializer
        if self.action in ('retrieve',):
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

    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        ser = self.get_serializer_class()(event, context={"request": request})
        return Response(ser.data, status=200)

    def update(self, request, pk):
        data = request.data
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        event = update_event(pk, **serializer.validated_data)
        return Response(serializer.data, status=200)


class TopicViewSet(ViewSet, GenericAPIView):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'update', 'retrieve'):
            return TopicDetailSerializer
        if self.action in ('create',):
            return TopicSerializer

    def list(self, request):
        data = request.data
        serializer = self.get_serializer_class()
        topics = self.filter_queryset(self.get_queryset())
        serializer = serializer(topics, many=True)
        return Response(data=serializer.data, status=200)

    def create(self, request):
        data = request.data
        topic_author = request.user
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        val_data = serializer.validated_data
        topic = create_topic(topic_author=topic_author, **val_data)
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk):
        topic = Topic.objects.get(pk=pk)
        serializer = self.get_serializer_class()(topic, context={"request": request})
        return Response(serializer.data, status=200)

    def update(self, request, pk):
        data = request.data
        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        topic = update_topic(pk, **serializer.validated_data)
        return Response(serializer.data, status=200)
