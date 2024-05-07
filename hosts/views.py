
import json

from django.core import serializers
from django.http import Http404
from django.http import HttpRequest
from django.http import JsonResponse

from .models import Cohort
from .models import Event
from .models import Host


def hosts(request: HttpRequest) -> JsonResponse:
    rs = serializers.serialize('json', Host.objects.all())
    return JsonResponse({'hosts': json.loads(rs)})


def host(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        rs = serializers.serialize('json', [Host.objects.get(id=uid)])
        return JsonResponse({'host': json.loads(rs)})
    except Host.DoesNotExist:
        raise Http404("Host(%s) not found" % uid)


def cohorts(request: HttpRequest) -> JsonResponse:
    rs = serializers.serialize('json', Cohort.objects.all())
    return JsonResponse({'cohorts': json.loads(rs)})


def cohort(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        rs = serializers.serialize('json', [Cohort.objects.get(id=uid)])
        return JsonResponse({'cohort': json.loads(rs)})
    except Cohort.DoesNotExist:
        raise Http404("Cohort(%s) not found" % uid)


def events(request: HttpRequest) -> JsonResponse:
        rs = serializers.serialize('json', Event.objects.all())
        return JsonResponse({'events': json.loads(rs)})


def event(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        rs = serializers.serialize('json', [Event.objects.get(id=uid)])
        return JsonResponse(json.loads({'event': json.loads(rs)}))
    except Cohort.DoesNotExist:
        raise Http404("Event(%s) not found" % uid)
