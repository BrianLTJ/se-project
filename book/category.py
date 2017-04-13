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


# Add cate list
def cate_add(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        cate_name = req[0]
        cate = Category(text=cate_name['text'])
        try:
            cate.save()
            response_data['result'] = 'ok'
            response_data['data'] = {'text': cate_name['text'], 'id': cate.id}
        except:
            response_data['result'] = 'error'
            response_data['message'] = 'Fail to fetch categories.'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)