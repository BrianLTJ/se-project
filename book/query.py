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
from apitools.decorators import accept_methods
from django.db.models import QuerySet

def wrap_book_list_item(book):
    try:
        resp_item={}
        resp_item['bookid']=book.bookid
        resp_item["title"]=book.title
        resp_item["author"]=book.author
        resp_item["translator"]=book.translator
        resp_item["isbn"]=book.isbn
        resp_item["pubhouse"]=book.pubhouse
        resp_item["pubtime"]=book.translator
        resp_item["cover"]=book.cover
        resp_item["clc"]=book.clc
        resp_item["edition"]=book.edition
        return resp_item
    except:
        return None


# List book
@csrf_exempt
@accept_methods(['post'])
def book_query_list(request):
    response_data = {}
    response_data['result'] = 'error'
    try:
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]
        resp_booklist = []

        start_filter = False

        booklist = QuerySet(model=Book)

        if len(req['title'])>0:
            booklist = Book.objects.filter(title__contains=req['title'])
            start_filter = True

        if len(req['isbn'])>0:
            if start_filter:
                booklist = booklist.filter(isbn__contains=req['isbn'])
            else:
                booklist = Book.objects.filter(isbn__contains=req['isbn'])
                start_filter = True

        if len(req['clc'])>0:
            if start_filter:
                booklist = booklist.filter(clc__contains=req['clc'])
            else:
                booklist = Book.objects.filter(clc__contains=req['clc'])
                start_filter = True

        if len(req['author'])>0:
            if start_filter:
                booklist = booklist.filter(author__contains=req['author'])
            else:
                booklist = Book.objects.filter(author__contains=req['author'])
                start_filter = True

        if len(req['translator'])>0:
            if start_filter:
                booklist = booklist.filter(translator__contains=req['translator'])
            else:
                booklist = Book.objects.filter(translator__contains=req['translator'])
                start_filter = True

        if len(req['pubhouse'])>0:
            if start_filter:
                booklist = booklist.filter(pubhouse__contains=req['pubhouse'])
            else:
                booklist = Book.objects.filter(pubhouse__contains=req['pubhouse'])
                start_filter = True


        if start_filter:
            for i in booklist:
                resp_booklist.append(wrap_book_list_item(i))
            response_data['result'] = 'ok'
            response_data['data']=resp_booklist

    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Cant query book'

    return JsonResponse(response_data)


# Show book details
@csrf_exempt
@accept_methods(['get'])
def book_detail(request, bid):
    response_data = {}
    response_data['result'] = 'error'
    try:
        book_item = Book.objects.get(bookid=int(bid))

        resp_book = {}
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
        resp_book['category'] = []
        resp_book['tag'] = []

        # print(len(book_item.category.all()))

        for i in book_item.category.all():
            item = {}
            item['id'] = i.id
            item['text'] = i.text
            resp_book['category'].append(item)

        for i in book_item.tag.all():
            item = {}
            item['id'] = i.id
            item['text'] = i.text
            resp_book['tag'].append(item)

        response_data['result'] = 'ok'

        response_data['data'] = resp_book
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Book not found'

    return JsonResponse(response_data)

# Show lib book details




