#-*- coding:utf-8 -*-
from django.db import models
from bbs.models import BBS_user

import django.utils.timezone as timezone

class Host(models.Model):
    
    STATUS_CHOICE = (
                 (0, '线上'),
                 (1, '下线'),
                 )    
    
    OPERSYS_CHOICE = (
                      (0, 'CentOS6.5'),
                      (1, 'RedHat7'),
                      (2, 'Ubuntu12'),
                      (3, 'Windows2008'),
                      )
    
    ipaddr = models.GenericIPAddressField()
    hostname = models.CharField(u'主机名', max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICE,
                                 default=0)
    opersys = models.IntegerField(choices = OPERSYS_CHOICE,
                                  default=0)
    supporter = models.ForeignKey(BBS_user)
    mroom = models.ForeignKey(u'Machine_Room')
    adddate = models.DateTimeField(default = timezone.now)
    updatedate = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = u'IP列表'
        verbose_name_plural = verbose_name
        
    def __unicode__(self):
        return self.hostname

class Machine_Room(models.Model):
    name = models.CharField(u'机房', max_length=20)
    address = models.CharField(u'地址', max_length=200)
    telphone = models.IntegerField(u'联系人')
    email = models.EmailField(u'邮箱')
    overtime = models.DateTimeField(u'到期时间')
    
    class Meta:
        verbose_name = u'机房信息'
        verbose_name_plural = verbose_name
        
    def __unicode__(self):
        return self.name
    
    
    



