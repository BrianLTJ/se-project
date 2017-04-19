import json
from django.http import JsonResponse
from django.contrib.auth import login


def user_login(request):
    response_data = {}
    response_data['result']='error'
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        req =req[0]
        try:
            username = req['username']
            password = req['password']

            login(request, username, password)

        except:


    else:
        response_data['message'] = 'Not a valid request.'

