
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Cohort


def filter(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Cohort, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    cohorts = Cohort.objects.filter(**kwargs)
    if len(cohorts) == 0:
        return HttpResponseNotFound("Query returned no cohorts")
    return JsonResponse({'cohorts': json.loads(serialize('json', cohorts))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        cohort = Cohort.objects.get(id=uid)
        return JsonResponse({'cohort': json.loads(serialize('json', [cohort]))})
    except Cohort.DoesNotExist:
        return HttpResponseNotFound("Cohort(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        cohort = Cohort.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(cohort, str(k)):
                setattr(cohort, str(k), v)
        cohort.save()
    except Cohort.DoesNotExist:
        return HttpResponseNotFound("Cohort(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    cohort = Cohort()
    for k, v in request.POST.items():
        if hasattr(cohort, str(k), v):
            setattr(cohort, str(k), v)
    cohort.save()
    return JsonResponse({'cohort': json.loads(serialize('json', [cohort]))})
