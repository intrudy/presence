
from django.http import HttpRequest
from django.http import JsonResponse

from ..models import Cohort as CohortModel
from presence.views import Plural
from presence.views import Singular


class Cohort(Singular):
    model = CohortModel
    entity = 'cohort'


class Cohorts(Plural):
    model = CohortModel
    entity = 'cohorts'

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(self.model, str(k))])
        for k in kwargs.keys():
            kwargs.update({k: request.GET.get(k)})
        return super().get(request, *args, **kwargs)
