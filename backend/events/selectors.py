from django_filters import rest_framework as filters
from events.models import Event


class EventsFilter(filters.FilterSet):
    """Фильтры событий: city - по городу, проведения события, topic: по темам, которые будут в рамках события
    start - началльная дата события, end - конечная дата события"""
    city = filters.CharFilter(field_name='address__city', lookup_expr='icontains')
    topic = filters.CharFilter(field_name='topics__title', lookup_expr='icontains', distinct=True)
    start = filters.DateTimeFilter(field_name='dos', lookup_expr='gte')
    end = filters.DateTimeFilter(field_name='doe', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ('city', 'topic', 'start', 'end')


