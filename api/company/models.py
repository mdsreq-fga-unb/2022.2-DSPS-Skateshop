from django.db import models
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(max_length=64)
    insta = models.CharField(max_length=32)
    youtube = models.CharField(max_length=70)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    business_hours = models.CharField(max_length=64)
    address = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
