
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Teams as TeamsModel
from presence.views import Plural
from presence.views import Singular


class Team(Singular):
    model = TeamsModel
    entity = 'team'


class Teams(Plural):
    model = TeamsModel
    entity = 'teams'

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(self.model, str(k))])
        for k in kwargs.keys():
            kwargs.update({k: request.GET.get(k)})
        return super().get(request, *args, **kwargs)
