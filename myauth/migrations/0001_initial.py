# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUID',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='\u662f\u5426\u8d85\u7ea7\u7ba1\u7406\u5458')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, b'enabled'), (1, b'disabled'), (2, b'removed')])),
                ('company', models.CharField(max_length=20, null=True, verbose_name='\u516c\u53f8', blank=True)),
                ('telephone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('wechat', models.CharField(max_length=20, verbose_name='\u5fae\u4fe1')),
                ('qq', models.CharField(max_length=20, null=True, verbose_name='QQ', blank=True)),
                ('first_name', models.CharField(max_length=20, verbose_name='\u540d\u5b57')),
                ('last_name', models.CharField(max_length=20, verbose_name='\u59d3\u6c0f')),
                ('avatar', models.ImageField(default=b'media/avatar/default.png', upload_to=b'media/avatar', verbose_name='\u5934\u50cf')),
                ('email', models.EmailField(max_length=20, verbose_name='\u90ae\u7bb1')),
                ('salt', models.CharField(max_length=20, verbose_name='\u52a0\u76d0')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
                ('url', models.URLField(max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u5217\u8868',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f\u5217\u8868',
            },
        ),
    ]
