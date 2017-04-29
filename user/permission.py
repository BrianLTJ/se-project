from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
import json


def perm_wrapper(perm):
    return {'id':perm.id,'name':perm.name, 'codename': perm.codename}


# Permission list
def perm_list(request):
    response_data={}
    response_data['result']='error'
    try:
        perms = Permission.objects.all()

        permslist=[]
        for item in perms:
            permslist.append(perm_wrapper(item))
        response_data['perms'] = permslist
        response_data['result']='ok'
    except:
        response_data['message']='Fail to get permissions'

    return JsonResponse(response_data)

