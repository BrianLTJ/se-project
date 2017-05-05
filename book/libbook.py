from book.models import Book, LibBook, BookBorrow
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.borrow import libbook_borrowed, bookborrow_getexpireday
from user.models import BorrowRight, UserBorrowRight
from apitools.decorators import accept_methods
from apitools.snippets import lt_time_str
from user.borrow import bookborrow_getexpireday, libbook_borrowed
import json


def libbook_wrapper(libbook):
    book = libbook.book
    state = {}
    state['borrowed'] = libbook_borrowed(libbook)
    if state['borrowed'] == True:
        # Fetch duedate
        expire = bookborrow_getexpireday(libbook)
        state['expire']=expire
    else:
        state['expire'] = ""
    return {"id": libbook.libbookid, "barid":libbook.barid, "location": libbook.location, "state": state}


def borrowlog_wrapper(bookborrow):
    return {"id": bookborrow.id,
            "operator": bookborrow.operator.username,
            "user": bookborrow.user.username,
            "borrowtime": lt_time_str(bookborrow.borrowtime),
            "returntime": lt_time_str(bookborrow.returntime),
            "borrowtype": bookborrow.borrowtype,
            "returntype": bookborrow.returntype,
            "expire": bookborrow_getexpireday(bookborrow.libbook)}

# add libbook
@csrf_exempt
@accept_methods(['post'])
def libbook_add(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        libbook = LibBook()
        book = Book.objects.get(bookid=int(req['bookid']))
        libbook.book = book
        libbook.barid = req['barid']
        libbook.location = req['location']
        libbook.save()
        response_data['result'] = 'ok'
    except:
        response_data['result'] = 'error'

    return JsonResponse(response_data)


# edit
@accept_methods(['post'])
def libbook_edit(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        libbook = LibBook(libbookid=req['id'])
        libbook.location = req['location']
        libbook.save()
        response_data['result'] = 'ok'
    except:
        response_data['result'] = 'error'

    return JsonResponse(response_data)


# get libbook list
@csrf_exempt
@accept_methods(['post'])
def libbook_list(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        bookid=req['bookid']
        libbooks = LibBook.objects.filter(book=Book.objects.get(bookid=int(req['bookid'])))
        resp_libbookdata=[]
        for libitem in libbooks:
            # Fetch borrowlog
            resp_libbookdata.append(libbook_wrapper(libitem))

        response_data['result'] = 'ok'
        response_data['data']=resp_libbookdata
    except:
        response_data['message'] = 'Book Not found.'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def libbook_list_with_borrowlog(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        bookid=req['bookid']
        libbooks = LibBook.objects.filter(book=Book.objects.get(bookid=int(req['bookid'])))
        # print(len(libbooks))
        resp_libbookdata=[]
        for libitem in libbooks:
            respitem=libbook_wrapper(libitem)
            respitem['logs']=[]
            logs = BookBorrow.objects.filter(libbook=libitem)
            print(logs)
            for log in logs:
                respitem['logs'].append(borrowlog_wrapper(log))

            resp_libbookdata.append(respitem)

        response_data['result'] = 'ok'
        response_data['data']=resp_libbookdata
    except:
        response_data['message'] = 'Book Not found.'

    return JsonResponse(response_data)


@accept_methods(['post'])
def libbook_del(request):
    response_data={}
    response_data['result']='error'
    try:
        req=json.loads(request.body.decode('utf-8'))
        libbook_item = LibBook.objects.get(libbookid=req['id'])
        #Check if libbook is borrowed
        if libbook_borrowed(libbook_item):
            response_data['message']='Book is borrowed'
        else:
            libbook_item.delete()
            response_data['result']='ok'

    except:
        response_data['message']='Fail to delete the libbook'

    return JsonResponse(response_data)

