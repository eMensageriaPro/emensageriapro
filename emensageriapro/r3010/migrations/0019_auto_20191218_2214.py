# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r3010', '0018_auto_20190623_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r3010boletim',
            name='categevento',
            field=models.IntegerField(choices=[(1, '1 - Internacional'), (2, '2 - Interestadual'), (3, '3 - Estadual'), (4, '4 - Local')], null=True),
        ),
        migrations.AlterField(
            model_name='r3010receitaingressos',
            name='tpingresso',
            field=models.IntegerField(choices=[(1, '1 - Arquibancada'), (2, '2 - Geral'), (3, '3 - Cadeiras'), (4, '4 - Camarote')], null=True),
        ),
    ]
