# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0021_auto_20190929_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrbccp00va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrbccp15va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrbccp20va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrbccp25va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrsuspbccp00va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrsuspbccp15va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrsuspbccp20va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='s5011basesremun',
            name='vrsuspbccp25va',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
