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
            name='s1030alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcargo', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('nmcargo', models.CharField(max_length=100)),
                ('codcbo', models.CharField(max_length=6)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_evttabcargo', models.OneToOneField(related_name='s1030alteracao_s1030_evttabcargo', to='esocial.s1030evtTabCargo')),
            ],
            options={
                'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid', 'fimvalid', 'nmcargo', 'codcbo'],
                'db_table': 's1030_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1030alteracaocargoPublico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acumcargo', models.IntegerField(choices=[(1, '1 - N\xe3o acumul\xe1vel'), (2, '2 - Profissional de Sa\xfade'), (3, '3 - Professor'), (4, '4 - T\xe9cnico/Cient\xedfico')])),
                ('contagemesp', models.IntegerField(choices=[(1, '1 - N\xe3o'), (2, '2 - Professor (Infantil, Fundamental e M\xe9dio)'), (3, '3 - Professor de Ensino Superior, Magistrado, Membro de Minist\xe9rio P\xfablico, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'), (4, '4 - Atividade de risco')])),
                ('dedicexcl', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('nrlei', models.CharField(max_length=12)),
                ('dtlei', models.DateField()),
                ('sitcargo', models.IntegerField(choices=[(1, '1 - Cria\xe7\xe3o'), (2, '2 - Extin\xe7\xe3o'), (3, '3 - Reestrutura\xe7\xe3o')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030alteracaocargopublico_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030alteracaocargopublico_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_alteracao', models.OneToOneField(related_name='s1030alteracaocargopublico_s1030_alteracao', to='s1030.s1030alteracao')),
            ],
            options={
                'ordering': ['s1030_alteracao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo'],
                'db_table': 's1030_alteracao_cargopublico',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1030alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_alteracao', models.OneToOneField(related_name='s1030alteracaonovavalidade_s1030_alteracao', to='s1030.s1030alteracao')),
            ],
            options={
                'ordering': ['s1030_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 's1030_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1030exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcargo', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_evttabcargo', models.OneToOneField(related_name='s1030exclusao_s1030_evttabcargo', to='esocial.s1030evtTabCargo')),
            ],
            options={
                'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid', 'fimvalid'],
                'db_table': 's1030_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1030inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcargo', models.CharField(max_length=30)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('nmcargo', models.CharField(max_length=100)),
                ('codcbo', models.CharField(max_length=6)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_evttabcargo', models.OneToOneField(related_name='s1030inclusao_s1030_evttabcargo', to='esocial.s1030evtTabCargo')),
            ],
            options={
                'ordering': ['s1030_evttabcargo', 'codcargo', 'inivalid', 'fimvalid', 'nmcargo', 'codcbo'],
                'db_table': 's1030_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1030inclusaocargoPublico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acumcargo', models.IntegerField(choices=[(1, '1 - N\xe3o acumul\xe1vel'), (2, '2 - Profissional de Sa\xfade'), (3, '3 - Professor'), (4, '4 - T\xe9cnico/Cient\xedfico')])),
                ('contagemesp', models.IntegerField(choices=[(1, '1 - N\xe3o'), (2, '2 - Professor (Infantil, Fundamental e M\xe9dio)'), (3, '3 - Professor de Ensino Superior, Magistrado, Membro de Minist\xe9rio P\xfablico, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'), (4, '4 - Atividade de risco')])),
                ('dedicexcl', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('nrlei', models.CharField(max_length=12)),
                ('dtlei', models.DateField()),
                ('sitcargo', models.IntegerField(choices=[(1, '1 - Cria\xe7\xe3o'), (2, '2 - Extin\xe7\xe3o'), (3, '3 - Reestrutura\xe7\xe3o')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1030inclusaocargopublico_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1030inclusaocargopublico_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1030_inclusao', models.OneToOneField(related_name='s1030inclusaocargopublico_s1030_inclusao', to='s1030.s1030inclusao')),
            ],
            options={
                'ordering': ['s1030_inclusao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo'],
                'db_table': 's1030_inclusao_cargopublico',
                'managed': True,
            },
        ),
    ]
