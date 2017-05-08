import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from apitools.snippets import lt_day_str,lt_time_str
from django.http import JsonResponse
from apitools.decorators import accept_methods,have_perms
from book.models import BookBorrow,Book,LibBook
from user.borrow import bookborrow_getexpireday
from django.utils.timezone import localtime

def bookborrow_wrapper(bookborrow,withid):
    if bookborrow.returntype == 'n':
        expire = bookborrow_getexpireday(bookborrow.libbook)
    else:
        expire = ""
    return { "book":{"title":bookborrow.libbook.book.title,
                     "bookid":bookborrow.libbook.book.bookid,
                     "author": bookborrow.libbook.book.author,
                     "translator": bookborrow.libbook.book.translator,
                     "clc": bookborrow.libbook.book.clc },
             "barid":bookborrow.libbook.barid,
             "borrowtime": lt_time_str(bookborrow.borrowtime),
             "returntime": lt_day_str(bookborrow.returntime),
             "borrowtype": bookborrow.borrowtype,
             "returntype": bookborrow.returntype,
             "expire": expire
             }


@accept_methods(['post'])
def get_userinfo(request):
    response_data={}
    response_data['result']='error'
    try:
        user = request.user
        response_data['user']={"id": user.id, "username": user.username}
        response_data['result']='ok'
    except:
        response_data['message']='用户信息查询失败'
    return JsonResponse(response_data)

@csrf_exempt
@accept_methods(['post'])
@have_perms(['auth.auth.user_change_password'])
def change_password(request):
    response_data={}
    response_data['result']='error'
    try:
        req = json.loads(request.body.decode('utf-8'))
        usertochange=get_user(request)
        # Challenge old password
        if usertochange.check_password(req['oldpsw']):
            usertochange.set_password(req['newpsw'])
            usertochange.save()
            response_data['result']='ok'
        else:
            response_data['message']='Fail to change password.'
    except:
        response_data['message'] = 'Error occurred when changing password.'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['get'])
@have_perms(['book.book.user_read_borrowlog'])
def current_user_borrowlog(request):
    response_data={}
    response_data['result']='error'
    try:
        user = request.user
        borrowbooks = BookBorrow.objects.filter(user=user).order_by(('-borrowtime'))
        response_data['logs']=[]
        for item in borrowbooks:
            response_data['logs'].append(bookborrow_wrapper(item,False))

        response_data['result']='ok'

    except:
        response_data['message']='Fail to find logs'

    return JsonResponse(response_data)

