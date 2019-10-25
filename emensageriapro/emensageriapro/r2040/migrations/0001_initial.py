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
            name='r2040infoProc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('vlrnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2040infoproc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2040infoproc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2040_recursosrep', 'tpproc', 'nrproc', 'codsusp', 'vlrnret'],
                'db_table': 'r2040_infoproc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2040infoRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tprepasse', models.IntegerField(choices=[(1, '1 - Patroc\xednio'), (2, '2 - Licenciamento de marcas e s\xedmbolos'), (3, '3 - Publicidade'), (4, '4 - Propaganda'), (5, '5 - Transmiss\xe3o de espet\xe1culos')])),
                ('descrecurso', models.CharField(max_length=20)),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrretapur', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2040inforecurso_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2040inforecurso_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2040_recursosrep', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur'],
                'db_table': 'r2040_inforecurso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2040recursosRep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjassocdesp', models.CharField(max_length=14)),
                ('vlrtotalrep', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalnret', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2040recursosrep_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2040recursosrep_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2040_evtassocdesprep', models.ForeignKey(related_name='r2040recursosrep_r2040_evtassocdesprep', to='efdreinf.r2040evtAssocDespRep')),
            ],
            options={
                'ordering': ['r2040_evtassocdesprep', 'cnpjassocdesp', 'vlrtotalrep', 'vlrtotalret', 'vlrtotalnret'],
                'db_table': 'r2040_recursosrep',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2040inforecurso',
            name='r2040_recursosrep',
            field=models.ForeignKey(related_name='r2040inforecurso_r2040_recursosrep', to='r2040.r2040recursosRep'),
        ),
        migrations.AddField(
            model_name='r2040infoproc',
            name='r2040_recursosrep',
            field=models.ForeignKey(related_name='r2040infoproc_r2040_recursosrep', to='r2040.r2040recursosRep'),
        ),
    ]
