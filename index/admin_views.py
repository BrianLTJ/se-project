from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def admin_index(request):
    return render(request, 'admin/index.html')


def admin_book_add(request):
    return render(request, 'admin/book/add.html')

def admin_libbook(request):
    return render(request, 'admin/libbook/add.html')


def admin_borrow(request):
    return render(request, 'admin/borrow/borrow.html')

def admin_return(request):
    return render(request, 'admin/borrow/return.html')


# User
def admin_user_add(request):
    return render(request, 'admin/user/add.html', {"pagetitle": "添加用户"})

def admin_user_edit(request, userid):
    return render(request, 'admin/user/add.html', {"pagetitle": "修改用户", "id": int(userid)})

def admin_user_list(request):
    return render(request, 'admin/user/list.html')

# Group
def admin_group_list(request):
    return render(request, 'admin/group/list.html')


def admin_group_add(request):
    return render(request, 'admin/group/add.html', {'pagetitle': '添加用户组'})

def admin_group_edit(request,groupid):
    return render(request, 'admin/group/add.html', {'pagetitle': '修改用户组', 'id': int(groupid)})

# Borrowrights

def admin_br_list(request):
    return render(request, 'admin/borrowright/list.html')

def admin_br_add(request):
    return render(request, 'admin/borrowright/add.html', {"pagetitle":"添加借书权限组"})

def admin_br_edit(request, brid):
    return render(request, 'admin/borrowright/add.html', {"pagetitle":"修改借书权限组", "id":int(brid)})


