# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2017/9/27 上午11:43'

from django.conf.urls import url
from activitys import views

urlpatterns = [
    url(r'^activitys/$', views.activitys_list),
    url(r'^activitys/(?P<pk>[0-9]+)/$', views.activitys_detail),
]