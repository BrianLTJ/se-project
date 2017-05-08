from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from apitools.decorators import accept_methods,have_perms
import json


def perm_wrapper(perm):
    # return {"id":000}
    return {'id':perm.id,'name':perm.name, 'codename': perm.codename}


# Permission list
@accept_methods(['get'])
@have_perms(['auth.auth.admin_user_permissions_view'])
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

