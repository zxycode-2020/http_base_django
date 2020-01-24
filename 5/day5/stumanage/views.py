#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
import models

def index(request):
    stus = models.Student.objects.all() # QuerySet类型可以被直接遍历

    context = {
        'index' : 'active',
        'stus' : stus,
    }
    return render(request, 'stumanage/index.html',context)

#删除学生业务处理
def stu_del(request):
    return HttpResponse('ok')

#添加学生业务处理
def stu_add(request):
    if request.method == 'POST':
        cid = request.POST.get('cls',None)
        print cid
        return HttpResponseRedirect('/')
    else:
        classes = models.Class.objects.all()
        context = {
            'manage' : 'active',
            'classes' : classes,
        }
        return render(request,'stumanage/stu_add.html',context)