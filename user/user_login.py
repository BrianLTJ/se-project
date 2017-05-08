import json
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from apitools.decorators import accept_methods
from django.contrib.auth.models import User


@csrf_exempt
@accept_methods(['post'])
def user_login(request):
    response_data = {}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        username = req['username']
        password = req['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response_data['result']='ok'
        else:
            response_data['message'] = 'User not found or password is wrong'
    except:
        response_data['message'] = 'Fail to login'

    return JsonResponse(response_data)


@accept_methods(['get','post'])
def user_logout(request):
    logout(request)
    return JsonResponse({'result':'ok'})


@accept_methods(['get','post'])
def user_login_state(request):
    response_data={}
    response_data['result']='error'
    try:
        user = request.user
        if user.is_authenticated():
            response_data['result']='ok'
            response_data['user']={'id':user.id,'username':user.username}
    except:
        pass
    return JsonResponse(response_data)

