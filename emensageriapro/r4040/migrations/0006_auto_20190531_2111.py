# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r4040', '0005_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r4040idenat',
            options={'managed': True, 'ordering': ['r4040_evtbenefnid', 'natrendim'], 'permissions': (('can_view_r4040ideNat', 'Can view R4040IDENAT'), ('can_view_menu_r4040ideNat', 'Can view menu R4040IDENAT'))},
        ),
        migrations.AlterModelOptions(
            name='r4040infopgto',
            options={'managed': True, 'ordering': ['r4040_idenat', 'dtfg', 'vlrliq', 'vlrreaj', 'vlrir', 'descr'], 'permissions': (('can_view_r4040infoPgto', 'Can view R4040INFOPGTO'), ('can_view_menu_r4040infoPgto', 'Can view menu R4040INFOPGTO'))},
        ),
    ]