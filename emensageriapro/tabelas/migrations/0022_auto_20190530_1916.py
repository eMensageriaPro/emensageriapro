# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0021_auto_20190530_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcoes',
            name='opcoes_slug',
            field=models.CharField(max_length=250),
        ),
    ]
