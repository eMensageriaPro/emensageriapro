# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2099', '0006_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r2099iderespinf',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2099iderespinf',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]