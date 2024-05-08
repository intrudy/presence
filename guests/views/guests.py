
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Guest


def all(request: HttpRequest) -> JsonResponse:
    rs = serialize('json', Guest.objects.all())
    return JsonResponse({'guests': json.loads(rs)})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        rs = serialize('json', [Guest.objects.get(id=uid)])
        return JsonResponse({'guest': json.loads(rs)})
    except Guest.DoesNotExist:
        return HttpResponseNotFound("Guest(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        g = Guest.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(g, str(k)):
                setattr(g, str(k), v)
        g.save()
        return JsonResponse({'guest': json.loads(serialize('json', [g]))})
    except Guest.DoesNotExist:
        return HttpResponseNotFound("Guest(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    g = Guest()
    for k, v in request.POST.items():
        if hasattr(g, str(k)):
            setattr(g, str(k), v)
    g.save()
    return JsonResponse({'guest': json.loads(serialize('json', [g]))})
