from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1(request):
    return render(request,'test1.html')

def test2(request):
    return render(request,'test2.html')

def test3(request):
    return HttpResponse('the first string')