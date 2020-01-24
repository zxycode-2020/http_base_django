#coding:utf8
"""poll_1701 URL Configuration

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
from poll import views as poll_views
from cookie import views as cookie_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', poll_views.index,name='index'), # 首页路由地址
    url(r'^detail/(?P<qid>\d+)/$', poll_views.detail,name='detail'), # 详情路由地址
    url(r'^vote/(?P<qid>\d+)/$', poll_views.vote,name='vote'), # 投票业务逻辑处理路由地址
    url(r'^cookie/$', cookie_views.cookie,name='vote'), # 投票业务逻辑处理路由地址
]
