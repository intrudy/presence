
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Guest


def filter(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Guest, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    guests = Guest.objects.filter(**kwargs)
    if len(guests) == 0:
        return HttpResponseNotFound("Query returned no guests")
    return JsonResponse({'guests': json.loads(serialize('json', guests))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        guest = Guest.objects.get(id=uid)
        return JsonResponse({'guest': json.loads(serialize('json', [guest]))})
    except Guest.DoesNotExist:
        return HttpResponseNotFound("Guest(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        guest = Guest.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(guest, str(k)):
                setattr(guest, str(k), v)
        guest.save()
        return JsonResponse({'guest': json.loads(serialize('json', [guest]))})
    except Guest.DoesNotExist:
        return HttpResponseNotFound("Guest(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    guest = Guest()
    for k, v in request.POST.items():
        if hasattr(guest, str(k)):
            setattr(guest, str(k), v)
    guest.save()
    return JsonResponse({'guest': json.loads(serialize('json', [guest]))})


def delete(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        guest = Guest.objects.get(id=uid)
        guest.delete()
        return JsonResponse("Guest(%s) deleted")
    except Guest.DoesNotExist:
        return HttpResponseNotFound("Guest(%s) not found" % uid)
