'''
Author: Tingjun Li
Description:
Functions for Adding, Editing books, author, etc

'''
from django.http import JsonResponse
from book.models import Book, Author, Category, Tag, LibBook
import json

def book_add(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        # Requests
        raw_data = request.body
        req = json.loads(raw_data)

        print(req['isbn'])




        # Response Data
        response_data['result'] = 'ok'
        response_data['book_id'] = '12345'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

