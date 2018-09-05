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
            name='r2050infoProc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('vlrcpsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrratsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vlrsenarsusp', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2050infoproc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2050infoproc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2050_tipocom', 'tpproc', 'nrproc', 'codsusp', 'vlrcpsusp', 'vlrratsusp', 'vlrsenarsusp'],
                'db_table': 'r2050_infoproc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2050tipoCom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indcom', models.IntegerField(choices=[(1, '1 - Comercializa\xe7\xe3o da Produ\xe7\xe3o por Prod. Rural PJ/Agroind\xfastria, exceto para entidades executoras do PAA'), (8, '8 - Comercializa\xe7\xe3o da Produ\xe7\xe3o para Entidade do Programa de Aquisi\xe7\xe3o de Alimentos - PAA'), (9, '9 - Comercializa\xe7\xe3o direta da Produ\xe7\xe3o no Mercado Externo')])),
                ('vlrrecbruta', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2050tipocom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2050tipocom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2050_evtcomprod', models.ForeignKey(related_name='r2050tipocom_r2050_evtcomprod', to='efdreinf.r2050evtComProd')),
            ],
            options={
                'ordering': ['r2050_evtcomprod', 'indcom', 'vlrrecbruta'],
                'db_table': 'r2050_tipocom',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2050infoproc',
            name='r2050_tipocom',
            field=models.ForeignKey(related_name='r2050infoproc_r2050_tipocom', to='r2050.r2050tipoCom'),
        ),
    ]
