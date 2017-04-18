import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.http import JsonResponse

@csrf_exempt
def change_password(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
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
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)