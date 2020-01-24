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
    sid = request.GET.get('sid',None)
    if sid is not None:
        models.Student.objects.filter(id=sid).delete()  # 删除操作
        return HttpResponseRedirect('/') # 重定向到首页
    return HttpResponse('ok')

#添加学生业务处理
def stu_add(request):
    if request.method == 'POST':
        name = request.POST.get('name',None) #班级ID
        age = request.POST.get('age',None) #班级ID
        score = request.POST.get('score',None) #班级ID
        email = request.POST.get('email',None) #班级ID
        cls_id = request.POST.get('cls',None) #班级ID

        stu_info = {
            'name' : name,
            'age' : age,
            'score' : score,
            'email' : email,
            'cls_id': cls_id
        }

        return HttpResponseRedirect('/')
    else:
        classes = models.Class.objects.all()
        context = {
            'manage' : 'active',
            'classes' : classes,
        }
        return render(request,'stumanage/stu_add.html',context)

#修改的业务逻辑处理
def stu_edit(request):
    sid = request.GET.get('sid',None) # 获取要修改的学生id
    if request.method == 'POST':
        name = request.POST.get('name',None) #班级ID
        age = request.POST.get('age',None) #班级ID
        score = request.POST.get('score',None) #班级ID
        email = request.POST.get('email',None) #班级ID
        cls_id = request.POST.get('cls',None) #班级ID

        stu_info = {
            'name' : name,
            'age' : age,
            'score' : score,
            'email' : email,
            'cls_id': cls_id
        }
        models.Student.objects.filter(id=sid).update(**stu_info)
        return HttpResponseRedirect('/')

    else:
        stu = models.Student.objects.get(id=sid) # 获取要修改的学生对象
        classes = models.Class.objects.all()
        return render(request,'stumanage/stu_add.html' ,{'stu':stu,'classes':classes})