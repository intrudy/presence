
from django.http import HttpRequest
from django.http import JsonResponse

from presence.views import Plural
from presence.views import Singular
from ..models import Host as HostModel


class Host(Singular):
    entity = 'host'
    model = HostModel

    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(self.model, str(k))])
        return super().post(request, *args, **kwargs)


class Hosts(Plural):
    entity = 'hosts'
    model = HostModel

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(self.model, str(k))])
        for k in kwargs.keys():
            kwargs.update({k: request.GET.get(k)})
        return super().get(request, *args, **kwargs)
