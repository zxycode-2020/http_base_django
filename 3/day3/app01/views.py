#coding:utf8
from django.template import Template,Context
from django.shortcuts import render
import datetime

# Create your views here.

class Human(object):
    name = '人类'
    age = 10000
    def sayhello(self):
        return 'Hello Goodbye'

def index(reuqest):
    title = 'title'
    content = 'content'
    time = datetime.datetime.now() # 当前系统时间
    # print type(time)
    # ls = ['python','php','java']
    ls = []
    info = {
        'name':'alice',
        'age':18,
    }
    h1 = Human()
    citys = [ # 大列表，里边每一项是一个字典
        {'黑龙江':['哈尔滨','大庆','肇东']}, #省 和城市的字典
        {'北京':['朝阳','海淀','昌平']},
    ]
    a = 100
    b = 1
    link = 'how old are you we lkweljlkwe'
    context = {
        'title' : title,
        'content' : content,
        'time' : time,
        'language' : ls,
        'info': info,
        'h1':h1,
        'citys':citys,
        'a' : a,
        'b' : b,
        'link':link
    }

    return render(reuqest,'app01/index.html',context)

def demo1(request):
    tpl = Template('{{name}}--{{age}}')
    info = {
        'name':'啦啦啦',
        'age':18,
    }
    c = Context(info)
    html = tpl.render(c)
    return html