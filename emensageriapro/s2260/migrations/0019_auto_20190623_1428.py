# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-23 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2260', '0018_remove_s2260localtrabinterm_excluido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2260localtrabinterm',
            name='codmunic',
            field=models.IntegerField(null=True),
        ),
    ]
