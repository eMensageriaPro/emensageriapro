# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1280', '0004_auto_20181213_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatropport',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
