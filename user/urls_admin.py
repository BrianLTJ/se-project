'''

API url for admin

'''
from django.conf.urls import url
from user import user_admin as user_admin
from user import group, permission

urlpatterns = [
    url(r'user/add', user_admin.admin_user_add, name='user_add'),
    url(r'user/edit', user_admin.admin_user_edit, name='user_edit'),
    url(r'user/list', user_admin.admin_user_list, name='user_list'),
    url(r'user/detail', user_admin.admin_user_detail, name='user_detail'),
    url(r'user/delete', user_admin.admin_user_delete, name='user_delete'),

    # Group
    url(r'group/list', group.group_list, name='group_list'),
    url(r'group/add', group.group_add, name='group_add'),
    url(r'group/change', group.group_change, name='group_change'),
    url(r'group/delete', group.group_delete, name='group_delete'),
    url(r'group/detail', group.group_detail, name='group_detail'),

    # Permission
    url(r'permission/list', permission.perm_list, name='permission_list'),

]