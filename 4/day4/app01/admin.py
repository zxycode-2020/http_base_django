#coding:utf8
from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Student) # 注册数据模型到django admin后台
admin.site.register(models.Class)