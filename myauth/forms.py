#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time: 2017-11-19
@Desc:
@Author: sendal
@Email: <schangech@gmail.com>
@Version: 0.0.1
'''

from django.forms import ModelForm

from .models import User


class UserDetailForm(ModelForm):

    class Meta:
        # 关联数据库模型，用户模型
        model = User
        # 前端显示，可以修改的字段
        fields = ('username', 'qq', 'wechat', 'is_superuser',
                  'status', 'company', 'telephone', 'first_name',
                  'last_name', 'avatar', 'email', 'url')
