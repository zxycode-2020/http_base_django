from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^article/(?P<aid>\d+)/$', views.article,name='article'),
]