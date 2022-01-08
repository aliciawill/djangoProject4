from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def page1Function(request):
    print('내가 호출됨.@@')
    #return HttpResponse('hello')
    return render(request, "app1/css_test.html")

