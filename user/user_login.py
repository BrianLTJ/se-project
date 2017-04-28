import json
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login(request):
    response_data = {}
    response_data['result']='error'
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        print(req)
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

    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)


def user_logout(request):
    logout(request)
    return JsonResponse({'result':'ok'})


def user_login_state(request):
    return JsonResponse({"result":"ok"})

