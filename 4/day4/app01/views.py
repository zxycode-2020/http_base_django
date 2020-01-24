#coding:utf8
from django.shortcuts import render,HttpResponse

# Create your views here.
import models

def index(request):
    return HttpResponse('ok')

def add(request):
    # 增加记录第一种
    # s1 = models.Student()
    # s1.name = '小美'
    # s1.age = 19
    # s1.email = '423'
    # s1.score = 99.99
    # s1.save()’

    # 增加第二种
    # models.Student(name='小兰',age='16').save()

    # 第三种
    #models.Student.objects.create(name='小明',age=8,score=99.99)

    # 第四种
    # stu_info = {
    #     'name':'小缘',
    #     'age':6,
    #     'score':111.99,
    #     'email' : 'xiaoyuan@qq.com',
    # }
    # models.Student.objects.create(**stu_info)

    #删除
    # models.Student.objects.filter(pk=7).delete() # 删除返回值None

    #更新
    # 第一
    #res = models.Student.objects.filter(pk=2).update(score=300,email='xiaofang@qq.com') #返回影像记录行数

    # 第二
    # xiaofang = models.Student.objects.get(pk=1) # 获取单条记录
    # xiaofang.score = 600
    # xiaofang.save()

    #查询单条
    # xiaofang = models.Student.objects.get(pk=1) # 获取单条记录

    #查询多条
    # stus = models.Student.objects.all() #返回queryset类型 可以被迭代
    # for stu in stus:
    #     print stu.name,stu.age,stu.score

    # stus = models.Student.objects.filter().all()[:5] # limit 语句
    # print stus
    # print stus.query # 返回执行的sql语句

    # 精准查找
    # models.Student.objects.filter(name='小美')
    # models.Student.objects.filter(name__exact='小美')

    # 忽略大小写
    # stus = models.Student.objects.filter(name__iexact='xiaomei')
    # print stus

    # 模糊查询
    # stu = models.Student.objects.filter(name__contains='xiao') # 不忽略大小写
    # print stu
    # stu = models.Student.objects.filter(name__icontains='xiao') # 忽略大小写
    # print stu

    #正则匹配法
    # stu = models.Student.objects.filter(name__regex='^x')
    # print stu
    # stu = models.Student.objects.filter(name__iregex='^x')
    # print stu

    # 大于 小于
    # stu = models.Student.objects.filter(age__gt=17, age__lt=19)
    # print stu

    # in 一个集合中的所有
    # stu = models.Student.objects.filter(age__in=(18,17,16))
    # print stu

    # stus = models.Student.objects.all().order_by('age') 升序
    # stus = models.Student.objects.all().order_by('-age') #升序
    # stus = models.Student.objects.all().order_by('-age','id') #升序
    # for stu in stus:
    #     print stu.age,stu.id

    # 外键添加
    # cls2 = models.Class.objects.get(pk=2)
    # # 第一种
    # stu_info = {
    #     'name' : '大大美',
    #     'age' :  30,
    #     'cls' : cls2,
    # }
    # # 第二种
    # stu_info = {
    #     'name' : '大大美',
    #     'age' :  30,
    #     'cls_id' : 3,
    # }
    # models.Student.objects.create(**stu_info)

    # 指定字段查询
    # 第一种
    # stus = models.Student.objects.values('name','age').all()
    # stus
    # print stus

    # 第二种
    # stus = models.Student.objects.values_list('name','age','score').all()
    # print stus

    # 连表查询
    # 第一种
    # stus = models.Student.objects.all()
    # for stu in stus:
    #     print stu.name,stu.cls.id,stu.cls.name

    # 第二种 : 牛逼的双下划线(跨表)
    #stus = models.Student.objects.values('name','cls__name').all()


    # 查询一个班级所有学生，执行两次sql语句
    # cls1 = models.Class.objects.get(name='1701')
    # stus = models.Student.objects.filter(cls=cls1)
    # print stus

    # 查询一个班级所有学生，执行一次sql语句
    # stus = models.Student.objects.filter(cls__name='1701').all().values('name','cls__name')
    # print stus

    # 查询一个班级所有学生，起始表从班级表开始查询,反向查询
    # stus = models.Class.objects.get(name='1702').student_set.all()
    # print stus

    # 按照分数查询 大于100分
    # print models.Student.objects.filter(score__gt=100).all()

    return HttpResponse('ok')