from django.conf.urls import url
from index import views_center

urlpatterns = [
    url(r'/borrowlog$', views_center.center_borrowlog),
    url(r'/changepsw$', views_center.center_changepsw),
    url(r'$', views_center.center_index),
]