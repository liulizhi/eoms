#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time: 2017-11-19
@Desc:
@Author: sendal
@Email: <schangech@gmail.com>
@Version: 0.0.1
'''

from . import views
from django.conf.urls import patterns, url


urlpatterns = patterns('myauth.views',
    url(r'^list/$', views.userList, name='user_list'),
    url(r'^profile/$', views.account_profile, name='account_profile'),

)
