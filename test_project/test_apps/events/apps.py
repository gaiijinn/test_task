from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_apps.events'

    def ready(self):
        from ..events import signals
