import json

from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from django.db import Error as DatabaseError
from django.http import JsonResponse
from django.http import HttpRequest
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.views import View


class Plural(View):
    model = None
    entity = 'none'

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        rset = self.model.objects.filter(**kwargs)
        if len(rset):
            return HttpResponseNotFound("Query returned no items")
        return JsonResponse({self.entity: json.loads(serialize('json', [rset]))})


class Singular(View):
    model = None
    entity = 'none'

    def post(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        rset = self.model()
        for k, v in request.POST.items():
            if hasattr(rset, str(k)):
                setattr(rset, str(k), v)
        try:
            rset.save()
            return JsonResponse({self.entity: json.loads(serialize('json', [rset]))})
        except (DatabaseError, ValidationError) as err:
            return HttpResponseServerError("Failed to register new %s" % (self.entity, err))

    def get(self, request: HttpRequest, uid: str, *args, **kwargs) -> JsonResponse:
        try:
            rset = self.model.objects.get(id=uid)
            return JsonResponse({self.entity: json.loads(serialize('json', [rset]))})
        except self.model.DoesNotExist:
            return HttpResponseNotFound("%s(%s) not found" % (self.entity.capitalize(), uid))

    def put(self, request: HttpRequest, uid: str, *args, **kwargs) -> JsonResponse:
        try:
            rset = self.model.objects.get(id=uid)
            for k, v in request.POST.items():
                if hasattr(rset, str(k)):
                    setattr(rset, str(k), v)
            rset.save()
            return JsonResponse({self.entity: json.loads(serialize('json', [rset]))})
        except self.model.DoesNotExist:
            return HttpResponseNotFound("%s(%s) not found" % (self.entity.capitalize(), uid))

    def delete(self, request: HttpRequest, uid: str, *args, **kwargs) -> JsonResponse:
        try:
            rset = self.model.objects.get(id=uid)
            rset.delete()
            return JsonResponse({self.entity: str(rset), 'deleted': True})
        except DatabaseError as err:
            return HttpResponseServerError("Failed to delete %s" % self.entity, err)
        except self.model.DoesNotExist:
            return HttpResponseNotFound("%s(%s) not found" % (self.entity.capitalize(), uid))
