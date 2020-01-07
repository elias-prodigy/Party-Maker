from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.contrib.gis.admin import OSMGeoAdmin


class Place(models.Model):
    city = models.CharField(max_length=255)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location_ev = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
    #location = models.PointField()
    date = models.DateField()

    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

#
# class ShopAdmin(OSMGeoAdmin):
#     list_display = ('name', 'location')
