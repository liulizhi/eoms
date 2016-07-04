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
from django.contrib.auth.models import User

import django.utils.timezone as timezone

#自定义form表单
#class HostForm(forms.Form):
#继承关联ORM定义的Model数据表单
class HostForm(ModelForm):
    HOST_STATUS = {
                  (1, '线上'),
                  (0, '线下'),
                  }
    OPER_SYS = {
                (0, 'CentOS6.5 x86_64'),
                (1, 'RedHat5.8 x86_64'),
                (2, 'Ubuntu11 x86 Server'),
                (3, 'Debian11 x86_64'),
                (4, 'Suse8 x86_64'),
                }
    ipaddr = forms.CharField(label=(u'IP地址'), max_length=50, required=False, widget=forms.TextInput(attrs={'type': "text", 'class': 'form-control', "placeholder":"218.30.110.192", 'style':'width:180px;height:30px'}))
    hostname = forms.CharField(label=(u'主机名'), max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"sjhl-o-hc01v", 'style':'width:180px;height:30px'}))
    status = forms.ChoiceField(label=(u'主机状态'), required=False, choices=HOST_STATUS, widget=forms.Select(attrs={'data-rel': 'chosen', 'style':'width:100px;'}))
    opersys = forms.ChoiceField(label=(u'操作系统选择'), required=False, choices=OPER_SYS, widget=forms.Select(attrs={'data-rel': 'chosen', 'style':'width:200px;'}))
    
    user_list = User.objects.values_list('username')
    kv_user = map(lambda mr:(mr[0], mr[0]), user_list)
    supporter = forms.ChoiceField(label=(u'运维负责人'), required=False, choices=kv_user, widget=forms.Select(attrs={'class':'control-label','data-rel': 'chosen', 'style':'width:100px;'}))
    
#   返回字典格式
#    mroom_list = Machine_Room.objects.values('name')
#   返回元祖格式
    mroom_list = Machine_Room.objects.values_list('name')
    kv_mroom = map(lambda mr:(mr[0], mr[0]), mroom_list)
    #mroom = forms.MultipleChoiceField(label=(u'机房位置'), required=False, choices=kv_mroom, widget=forms.SelectMultiple(attrs={'data-rel': 'chosen'}))
    mroom = forms.ChoiceField(label=(u'机房位置'), required=False, choices=kv_mroom, widget=forms.Select(attrs={'data-rel': 'chosen', 'style':'width:150px;'}))
    class Meta:  
        model = Host
        fields = ['ipaddr', 'hostname', 'status', 'supporter', 'mroom', 'opersys']


    def clean_supporter(self):
        user = User.objects.get(username=self.cleaned_data['supporter'])
        print user
        return BBS_user.objects.get(user = user)
    
    def clean_mroom(self):
        return Machine_Room.objects.get(name=self.cleaned_data['mroom'])
    
    
    
    
    
    
    