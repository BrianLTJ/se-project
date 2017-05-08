from django.shortcuts import render
from apitools.decorators import have_perms

@have_perms(['book.book.user_read_borrowlog'])
def center_index(request):
    return  render(request, 'center/index.html')


@have_perms(['auth.auth.user_read_borrowlog'])
def center_borrowlog(request):
    return render(request, 'center/borrowlog.html')


@have_perms(['auth.auth.user_change_password'])
def center_changepsw(request):
    return render(request, 'center/changepsw.html')

