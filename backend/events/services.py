from datetime import datetime

from django.contrib.auth.models import User
from django.db import transaction

from events.models import Event, Topic
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


@transaction.atomic
def update_event(pk, **kwargs):
    event = Event.objects.get(uuid=pk)
    event.__dict__.update(kwargs)
    topics = kwargs.get('topics')
    event.topics.set(topics)
    event.full_clean()
    event.save()
    return event


def create_topic(topic_author: User, title: str, speaker: str):
    topic = Topic(topic_author=topic_author, title=title, speaker=speaker)
    topic.full_clean()
    topic.save()
    return topic


def update_topic(pk, **kwargs):
    topic = Topic.objects.get(uuid=pk)
    topic.__dict__.update(kwargs)
    topic.full_clean()
    topic.save()
    return topic
