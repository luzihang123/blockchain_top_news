# coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("欢迎来到链圈头条!")


def index(request):
    return render(request, 'home/index.html', context={
        'title': '链圈头条', 'text': '欢迎进入链圈头条'
    })
