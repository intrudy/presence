
from django.urls import path

from .views.guests import Guest
from .views.guests import Guests
from .views.markers import Marker
from .views.markers import Markers
from .views.teams import Team
from .views.teams import Teams


urlpatterns = [
    path("guests", Guests.as_view(), name="View all guests"),
    path("guests/<str:uid>", Guest.as_view(), name="View guest details"),
    path("guests/<str:uid>/edit", Guest.as_view(), name="Edit guest details"),
    path("guests/register", Guest.as_view(), name="Register new guest profile"),

    path("markers", Markers.as_view(), name="Filter attendance markers"),
    path("markers/<str:uid>", Marker.as_view(), name="Attendance marker details"),
    path("markers/<str:uid>/edit", Marker.as_view(), name="Edit attendance marker"),
    path("markers/<str:uid>/delete", Marker.as_view(), name="Delete attendance marker"),
    path("markers/register", Marker.as_view(), name="Create attendance marker"),

    path("teams", Teams.as_view(), name="View all teams"),
    path("teams/<str:uid>", Team.as_view(), name="View team details"),
    path("teams/<str:uid>/edit", Team.as_view(), name="Edit team details"),
    path("teams/register", Team.as_view(), name="Register a new team")
]