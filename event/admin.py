from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Event, Place, PartyRegPartners

admin.site.register(Event)
admin.site.register(Place)
admin.site.register(PartyRegPartners)
