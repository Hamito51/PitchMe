from datetime import datetime

from django.contrib.auth.models import User
from django.db import transaction

from events.models import Event
from information.models import Address


@transaction.atomic
def create_event(event_author: User, title: str, dos: datetime, doe: datetime, address: dict, topics: list = None):
    address = Address(**address)
    address.full_clean()
    address.save()
    event = Event(event_author=event_author, title=title, dos=dos, doe=doe, address=address)
    event.topics.set(topics)
    event.full_clean()
    event.save()
    return event
