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
            name='r2010infoProcRetAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpprocretadic', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrprocretadic', models.CharField(max_length=21)),
                ('codsuspadic', models.IntegerField(null=True, blank=True)),
                ('valoradic', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2010infoprocretad_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2010infoprocretad_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2010_evtservtom', models.ForeignKey(related_name='r2010infoprocretad_r2010_evtservtom', to='efdreinf.r2010evtServTom')),
            ],
            options={
                'ordering': ['r2010_evtservtom', 'tpprocretadic', 'nrprocretadic', 'codsuspadic', 'valoradic'],
                'db_table': 'r2010_infoprocretad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2010infoProcRetPr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpprocretprinc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrprocretprinc', models.CharField(max_length=21)),
                ('codsuspprinc', models.IntegerField(null=True, blank=True)),
                ('valorprinc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2010infoprocretpr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2010infoprocretpr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2010_evtservtom', models.ForeignKey(related_name='r2010infoprocretpr_r2010_evtservtom', to='efdreinf.r2010evtServTom')),
            ],
            options={
                'ordering': ['r2010_evtservtom', 'tpprocretprinc', 'nrprocretprinc', 'codsuspprinc', 'valorprinc'],
                'db_table': 'r2010_infoprocretpr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2010infoTpServ',
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
                ('criado_por', models.ForeignKey(related_name='r2010infotpserv_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2010infotpserv_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2010_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao', 'vlrretsub', 'vlrnretprinc', 'vlrservicos15', 'vlrservicos20', 'vlrservicos25', 'vlradicional', 'vlrnretadic'],
                'db_table': 'r2010_infotpserv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2010nfs',
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
                ('criado_por', models.ForeignKey(related_name='r2010nfs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2010nfs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2010_evtservtom', models.ForeignKey(related_name='r2010nfs_r2010_evtservtom', to='efdreinf.r2010evtServTom')),
            ],
            options={
                'ordering': ['r2010_evtservtom', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto', 'obs'],
                'db_table': 'r2010_nfs',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2010infotpserv',
            name='r2010_nfs',
            field=models.ForeignKey(related_name='r2010infotpserv_r2010_nfs', to='r2010.r2010nfs'),
        ),
    ]
