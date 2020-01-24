#coding:utf8
from django import template
import datetime

register = template.Library() # 实例化register对象  注册模板标签用的

@register.simple_tag
def tag1(v1 ,v2):
    return v1 + v2

@register.simple_tag
def nowtime():
    return datetime.datetime.now().strftime('%Y-%m-%d')