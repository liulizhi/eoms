#-*- coding:utf-8 -*-
from django.db import models

import django.utils.timezone as timezone

from django.contrib.auth.models import User
    
from ckeditor.fields import RichTextField


    
class Category(models.Model):
    name = models.CharField(max_length=32, unique = True)
    user = models.ForeignKey('BBS_user')
    
    class Meta:
        verbose_name = u'论坛类别'
        verbose_name_plural = verbose_name
    

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='This guy is lazy, nothing')
    photo = models.ImageField() 
    models.ImageField(upload_to="upload_img/", default="upload_img/user-1.jpg")
    
    class Meta:
        verbose_name = u'论坛账号'
        verbose_name_plural = verbose_name
        
    def __unicode__(self):
        return self.user.username
    
    signature.short_Description = '开发者账号描述'

class Bbs(models.Model):
    title = models.CharField(max_length=64)
    summary = models.TextField(default='Lazy, nothing')
    content = models.TextField()
    content = RichTextField(u'文章正文')
    author = models.ForeignKey(BBS_user)
    view_count = models.IntegerField(default='0')
    ranking = models.IntegerField(default='0')
    create_date = models.DateTimeField(default = timezone.now)
    updated_date = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = u'论坛列表'
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.title