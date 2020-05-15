from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    news = News.objects.all()
    title = 'Main page'
    return render(request, 'news/index.html', {'news': news, 'title': title})

