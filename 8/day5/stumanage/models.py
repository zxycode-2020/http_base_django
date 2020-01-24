#coding:utf8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='学生姓名',max_length=20) # 字符类型
    age = models.IntegerField(verbose_name='学生年龄') # 整形
    score = models.DecimalField(verbose_name='成绩',max_digits=5,decimal_places=2,null=True,blank=True) # 浮点型
    email = models.EmailField(verbose_name='邮箱',null=True,blank=True)
    add_date = models.DateTimeField(verbose_name='添加日期',auto_now_add=True)
    cls = models.ForeignKey('Class')
    # 如果用ImageField字段类型 你需要安装Pillow模块  pip install Pillow
    # upload_to ： django-admin 上传路径
    avatar = models.ImageField(verbose_name='头像',upload_to='avatar/',default='avatar/default.jpg')
    group = models.ManyToManyField('Group') # 跟group表建立多对多关系
    #给对象起别名
    def __unicode__(self):
        return self.name

    # 内部类 对表的一些配置
    class Meta:
        verbose_name = verbose_name_plural =  '学生'

class Class(models.Model): # 班级表
    name = models.CharField(verbose_name='班级名称',max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '班级'

class UserProfile(models.Model):
    phone = models.CharField(verbose_name='手机', max_length=20)
    nick = models.CharField(max_length=30)
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = verbose_name_plural = '用户信息'

    def __unicode__(self):
        return self.nick

class Group(models.Model):
    name = models.CharField(verbose_name='小组名称',max_length=30)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = '兴趣小组'
