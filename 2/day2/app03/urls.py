from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^link/$', views.link , name='link'),
    url(r'^new_link/$', views.new_link, name='new_link'),
]
