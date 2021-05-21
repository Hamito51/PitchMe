from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=40)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    patronymic = models.CharField(max_length=40, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

