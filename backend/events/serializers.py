from rest_framework import serializers

from events.models import Event, Topic
from information.serializers import AddressSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        exclude = ('topic_author', 'uuid')


class EventCreateSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Event
        fields = ('uuid', 'title', 'dos', 'doe', 'address', 'topics')


class EventDetailSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Event
        fields = ('uuid', 'title', 'dos', 'doe', 'address', 'topics')


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('uuid', 'title', 'dos', 'doe')




