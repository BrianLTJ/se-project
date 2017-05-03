from book.models import Book, LibBook, BookBorrow
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.borrow import libbook_borrowed, bookborrow_getexpireday
from user.models import BorrowRight, UserBorrowRight
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

# add libbook
@csrf_exempt
def libbook_add(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
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

    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

# get libbook list
@csrf_exempt
def libbook_list(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        # try:
        bookid=req['bookid']
        libbooks = LibBook.objects.filter(book=Book.objects.get(bookid=int(req['bookid'])))
        # print(len(libbooks))
        resp_libbookdata=[]
        for libitem in libbooks:
            # item={}
            # item['libbookid']=libitem.libbookid
            # item['barid']=libitem.barid
            # item['location']=libitem.location
            resp_libbookdata.append(libbook_wrapper(libitem))

        response_data['result'] = 'ok'
        response_data['data']=resp_libbookdata
        # except:
        #     response_data['message'] = 'Book Not found.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)
