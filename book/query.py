'''
Author: Tingjun Li
Create Time: 2017-04-10
Function: Find and show book details
'''
from django.http import JsonResponse
from django.core import serializers, exceptions
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from book.models import Book, Tag, Category

# List book
def book_query_list(request):

    return None


# Show book details
@csrf_exempt
def book_detail(request, bid):
    # raw_data = request.body
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "GET":
        # book_item = Book.objects.values().filter(bookid=bid).values_list()
        # response_data['data'] = serializers.serialize('json',book_item)
        try:
            book_item = Book.objects.filter(bookid=bid)
            if len(book_item)!=1:
                raise exceptions.ObjectDoesNotExist
            resp_book = []
            resp_book['isbn'] = book_item.isbn
            resp_book['title'] = book_item.title
            resp_book['author'] = book_item.author
            resp_book['translator'] = book_item.translator
            resp_book['edition'] = book_item.edition
            resp_book['pubhouse'] = book_item.pubhouse
            resp_book['pubtime'] = book_item.pubtime
            resp_book['summary'] = book_item.summary
            resp_book['context'] = book_item.context
            resp_book['clc'] = book_item.clc
            resp_book['price'] = book_item.price

            for i in book_item.category:
                item = []
                item['id'] = i.id
                item['text'] = i.text
                resp_book['category'].append(item)

            response_data['result'] = 'ok'

            response_data['data'] = book_item
        except:
            response_data['result'] = 'error'
            response_data['message'] = 'Book not found'

    else:
        response_data['message'] = 'Not a valid request.'
        
    return JsonResponse(response_data)

# Show lib book details




