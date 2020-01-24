from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'app02/index.html')

def article(request):
    return render(request,'app02/article.html')