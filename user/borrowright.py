import json
from user.models import BorrowRight,UserBorrowRight
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apitools.decorators import accept_methods

def borrowright_wrapper(br):
    return {'id':br.id, 'name':br.name, 'day':br.day, 'booknum': br.booknum, 'allowborrow': br.allowborrow}


@csrf_exempt
@accept_methods(['get'])
def borrowright_list(request):
    response_data = {}
    response_data['result'] = 'error'
    try:
        br=BorrowRight.objects.all()

        response_data['borrowrights']=[]
        for i in br:
            response_data['borrowrights'].append(borrowright_wrapper(i))

        response_data['result']='ok'
    except:
        response_data['message']="Fail to get borrow rights"

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def borrowright_detail(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        response_data['borrowright']=borrowright_wrapper(BorrowRight.objects.get(id=req['id']))
        response_data['result']='ok'
    except:
        response_data['message']="Fail to get the detail"

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def borrowright_add(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        br = BorrowRight()
        br.name=req['name']
        br.day=req['day']
        br.booknum=req['booknum']
        br.allowborrow=req['allowborrow']
        br.save()
        response_data['borrowright']=br.id
        response_data['result']='ok'
    except:
        response_data['message']="Fail to get the detail"

    return JsonResponse(response_data)



@csrf_exempt
@accept_methods(['post'])
def borrowright_edit(request):
    response_data = {}
    response_data['result'] = 'error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        br = BorrowRight(id=req['id'])
        br.name = req['name']
        br.day = req['day']
        br.booknum = req['booknum']
        br.allowborrow = req['allowborrow']
        br.save()
        response_data['result'] = 'ok'
    except:
        response_data['message'] = "Fail to get the detail"

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def borrowright_delete(request):
    response_data = {}
    response_data['result'] = 'error'

    req = json.loads(request.body.decode('utf-8'))
    try:
        br=BorrowRight.objects.get(id=req['id'])
        # Clear br in ubr
        ubr = UserBorrowRight.objects.filter(borrowright=br)
        for i in ubr:
            i.delete()
        br.delete()
        response_data['result']='ok'
    except:
        response_data['message']='Fail to delete'

    return JsonResponse(response_data)

