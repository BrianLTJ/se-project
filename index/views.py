from django.shortcuts import render


# Create your views here.
def index_index(request):
    return render(request, template_name='index/index.html')
