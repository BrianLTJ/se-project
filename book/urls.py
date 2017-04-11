from django.conf.urls import url
from book import query as book_query
from book import modify as book_modify

urlpatterns =[
    url(r'book/add', book_modify.book_add),
    url(r'detail/book', book_query.book_detail),
    # url(r'detail/libbook', ),
]
