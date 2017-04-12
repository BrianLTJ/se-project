from django.conf.urls import url
from index import views as index_views
from index import admin_views as admin_views


urlpatterns = [
    url(r'book/detail/(.+)', index_views.book_detail, name='book_detail'),
    url(r'^', index_views.index_index),
]
