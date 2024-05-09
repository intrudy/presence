
from django.urls import path

from . import views


urlpatterns = [
    path("hosts", views.hosts.filter, name="Hosts"),
    path("hosts/<str:uid>", views.hosts.fetch, name="View Host details"),
    path("hosts/<str:uid>/edit", views.hosts.edit, name="Edit host details"),
    path("hosts/<str:uid>/delete", views.hosts.delete, name="Delete a host"),
    path("hosts/register", views.hosts.register, name='Register a new host'),

    path("cohorts", views.cohorts.filter, name="Cohort history"),
    path("cohorts/<str:uid>", views.cohorts.fetch, name="View cohort details"),
    path("cohorts/<str:uid>/edit", views.cohorts.edit, name="Edit cohort detail"),
    path("cohorts/<str:uid>/delete", views.cohorts.delete, name="Delete a cohort"),
    path("cohorts/register", views.cohorts.register, name="Register a new cohort"),

    path("events", views.events.filter, name="Event history"),
    path("events/<str:uid>", views.events.fetch, name="Event details"),
    path("events/<str:uid>/edit", views.events.edit, name="Edit event details"),
    path("events/<str:uid>/delete", views.events.delete, name="Delete an event"),
    path("events/register", views.events.register, name="Register a new event")
]