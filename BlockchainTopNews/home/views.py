# coding:utf-8
from django.shortcuts import render
from home.models import Article
from django.http import HttpResponse


# Create your views here.


# Create your views here.
# def index(request):
#     return HttpResponse("欢迎来到链圈头条!")


# def index(request):
#     return render(request, 'home/index.html', context={
#         'title': '链圈头条', 'text': '欢迎进入链圈头条'
#     })


def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'home/index.html', context={'articles': articles})
