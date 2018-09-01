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
            name='r1070alteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('indautoria', models.IntegerField(choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade ou empresa')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070alteracao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070alteracao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_evttabprocesso', models.OneToOneField(related_name='r1070alteracao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso')),
            ],
            options={
                'ordering': ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria'],
                'db_table': 'r1070_alteracao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070alteracaodadosProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ufvara', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('codmunic', models.TextField(max_length=7)),
                ('idvara', models.CharField(max_length=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070alteracaodadosprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070alteracaodadosprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_alteracao', models.OneToOneField(related_name='r1070alteracaodadosprocjud_r1070_alteracao', to='r1070.r1070alteracao')),
            ],
            options={
                'ordering': ['r1070_alteracao', 'ufvara', 'codmunic', 'idvara'],
                'db_table': 'r1070_alteracao_dadosprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070alteracaoinfoSusp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('indsusp', models.CharField(max_length=2, choices=[(b'1', '01 - Liminar em Mandado de Seguran\xe7a'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'2', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'3', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'4', '04 - Antecipa\xe7\xe3o de Tutela'), (b'5', '05 - Liminar em Medida Cautelar'), (b'8', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'9', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade. Valida\xe7\xe3o: Se {tpProc} = [1], deve ser preenchido com [03, 90, 92]. Se {tpProc} = [2], deve ser preenchido com [01, 02, 04, 05, 08, 09, 10, 11, 12, 13, 90, 92]')])),
                ('dtdecisao', models.DateField()),
                ('inddeposito', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070alteracaoinfosusp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070alteracaoinfosusp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_alteracao', models.ForeignKey(related_name='r1070alteracaoinfosusp_r1070_alteracao', to='r1070.r1070alteracao')),
            ],
            options={
                'ordering': ['r1070_alteracao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'],
                'db_table': 'r1070_alteracao_infosusp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070alteracaonovaValidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070alteracaonovavalidade_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070alteracaonovavalidade_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_alteracao', models.OneToOneField(related_name='r1070alteracaonovavalidade_r1070_alteracao', to='r1070.r1070alteracao')),
            ],
            options={
                'ordering': ['r1070_alteracao', 'inivalid', 'fimvalid'],
                'db_table': 'r1070_alteracao_novavalidade',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070exclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070exclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070exclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_evttabprocesso', models.OneToOneField(related_name='r1070exclusao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso')),
            ],
            options={
                'ordering': ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid'],
                'db_table': 'r1070_exclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070inclusao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('inivalid', models.CharField(max_length=7, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('fimvalid', models.CharField(blank=True, max_length=7, null=True, choices=[(b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018')])),
                ('indautoria', models.IntegerField(choices=[(1, '1 - Pr\xf3prio contribuinte'), (2, '2 - Outra entidade ou empresa')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070inclusao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070inclusao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_evttabprocesso', models.OneToOneField(related_name='r1070inclusao_r1070_evttabprocesso', to='efdreinf.r1070evtTabProcesso')),
            ],
            options={
                'ordering': ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria'],
                'db_table': 'r1070_inclusao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070inclusaodadosProcJud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ufvara', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('codmunic', models.TextField(max_length=7)),
                ('idvara', models.CharField(max_length=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070inclusaodadosprocjud_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070inclusaodadosprocjud_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_inclusao', models.OneToOneField(related_name='r1070inclusaodadosprocjud_r1070_inclusao', to='r1070.r1070inclusao')),
            ],
            options={
                'ordering': ['r1070_inclusao', 'ufvara', 'codmunic', 'idvara'],
                'db_table': 'r1070_inclusao_dadosprocjud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r1070inclusaoinfoSusp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('indsusp', models.CharField(max_length=2, choices=[(b'1', '01 - Liminar em Mandado de Seguran\xe7a'), (b'10', '10 - Ac\xf3rd\xe3o do TRF Favor\xe1vel ao Contribuinte'), (b'11', '11 - Ac\xf3rd\xe3o do STJ em Recurso Especial Favor\xe1vel ao Contribuinte'), (b'12', '12 - Ac\xf3rd\xe3o do STF em Recurso Extraordin\xe1rio Favor\xe1vel ao Contribuinte'), (b'13', '13 - Senten\xe7a 1\xaa inst\xe2ncia n\xe3o transitada em julgado com efeito suspensivo'), (b'2', '02 - Dep\xf3sito Judicial do Montante Integral'), (b'3', '03 - Dep\xf3sito Administrativo do Montante Integral'), (b'4', '04 - Antecipa\xe7\xe3o de Tutela'), (b'5', '05 - Liminar em Medida Cautelar'), (b'8', '08 - Senten\xe7a em Mandado de Seguran\xe7a Favor\xe1vel ao Contribuinte'), (b'9', '09 - Senten\xe7a em A\xe7\xe3o Ordin\xe1ria Favor\xe1vel ao Contribuinte e Confirmada pelo TRF'), (b'90', '90 - Decis\xe3o Definitiva a favor do contribuinte'), (b'92', '92 - Sem suspens\xe3o da exigibilidade')])),
                ('dtdecisao', models.DateField()),
                ('inddeposito', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r1070inclusaoinfosusp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r1070inclusaoinfosusp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r1070_inclusao', models.ForeignKey(related_name='r1070inclusaoinfosusp_r1070_inclusao', to='r1070.r1070inclusao')),
            ],
            options={
                'ordering': ['r1070_inclusao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito'],
                'db_table': 'r1070_inclusao_infosusp',
                'managed': True,
            },
        ),
    ]
