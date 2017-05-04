from django.shortcuts import render


def center_borrowlog(request):
    return render(request, 'center/borrowlog.html')
