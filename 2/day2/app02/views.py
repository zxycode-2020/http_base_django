#coding:utf8
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print request.path
    print request.method
    print request.GET
    print request.POST
    #print request.GET.get('name','小妹')
    print request.COOKIES
    print request.session
    print request.is_ajax()
    return render(request,'app02/index.html')

def test1(request):
    return HttpResponse('test1 ok')

def test2(request):
    return HttpResponse('test2 ok')

def args(request):
    name = request.GET.get('name',None)
    age = request.GET.get('age',None)
    context = {
        'name':name,
        'age':age,
    }
    return render(request,'app02/args.html',context)
    #return HttpResponse(u'姓名:%s<br>年龄:%s' % (name,age))