from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import LibBook, BookBorrow
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from user.models import BorrowRight, UserBorrowRight, BanList
from django.http import HttpRequest
from apitools.decorators import accept_methods
import datetime, time
import json

def libbook_borrowed(libbook):
    bookborrow = BookBorrow.objects.filter(libbook=libbook).filter(returntype='n')
    if len(bookborrow) == 0:
        return False
    else:
        return True

def bookborrow_getexpireday(libbook):
    try:
        bookborrow = BookBorrow.objects.filter(libbook=libbook).filter(returntype='n').get()
        bookday = UserBorrowRight.objects.get(user=bookborrow.user).borrowright.day
        expiredatetime=(bookborrow.borrowtime + datetime.timedelta(days=bookday))
        expiredatetime=localtime(expiredatetime).strftime("%Y-%m-%d")
        return expiredatetime
    except:
        return None


@csrf_exempt
@accept_methods(['post'])
def book_borrow(request):
    response_data = {}
    response_data['result'] = 'error'

    req = json.loads(request.body.decode('utf-8'))

    try:
        user = User.objects.get(id=req['userid'])

        # Judge Whether User can borrow book
        allowborrow = True
        allownum=0

        # User active?
        allowborrow = allowborrow & user.is_active
        response_data['message'] = 'User is not active.'
        # Banned?
        try:
            ban=BanList.objects.get(user=user)
            allowborrow = False
            response_data['message'] = 'Banned.'
        except:
            pass

        # User borrowgroup allow?
        try:
            br=UserBorrowRight.objects.get(user=user).borrowright
            allownum = br.booknum
            if br.allowborrow == False | allownum == 0 | br.day == 0:
                allowborrow =False
                response_data['message'] = 'Group not allowed.'

        except:
            allowborrow=False
            response_data['message'] = 'Group not allowed.'

        # User borrowed book num
        borrowed = BookBorrow.objects.filter(user=user).filter(returntype='n')
        if len(borrowed) >= allownum:
            allowborrow = False
        response_data['message'] = 'Maximun allowed book number.'

        if allowborrow:
            # print("allowborrow")
            # Fetch libbook
            libbook=LibBook.objects.get(barid=req['barid'])

            if libbook_borrowed(libbook) == False:
                bookborrow = BookBorrow.objects.create(user=user, libbook=libbook)

                bookborrow.operator=request.user
                bookborrow.save()

                response_data['result'] = 'ok'
                response_data['username']=user.username
                response_data['expire']=bookborrow_getexpireday(libbook)
            else:
                response_data['message'] = 'Book has been borrowed.'
    except:
        response_data['message'] = 'Fail to borrow.'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def book_return(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))

    try:
        # Fetch libbook
        libbook=LibBook.objects.get(barid=req['barid'])
        # Query whether libbook is borrowed
        if libbook_borrowed(libbook):
            bookborrow=BookBorrow.objects.filter(libbook=libbook, returntype='n')
            bookborrow.returntime= datetime.datetime.now()
            bookborrow.returntype = 'r'
            bookborrow.save()
            response_data['result'] = 'ok'
        else:
            response_data['message'] = 'Book haven\'t been borrowed.'
    except:
        response_data['message'] = 'Fail to borrow.'

    return JsonResponse(response_data)