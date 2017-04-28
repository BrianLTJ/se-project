'''

API url for user

'''
from django.conf.urls import url
from user import user_login

urlpatterns = [
    url(r'login$', user_login.user_login, name='user_login'),
    url(r'logout$', user_login.user_logout, name='user_logout'),
    url(r'loginstate$', user_login.user_login_state, name='user_login_state'),
]