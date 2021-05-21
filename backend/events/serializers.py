from rest_framework import serializers

from events.models import Event


class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'dos', 'doe')
