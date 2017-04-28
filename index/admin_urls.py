from django.conf.urls import url
from index import admin_views as admin_views


urlpatterns = [
    url(r'book/add', admin_views.admin_book_add),

    url(r'libbook', admin_views.admin_libbook),

    url(r'borrow', admin_views.admin_borrow),

    url(r'user/add', admin_views.admin_user_add),


    url(r'$', admin_views.admin_index),
]
