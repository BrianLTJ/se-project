from django.shortcuts import render


def error_404(request):
    return render('errror/404.html')


def error_403(request):
    return render('error/403.html')

