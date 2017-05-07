from django.shortcuts import render


def error_404(request):
    return render(request, 'error/404.html')


def error_403(request):
    return render(request, 'error/403.html')

