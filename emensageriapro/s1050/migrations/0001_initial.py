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
            name='s1050alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codhorcontrat', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('hrentr', models.CharField(max_length=4)),
                ('hrsaida', models.CharField(max_length=4)),
                ('durjornada', models.IntegerField()),
                ('perhorflexivel', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_evttabhortur', models.OneToOneField(related_name='s1050alteracao_s1050_evttabhortur', to='esocial.s1050evtTabHorTur')),
            ],
            options={
                'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'],
                'db_table': 's1050_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1050alteracaohorarioIntervalo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinterv', models.IntegerField(choices=[(1, '1 - Intervalo em Hor\xe1rio Fixo'), (2, '2 - Intervalo em Hor\xe1rio Vari\xe1vel')])),
                ('durinterv', models.IntegerField()),
                ('iniinterv', models.CharField(max_length=4, null=True, blank=True)),
                ('terminterv', models.CharField(max_length=4, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050alteracaohorariointervalo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050alteracaohorariointervalo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_alteracao', models.ForeignKey(related_name='s1050alteracaohorariointervalo_s1050_alteracao', to='s1050.s1050alteracao')),
            ],
            options={
                'ordering': ['s1050_alteracao', 'tpinterv', 'durinterv', 'iniinterv', 'terminterv'],
                'db_table': 's1050_alteracao_horariointervalo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1050alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_alteracao', models.OneToOneField(related_name='s1050alteracaonovavalidade_s1050_alteracao', to='s1050.s1050alteracao')),
            ],
            options={
                'ordering': ['s1050_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 's1050_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1050exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codhorcontrat', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_evttabhortur', models.OneToOneField(related_name='s1050exclusao_s1050_evttabhortur', to='esocial.s1050evtTabHorTur')),
            ],
            options={
                'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid'],
                'db_table': 's1050_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1050inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codhorcontrat', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('hrentr', models.CharField(max_length=4)),
                ('hrsaida', models.CharField(max_length=4)),
                ('durjornada', models.IntegerField()),
                ('perhorflexivel', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_evttabhortur', models.OneToOneField(related_name='s1050inclusao_s1050_evttabhortur', to='esocial.s1050evtTabHorTur')),
            ],
            options={
                'ordering': ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel'],
                'db_table': 's1050_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1050inclusaohorarioIntervalo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinterv', models.IntegerField(choices=[(1, '1 - Intervalo em Hor\xe1rio Fixo'), (2, '2 - Intervalo em Hor\xe1rio Vari\xe1vel')])),
                ('durinterv', models.IntegerField()),
                ('iniinterv', models.CharField(max_length=4, null=True, blank=True)),
                ('terminterv', models.CharField(max_length=4, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1050inclusaohorariointervalo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1050inclusaohorariointervalo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1050_inclusao', models.ForeignKey(related_name='s1050inclusaohorariointervalo_s1050_inclusao', to='s1050.s1050inclusao')),
            ],
            options={
                'ordering': ['s1050_inclusao', 'tpinterv', 'durinterv', 'iniinterv', 'terminterv'],
                'db_table': 's1050_inclusao_horariointervalo',
                'managed': True,
            },
        ),
    ]
