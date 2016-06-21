# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bbs',
            options={'verbose_name': '\u8bba\u575b\u5217\u8868', 'verbose_name_plural': '\u8bba\u575b\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='bbs_user',
            options={'verbose_name': '\u8bba\u575b\u8d26\u53f7', 'verbose_name_plural': '\u8bba\u575b\u8d26\u53f7'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u8bba\u575b\u7c7b\u522b', 'verbose_name_plural': '\u8bba\u575b\u7c7b\u522b'},
        ),
    ]
