# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0001_initial'),
        ('efdreinf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='r2020infoProcRetAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpprocretadic', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrprocretadic', models.CharField(max_length=21)),
                ('codsuspadic', models.IntegerField(null=True, blank=True)),
                ('valoradic', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2020infoprocretad_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2020infoprocretad_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2020_evtservprest', models.ForeignKey(related_name='r2020infoprocretad_r2020_evtservprest', to='efdreinf.r2020evtServPrest')),
            ],
            options={
                'ordering': ['r2020_evtservprest', 'tpprocretadic', 'nrprocretadic', 'codsuspadic', 'valoradic'],
                'db_table': 'r2020_infoprocretad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2020infoProcRetPr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpprocretprinc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrprocretprinc', models.CharField(max_length=21)),
                ('codsuspprinc', models.IntegerField(null=True, blank=True)),
                ('valorprinc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2020infoprocretpr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2020infoprocretpr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2020_evtservprest', models.ForeignKey(related_name='r2020infoprocretpr_r2020_evtservprest', to='efdreinf.r2020evtServPrest')),
            ],
            options={
                'ordering': ['r2020_evtservprest', 'tpprocretprinc', 'nrprocretprinc', 'codsuspprinc', 'valorprinc'],
                'db_table': 'r2020_infoprocretpr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2020infoTpServ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpservico', models.IntegerField()),
                ('vlrbaseret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrretencao', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrretsub', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrnretprinc', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrservicos15', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrservicos20', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrservicos25', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlradicional', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrnretadic', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2020infotpserv_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2020infotpserv_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2020_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao', 'vlrretsub', 'vlrnretprinc', 'vlrservicos15', 'vlrservicos20', 'vlrservicos25', 'vlradicional', 'vlrnretadic'],
                'db_table': 'r2020_infotpserv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2020nfs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=5)),
                ('numdocto', models.CharField(max_length=15)),
                ('dtemissaonf', models.DateField()),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('obs', models.CharField(max_length=250, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2020nfs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2020nfs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2020_evtservprest', models.ForeignKey(related_name='r2020nfs_r2020_evtservprest', to='efdreinf.r2020evtServPrest')),
            ],
            options={
                'ordering': ['r2020_evtservprest', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto', 'obs'],
                'db_table': 'r2020_nfs',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2020infotpserv',
            name='r2020_nfs',
            field=models.ForeignKey(related_name='r2020infotpserv_r2020_nfs', to='r2020.r2020nfs'),
        ),
    ]
