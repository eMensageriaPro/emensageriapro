# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0023_auto_20180822_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retornoseventoshorarios',
            name='hrentr',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventoshorarios',
            name='hrsaida',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosintervalos',
            name='iniinterv',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosintervalos',
            name='terminterv',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
