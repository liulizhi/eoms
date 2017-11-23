#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time: 2017-11-19
@Desc:
@Author: sendal
@Email: <schangech@gmail.com>
@Version: 0.0.1
'''

import uuid

from django.db import models
from django.utils import timezone
# from imagekit.processors import ResizeToFill
# from imagekit.models import ProcessedImageField


class MyUUID(models.Model):
    #
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class User(models.Model):
    STATUS_CHOICE = (
        (0, 'enabled'),
        (1, 'disabled'),
        (2, 'removed')
        )
    # 定义用户表结构
    id = MyUUID()
    username = models.CharField(u'用户名', max_length=20)
    is_superuser = models.BooleanField(u'是否超级管理员', default=True)
    status = models.IntegerField(u'状态', choices=STATUS_CHOICE,
                                 default=0)
    company = models.CharField(blank=True, null=True,
                               verbose_name=u'公司', max_length=50)
    telephone = models.CharField(u'电话号码', max_length=20)
    wechat = models.CharField(u'微信', max_length=20)
    qq = models.CharField(verbose_name=u'QQ', blank=True,
                          null=True, max_length=20)
    first_name = models.CharField(u'名字', max_length=20)
    last_name = models.CharField(u'姓氏', max_length=20)
    avatar = models.ImageField(upload_to='avatar',
                               verbose_name=u'头像',
                               default='avatar/icon.jpg')
    email = models.EmailField(u'邮箱', max_length=100)
    salt = models.CharField(u'加盐', blank=True, null=True, max_length=100)
    password = models.CharField(u'密码', blank=True, null=True, max_length=500)
    url = models.URLField(max_length=100, blank=True,
                          null=True, verbose_name='个人网页地址')
    #
    register_time = models.DateTimeField(default = timezone.now)
    last_login_time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = u'用户信息列表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
