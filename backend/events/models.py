import uuid as uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from information.models import Address


class Topic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    topic_author = models.ForeignKey(User, on_delete=models.PROTECT)
    speaker = models.CharField(max_length=100, null=True, blank=True)


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    event_author = models.ForeignKey(User, on_delete=models.PROTECT)
    topics = models.ManyToManyField(Topic, null=True, blank=True, verbose_name="Темы")
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True, related_name='address', verbose_name="Адрес")
    dos = models.DateTimeField()
    doe = models.DateTimeField()
