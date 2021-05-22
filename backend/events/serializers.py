from rest_framework import serializers

from events.models import Event
from information.serializers import AddressSerializer


class EventDetailSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Event
        fields = ('title', 'dos', 'doe', 'address', 'topics')


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'dos', 'doe')
