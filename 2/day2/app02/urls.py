from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^test', views.test1,name='test1'),
    url(r'^test2', views.test2,name='test2'),
    url(r'^args/$', views.args,name='test2'),
]