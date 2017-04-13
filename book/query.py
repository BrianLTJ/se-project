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


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


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

            response_data['result'] = 'ok'
            response_data['data']=serializers.serialize('json',book_item)
        except:
            response_data['result'] = 'error'
            response_data['message'] = 'Book not found'

    else:
        response_data['message'] = 'Not a valid request.'
        
    return JsonResponse(response_data)

# Show lib book details


# Show cate list
def cate_list(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "GET":
        try:
            cates = Category.objects.all()
            response_data['result'] = 'ok'
            response_data['data'] = serializers.serialize('json', cates)
        except:
            response_data['result'] = 'error'
            response_data['message'] = 'Fail to fetch categories.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

