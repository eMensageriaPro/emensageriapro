# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2040', '0004_auto_20181213_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2040infoproc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r2040inforecurso',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='r2040recursosrep',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
