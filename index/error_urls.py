from django.conf.urls import url
from index import error_views


urlpatterns = [
    url(r'404$', error_views.error_404),
    url(r'403$', error_views.error_403),
]


