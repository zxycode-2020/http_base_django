#coding:utf8
from django.shortcuts import render,HttpResponse
# Create your views here.

def index(request):
    rep = HttpResponse()
    if not request.COOKIES.get('p1',None):
        rep.set_cookie('p1',1)
    else:
        print request.COOKIES['p1']
    rep.content = 'ok'
    return rep # 响应

def article(request,aid):
    return HttpResponse('article id : %s' % aid)