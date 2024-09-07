from django.contrib import admin
from . import models

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'organizer', 'time_created', 'date_created')


admin.site.register(models.Event, EventAdmin)
