
from django.urls import path

from .views.cohorts import Cohort
from .views.cohorts import Cohorts
from .views.events import Event
from .views.events import Events
from .views.hosts import Host
from .views.hosts import Hosts


urlpatterns = [
    path("hosts", Hosts.as_view(), name="Hosts"),
    path("hosts/<str:uid>", Host.as_view(), name="View Host details"),
    path("hosts/<str:uid>/edit", Host.as_view(), name="Edit host details"),
    path("hosts/<str:uid>/delete", Host.as_view(), name="Delete a host"),
    path("hosts/register", Host.as_view(), name='Register a new host'),

    path("cohorts", Cohorts.as_view(), name="Cohort history"),
    path("cohorts/<str:uid>", Cohort.as_view(), name="View cohort details"),
    path("cohorts/<str:uid>/edit", Cohort.as_view(), name="Edit cohort detail"),
    path("cohorts/<str:uid>/delete", Cohort.as_view(), name="Delete a cohort"),
    path("cohorts/register", Cohort.as_view(), name="Register a new cohort"),

    path("events", Events.as_view(), name="Event history"),
    path("events/<str:uid>", Event.as_view(), name="Event details"),
    path("events/<str:uid>/edit", Event.as_view(), name="Edit event details"),
    path("events/<str:uid>/delete", Event.as_view(), name="Delete an event"),
    path("events/register", Event.as_view(), name="Register a new event")
]