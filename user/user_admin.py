import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user
from django.http import JsonResponse,HttpRequest

def user_wrapper(user):
    groups=[]
    for g in user.groups.all():
        groups.append({"id":g.id, "name":g.name})
    return {"id":user.id, "username":user.username, "last_login": user.last_login, "groups":groups}

@csrf_exempt
def admin_change_password(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]
        try:
            usertochange = User.objects.get(id=req['userid'])
            usertochange.set_password(req['newpwd'])
            response_data['result']='ok'
        except:
            response_data['message']='Fail to set password'
    else:
        response_data['message']='Not a valid request.'


def admin_user_list(request):
    response_data={}
    response_data['result']='error'
    if request.method=='GET':
        users = User.objects.all()
        userlist=[]
        for user in users:
            userlist.append(user_wrapper(user))
        response_data['result']='ok'
        response_data['users']=userlist
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)



@csrf_exempt
def admin_user_add(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.create_user(username=req['username'], password=req['password'])
            # Add to group
            for i in req['groups']:
                user.groups.add(Group.objects.get(id=i['id']))

        except:
            response_data['message']='Fail to add user'
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)

@csrf_exempt
def admin_user_modify_group(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = request.user
            # Add to group
            grouplist=[]
            for i in req['groups']:
                grouplist.append(Group.objects.get(id=i['id']))

            user.groups.set(grouplist)

        except:
            response_data['message'] = 'Fail to add user'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

