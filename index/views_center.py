from django.shortcuts import render

def center_index(request):
    return  render(request, 'center/index.html')


def center_borrowlog(request):
    return render(request, 'center/borrowlog.html')
