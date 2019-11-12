# coding:utf-8
from django.shortcuts import render, get_object_or_404
from home.models import Article
from django.http import HttpResponse, Http404


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


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'home/article.html', context={'article': article})
    # try:
    #     article = Article.objects.get(pk=id)
    # except Article.DoesNotExist:
    #     raise Http404
    #     # article = get_object_or_404(Article, pk=id)
    # return render(request, 'home/article.html', context={'article': article})
