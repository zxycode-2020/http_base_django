#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
import models

#首页
def index(request):
    questions = models.Question.objects.all() # 获取所有投票美容
    return render(request,'index.html',{'questions':questions})

def detail(request,qid):
    question = models.Question.objects.get(pk=qid) #获取某一个投票

    return render(request,'detail.html',{'question':question})

def vote(request,qid):
    is_polled = request.COOKIES.get('is_polled',None) #获取是否投票的cookie
    if is_polled is None: # 如果是None 就是没投过票
        question = models.Question.objects.get(pk=qid) #获取某一个投票
        # 把相应选项的票数+1 再存入到数据库当中
        cid = request.POST.get('cid',None)
        if cid is not None:
            choice = models.Choice.objects.get(pk=cid) #获取相应投票选项
            choice.votes += 1 # 票数+1操作
            choice.save() # 存入数据库中

            rep = render(request,'result.html',{'question':question}) # 返回一个响应对象
            rep.set_cookie('is_polled',1,max_age=3600*24*365) # 设置投票cookie  过期时间1年
            return rep
        else:
            return HttpResponseRedirect('/')
    else: #投过票
        return HttpResponse('you have already voted?')

