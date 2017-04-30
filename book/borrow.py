from book.models import Book, LibBook
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import LibBook, BookBorrow
from django.contrib.auth.models import User
from django.http import HttpRequest
import time

import json
@csrf_exempt
def book_borrow(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))

        try:
            user = User.objects.get(id=req['userid'])
            # TODO Judge Whether User can borrow book
            # Fetch libbook
            libbook=LibBook.objects.get(barid=req['barid'])

            # Query whether libbook is borrowed
            if libbook.borrow is None:
                bookborrow = BookBorrow.objects.create(user=user)

                libbook.borrow=bookborrow
                libbook.save()

                bookborrow.operator=request.user
                bookborrow.save()

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

        try:
            # Fetch libbook
            libbook=LibBook.objects.get(barid=req['barid'])

            # Query whether libbook is borrowed
            if libbook.borrow is not None:
                bookborrow=BookBorrow.objects.get(libbook=libbook, returntype='n')
                bookborrow.returntime= time.time()
                bookborrow.returntype = 'r'
                bookborrow.save()
                libbook.borrow.clear()
                response_data['result'] = 'ok'
            else:
                response_data['message'] = 'Book haven\'t been borrowed.'
        except:
            response_data['message'] = 'Fail to borrow.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)