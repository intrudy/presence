
from django.urls import path

from . import views


urlpatterns = [
    path("hosts", views.hosts, name="Hosts"),
    path("hosts/<str:uid>", views.host, name="Host information"),

    path("cohorts", views.cohorts, name="Cohort history"),
    path("cohorts/<str:uid>", views.cohort, name="Cohort details"),

    path("events", views.events, name="Event history"),
    path("events/<str:uid>", views.event, name="Event details")
]