from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^manage/$', views.manage,name='manage'),
    url(r'^config/$', views.config,name='config'),
]