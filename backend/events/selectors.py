from django_filters import rest_framework as filters

from events.models import Event


class EventsFilter(filters.FilterSet):

    address = filters.CharFilter(field_name='address__city', lookup_expr='icontains')
    topic = filters.CharFilter(field_name='topics__title', lookup_expr='icontains')
    dos = filters.DateTimeFilter(field_name='dos', lookup_expr='gte')
    doe = filters.DateTimeFilter(field_name='doe', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ('address', 'topic', 'dos', 'doe')
