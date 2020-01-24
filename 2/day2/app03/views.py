#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username',None) # 获取表单提交数据 username就是input标签中的name值
        password = request.POST.get('password',None)
        gender = request.POST.get('sex',None)
        # interest = request.POST.get('interest',None)
        interest = request.POST.getlist('interest',None)
        print interest
        return HttpResponse(gender)

        # 模拟用户登录验证
        # username = request.POST.get('username',None) # 获取表单提交数据 username就是input标签中的name值
        # password = request.POST.get('password',None)
        # if username == 'dachui' and password == '123':
        #     return HttpResponse('登陆成功')
        # else:
        #     return HttpResponse('登录失败')
    elif request.method == "GET":
        return render(request,'app03/reg.html')
    else:
        return HttpResponse('fuck off')

def link(request):
    return HttpResponseRedirect('/app03/new_link/')

def new_link(request):
    return HttpResponse('new link ok')