import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group,Permission
from django.contrib.auth import get_user
from django.http import JsonResponse,HttpRequest
from user.models import BorrowRight, UserBorrowRight


def user_wrapper(user):
    groups=[]
    for g in user.groups.all():
        groups.append({"id":g.id, "name":g.name})
    perms=[]
    for p in user.get_all_permissions():
        perms.append(p)

    try:
        ubr=UserBorrowRight.objects.get(user=user)
        borrowright=ubr.borrowright
        borrowright_dict={"id":borrowright.id,"name": borrowright.name, "booknum":borrowright.booknum, "day":borrowright.day, "allowborrow":borrowright.allowborrow}
    except:
        borrowright_dict={"id":""}

    return {"id":user.id, "username":user.username, "last_login": user.last_login, "groups":groups, "perms": perms, "borrowright":borrowright_dict}

@csrf_exempt
def admin_change_password(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        req = req[0]
        try:
            usertochange = User.objects.get(id=req['userid'])
            usertochange.set_password(req['newpwd'])
            response_data['result']='ok'
        except:
            response_data['message']='Fail to set password'
    else:
        response_data['message']='Not a valid request.'

@csrf_exempt
def admin_user_list(request):
    response_data={}
    response_data['result']='error'
    if request.method=='GET':
        users = User.objects.all()
        userlist=[]
        for user in users:
            userlist.append(user_wrapper(user))
        response_data['result']='ok'
        response_data['users']=userlist
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)


@csrf_exempt
def admin_user_add(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.create_user(username=req['username'], password=req['password'])
            user.save()
            # Add to group
            for i in req['groups']:
                user.groups.add(Group.objects.get(id=i['id']))

            user.save()

            try:
                newbr = BorrowRight.objects.get(id=int(req['borrowright']['id']))
                newubr = UserBorrowRight()
                newubr.user = user
                newubr.borrowright = newbr
                newubr.save()
            except:
                pass

            response_data['result']='ok'
            response_data['userid']=user.id
        except:
            response_data['message']='Fail to add user'
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)


@csrf_exempt
def admin_user_edit(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(id=req['id'])
            # Add to group
            user.username=req['username']
            user.save()
            newgroup = []
            for i in req['groups']:
                newgroup.append(Group.objects.get(id=i['id']))

            user.groups.set(newgroup)

            # Set new borrowright
            ubr=UserBorrowRight.objects.filter(user=user)
            ubrnotchanged=False
            try:
                if len(ubr)==1:
                    ubrnotchanged = (ubr[0].id==int(req['borrowright']['id']))
            except:
                pass

            if not ubrnotchanged:
                # Clear all old ubr item
                for i in ubr:
                    i.delete()

                try:
                    newbr = BorrowRight.objects.get(id=int(req['borrowright']['id']))
                    newubr = UserBorrowRight()
                    newubr.user = user
                    newubr.borrowright = newbr
                    newubr.save()
                except:
                    pass

            user.save()
            response_data['result']='ok'
            response_data['userid']=user.id
        except:
            response_data['message']='Fail to edit user'
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)


@csrf_exempt
def admin_user_detail(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(id=req['id'])
            response_data['result']='ok'
            response_data['user']=user_wrapper(user)

        except:
            response_data['message']='User not found'
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)



@csrf_exempt
def admin_user_delete(request):
    response_data={}
    response_data['result']='error'
    if request.method=='POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(id=req['id'])
            # Delete user borrow right list
            ubr = UserBorrowRight.objects.filter(user=user)
            for i in ubr:
                i.delete()

            user.delete()

            response_data['result']='ok'
        except:
            response_data['message']='Fail to delete user'
    else:
        response_data['message']='Not a valid request.'

    return JsonResponse(response_data)


@csrf_exempt
def admin_user_modify_group(request):
    response_data = {}
    response_data['result'] = 'error'
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            user = request.user
            # Add to group
            grouplist=[]
            for i in req['groups']:
                grouplist.append(Group.objects.get(id=i['id']))

            user.groups.set(grouplist)

        except:
            response_data['message'] = 'Fail to add user'
    else:
        response_data['message'] = 'Not a valid request.'

    return JsonResponse(response_data)

