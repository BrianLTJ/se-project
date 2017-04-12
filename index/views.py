from django.shortcuts import render


# Create your views here.
def index_index(request):
    return render(request, template_name='index/index.html')

def book_detail(request, bid):
    return render(request, 'book/detail.html', {"book_id":bid})

def search_index(request):
    return render(request, template_name='search/index.html')

