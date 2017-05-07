from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import LibBook, BookBorrow
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from user.models import BorrowRight, UserBorrowRight, BanList
from django.http import HttpRequest
from apitools.decorators import accept_methods, have_perms
from apitools.snippets import lt_day_str,lt_time_str
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
        bookday = 0
        ubr = UserBorrowRight.objects.filter(user=bookborrow.user)
        if len(ubr) > 0:
            bookday = ubr.get().borrowright.day
        expiredatetime=lt_day_str(bookborrow.borrowtime + datetime.timedelta(days=bookday))
        return expiredatetime
    except:
        return None


@csrf_exempt
@accept_methods(['post'])
@have_perms(['book.admin_optborrow_borrow'])
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
        response_data['message'] = '用户被冻结。'
        # Banned?
        try:
            ban=BanList.objects.get(user=user)
            allowborrow = False
            response_data['message'] = '用户被禁止借阅。'
        except:
            pass

        # User borrowgroup allow?
        try:
            br=UserBorrowRight.objects.get(user=user).borrowright
            allownum = br.booknum
            if br.allowborrow == False | allownum == 0 | br.day == 0:
                allowborrow =False
                response_data['message'] = '借书组不允许借阅.'

        except:
            allowborrow=False
            response_data['message'] = '借书组不允许借阅.'

        # User borrowed book num
        borrowed = BookBorrow.objects.filter(user=user).filter(returntype='n')
        if len(borrowed) >= allownum:
            allowborrow = False
            response_data['message'] = '超过用户最大可借书数量.'

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
                response_data['message'] = '图书已被借出。'
    except:
        response_data['message'] = '借阅失败。'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
@have_perms(['book.admin_optborrow_return'])
def book_return(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))

    try:
        # Fetch libbook
        libbook=LibBook.objects.get(barid=req['barid'])
        # Query whether libbook is borrowed
        if libbook_borrowed(libbook):
            bookborrow=BookBorrow.objects.filter(libbook=libbook, returntype='n').get()
            bookborrow.returntime= datetime.datetime.now()
            bookborrow.returntype = 'r'
            bookborrow.save()
            response_data['result'] = 'ok'
        else:
            response_data['message'] = '图书尚未被借出。'
    except:
        response_data['message'] = '无法归还。'

    return JsonResponse(response_data)

