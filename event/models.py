from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.urls import reverse
from location_field.models.spatial import LocationField
from partners.models import Partners


class Place(models.Model):
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))

    def __str__(self):
        return self.city


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.TextField(null=True, blank=True)
    location_ev = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
    date = models.DateField()
    visitors = models.ManyToManyField(Partners, through='PartyRegPartners')
    event_image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.event_name


class PartyRegPartners(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE)
    is_visited = models.BooleanField(null=True, blank=True)
    SELECT_OPTIONS = (('no', 'NO'), ('yes', 'YES'))
    manager_approve = models.BooleanField(default=False)
    CEO_approve = models.BooleanField(default=False)

    def get_absolute_url_update_partner(self):
        return reverse('update_partners_event', kwargs={'pk': self.pk})
