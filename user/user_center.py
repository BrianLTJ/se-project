import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.http import JsonResponse
from apitools.decorators import accept_methods

@csrf_exempt
@accept_methods(['post'])
def change_password(request):
    response_data={}
    response_data['result']='error'
    try:
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]
        usertochange=get_user(request)
        # Challenge old password
        if usertochange.check_password(req['oldpwd']):
            usertochange.set_password(req['newpwd'])
            response_data['result']='ok'
        else:
            response_data['message']='Fail to change password.'
    except:
        response_data['message'] = 'Error occurred when changing password.'

    return JsonResponse(response_data)