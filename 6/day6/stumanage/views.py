#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# Create your views here.
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Q
import models

def index(request):
    wd = request.GET.get('wd',None)
    order = request.GET.get('order',None)
    rule = request.GET.get('rule',None)
    pn = request.GET.get('pn',1)

    # pn 不是数字，pn转成整形
    try:
        pn = int(pn)
    except Exception as e:
        pn = 1

    #搜索功能处理
    # models.Student.objects.all()
    if wd is not None:
        # 一个Q就是一个条件 然后用并集操作符连接
        condition = Q(name__icontains=wd) | Q(score__icontains=wd) | Q(age__icontains=wd) | Q(email__icontains=wd) | Q(cls__name__icontains=wd)
        stus = models.Student.objects.filter(condition)
        # 学霸做的
        # a = models.Student.objects.filter(name__icontains=wd)
        # b = models.Student.objects.filter(score__icontains=wd)
        # stus = a | b
    else:
        stus = models.Student.objects.all()

    #排序规则处理
    if order is not None:
        if rule == 'u': # 升序
            stus = stus.order_by(order)
        else: #降序
            stus = stus.order_by(order).reverse() #列表反响排序

    # 分页
    try:
        paginator = Paginator(stus,20) #返回一个分页对象，p1:Queryset p2:每页记录条数
        stus = paginator.page(pn) # 获取某一页的记录
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        print e

    # 分页数字生成
    page_nums = range(pn - 2,pn + 3)


    context = {
        'index' : 'active',
        'stus' : stus,
        'page_nums' : page_nums
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
        models.Student.objects.filter()
        return HttpResponseRedirect('/')

    else:
        stu = models.Student.objects.get(id=sid) # 获取要修改的学生对象
        classes = models.Class.objects.all()
        return render(request,'stumanage/stu_add.html' ,{'stu':stu,'classes':classes})