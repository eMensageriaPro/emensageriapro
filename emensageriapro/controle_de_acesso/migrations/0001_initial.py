# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tabela', models.CharField(max_length=200)),
                ('identidade', models.IntegerField()),
                ('situacao_anterior', models.TextField()),
                ('situacao_posterior', models.TextField()),
                ('tipo', models.IntegerField(choices=[(1, 'Inclus\xe3o'), (2, 'Altera\xe7\xe3o'), (3, 'Exclus\xe3o')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
            ],
            options={
                'ordering': ['identidade'],
                'db_table': 'auditoria',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConfigModulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('ordem', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
            ],
            options={
                'ordering': ['titulo'],
                'db_table': 'config_modulos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConfigPaginas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=2000)),
                ('endereco', models.CharField(max_length=500)),
                ('exibe_menu', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('tipo', models.IntegerField(choices=[(0, 'Manual'), (1, 'Autom\xe1tico')])),
                ('ordem', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('config_modulos', models.ForeignKey(related_name='configpaginas_config_modulos', to='controle_de_acesso.ConfigModulos')),
            ],
            options={
                'ordering': ['titulo'],
                'db_table': 'config_paginas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConfigPerfis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=25)),
                ('permissoes', models.TextField(null=True, blank=True)),
                ('modulos_permitidos', models.TextField(null=True, blank=True)),
                ('paginas_permitidas', models.TextField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
            ],
            options={
                'ordering': ['titulo'],
                'db_table': 'config_perfis',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConfigPermissoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permite_listar', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('permite_cadastrar', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('permite_editar', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('permite_visualizar', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('permite_apagar', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('config_paginas', models.ForeignKey(related_name='configpermissoes_config_paginas', to='controle_de_acesso.ConfigPaginas')),
                ('config_perfis', models.ForeignKey(related_name='configpermissoes_config_perfis', to='controle_de_acesso.ConfigPerfis')),
            ],
            options={
                'ordering': ['config_perfis', 'config_paginas'],
                'db_table': 'config_permissoes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=20)),
                ('senha', models.CharField(default=b'asdkl1231', max_length=300, blank=True)),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('config_perfis', models.ForeignKey(related_name='usuarios_config_perfis', to='controle_de_acesso.ConfigPerfis')),
                ('criado_por', models.ForeignKey(related_name='usuarios_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='usuarios_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['nome'],
                'db_table': 'usuarios',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='configpermissoes',
            name='criado_por',
            field=models.ForeignKey(related_name='configpermissoes_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configpermissoes',
            name='modificado_por',
            field=models.ForeignKey(related_name='configpermissoes_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configperfis',
            name='criado_por',
            field=models.ForeignKey(related_name='configperfis_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configperfis',
            name='modificado_por',
            field=models.ForeignKey(related_name='configperfis_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configpaginas',
            name='criado_por',
            field=models.ForeignKey(related_name='configpaginas_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configpaginas',
            name='modificado_por',
            field=models.ForeignKey(related_name='configpaginas_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configmodulos',
            name='criado_por',
            field=models.ForeignKey(related_name='configmodulos_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configmodulos',
            name='modificado_por',
            field=models.ForeignKey(related_name='configmodulos_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='configmodulos',
            name='modulo_pai',
            field=models.ForeignKey(related_name='configmodulos_modulo_pai', blank=True, to='controle_de_acesso.ConfigModulos', null=True),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='criado_por',
            field=models.ForeignKey(related_name='auditoria_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='modificado_por',
            field=models.ForeignKey(related_name='auditoria_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
    ]
