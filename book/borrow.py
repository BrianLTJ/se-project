from book.models import Book, LibBook
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import LibBook, BookOperation
from django.contrib.auth.models import User

import json
@csrf_exempt
def book_borrow(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]

        try:
            # Fetch libbook
            libbook=LibBook.objects.get(barid=req['barid'])

            # Query whether libbook is borrowed
            if libbook.borrowuser is None:
                user = User.objects.get(id=req['userid'])
                bookoperation=BookOperation()
                bookoperation.libbook=libbook
                bookoperation.user=user
                bookoperation.operation='b'
                bookoperation.save()
                response_data['result'] = 'ok'
            else:
                response_data['message'] = 'Book has been borrowed.'
        except:
            response_data['message'] = 'Fail to borrow.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

@csrf_exempt
def book_return(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]

        try:
            # Fetch libbook
            libbook=LibBook.objects.get(barid=req['barid'])

            # Query whether libbook is borrowed
            if libbook.borrowuser is not None:
                bookoperation=BookOperation()
                bookoperation.libbook=libbook
                bookoperation.user=libbook.borrowuser
                bookoperation.operation='r'
                bookoperation.save()
                libbook.borrowuser.clear()
                response_data['result'] = 'ok'
            else:
                response_data['message'] = 'Book haven\'t been borrowed.'
        except:
            response_data['message'] = 'Fail to borrow.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)