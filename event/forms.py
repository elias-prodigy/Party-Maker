from django.forms import ModelForm
from event.models import Event, PartyRegPartners


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description',
            'location_ev',
            'event_image',
            'date'
        ]

