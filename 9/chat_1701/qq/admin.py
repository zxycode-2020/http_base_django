#coding:utf8
from django.contrib import admin

# Register your models here.
from models import UserProfile

admin.site.register(UserProfile) #注册用户扩展表到后台