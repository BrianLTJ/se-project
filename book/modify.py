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
    response_data['result'] = 'ok'
    response_data['book_id'] = '12345'

    return JsonResponse(response_data)

