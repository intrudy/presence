
import json

from django.core.serializers import serialize
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import JsonResponse

from ..models import Teams


def filter(request: HttpRequest) -> JsonResponse:
    kwargs = dict.fromkeys([str(k) for k in request.GET.keys() if hasattr(Teams, str(k))])
    for k in kwargs.keys():
        kwargs.update({k: request.GET.get(k)})

    teams = Teams.objects.filter(**kwargs)
    if len(teams) == 0:
        return HttpResponseNotFound("Query returned no teams")
    return JsonResponse({'teams': json.loads(serialize('json', teams))})


def fetch(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        team = Teams.objects.get(id=uid)
        return JsonResponse({'team': json.loads(serialize('json', [team]))})
    except Teams.DoesNotExist:
        return HttpResponseNotFound("Team(%s) not found" % uid)


def edit(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        team = Teams.objects.get(id=uid)
        for k, v in request.POST.items():
            if hasattr(team, str(k)):
                setattr(team, str(k), v)
        team.save()
    except Teams.DoesNotExist:
        return HttpResponseNotFound("Team(%s) not found" % uid)


def register(request: HttpRequest) -> JsonResponse:
    team = Teams()
    for k, v in request.POST.items():
        if hasattr(team, str(k), v):
            setattr(team, str(k), v)
    team.save()
    return JsonResponse({'team': json.loads(serialize('json', [team]))})


def delete(request: HttpRequest, uid: str) -> JsonResponse:
    try:
        team = Teams.objects.get(id=uid)
        team.delete()
        return JsonResponse({'team': str(team), 'deleted': True})
    except Teams.DoesNotExist:
        return HttpResponseNotFound("Team(%s) not found" % uid)
