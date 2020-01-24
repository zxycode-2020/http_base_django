#coding:utf8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# Create your views here.
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger # 引入分页处理类和异常类
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import auth # 登录 推出 验证
from django.db.models import Q
from django.contrib.auth.models import User
import models

@login_required
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
        paginator = Paginator(stus,3) #返回一个分页对象，p1:Queryset p2:每页记录条数
        stus = paginator.page(pn) # 获取某一页的记录
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        pn = 1
        stus = paginator.page(pn) # 获取某一页的记录
        print e

    num_pages = stus.paginator.num_pages #获取总页数  7 pn=2

    # 分页数字生成
    if num_pages < 5: # 最大页数小于你想要显示的数字个数
        start = 1
        end = num_pages + 1
    else:  # 最大页数大于等于你想要显示的数字个数
        if pn <= 2: # 页数左边界
            start = 1
            end = 6
        elif pn >= num_pages - 2: #页数右边界
            start = num_pages - 4
            end = num_pages + 1
        else: # 页数不触及边界的情况
            start = pn - 2
            end = pn + 3

    page_nums = range(start,end)

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password:
            user = auth.authenticate(username=username,password=password) #如果验证成功返回用户对象，如果失败返回None
            if user is not None:
                if user.is_active:
                    #做登陆操作
                    auth.login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request,'stumanage/login.html',{'error':'账号已冻结'})
            else:
                return render(request,'stumanage/login.html',{'error':'用户名或密码错误'})
    else:
        return render(request,'stumanage/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def reg(request):
    if request.method == 'POST':
        #收集用户信息
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        nick = request.POST.get('nick','')
        phone = request.POST.get('phone','')

        print username

        if username and password1 and password2:
            if password1 == password2:
                u_count = User.objects.filter(username=username).count()
                if u_count == 0: #没有这个用户名

                    # 添加自带用户表
                    user_info = {
                        'username' : username,
                        'password' : make_password(password1),
                    }
                    user_info = User.objects.create(**user_info)

                    # 添加用户扩展信息
                    user_profile = {
                        'nick' : nick,
                        'phone' : phone,
                        'user' : user_info
                    }

                    models.UserProfile.objects.create(**user_profile)

                    return HttpResponseRedirect('/login/')

                else: #用户名已存在
                    return render(request,'stumanage/reg.html',{'error':'用户名已存在'})
            else:
                return render(request,'stumanage/reg.html',{'error':'两次密码不一样'})

    else:
        return render(request,'stumanage/reg.html')