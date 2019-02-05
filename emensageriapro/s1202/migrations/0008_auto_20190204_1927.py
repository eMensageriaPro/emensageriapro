# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1202', '0007_auto_20190202_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1202dmdev',
            options={'managed': True, 'ordering': ['s1202_evtrmnrpps', 'idedmdev', 'codcateg'], 'permissions': (('can_view_s1202_dmdev', 'Can view s1202_dmdev'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideadc',
            options={'managed': True, 'ordering': ['s1202_dmdev', 'dtlei', 'nrlei', 'tpacconv', 'dsc'], 'permissions': (('can_view_s1202_infoperant_ideadc', 'Can view s1202_infoperant_ideadc'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideestab',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideperiodo', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_s1202_infoperant_ideestab', 'Can view s1202_infoperant_ideestab'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideperiodo',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideadc', 'perref'], 'permissions': (('can_view_s1202_infoperant_ideperiodo', 'Can view s1202_infoperant_ideperiodo'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantitensremun',
            options={'managed': True, 'ordering': ['s1202_infoperant_remunperant', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1202_infoperant_itensremun', 'Can view s1202_infoperant_itensremun'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantremunperant',
            options={'managed': True, 'ordering': ['s1202_infoperant_ideestab', 'codcateg'], 'permissions': (('can_view_s1202_infoperant_remunperant', 'Can view s1202_infoperant_remunperant'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurdetoper',
            options={'managed': True, 'ordering': ['s1202_infoperapur_remunperapur', 'cnpjoper', 'regans', 'vrpgtit'], 'permissions': (('can_view_s1202_infoperapur_detoper', 'Can view s1202_infoperapur_detoper'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurdetplano',
            options={'managed': True, 'ordering': ['s1202_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep'], 'permissions': (('can_view_s1202_infoperapur_detplano', 'Can view s1202_infoperapur_detplano'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurideestab',
            options={'managed': True, 'ordering': ['s1202_dmdev', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_s1202_infoperapur_ideestab', 'Can view s1202_infoperapur_ideestab'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapuritensremun',
            options={'managed': True, 'ordering': ['s1202_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1202_infoperapur_itensremun', 'Can view s1202_infoperapur_itensremun'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurremunperapur',
            options={'managed': True, 'ordering': ['s1202_infoperapur_ideestab', 'codcateg'], 'permissions': (('can_view_s1202_infoperapur_remunperapur', 'Can view s1202_infoperapur_remunperapur'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202procjudtrab',
            options={'managed': True, 'ordering': ['s1202_evtrmnrpps', 'tptrib', 'nrprocjud'], 'permissions': (('can_view_s1202_procjudtrab', 'Can view s1202_procjudtrab'),)},
        ),
    ]
