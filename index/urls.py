from django.conf.urls import url
from index import views as index_views


urlpatterns = [
    url(r'^', index_views.index_index),
]
