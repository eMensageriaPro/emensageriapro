# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0003_auto_20180912_1556'),
        ('s1207', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1207infoPerAnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperant_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperant_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1207_dmdev'],
                'db_table': 's1207_infoperant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerAntideADC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtacconv', models.DateField(null=True, blank=True)),
                ('tpacconv', models.CharField(max_length=1, choices=[(b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'G', 'G - Decis\xe3o administrativa'), (b'H', 'H - Decis\xe3o judicial')])),
                ('compacconv', models.CharField(max_length=7, null=True, blank=True)),
                ('dtefacconv', models.DateField(null=True, blank=True)),
                ('dsc', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperantideadc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperantideadc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_infoperant', models.ForeignKey(related_name='s1207infoperantideadc_s1207_infoperant', to='s1207.s1207infoPerAnt')),
            ],
            options={
                'ordering': ['s1207_infoperant', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc'],
                'db_table': 's1207_infoperant_ideadc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerAntideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField()),
                ('nrinsc', models.CharField(max_length=15)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperantideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperantideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1207_infoperant_ideperiodo', 'tpinsc', 'nrinsc'],
                'db_table': 's1207_infoperant_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerAntidePeriodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perref', models.CharField(max_length=7)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperantideperiodo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperantideperiodo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_infoperant_ideadc', models.ForeignKey(related_name='s1207infoperantideperiodo_s1207_infoperant_ideadc', to='s1207.s1207infoPerAntideADC')),
            ],
            options={
                'ordering': ['s1207_infoperant_ideadc', 'perref'],
                'db_table': 's1207_infoperant_ideperiodo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerAntitensRemun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codrubr', models.CharField(max_length=30)),
                ('idetabrubr', models.CharField(max_length=8)),
                ('qtdrubr', models.DecimalField(max_length=6, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('fatorrubr', models.DecimalField(max_length=5, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrunit', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrrubr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperantitensremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperantitensremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1207_infoperant_remunperant', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's1207_infoperant_itensremun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerAntremunPerAnt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperantremunperant_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperantremunperant_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_infoperant_ideestab', models.ForeignKey(related_name='s1207infoperantremunperant_s1207_infoperant_ideestab', to='s1207.s1207infoPerAntideEstab')),
            ],
            options={
                'ordering': ['s1207_infoperant_ideestab'],
                'db_table': 's1207_infoperant_remunperant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerApur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperapur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperapur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1207_dmdev'],
                'db_table': 's1207_infoperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerApurideEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField()),
                ('nrinsc', models.CharField(max_length=15)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperapurideestab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperapurideestab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_infoperapur', models.ForeignKey(related_name='s1207infoperapurideestab_s1207_infoperapur', to='s1207.s1207infoPerApur')),
            ],
            options={
                'ordering': ['s1207_infoperapur', 'tpinsc', 'nrinsc'],
                'db_table': 's1207_infoperapur_ideestab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerApuritensRemun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codrubr', models.CharField(max_length=30)),
                ('idetabrubr', models.CharField(max_length=8)),
                ('qtdrubr', models.DecimalField(max_length=6, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('fatorrubr', models.DecimalField(max_length=5, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrunit', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('vrrubr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperapuritensremun_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperapuritensremun_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1207_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's1207_infoperapur_itensremun',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207infoPerApurremunPerApur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207infoperapurremunperapur_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207infoperapurremunperapur_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_infoperapur_ideestab', models.ForeignKey(related_name='s1207infoperapurremunperapur_s1207_infoperapur_ideestab', to='s1207.s1207infoPerApurideEstab')),
            ],
            options={
                'ordering': ['s1207_infoperapur_ideestab'],
                'db_table': 's1207_infoperapur_remunperapur',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207procJudTrab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tptrib', models.IntegerField(choices=[(1, '1 - IRRF'), (5, '5 - Contribui\xe7\xe3o para o RPPS/regime militar')])),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207procjudtrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207procjudtrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_evtbenprrp', models.ForeignKey(related_name='s1207procjudtrab_s1207_evtbenprrp', to='esocial.s1207evtBenPrRP')),
            ],
            options={
                'ordering': ['s1207_evtbenprrp', 'tptrib', 'nrprocjud', 'codsusp'],
                'db_table': 's1207_procjudtrab',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='s1207dmdev',
            name='tpbenef',
            field=models.IntegerField(choices=[(1, '1 - Aposentadoria Volunt\xe1ria por Idade e Tempo de Contribui\xe7\xe3o - Proventos Integrais: Art. 40, \xa7 1\xba, III \u201ca\u201d da CF, Reda\xe7\xe3o EC 20/98'), (10, '10 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03, c/c LC 152/2015'), (11, '11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o: Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98'), (12, '12 - Aposentadoria - Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o - Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98: Geral'), (13, '13 - Aposentadoria Especial do Professor - Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o.'), (14, '14 - Aposentadoria com proventos proporcionais calculados sobre a \xfaltima remunera\xe7\xe3oRegra de Transi\xe7\xe3o do Art. 8\xba, da EC20/98 - Geral'), (15, '15 - Aposentadoria - Regra de Transi\xe7\xe3o do Art. 3\xba, da EC 47/05: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o'), (16, '16 - Aposentadoria Especial de Professor - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o a partir de 01/01/2006)'), (17, '17 - Aposentadoria Especial de Professor - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (18, '18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o a partir de 01/01/2006)'), (19, '19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (2, '2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF reda\xe7\xe3o original - Anterior \xe0 EC 20/1998'), (20, '20 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC 41/03 - Proventos pela M\xe9dia com redutor - Geral (Implementa\xe7\xe3o a partir de 01/01/2006)'), (21, '21 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC 41/03 - Proventos pela M\xe9dia reduzida - Geral (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (22, '22 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 6\xba, da EC41/03: Proventos Integrais correspondentes \xe1 ultima remunera\xe7\xe3o do cargo - Geral'), (23, '23 - Aposentadoria Volunt\xe1ria Professor Educa\xe7\xe3o infantil, ensino fundamental e m\xe9dioRegra de Transi\xe7\xe3o do Art. 6\xba, da EC41/03: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o do cargo'), (24, '24 - Aposentadoria Volunt\xe1ria por Idade - Proventos Proporcionais calculados sobre a \xfaltima remunera\xe7\xe3o do cargo: Art. 40, \xa7 1\xba, Inciso III, al\xednea "b" CF, Reda\xe7\xe3o EC 20/98'), (25, '25 - Aposentadoria Volunt\xe1ria por Idade - Proventos pela M\xe9dia proporcionais - Art. 40, \xa7 1\xba, Inciso III, al\xednea "b" CF, Reda\xe7\xe3o EC 41/03'), (26, '26 - Aposentadoria Volunt\xe1ria por Idade e por Tempo de Contribui\xe7\xe3o - Proventos pela M\xe9dia: Art. 40, \xa7 1\xba, Inciso III, aliena "a", CF, Reda\xe7\xe3o EC 41/03'), (27, '27 - Aposentadoria Volunt\xe1ria por Tempo de Contribui\xe7\xe3o - Especial do professor de q/q n\xedvel de ensino - Art. 40, III, al\xednea b, da CF- Red. Original at\xe9 EC 20/1998'), (28, '28 - Aposentadoria Volunt\xe1ria por idade e Tempo de Contribui\xe7\xe3o - Especial do professor ed. infantil, ensino fundamental e m\xe9dio - Art. 40, \xa7 1\xba, Inciso III, al\xednea a, c/c \xa7 5\xba da CF red. da EC 20/1998 )'), (29, '29 - Aposentadoria Volunt\xe1ria por idade e Tempo de Contribui\xe7\xe3o - Especial de Professor - Proventos pela M\xe9dia: Art. 40, \xa7 1\xba, Inciso III, al\xednea "a", C/C \xa7 5\xba da CF, Reda\xe7\xe3o EC 41/2003'), (3, '3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998'), (30, '30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40, Inciso I, Reda\xe7\xe3o Original, CF'), (31, '31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40, \xa7 1\xba, Inciso I da CF com Reda\xe7\xe3o da EC 20/1998'), (32, '32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela m\xe9dia) - Art. 40, \xa7 1\xba, Inciso I da CF com Reda\xe7\xe3o da EC 41/2003'), (33, '33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40 \xba 1\xba, Inciso I da CF C/C combinado com Art. 6\xaa- A da EC 70/2012'), (34, '34 - Reforma por invalidez'), (35, '35 - Reserva Remunerada Compuls\xf3ria'), (36, '36 - Reserva Remunerada Integral'), (37, '37 - Reserva Remunerada Proporcional'), (38, '38 - Aux\xedlio Doen\xe7a - Conforme lei do Ente'), (39, '39 - Aux\xedlio Reclus\xe3o - Art. 13 da EC 20/1998 c/c lei do Ente'), (4, '4 - Aposentadoria Compuls\xf3ria - Proventos proporcionais: Art. 40, II da CF reda\xe7\xe3o original, anterior \xe0 EC 20/1998 *'), (40, '40 - Pens\xe3o por Morte'), (41, '41 - Sal\xe1rio Fam\xedlia - Art. 13 da EC 20/1998 c/c lei do Ente'), (42, '42 - Sal\xe1rio Maternidade - Art. 7\xba, XVIII c/c art. 39, \xa7 3\xba da Constitui\xe7\xe3o Federal'), (43, '43 - Complementa\xe7\xe3o de Aposentadoria do Regime Geral de Previd\xeancia Social (RGPS)'), (44, '44 - Complementa\xe7\xe3o de Pens\xe3o por Morte do Regime Geral de Previd\xeancia Social (RGPS)'), (5, '5 - Aposentadoria por Tempo de Servi\xe7o Integral - Art. 40, III, a da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998 *'), (6, '6 - Aposentadoria por Tempo de Servi\xe7o Proporcional - Art. 40, III, a da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998 *'), (7, '7 - Aposentadoria Compuls\xf3ria Proporcional calculada sobre a \xfaltima remunera\xe7\xe3o- Art. 40, \xa7 1\xba, Inciso II da CF, Reda\xe7\xe3o EC 20/1998'), (8, '8 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03'), (9, '9 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03, c/c EC 88/2015'), (91, '91 - Aposentadoria sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (92, '92 - Aposentadoria com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (93, '93 - Aposentadoria por invalidez com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (94, '94 - Aposentadoria por invalidez sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (95, '95 - Transfer\xeancia para reserva concedida antes do in\xedcio de vig\xeancia do eSocial'), (96, '96 - Reforma concedida antes do in\xedcio de vig\xeancia do eSocial'), (97, '97 - Pens\xe3o por morte com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (98, '98 - Pens\xe3o por morte sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (99, '99 - Outros Benef\xedcios previdenci\xe1rios concedidos antes do in\xedcio de vig\xeancia do eSocial')]),
        ),
        migrations.AddField(
            model_name='s1207infoperapuritensremun',
            name='s1207_infoperapur_remunperapur',
            field=models.ForeignKey(related_name='s1207infoperapuritensremun_s1207_infoperapur_remunperapur', to='s1207.s1207infoPerApurremunPerApur'),
        ),
        migrations.AddField(
            model_name='s1207infoperapur',
            name='s1207_dmdev',
            field=models.OneToOneField(related_name='s1207infoperapur_s1207_dmdev', to='s1207.s1207dmDev'),
        ),
        migrations.AddField(
            model_name='s1207infoperantitensremun',
            name='s1207_infoperant_remunperant',
            field=models.ForeignKey(related_name='s1207infoperantitensremun_s1207_infoperant_remunperant', to='s1207.s1207infoPerAntremunPerAnt'),
        ),
        migrations.AddField(
            model_name='s1207infoperantideestab',
            name='s1207_infoperant_ideperiodo',
            field=models.ForeignKey(related_name='s1207infoperantideestab_s1207_infoperant_ideperiodo', to='s1207.s1207infoPerAntidePeriodo'),
        ),
        migrations.AddField(
            model_name='s1207infoperant',
            name='s1207_dmdev',
            field=models.OneToOneField(related_name='s1207infoperant_s1207_dmdev', to='s1207.s1207dmDev'),
        ),
    ]
