from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission
from django.views.decorators.csrf import csrf_exempt
import json
from apitools.decorators import accept_methods,have_perms
def group_wrapper(group):
    perms = []
    for perm in group.permissions.all():
        perms.append({'id':perm.id,'name':perm.name, 'codename': perm.codename})
    return {'id':group.id, 'name':group.name, 'perms':perms}


# Get group list
@csrf_exempt
@accept_methods(['get'])
@have_perms(['auth.admin_user_group_view'])
def group_list(request):
    response_data={}
    response_data['result']='error'
    groups = Group.objects.all()
    response_data['result'] = 'ok'
    response_data['groups']=[]
    for item in groups:
        response_data['groups'].append(group_wrapper(item))

    return JsonResponse(response_data)


# Group detail
@csrf_exempt
@accept_methods(['post'])
@have_perms(['auth.admin_user_group_view'])
def group_detail(request):
    response_data = {}
    response_data['result'] = 'error'
    req=json.loads(request.body.decode('utf-8'))
    try:
        group = Group.objects.get(id=req['id'])

        response_data['result'] = 'ok'
        response_data['group'] = group_wrapper(group)
    except:
        response_data['message'] = 'Group not found.'

    return JsonResponse(response_data)

# Add group
@csrf_exempt
@accept_methods(['post'])
@have_perms(['auth.admin_user_group_add'])
def group_add(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    # try:
    group = Group(name=req['name'])
    group.save()
    # set group permissions:
    # Get perm object list
    perm_list = []
    for perm in req['perms']:
        perm = Permission.objects.get(id=perm['id'])
        perm_list.append(perm)

    group.permissions.set(perm_list)
    group.save()

    response_data['result']='ok'
    response_data['group']={'id':group.id,'name':group.name}

    return JsonResponse(response_data)


# Change group
@csrf_exempt
@accept_methods(['post'])
@have_perms(['auth.admin_user_group_edit'])
def group_change(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    # try:
    group = Group.objects.get(id=req['id'])
    # Change group name
    group.name = req['name']
    # Change group permissions:
    # Get perm object list
    perm_list = []
    for permid in req['perms']:
        perm = Permission.objects.get(id=permid['id'])
        perm_list.append(perm)

    group.permissions.set(perm_list)
    group.save()
    response_data['result']='ok'
    response_data['group']=group_wrapper(group)

    return JsonResponse(response_data)


# Delete group
@csrf_exempt
@accept_methods(['post'])
@have_perms(['auth.admin_user_group_delete'])
def group_delete(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    group = Group.objects.get(id=req['id'])
    group.delete()
    response_data['result']='ok'

    return JsonResponse(response_data)

