from book.models import Book, LibBook
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# add libbook
@csrf_exempt
def libbook_add(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]

        try:
            libbook = LibBook()
            # print(req['bookid'])
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
        req=req[0]
        try:
            bookid=req['bookid']
            libbooks = LibBook.objects.filter(book=Book.objects.get(bookid=int(req['bookid'])))
            # print(len(libbooks))
            resp_libbookdata=[]
            for libitem in libbooks:
                item={}
                item['libbookid']=libitem.libbookid
                item['barid']=libitem.barid
                item['location']=libitem.location
                resp_libbookdata.append(item)

            response_data['result'] = 'ok'
            response_data['data']=resp_libbookdata
        except:
            response_data['message'] = 'Book Not found.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)
