# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-26 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0012_auto_20181213_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='foto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
