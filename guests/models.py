
import os
import uuid

from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models as db
from django.utils import timezone
from geopy import geocoders
from geopy.exc import GeocoderServiceError

from hosts.models import Cohort


class Guest(User):
    fingerprint = db.BinaryField(blank=True, max_length=512)
    phone = db.CharField(verbose_name="Contact Number", max_length=17, blank=True,
                         validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format(15 dig): '+999999999'")])
    cohort = db.ForeignKey(Cohort, on_delete=db.PROTECT)

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self) -> str:
        return 'Guest<%s>' % self.get_full_name()


class Teams(db.Model):
    size = db.IntegerField(default=4)
    members = db.JSONField(blank=True)
    name = db.CharField(max_length=128, blank=False, default=str(uuid.uuid4()))

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self) -> str:
        return 'Team<%s>' % self.name


class Marker(db.Model):
    start = db.TimeField(auto_now=True)
    ended = db.TimeField(auto_now=True)
    date = db.DateTimeField(default=timezone.now)
    area = db.CharField(max_length=40, blank=True)
    fingerprint = db.BinaryField(blank=False, max_length=512)
    lat = db.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    lon = db.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    member = db.ForeignKey(Guest, on_delete=db.PROTECT)

    class Meta:
        verbose_name = 'Marker'
        verbose_name_plural = 'Markers'

    def __str__(self) -> str:
        return "Marker<%s>" % (self.member)

    def save(self, *args, **kwargs) -> str:
        if self.area and (self.lat == 0.0 and self.lon == 0.0):
            try:
                mapbox = geocoders.MapBox(api_key=os.getenv('MAPBOX_ACCESS_TOKEN'))
                coordinates = mapbox.geocode(self.area)
                self.lat = coordinates.latitude
                self.lon = coordinates.longitude
            except (KeyError, GeocoderServiceError):
                pass
        super().save(*args, **kwargs)
