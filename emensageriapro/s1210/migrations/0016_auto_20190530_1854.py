# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1210', '0015_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1210detpgtoant',
            name='codcateg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='tpbcirrf',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='codcateg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='codpais',
            field=models.TextField(null=True),
        ),
    ]
