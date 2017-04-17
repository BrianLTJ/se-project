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
        res_data=[]

        for item in req:
            res_data_item=[]
            res_data_item['barid']=item['barid']
            try:
                libbook = LibBook()
                libbook.book = Book.objects.get(bookid=item['bookid'])
                libbook.barid = item['barid']
                libbook.location = item['location']
                libbook.save()
                res_data_item['result'] = 'ok'
            except:
                res_data_item['result'] = 'error'
            finally:
                res_data.append(res_data_item)
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
        try:
            bookid=req['bookid']
            libbooks = LibBook.objects.filter(book_bookid=bookid)
            resp_libbookdata=[]
            for i in libbooks:
                item=[]
                item['libbookid']=i.libbookid
                item['barid']=i.barid
                item['location']=i.location
                resp_libbookdata.append(item)

            response_data['result'] = 'ok'
            response_data['data']=resp_libbookdata
        except:
            response_data['message'] = 'Book Not found.'
    else:
        response_data['message'] = 'Not a valid request.'
