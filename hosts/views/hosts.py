
import json

from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.http import JsonResponse

from ..models import Host


def filter(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Host, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    hosts = Host.objects.filter(**kwargs)
    if len(hosts) == 0:
        return HttpResponseNotFound("No results found")
    return JsonResponse({'hosts': json.loads(serialize('json', hosts))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        host = Host.objects.get(id=uid)
        return JsonResponse({'host': json.loads(serialize('json', [host]))})
    except Host.DoesNotExist:
        return HttpResponseNotFound("Host(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        host = Host.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(host, str(k)):
                setattr(host, str(k), v)
        host.save()
        return JsonResponse({'host': json.loads(serialize('json', [host]))})
    except Host.DoesNotExist:
        return HttpResponseNotFound("Host(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Host, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    try:
        host = Host(**kwargs)
        host.save()
        return JsonResponse({'host': json.loads(serialize('json', [host]))})
    except ValidationError as err:
        return HttpResponseServerError("Failed to register new user", err)


def delete(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        host = Host.objects.get(id=uid)
        host.delete()
        return JsonResponse({'host': str(host), 'deleted': True})
    except Host.DoesNotExist:
        return HttpResponseNotFound("Host(%s) not found" % uid)
