from django.shortcuts import render


def admin_book_add(request):
    return render(request, 'admin/book/add.html')

def admin_libbook(request):
    return render(request, 'admin/libbook/add.html')


def admin_borrow(request):
    return render(request, 'admin/borrow/borrow.html')
