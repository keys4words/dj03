from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(dir(request))
    return HttpResponse('Hello Max')

def test(request):
    return HttpResponse('<h2>Test page</h2>')
