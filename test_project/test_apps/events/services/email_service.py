from abc import ABC, abstractmethod
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class BaseEmailSender(ABC):
    @abstractmethod
    def send_mail(self, fail_silently=False):
        pass


class LinkGenerator:
    def get_link(self, event_obj):
        base_path = f"{settings.DOMAIN_NAME}:{settings.PORT}"
        event_url = reverse("event:event-detail", kwargs={'pk': event_obj.id})

        return f"{base_path}{event_url}"


class EventCreatorEmail(BaseEmailSender):
    def __init__(self, event_obj):
        self.event = event_obj

        self.link = LinkGenerator().get_link(self.event)

    def send_mail(self, fail_silently=False):
        send_mail(
            f"Event was successfully created!",
            f'{self.link}',
            settings.EMAIL_HOST_USER,
            [self.event.organizer.email],
            fail_silently,
        )


class EventGuestEmail(BaseEmailSender):
    def __init__(self, guest_email, event_obj):
        self.email = guest_email
        self.event = event_obj

        self.link = LinkGenerator().get_link(self.event)

    def send_mail(self, fail_silently=False):
        send_mail(
            f"You successfully become a guest in event",
            f"{self.link}",
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently,
        )

