
from django.urls import path

from . import views


urlpatterns = [
    path("guests", views.guests.filter, name="View all guests"),
    path("guests/<str:uid>", views.guests.fetch, name="View guest details"),
    path("guests/<str:uid>/edit", views.guests.edit, name="Edit guest details"),
    path("guests/register", views.guests.register, name="Register new guest profile"),

    path("markers", views.markers.filter, name="Filter attendance markers"),
    path("markers/<str:uid>", views.markers.fetch, name="Attendance marker details"),
    path("markers/<str:uid>/edit", views.markers.edit, name="Edit attendance marker"),
    path("markers/<str:uid>/delete", views.markers.delete, name="Delete attendance marker"),
    path("markers/register", views.markers.register, name="Create attendance marker"),

    path("teams", views.teams.filter, name="View all teams"),
    path("teams/<str:uid>", views.teams.fetch, name="View team details"),
    path("teams/<str:uid>/edit", views.teams.edit, name="Edit team details"),
    path("teams/register", views.teams.register, name="Register a new team")
]