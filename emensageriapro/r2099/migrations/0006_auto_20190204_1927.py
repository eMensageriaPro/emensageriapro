# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2099', '0005_auto_20190202_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2099iderespinf',
            options={'managed': True, 'ordering': ['r2099_evtfechaevper', 'nmresp', 'cpfresp'], 'permissions': (('can_view_r2099_iderespinf', 'Can view r2099_iderespinf'),)},
        ),
    ]
