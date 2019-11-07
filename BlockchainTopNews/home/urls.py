# -*- coding:utf-8 -*-
# @Author: clark
# @Time: 2019-11-08 00:24
# @File: urls.py
# @project demand:
# coding:utf-8
from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
