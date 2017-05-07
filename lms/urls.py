"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from rest_framework import routers, serializers, viewsets


urlpatterns = [

    url(r'^api/book/', include('book.urls', namespace='book', app_name='book')),
    url(r'^api/admin/', include('user.urls_admin', namespace='admin', app_name='api_admin_user')),
    url(r'^api/user/', include('user.urls_user', namespace='login', app_name='api_user')),
    url(r'^admin',include('index.admin_urls', namespace='admin_urls', app_name='admin')),
    url(r'^center', include('index.urls_center', namespace='center_urls', app_name='center_urls')),
    url(r'^error/', include('index.error_urls', namespace='error_urls', app_name='error_urls')),
    url(r'^', include('index.urls', namespace="index", app_name='index')),
]
