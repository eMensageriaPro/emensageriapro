# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2060', '0006_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r2060infoproc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2060infoproc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2060tipoajuste',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2060tipoajuste',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2060tipocod',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2060tipocod',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='r2060infoproc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2060infoproc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2060tipoajuste',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2060tipoajuste',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2060tipocod',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2060tipocod',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
