'''

API url for admin

'''
from django.conf.urls import url
from user import user_admin as user_admin

urlpatterns = [
    url(r'user/add', user_admin.admin_user_add, name='user_add'),
]