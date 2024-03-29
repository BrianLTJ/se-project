from django.conf.urls import url
from book import query as book_query
from book import modify as book_modify
from book import category as book_category
from book import libbook as book_libbook


urlpatterns =[
    #libbook
    url(r'libbook/add$', book_libbook.libbook_add, name='libbook_add'),
    url(r'libbook/list$', book_libbook.libbook_list, name='libbook_list'),
    url(r'libbook/listlog$', book_libbook.libbook_list_with_borrowlog, name='libbook_list_log'),
    url(r'libbook/delete$', book_libbook.libbook_del, name='libbook_delete'),

    url(r'book/add$', book_modify.book_add, name='add'),
    url(r'book/edit$', book_modify.book_edit, name='book_edit'),

    # book info
    url(r'book/query$', book_query.book_query_list, name='query'),
    url(r'book/detail/(.+)$', book_query.book_detail, name='detail'),

    # category
    url(r'cate/list$', book_category.cate_list, name='cate_list'),
    url(r'cate/add$', book_category.cate_add, name='cate_add'),

    # tag
    url(r'tag/list$', book_category.tag_list, name='tag_list'),
    url(r'tag/add$', book_category.tag_add, name='tag_add'),
]
