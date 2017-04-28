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


# User
def admin_user_add(request):
    return render(request, 'admin/user/add.html')
