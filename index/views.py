from django.shortcuts import render
from book.models import Book, Category, Tag

# Create your views here.
def index_index(request):
    return render(request, template_name='index/index.html')

def book_detail(request, bid):
    bookitem=Book.objects.filter(bookid=bid)
    if len(bookitem)==1:
        # return render(request, 'book/detail.html', {"book_id":bid, "book":bookitem})
        return render(request, 'book/detail_bk.html', {"book_id": bid, "book": bookitem[0]})
    else:
        return render(request, 'universal/error.html', {'msg': "找不到这本书"})

def book_detail_rest(request, bid):
    return render(request, 'book/detail.html', {"book_id": bid})

def search_index(request):
    return render(request, template_name='search/index.html')


