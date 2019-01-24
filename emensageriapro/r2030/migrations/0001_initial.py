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
            name='r2030infoProc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('vlrnret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2030infoproc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2030infoproc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2030_recursosrec', 'tpproc', 'nrproc', 'codsusp', 'vlrnret'],
                'db_table': 'r2030_infoproc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2030infoRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tprepasse', models.IntegerField(choices=[(1, '1 - Patroc\xednio'), (2, '2 - Licenciamento de marcas e s\xedmbolos'), (3, '3 - Publicidade'), (4, '4 - Propaganda'), (5, '5 - Transmiss\xe3o de espet\xe1culos')])),
                ('descrecurso', models.CharField(max_length=20)),
                ('vlrbruto', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrretapur', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2030inforecurso_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2030inforecurso_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2030_recursosrec', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur'],
                'db_table': 'r2030_inforecurso',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2030recursosRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjorigrecurso', models.CharField(max_length=14)),
                ('vlrtotalrec', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalret', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrtotalnret', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2030recursosrec_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2030recursosrec_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2030_evtassocdesprec', models.ForeignKey(related_name='r2030recursosrec_r2030_evtassocdesprec', to='efdreinf.r2030evtAssocDespRec')),
            ],
            options={
                'ordering': ['r2030_evtassocdesprec', 'cnpjorigrecurso', 'vlrtotalrec', 'vlrtotalret', 'vlrtotalnret'],
                'db_table': 'r2030_recursosrec',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2030inforecurso',
            name='r2030_recursosrec',
            field=models.ForeignKey(related_name='r2030inforecurso_r2030_recursosrec', to='r2030.r2030recursosRec'),
        ),
        migrations.AddField(
            model_name='r2030infoproc',
            name='r2030_recursosrec',
            field=models.ForeignKey(related_name='r2030infoproc_r2030_recursosrec', to='r2030.r2030recursosRec'),
        ),
    ]
