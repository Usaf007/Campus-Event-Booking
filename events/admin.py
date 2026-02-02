from django.contrib import admin
from .models import Event, Booking

# This line adds the Event table to the admin panel
admin.site.register(Event)

# This line adds the Booking table to the admin panel
admin.site.register(Booking)