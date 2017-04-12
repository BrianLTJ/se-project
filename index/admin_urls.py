from django.conf.urls import url
from index import admin_views as admin_views


urlpatterns = [
    url(r'book/add', admin_views.admin_book_add),
]
