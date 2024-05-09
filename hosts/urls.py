
from django.urls import path

from . import views


urlpatterns = [
    path("hosts", views.hosts.filter, name="Hosts"),
    path("hosts/<str:uid>", views.hosts.fetch, name="View Host details"),
    path("hosts/<str:uid>/edit", views.hosts.edit, name="Edit host details"),
    path("hosts/<str:uid>/delete", views.hosts.delete, name="Delete a host"),

    path("cohorts", views.cohorts.filter, name="Cohort history"),
    path("cohorts/<str:uid>", views.cohorts.fetch, name="Cohort details"),
    path("cohorts/<str:uid>/edit", views.cohorts.edit, name="Edit Cohort detail"),
    path("cohorts/<str:uid>/delete", views.cohorts.delete, name="Delete a Cohort"),

    path("events", views.events, name="Event history"),
    path("events/<str:uid>", views.events.fetch, name="Event details"),
    path("events/<str:uid>/edit", views.events.edit, name="Edit event details"),
    path("events/<str:uid>/delete", views.events.delete, )
]