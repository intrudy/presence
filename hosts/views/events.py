
from django.http import HttpRequest
from django.http import JsonResponse

from ..models import Event as EventModel
from presence.views import Plural
from presence.views import Singular


class Event(Singular):
    model = EventModel
    entity = 'event'


class Events(Plural):
    model = EventModel
    entity = 'events'

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Event, str(k))])
        for k in kwargs.keys():
            kwargs.update({k: request.GET.get(k)})
        return super().get(request, *args, **kwargs)
