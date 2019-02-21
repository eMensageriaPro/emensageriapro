# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1050', '0005_auto_20190202_1242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1050alteracao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'], 'permissions': (('can_view_s1050_alteracao', 'Can view s1050_alteracao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1050alteracaohorariointervalo',
            options={'managed': True, 'ordering': ['s1050_alteracao', 'tpinterv', 'durinterv'], 'permissions': (('can_view_s1050_alteracao_horariointervalo', 'Can view s1050_alteracao_horariointervalo'),)},
        ),
        migrations.AlterModelOptions(
            name='s1050alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1050_alteracao', 'inivalid'], 'permissions': (('can_view_s1050_alteracao_novavalidade', 'Can view s1050_alteracao_novavalidade'),)},
        ),
        migrations.AlterModelOptions(
            name='s1050exclusao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid'], 'permissions': (('can_view_s1050_exclusao', 'Can view s1050_exclusao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1050inclusao',
            options={'managed': True, 'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'], 'permissions': (('can_view_s1050_inclusao', 'Can view s1050_inclusao'),)},
        ),
        migrations.AlterModelOptions(
            name='s1050inclusaohorariointervalo',
            options={'managed': True, 'ordering': ['s1050_inclusao', 'tpinterv', 'durinterv'], 'permissions': (('can_view_s1050_inclusao_horariointervalo', 'Can view s1050_inclusao_horariointervalo'),)},
        ),
    ]