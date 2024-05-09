
import json

from django.core.serializers import serialize
from django.http import HttpResponseNotFound
from django.http import HttpRequest
from django.http import JsonResponse

from ..models import Marker
from hosts.models import Cohort


def filter(request: HttpRequest) -> JsonResponse:
        kwargs = {}
        if 'date' in request.GET.keys(): kwargs['date'] = request.GET.get('date')
        if 'start' in request.GET.keys(): kwargs['start'] = request.GET.get('start')
        if 'ended' in request.GET.keys(): kwargs['ended'] = request.GET.get('ended')
        if 'cohort' in request.GET.keys():
            cohort = Cohort.objects.get(request.GET.get('cohort'))
            kwargs['cohort'] = cohort.id

        markers = Marker.objects.filter(**kwargs)
        if len(markers) == 0:
            return HttpResponseNotFound("Query returned no markers")
        return JsonResponse({'markers': json.loads(serialize('json', markers))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        marker = Marker.objects.get(id=uid)
        return JsonResponse({'marker': json.loads(serialize('json', [marker]))})
    except Marker.DoesNotExist:
        return HttpResponseNotFound("Marker(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        marker = Marker.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(marker, str(k)):
                setattr(marker, str(k), v)
        marker.save()
        return JsonResponse({'marker': json.loads(serialize('json', [marker]))})
    except Marker.DoesNotExist:
        return HttpResponseNotFound("Marker(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    marker = Marker()
    for k, v in request.POST.items():
        if hasattr(marker, str(k)):
            setattr(marker, str(k), v)
    marker.save()
    return JsonResponse({'marker': json.loads(serialize('json', [marker]))})


def delete(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        marker = Marker.objects.get(id=uid)
        marker.delete()
        return JsonResponse({'marker': str(marker), 'deleted': True})
    except Marker.DoesNotExist:
        return HttpResponseNotFound("Marker(%s) not found" % uid)