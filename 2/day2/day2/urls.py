"""day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from app01 import views
from app01 import urls as app01_urls
from app02 import urls as app02_urls
from app03 import urls as app03_urls

urlpatterns = [
    #url(r'^$', views.article,name='index'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^article/(?P<aid>\d+)/(?P<name>\w+)/(?P<age>\d+)/$', views.article,name='article'),
    url(r'^app01/',include(app01_urls,namespace='app01')),
    url(r'^app02/',include(app02_urls,namespace='app02')),
    url(r'^app03/',include(app03_urls,namespace='app03'))
]
