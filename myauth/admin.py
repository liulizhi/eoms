#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time: 2017-11-19
@Desc:
@Author: sendal
@Email: <schangech@gmail.com>
@Version: 0.0.1
'''

from django.contrib import admin
from models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'qq', 'wechat', 'is_superuser',
                  'status', 'company', 'telephone', 'first_name',
                  'last_name', 'avatar', 'email', 'url')
    list_filter = ('username', 'qq', 'wechat', 'is_superuser',
                  'status', 'company', 'telephone', 'first_name',
                  'last_name', 'avatar', 'email', 'url')

admin.site.register(User, UserAdmin)