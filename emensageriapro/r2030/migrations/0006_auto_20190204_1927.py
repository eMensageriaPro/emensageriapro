# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2030', '0005_auto_20190202_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2030infoproc',
            options={'managed': True, 'ordering': ['r2030_recursosrec', 'tpproc', 'nrproc', 'vlrnret'], 'permissions': (('can_view_r2030_infoproc', 'Can view r2030_infoproc'),)},
        ),
        migrations.AlterModelOptions(
            name='r2030inforecurso',
            options={'managed': True, 'ordering': ['r2030_recursosrec', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur'], 'permissions': (('can_view_r2030_inforecurso', 'Can view r2030_inforecurso'),)},
        ),
        migrations.AlterModelOptions(
            name='r2030recursosrec',
            options={'managed': True, 'ordering': ['r2030_evtassocdesprec', 'cnpjorigrecurso', 'vlrtotalrec', 'vlrtotalret'], 'permissions': (('can_view_r2030_recursosrec', 'Can view r2030_recursosrec'),)},
        ),
    ]
