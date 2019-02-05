# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1030', '0006_auto_20190202_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1030alteracao',
            options={'managed': True, 'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid', 'nmcargo', 'codcbo'], 'permissions': (('can_view_s1030_alteracao', 'Can view s1030_alteracao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1030alteracaocargopublico',
            options={'managed': True, 'ordering': ['s1030_alteracao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo'], 'permissions': (('can_view_s1030_alteracao_cargopublico', 'Can view s1030_alteracao_cargopublico'),)},
        ),
        migrations.AlterModelOptions(
            name='s1030alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1030_alteracao', 'inivalid'], 'permissions': (('can_view_s1030_alteracao_novavalidade', 'Can view s1030_alteracao_novavalidade'),)},
        ),
        migrations.AlterModelOptions(
            name='s1030exclusao',
            options={'managed': True, 'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid'], 'permissions': (('can_view_s1030_exclusao', 'Can view s1030_exclusao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1030inclusao',
            options={'managed': True, 'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid', 'nmcargo', 'codcbo'], 'permissions': (('can_view_s1030_inclusao', 'Can view s1030_inclusao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1030inclusaocargopublico',
            options={'managed': True, 'ordering': ['s1030_inclusao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo'], 'permissions': (('can_view_s1030_inclusao_cargopublico', 'Can view s1030_inclusao_cargopublico'),)},
        ),
    ]
