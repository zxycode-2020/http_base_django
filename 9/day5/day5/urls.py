#coding:utf8
"""day5 URL Configuration

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
from stumanage import views
from django.views.static import serve # 处理媒体文件的API
from django.conf import settings # 把django 的配置文件导入进来

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^stu_del/$', views.stu_del,name='stu_del'),
    url(r'^stu_add/$', views.stu_add,name='stu_add'),
    url(r'^stu_edit/$', views.stu_edit,name='stu_edit'),
    url(r'^login/$', views.login,name='login'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^reg/$', views.reg,name='reg'),
    url(r'^config/$', views.config,name='config'), # 系统配置路由
    url(r'^checkname/$', views.checkname,name='checkname'), # 系统配置路由

    #写一个媒体文件的url 并且用serve函数处理 指定媒体文件的路径
    url(r'^upload/(.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]
