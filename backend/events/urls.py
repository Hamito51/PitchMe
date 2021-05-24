from rest_framework.routers import DefaultRouter

from events.views import EventViewSet, TopicViewSet

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('topics', TopicViewSet, basename='topic')


urlpatterns = [

]
urlpatterns += router.urls
