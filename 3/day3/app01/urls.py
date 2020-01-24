from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^demo1/$', views.demo1),
]
