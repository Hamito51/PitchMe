from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=50)
    speaker = models.ForeignKey(User, on_delete=models.PROTECT)


class Event(models.Model):
    title = models.CharField(max_length=50)
    topics = models.ManyToManyField(Topic, null=True, blank=True, verbose_name="темы")
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True, related_name='address', verbose_name="Адрес")
    dos = models.DateTimeField()
    doe = models.DateTimeField()