from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def test3(request):
    return render(request,'test3.html')

def test4(request):
    return render(request,'test4.html')

def test5(request):
    return HttpResponse('the second  string')