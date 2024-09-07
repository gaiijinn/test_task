from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from .services.email_service import EventCreatorEmail


@receiver(signal=post_save, sender=Event)
def set_first_guest(instance, created, **kwargs):
    if created:
        instance.guests.add(instance.organizer)
        sender = EventCreatorEmail(instance)
        sender.send_mail()
