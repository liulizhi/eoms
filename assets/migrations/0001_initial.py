# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20160619_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddr', models.GenericIPAddressField()),
                ('hostname', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u540d')),
                ('status', models.IntegerField(default=0, choices=[(0, b'\xe7\xba\xbf\xe4\xb8\x8a'), (1, b'\xe4\xb8\x8b\xe7\xba\xbf')])),
                ('opersys', models.IntegerField(default=0, choices=[(0, b'CentOS6.5'), (1, b'RedHat7'), (2, b'Ubuntu12'), (3, b'Windows2008')])),
                ('adddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'IP\u5217\u8868',
                'verbose_name_plural': 'IP\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Machine_Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u673a\u623f')),
                ('address', models.CharField(max_length=200, verbose_name='\u5730\u5740')),
                ('telphone', models.IntegerField(verbose_name='\u8054\u7cfb\u4eba')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('overtime', models.DateTimeField(verbose_name='\u5230\u671f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u623f\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='mroom',
            field=models.ForeignKey(to='assets.Machine_Room'),
        ),
        migrations.AddField(
            model_name='host',
            name='supporter',
            field=models.ForeignKey(to='bbs.BBS_user'),
        ),
    ]
