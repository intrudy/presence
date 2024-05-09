
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Event


def filter(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Event, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    events = Event.objects.filter(**kwargs)
    if len(events) == 0:
        return HttpResponseNotFound("Query returned no Events")
    return JsonResponse({'events': json.loads(serialize('json', events))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        event = Event.objects.get(id=uid)
        return JsonResponse({'event': json.loads(serialize('json', [event]))})
    except Event.DoesNotExist:
        return HttpResponseNotFound("Event(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        event = Event.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(event, str(k)):
                setattr(event, str(k), v)
        event.save()
        return JsonResponse({'event': json.loads(serialize('json', [event]))})
    except Event.DoesNotExist:
        return HttpResponseNotFound("Event(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    event = Event()
    for k, v in request.POST.items():
        if hasattr(event, str(k), v):
            setattr(event, str(k), v)
    event.save()
    return JsonResponse({'event': json.loads(serialize('json', [event]))})


def delete(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        event = Event.objects.get(id=uid)
        event.delete()
        return JsonResponse({'event': str(event), 'deleted': True})
    except Event.DoesNotExist:
        return HttpResponseNotFound("Event(%s) not found" % uid)
