from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class AdditionalInfo(models.Model):
    time_created = models.TimeField(auto_now_add=True)
    date_created = models.DateField(auto_now_add=True)


class Event(AdditionalInfo):
    title = models.CharField(max_length=128, verbose_name='Event title')
    description = models.CharField(max_length=512, verbose_name='Event description')
    location = models.JSONField(verbose_name='Event coordinates')
    organizer = models.ForeignKey(to=get_user_model(), related_name='event', verbose_name='Event organizer',
                                  on_delete=models.CASCADE)

    guests = models.ManyToManyField(to=get_user_model())
