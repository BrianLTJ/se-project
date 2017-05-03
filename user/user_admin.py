import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group,Permission
from django.contrib.auth import get_user
from django.http import JsonResponse,HttpRequest
from user.models import BorrowRight, UserBorrowRight, BanList
from apitools.decorators import accept_methods

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

    banned=False
    ban=BanList.objects.filter(user=user)
    if len(ban)>0:
        banned = True

    return {"id":user.id, "username":user.username, "last_login": user.last_login, "groups":groups, "perms": perms, "borrowright":borrowright_dict, "banned": banned,"active":user.is_active}


@csrf_exempt
@accept_methods(['post'])
def admin_change_password(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    req = req[0]
    try:
        usertochange = User.objects.get(id=req['userid'])
        usertochange.set_password(req['newpwd'])
        response_data['result']='ok'
    except:
        response_data['message']='Fail to set password'

    return JsonResponse(response_data)

@csrf_exempt
@accept_methods(['get'])
def admin_user_list(request):
    response_data={}
    response_data['result']='error'
    users = User.objects.all()
    userlist=[]
    for user in users:
        userlist.append(user_wrapper(user))
    response_data['result']='ok'
    response_data['users']=userlist

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def admin_user_add(request):
    response_data={}
    response_data['result']='error'
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

        #is active
        user.is_active=bool(req['active'])

        # Banlist
        if req['banlist'] == True:
            banlist=BanList(user=user)
            banlist.save()

        response_data['result']='ok'
        response_data['userid']=user.id
    except:
        response_data['message']='Fail to add user'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def admin_user_edit(request):
    response_data={}
    response_data['result']='error'
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

        # banned
        if req['banned'] == True:
            try:
                BanList(user=user).save()
            except:
                pass
        else:
            try:
                BanList.objects.get(user=user).delete()
            except:
                pass

        user.is_active=bool(req['active'])
        user.save()

        response_data['result']='ok'
        response_data['userid']=user.id
    except:
        response_data['message']='Fail to edit user'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def admin_user_detail(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        user = User.objects.get(id=req['id'])
        response_data['result']='ok'
        response_data['user']=user_wrapper(user)

    except:
        response_data['message']='User not found'

    return JsonResponse(response_data)



@csrf_exempt
@accept_methods(['post'])
def admin_user_delete(request):
    response_data={}
    response_data['result']='error'
    req = json.loads(request.body.decode('utf-8'))
    try:
        user = User.objects.get(id=req['id'])
        # Delete user borrow right list
        ubr = UserBorrowRight.objects.filter(user=user)
        for i in ubr:
            i.delete()

        # Delete banlist
        banlist = BanList.objects.filter(user=user)
        for i in banlist:
            i.delete()

        user.delete()

        response_data['result']='ok'
    except:
        response_data['message']='Fail to delete user'

    return JsonResponse(response_data)


@csrf_exempt
@accept_methods(['post'])
def admin_user_modify_group(request):
    response_data = {}
    response_data['result'] = 'error'
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

    return JsonResponse(response_data)

