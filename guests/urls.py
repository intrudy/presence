
from django.urls import path

from . import views


urlpatterns = [
    path("guests", views.guests.all, name="View all guests"),
    path("guests/<str:uid>", views.guests.fetch, name="View guest details"),
    path("guests/<str:uid>/edit", views.guests.edit, name="Edit guest details"),
    path("guests/register", views.guests.register, name="Register new guest profile"),

    path("teams", views.teams.all, name="View all teams"),
    path("teams/<str:uid>", views.teams.fetch, name="View team details"),
    path("teams/<str:uid>/edit", views.teams.edit, name="Edit team details"),
    path("teams/register", views.teams.register, name="Register a new team")
]