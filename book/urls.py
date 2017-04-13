from django.conf.urls import url
from book import query as book_query
from book import modify as book_modify
from book import category as book_category

urlpatterns =[
    url(r'book/add', book_modify.book_add, name='add'),

    url(r'book/detail/(.+)', book_query.book_detail, name='detail'),
    # url(r'detail/libbook', ),

    # category
    url(r'cate/list', book_category.cate_list, name='cate_list'),
    url(r'cate/add', book_category.cate_add, name='cate_add'),
]
