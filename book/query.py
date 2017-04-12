'''
Author: Tingjun Li
Create Time: 2017-04-10
Function: Find and show book details
'''
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from book.models import Book, Author, Tag, Category

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
        

        book_item = Book.objects.filter(bookid=bid)

        response_data = {}
        if len(book_item) != 1:
            response_data['result']='error'
            response_data['message']='Book not found'
        else:
            response_data=book_item[0]
    else:
        response_data['message'] = 'Not a valid request.'
        
    return JsonResponse(response_data)

# Show lib book details

