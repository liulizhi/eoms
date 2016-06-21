#-*- coding:utf-8 -*-
'''
Created on 2016/6/19

@author: QiRui.Su schangech@gmail.com
'''

from django import forms
from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView
from models import Host, Machine_Room
from bbs.models import BBS_user

import django.utils.timezone as timezone

#自定义form表单
#class HostForm(forms.Form):
#继承关联ORM定义的Model数据表单
class HostForm(ModelForm):
    ipaddr = forms.CharField(label=(u'IP地址'), max_length=50, required=False)
#   返回字典格式
#    mroom_list = Machine_Room.objects.values('name')
#   返回元祖格式
    mroom_list = Machine_Room.objects.values_list('name')
    kv_mroom = map(lambda mr:(mr[0], mr[0]+"--------Machine Room-------"), mroom_list)
    #mroom = forms.MultipleChoiceField(label=(u'机房位置'), required=False, choices=kv_mroom, widget=forms.SelectMultiple(attrs={'data-rel': 'chosen'}))
    mroom = forms.ChoiceField(label=(u'机房位置'), required=False, choices=kv_mroom, widget=forms.Select(attrs={'data-rel': 'chosen'}))
    class Meta:  
        model = Host
        fields = ['ipaddr', 'hostname', 'status', 'opersys', 'supporter', 'mroom']
