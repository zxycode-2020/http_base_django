from django.shortcuts import render,HttpResponse

# Create your views here.

def csrf(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.get('name'))
    return render(request,'csrf.html')