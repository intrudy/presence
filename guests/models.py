
import uuid

from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models as db
from django.utils import timezone

from hosts.models import Cohort


class Guest(User):
    phone = db.CharField(verbose_name="Contact Number", max_length=17, blank=True,
                         validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format(15 dig): '+999999999'")])
    cohort = db.ForeignKey(Cohort, on_delete=db.PROTECT)

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'

    def __str__(self) -> str:
        return self.get_full_name()


class Teams(db.Model):
    size = db.IntegerField(default=4)
    members = db.JSONField(blank=True)
    name = db.CharField(max_length=128, blank=False, default=str(uuid.uuid4()))

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self) -> str:
        return self.name
