from django.shortcuts import render


def admin_book_add(request):

    return render(request, 'admin/book/add.html')

