#coding:utf8
from django.shortcuts import render,HttpResponse

# Create your views here.

def cookie(request):
    # 设置普通cookie
    # print request.COOKIES,type(request.COOKIES) #获取cookie 和 cookie类型（字典）
    # rep.set_cookie('test3','test3',max_age=60) #向浏览器设置cookie max_age 过期时间 ,path=设置cookie的有效路径
    # return rep

    # 设置带签名的cookie
    # rep = HttpResponse('ok')
    # rep.set_signed_cookie('alice','kami',salt='123')

    # 获取带签名的cookie
    # alice = request.get_signed_cookie('alice',default=None,salt='123')
    # print alice
    return HttpResponse('ok')
