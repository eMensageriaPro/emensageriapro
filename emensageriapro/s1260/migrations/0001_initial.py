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
            name='s1260ideAdquir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('vrcomerc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1260ideadquir_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1260ideadquir_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1260_tpcomerc', 'tpinsc', 'nrinsc', 'vrcomerc'],
                'db_table': 's1260_ideadquir',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1260infoProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField()),
                ('vrcpsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrratsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrsenarsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1260infoprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1260infoprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1260_tpcomerc', 'tpproc', 'nrproc', 'codsusp', 'vrcpsusp', 'vrratsusp', 'vrsenarsusp'],
                'db_table': 's1260_infoprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1260nfs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=5, null=True, blank=True)),
                ('nrdocto', models.CharField(max_length=20)),
                ('dtemisnf', models.DateField()),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrcpdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrratdescpr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrsenardesc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1260nfs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1260nfs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1260_ideadquir', models.ForeignKey(related_name='s1260nfs_s1260_ideadquir', to='s1260.s1260ideAdquir')),
            ],
            options={
                'ordering': ['s1260_ideadquir', 'serie', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc'],
                'db_table': 's1260_nfs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1260tpComerc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indcomerc', models.IntegerField(choices=[(2, '2 - Comercializa\xe7\xe3o da Produ\xe7\xe3o efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa f\xedsica por Produtor Rural Pessoa F\xedsica, inclusive por Segurado Especial ou por Pessoa F\xedsica n\xe3o produtor rural'), (3, '3 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PF/Seg. Especial - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA) ou a Intermedi\xe1rio PF'), (7, '7 - Comercializa\xe7\xe3o da Produ\xe7\xe3o Isenta de acordo com a Lei no 13.606/2018'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o da Pessoa F\xedsica/Segurado Especial para Entidade inscrita no Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o da Produ\xe7\xe3o no Mercado Externo')])),
                ('vrtotcom', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1260tpcomerc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1260tpcomerc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1260_evtcomprod', models.ForeignKey(related_name='s1260tpcomerc_s1260_evtcomprod', to='esocial.s1260evtComProd')),
            ],
            options={
                'ordering': ['s1260_evtcomprod', 'indcomerc', 'vrtotcom'],
                'db_table': 's1260_tpcomerc',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s1260infoprocjud',
            name='s1260_tpcomerc',
            field=models.ForeignKey(related_name='s1260infoprocjud_s1260_tpcomerc', to='s1260.s1260tpComerc'),
        ),
        migrations.AddField(
            model_name='s1260ideadquir',
            name='s1260_tpcomerc',
            field=models.ForeignKey(related_name='s1260ideadquir_s1260_tpcomerc', to='s1260.s1260tpComerc'),
        ),
    ]
