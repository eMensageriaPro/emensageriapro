# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1035', '0004_auto_20181213_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1035alteracao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1035alteracaonovavalidade',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1035exclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1035inclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
