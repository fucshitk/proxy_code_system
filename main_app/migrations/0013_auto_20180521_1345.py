# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20180518_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_code',
            name='code',
            field=models.CharField(verbose_name='API用密链', max_length=50, default='xxxx'),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='到期时间', default=datetime.datetime(2018, 5, 21, 13, 45, 2, 656493)),
        ),
        migrations.AlterField(
            model_name='others_info',
            name='TOKEN',
            field=models.CharField(verbose_name='API密链', max_length=15, unique=True, default='J7f8H2I3u5i6Q7'),
        ),
        migrations.AlterField(
            model_name='time_code',
            name='begin_time',
            field=models.DateTimeField(verbose_name='创卡时间', default=datetime.datetime(2018, 5, 21, 13, 45, 2, 659426)),
        ),
    ]
