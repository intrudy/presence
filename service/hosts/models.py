
import uuid

from datetime import datetime
from datetime import timedelta
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models as db
from django.utils import timezone


class Host(User):
    phone = db.CharField(verbose_name="Contact Number", max_length=17, blank=True,
                         validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format(15 dig): '+999999999'")])
    workplace = db.CharField(verbose_name="Workplace", blank=True, max_length=60, default='NA')

    class Meta:
        verbose_name = 'Host'
        verbose_name_plural = 'Hosts'

    def __str__(self) -> str:
        return self.get_full_name()


class Cohort(db.Model):
    strength = db.IntegerField(default=10)
    name = db.CharField(max_length=128, blank=False, default=str(uuid.uuid4()))
    year = db.CharField(max_length=128, blank=False, default=str(datetime.today().year))

    class Meta:
        verbose_name = 'Cohort'
        verbose_name_plural = 'Cohorts'

    def __str__(self) -> str:
        return self.name


class Event(db.Model):
    active = db.BooleanField(default=False)
    duration = db.IntegerField(default=60)
    start = db.DateTimeField(default=timezone.now)
    ended = db.DateTimeField(default=timezone.now)
    title = db.CharField(blank=False, max_length=128)
    description = db.TextField(blank=False, max_length=240)
    host = db.ForeignKey(Host, on_delete=db.PROTECT)
    cohort = db.ForeignKey(Cohort, on_delete=db.PROTECT)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def save(self, *args, **kwargs):
        if self.start == self.ended:
            self.ended = self.start + timedelta(0, self.duration)
        super().save(*args, **kwargs)
