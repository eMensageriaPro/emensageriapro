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
            name='s1070alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial'), (3, '3 - N\xfamero de Benef\xedcio (NB) do INSS')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('indautoria', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade, empresa ou empregado')])),
                ('indmatproc', models.IntegerField(choices=[(1, '1 - Tribut\xe1ria'), (2, '2 - Autoriza\xe7\xe3o de trabalho de menor'), (3, '3 - Dispensa, ainda que parcial, de contrata\xe7\xe3o de pessoa com defici\xeancia (PCD)'), (4, '4 - Dispensa, ainda que parcial, de contrata\xe7\xe3o de aprendiz'), (5, '5 - Seguran\xe7a e Sa\xfade do Trabalho'), (6, '6 - Convers\xe3o de Licen\xe7a Sa\xfade em Acidente de Trabalho'), (7, '7 - FGTS'), (8, '8 - Contribui\xe7\xe3o sindical'), (99, '99 - Outros assuntos')])),
                ('observacao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_evttabprocesso', models.OneToOneField(related_name='s1070alteracao_s1070_evttabprocesso', to='esocial.s1070evtTabProcesso')),
            ],
            options={
                'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria', 'indmatproc', 'observacao'],
                'db_table': 's1070_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070alteracaodadosProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ufvara', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('codmunic', models.TextField(max_length=7)),
                ('idvara', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070alteracaodadosprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070alteracaodadosprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_alteracao', models.OneToOneField(related_name='s1070alteracaodadosprocjud_s1070_alteracao', to='s1070.s1070alteracao')),
            ],
            options={
                'ordering': ['s1070_alteracao', 'ufvara', 'codmunic', 'idvara'],
                'db_table': 's1070_alteracao_dadosprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070alteracaoinfoSusp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codsusp', models.IntegerField()),
                ('indsusp', models.CharField(max_length=2, choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'14', '14 - Contesta\xe7\xe3o Administrativa FAP'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade')])),
                ('dtdecisao', models.DateField()),
                ('inddeposito', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070alteracaoinfosusp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070alteracaoinfosusp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_alteracao', models.ForeignKey(related_name='s1070alteracaoinfosusp_s1070_alteracao', to='s1070.s1070alteracao')),
            ],
            options={
                'ordering': ['s1070_alteracao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'],
                'db_table': 's1070_alteracao_infosusp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_alteracao', models.OneToOneField(related_name='s1070alteracaonovavalidade_s1070_alteracao', to='s1070.s1070alteracao')),
            ],
            options={
                'ordering': ['s1070_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 's1070_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial'), (3, '3 - N\xfamero de Benef\xedcio (NB) do INSS')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_evttabprocesso', models.OneToOneField(related_name='s1070exclusao_s1070_evttabprocesso', to='esocial.s1070evtTabProcesso')),
            ],
            options={
                'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid'],
                'db_table': 's1070_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial'), (3, '3 - N\xfamero de Benef\xedcio (NB) do INSS')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('indautoria', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade, empresa ou empregado')])),
                ('indmatproc', models.IntegerField(choices=[(1, '1 - Tribut\xe1ria'), (2, '2 - Autoriza\xe7\xe3o de trabalho de menor'), (3, '3 - Dispensa, ainda que parcial, de contrata\xe7\xe3o de pessoa com defici\xeancia (PCD)'), (4, '4 - Dispensa, ainda que parcial, de contrata\xe7\xe3o de aprendiz'), (5, '5 - Seguran\xe7a e Sa\xfade do Trabalho'), (6, '6 - Convers\xe3o de Licen\xe7a Sa\xfade em Acidente de Trabalho'), (7, '7 - FGTS'), (8, '8 - Contribui\xe7\xe3o sindical'), (99, '99 - Outros assuntos')])),
                ('observacao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_evttabprocesso', models.OneToOneField(related_name='s1070inclusao_s1070_evttabprocesso', to='esocial.s1070evtTabProcesso')),
            ],
            options={
                'ordering': ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria', 'indmatproc', 'observacao'],
                'db_table': 's1070_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070inclusaodadosProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ufvara', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('codmunic', models.TextField(max_length=7)),
                ('idvara', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070inclusaodadosprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070inclusaodadosprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_inclusao', models.OneToOneField(related_name='s1070inclusaodadosprocjud_s1070_inclusao', to='s1070.s1070inclusao')),
            ],
            options={
                'ordering': ['s1070_inclusao', 'ufvara', 'codmunic', 'idvara'],
                'db_table': 's1070_inclusao_dadosprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1070inclusaoinfoSusp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codsusp', models.IntegerField()),
                ('indsusp', models.CharField(max_length=2, choices=[(b'01', '01 - Liminar em Mandado de Seguran\xe7a'), (b'02', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'03', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'04', '04 - Antecipa\xe7\xe3o de Tutela'), (b'05', '05 - Liminar em Medida Cautelar'), (b'08', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'09', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'14', '14 - Contesta\xe7\xe3o Administrativa FAP'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade')])),
                ('dtdecisao', models.DateField()),
                ('inddeposito', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1070inclusaoinfosusp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1070inclusaoinfosusp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1070_inclusao', models.ForeignKey(related_name='s1070inclusaoinfosusp_s1070_inclusao', to='s1070.s1070inclusao')),
            ],
            options={
                'ordering': ['s1070_inclusao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'],
                'db_table': 's1070_inclusao_infosusp',
                'managed': True,
            },
        ),
    ]
