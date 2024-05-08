
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Teams


def all(request: HttpRequest) -> JsonResponse:
    rs = serialize('json', Teams.objects.all())
    return JsonResponse({'teams': json.loads(rs)})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        rs = serialize('json', [Teams.objects.get(id=uid)])
        return JsonResponse({'team': json.loads(rs)})
    except Teams.DoesNotExist:
        return HttpResponseNotFound("Team(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        t = Teams.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(t, str(k)):
                setattr(t, str(k), v)
        t.save()
    except Teams.DoesNotExist:
        return HttpResponseNotFound("Team(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    t = Teams()
    for k, v in request.POST.items():
        if hasattr(t, str(k), v):
            setattr(t, str(k), v)
    t.save()
    return JsonResponse({'team': json.loads(serialize('json', [t]))})
