# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1080', '0004_auto_20181213_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1080alteracao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1080alteracaonovavalidade',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1080exclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1080inclusao',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
