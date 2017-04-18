import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user
from django.http import JsonResponse


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

@csrf_exempt
def admin_user_add(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]
        try:
            user = User.objects.create_user(username=req['username'], password=req['pwd'])
            # Add to group
            for i in req['group']:
                user.groups.add(Group.objects.get(id=i['groupid']))

        except:
            response_data['message']='Fail to add user'
    else:
        response_data['message']='Not a valid request.'

