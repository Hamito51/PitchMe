from datetime import datetime

from rest_framework.authtoken.admin import User

from events.models import Event


def create_event(event_author: User, title: str, dos: datetime, doe: datetime, topics: dict = None, address: dict = None):
    event = Event(event_author=event_author, title=title, dos=dos, doe=doe, topics=topics, address=address)
    event.full_clean()
    event.save()
    return event
