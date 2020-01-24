#coding:utf8
from django.db import models

# Create your models here.

class Student(models.Model): # 一定要继承
    name = models.CharField(max_length=30) # 字符型
    age = models.IntegerField(default=16) # 整形
    pub_date = models.DateTimeField(auto_now_add=True) # 时间日期字段，自动添加系统当前时间

# 自己设计班级表 兴趣小组表