# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(max_length=50, null=True, verbose_name='\u516c\u53f8', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500, null=True, verbose_name='\u5bc6\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(max_length=100, null=True, verbose_name='\u52a0\u76d0', blank=True),
        ),
    ]
