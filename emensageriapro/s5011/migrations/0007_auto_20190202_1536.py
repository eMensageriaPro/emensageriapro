# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0006_auto_20181213_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infocomplobra',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infosubstpatropport',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5011infotercsusp',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
