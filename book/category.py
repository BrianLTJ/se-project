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

# Show cate list
@accept_methods(['get'])
def cate_list(request):
    response_data = {}
    response_data['result'] = 'error'
    try:
        cates = Category.objects.all()
        respdata = list()
        for item in cates:
            cateitem = {}
            cateitem['id']=item.id
            cateitem['text']=item.text
            cateitem['note']=item.note
            respdata.append(cateitem)

        response_data['result'] = 'ok'
        response_data['data'] = json.dumps(respdata)
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Fail to fetch categories.'

    return JsonResponse(response_data)

# Add cate
@csrf_exempt
@accept_methods(['post'])
def cate_add(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    cate_name = req
    cate = Category(text=cate_name['text'])
    try:
        cate.save()
        response_data['result'] = 'ok'
        response_data['data'] = {'text': cate_name['text'], 'id': cate.id}
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Fail to fetch categories.'


    return JsonResponse(response_data)

@accept_methods(['post'])
def cate_getname(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    cate_id = req['id']
    try:
        cate = Category.objects.get(id=cate_id)
        response_data['result'] = 'ok'
        response_data['data'] = {'text': cate.text, 'id': cate.id}
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Not found.'

    return JsonResponse(response_data)


# Tag list
@accept_methods(['get'])
def tag_list(request):
    response_data = {}
    response_data['result'] = 'error'
    try:
        tags = Tag.objects.all()
        respdata = list()
        for item in tags:
            tagitem = {}
            tagitem['id']=item.id
            tagitem['text']=item.text
            tagitem['note']=item.note
            respdata.append(tagitem)

        response_data['result'] = 'ok'
        response_data['data'] = json.dumps(respdata)
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Fail to fetch categories.'

    return JsonResponse(response_data)

# Add cate
@csrf_exempt
@accept_methods(['post'])
def tag_add(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    tag_name = req
    tag = Tag(text=tag_name['text'])
    try:
        tag.save()
        response_data['result'] = 'ok'
        response_data['data'] = {'text': tag_name['text'], 'id': tag.id}
    except:
        response_data['result'] = 'error'
        response_data['message'] = 'Fail to fetch taggories.'

    return JsonResponse(response_data)

