# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0027_auto_20190620_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='name',
            field=models.CharField(default='admin', max_length=120),
            preserve_default=False,
        ),
    ]
