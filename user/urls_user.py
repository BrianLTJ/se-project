'''

API url for user

'''
from django.conf.urls import url
from user import user_login, user_center


urlpatterns = [
    url(r'login$', user_login.user_login, name='user_login'),
    url(r'logout$', user_login.user_logout, name='user_logout'),
    url(r'loginstate$', user_login.user_login_state, name='user_login_state'),

    url(r'borrowlog$', user_center.current_user_borrowlog, name='user_borrow_log'),
    url(r'userinfo$', user_center.get_userinfo, name='user_info'),
    url(r'userchangepsw$',user_center.change_password, name='user_changepassword'),
]

