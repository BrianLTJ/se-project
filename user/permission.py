from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
import json


def perm_wrapper(perm):
    return JsonResponse({ "id": perm.id, "name": perm.name })


# Permission list
def perm_list(request):
    response_data={}
    response_data['result']='error'
    groups = Permission.objects.all()
    response_data['perms']=[]
    for item in groups:
        response_data['perms'].append(perm_wrapper(item))

    return JsonResponse(response_data)

