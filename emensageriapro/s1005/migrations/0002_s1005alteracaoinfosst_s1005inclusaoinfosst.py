# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('s1005', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1005alteracaoinfoSST',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('progsst', models.CharField(max_length=4)),
                ('dtiniprog', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1005alteracaoinfosst_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1005alteracaoinfosst_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1005_alteracao', models.ForeignKey(related_name='s1005alteracaoinfosst_s1005_alteracao', to='s1005.s1005alteracao')),
            ],
            options={
                'ordering': ['s1005_alteracao', 'progsst', 'dtiniprog'],
                'db_table': 's1005_alteracao_infosst',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1005inclusaoinfoSST',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('progsst', models.CharField(max_length=4)),
                ('dtiniprog', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1005inclusaoinfosst_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1005inclusaoinfosst_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1005_inclusao', models.ForeignKey(related_name='s1005inclusaoinfosst_s1005_inclusao', to='s1005.s1005inclusao')),
            ],
            options={
                'ordering': ['s1005_inclusao', 'progsst', 'dtiniprog'],
                'db_table': 's1005_inclusao_infosst',
                'managed': True,
            },
        ),
    ]
