from django.conf.urls import url
from book import query as book_query
from book import modify as book_modify

urlpatterns =[
    url(r'book/add', book_modify.book_add),
]
