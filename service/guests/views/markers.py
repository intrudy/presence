
from django.http import HttpRequest
from django.http import JsonResponse

from ..models import Marker as MarkerModel
from presence.views import Plural
from presence.views import Singular


class Marker(Singular):
    model = MarkerModel
    entity = 'marker'


class Markers(Plural):
    model = MarkerModel
    entity = 'markers'

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = {}
        if 'date' in request.GET.keys(): kwargs['date'] = request.GET.get('date')
        if 'start' in request.GET.keys(): kwargs['start'] = request.GET.get('start')
        if 'ended' in request.GET.keys(): kwargs['ended'] = request.GET.get('ended')
        if 'cohort' in request.GET.keys():
            cohort = self.model.objects.get(request.GET.get('cohort'))
            kwargs['cohort'] = cohort.id
        return super().get(request, *args, **kwargs)
