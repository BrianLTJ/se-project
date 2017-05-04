from django.conf.urls import url
from index import admin_views as admin_views


urlpatterns = [
    url(r'book/add', admin_views.admin_book_add),

    url(r'libbook/list/(\d+)$', admin_views.admin_libbook),

    url(r'borrow/borrow', admin_views.admin_borrow),
    url(r'borrow/return', admin_views.admin_return),
    # User
    url(r'user/list', admin_views.admin_user_list),
    url(r'user/add', admin_views.admin_user_add),
    url(r'user/edit/(\d+)', admin_views.admin_user_edit),

    #group
    url(r'group/list',admin_views.admin_group_list),
    url(r'group/add', admin_views.admin_group_add),
    url(r'group/edit/(?P<groupid>\d+)', admin_views.admin_group_edit),

    # borrowright
    url(r'borrowright/list', admin_views.admin_br_list),
    url(r'borrowright/add', admin_views.admin_br_add),
    url(r'borrowright/edit/(\d+)', admin_views.admin_br_edit),

    url(r'$', admin_views.admin_index),
]
