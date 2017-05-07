from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apitools.decorators import have_perms

@have_perms(['admin.admin_entry'])
def admin_index(request):
    return render(request, 'admin/index.html')

def admin_book_list(request):
    return render(request, 'admin/book/list.html')


def admin_book_add(request):
    return render(request, 'admin/book/add.html',{"bookid": -1})


def admin_book_edit(request, bookid):
    return render(request, 'admin/book/add.html', {"bookid": int(bookid)})


def admin_libbook(request, bookid):
    return render(request, 'admin/libbook/add.html', {"bookid": int(bookid)})


@have_perms(['book.admin_optborrow_borrow'])
def admin_borrow(request):
    return render(request, 'admin/borrow/borrow.html')

@have_perms(['book.admin_optborrow_return'])
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


