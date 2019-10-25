# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0001_initial'),
        ('controle_de_acesso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1270remunAvNP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codlotacao', models.CharField(max_length=30)),
                ('vrbccp00', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp15', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp20', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp25', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbccp13', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrbcfgts', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdesccp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1270remunavnp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1270remunavnp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1270_evtcontratavnp', models.ForeignKey(related_name='s1270remunavnp_s1270_evtcontratavnp', to='esocial.s1270evtContratAvNP')),
            ],
            options={
                'ordering': ['s1270_evtcontratavnp', 'tpinsc', 'nrinsc', 'codlotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp'],
                'db_table': 's1270_remunavnp',
                'managed': True,
            },
        ),
    ]
