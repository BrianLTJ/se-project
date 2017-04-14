'''
Author: Tingjun Li
Description:
Functions for Adding, Editing books, author, etc

'''
from django.http import JsonResponse
from book.models import Book, Category, Tag, LibBook
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def book_add(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        # Requests
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]

        book_item = Book()
        book_item.isbn = req['isbn']
        book_item.title= req['title']
        book_item.author = req['author']
        book_item.translator = req['translator']
        book_item.edition = req['edition']
        book_item.pubhouse = req['pubhouse']
        book_item.pubtime = req['pubtime']
        book_item.summary = req['summary']
        book_item.context = req['context']
        book_item.clc = req['clc']
        book_item.price = req['price']
        # add cate
        book_item.save()
        for item in req['category']:
            try:
                # print(item['id'])
                cate = Category.objects.get(id=item['id'])
                book_item.category.add(cate)
            except:
                pass

        # Save book
        try:
            book_item.save()
            # Response Data
            response_data['result'] = 'ok'
            response_data['book_id'] = book_item.bookid
        except:
            response_data['message'] = 'Fail to save data.'
        
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

