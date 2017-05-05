'''
Author: Tingjun Li
Description:
Functions for Adding, Editing books, author, etc

'''
from django.http import JsonResponse
from book.models import Book, Category, Tag, LibBook
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from apitools.decorators import accept_methods

@csrf_exempt
@accept_methods(['post'])
def book_add(request):
    response_data = {}
    response_data['result'] = 'error'
    # Requests
    req = json.loads(request.body.decode('utf-8'))

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

    # add tag
    for item in req['tag']:
        try:
            tag = Tag.objects.get(id=item['id'])
            book_item.tag.add(tag)
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

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def book_edit(request):
    response_data = {}
    response_data['result'] = 'error'
    # Requests
    req = json.loads(request.body.decode('utf-8'))

    book_item = Book.objects.filter(bookid=req['bookid'])
    if len(book_item)!=1:
        return JsonResponse(response_data)

    book_item=book_item.get()
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
    book_item.save()
    # add cate

    book_item.category.clear()
    for item in req['category']:
        try:
            # print(item['id'])
            cate = Category.objects.get(id=item['id'])
            book_item.category.add(cate)
        except:
        #     print("CATE fail")
            pass

    # add tag
    book_item.tag.clear()
    for item in req['tag']:
        try:
            tag = Tag.objects.get(id=item['id'])
            book_item.tag.add(tag)
        except:
        #     print("TAG fail")
            pass

    # Save book
    try:
        book_item.save()
        # Response Data
        response_data['result'] = 'ok'
        response_data['book_id'] = book_item.bookid
    except:
        # print("SAVE fail")
        response_data['message'] = 'Fail to save data.'

    return JsonResponse(response_data)



@accept_methods(['post'])
def book_del(request):
    response_data = {}
    response_data['result'] = 'error'

    # Requests
    req = json.loads(request.body.decode('utf-8'))
    req = req[0]
    bookid = req['bookid']

    try:
        book = Book.objects.get(bookid=bookid)
        book.delete()

        response_data['result'] = 'ok'
    except:
        response_data['message'] = 'Fail to delete.'

    return JsonResponse(response_data)

