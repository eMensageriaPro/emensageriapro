# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0015_auto_20190202_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditoria',
            options={'managed': True, 'ordering': ['identidade'], 'permissions': (('can_view_auditoria', 'Can view auditoria'),)},
        ),
        migrations.AlterModelOptions(
            name='configmodulos',
            options={'managed': True, 'ordering': ['titulo'], 'permissions': (('can_view_config_modulos', 'Can view config_modulos'),)},
        ),
        migrations.AlterModelOptions(
            name='configpaginas',
            options={'managed': True, 'ordering': ['titulo'], 'permissions': (('can_view_config_paginas', 'Can view config_paginas'),)},
        ),
        migrations.AlterModelOptions(
            name='configperfis',
            options={'managed': True, 'ordering': ['titulo'], 'permissions': (('can_view_config_perfis', 'Can view config_perfis'),)},
        ),
        migrations.AlterModelOptions(
            name='configpermissoes',
            options={'managed': True, 'ordering': ['config_perfis', 'config_paginas'], 'permissions': (('can_view_config_permissoes', 'Can view config_permissoes'),)},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True, 'permissions': (('can_view_usuarios', 'Can view usuarios'),)},
        ),
    ]
