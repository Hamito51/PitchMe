from django.db import models

# Create your models here.
class Address(models.Model):
    STREET_TYPE = [
        ('Улица', 'ул'),
        ('Проспект', 'пр-кт'),
        ('Проезд', 'пр-зд'),
        ('Аллея', 'ал.'),
        ('Бульвар', 'бул.'),
        ('Линия', 'лин.'),
        ('Набережная', 'наб.'),
        ('Площадь', 'пл.'),
        ('Шоссе', 'ш.'),
    ]

    city = models.CharField(max_length=30)
    street_type = models.CharField(max_length=10, choices=STREET_TYPE)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=10)
    flat = models.CharField(max_length=10)