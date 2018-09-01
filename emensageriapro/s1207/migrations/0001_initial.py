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
            name='s1207dmDev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpbenef', models.IntegerField(choices=[(1, '1 - Aposentadoria Volunt\xe1ria por Idade e Tempo de Contribui\xe7\xe3o - Proventos Integrais: Art. 40, \xa7 1\xba, III \u201ca\u201d da CF, Reda\xe7\xe3o EC 20/98'), (10, '10 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03, c/c LC 152/2015'), (11, '11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o: Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98'), (12, '12 - Aposentadoria - Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o - Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98: Geral'), (13, '13 - Aposentadoria Especial do Professor - Regra de Transi\xe7\xe3o do Art. 8\xba, da EC 20/98: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o.'), (14, '14 - Aposentadoria com proventos proporcionais calculados sobre a \xfaltima remunera\xe7\xe3oRegra de Transi\xe7\xe3o do Art. 8\xba, da EC20/98 - Geral'), (15, '15 - Aposentadoria - Regra de Transi\xe7\xe3o do Art. 3\xba, da EC 47/05: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o'), (16, '16 - Aposentadoria Especial de Professor - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o a partir de 01/01/2006)'), (17, '17 - Aposentadoria Especial de Professor - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (18, '18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o a partir de 01/01/2006)'), (19, '19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC41/03: Proventos pela M\xe9dia com redutor (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (2, '2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF reda\xe7\xe3o original - Anterior \xe0 EC 20/1998'), (20, '20 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC 41/03 - Proventos pela M\xe9dia com redutor - Geral (Implementa\xe7\xe3o a partir de 01/01/2006)'), (21, '21 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 2\xba, da EC 41/03 - Proventos pela M\xe9dia reduzida - Geral (Implementa\xe7\xe3o at\xe9 31/12/2005)'), (22, '22 - Aposentadoria Volunt\xe1ria - Regra de Transi\xe7\xe3o do Art. 6\xba, da EC41/03: Proventos Integrais correspondentes \xe1 ultima remunera\xe7\xe3o do cargo - Geral'), (23, '23 - Aposentadoria Volunt\xe1ria Professor Educa\xe7\xe3o infantil, ensino fundamental e m\xe9dioRegra de Transi\xe7\xe3o do Art. 6\xba, da EC41/03: Proventos Integrais correspondentes \xe0 \xfaltima remunera\xe7\xe3o do cargo'), (24, '24 - Aposentadoria Volunt\xe1ria por Idade - Proventos Proporcionais calculados sobre a \xfaltima remunera\xe7\xe3o do cargo: Art. 40, \xa7 1\xba, Inciso III, al\xednea "b" CF, Reda\xe7\xe3o EC 20/98'), (25, '25 - Aposentadoria Volunt\xe1ria por Idade - Proventos pela M\xe9dia proporcionais - Art. 40, \xa7 1\xba, Inciso III, al\xednea "b" CF, Reda\xe7\xe3o EC 41/03'), (26, '26 - Aposentadoria Volunt\xe1ria por Idade e por Tempo de Contribui\xe7\xe3o - Proventos pela M\xe9dia: Art. 40, \xa7 1\xba, Inciso III, aliena "a", CF, Reda\xe7\xe3o EC 41/03'), (27, '27 - Aposentadoria Volunt\xe1ria por Tempo de Contribui\xe7\xe3o - Especial do professor de q/q n\xedvel de ensino - Art. 40, III, al\xednea b, da CF- Red. Original at\xe9 EC 20/1998'), (28, '28 - Aposentadoria Volunt\xe1ria por idade e Tempo de Contribui\xe7\xe3o - Especial do professor ed. infantil, ensino fundamental e m\xe9dio - Art. 40, \xa7 1\xba, Inciso III, al\xednea a, c/c \xa7 5\xba da CF red. da EC 20/1998 )'), (29, '29 - Aposentadoria Volunt\xe1ria por idade e Tempo de Contribui\xe7\xe3o - Especial de Professor - Proventos pela M\xe9dia: Art. 40, \xa7 1\xba, Inciso III, al\xednea "a", C/C \xa7 5\xba da CF, Reda\xe7\xe3o EC 41/2003'), (3, '3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998'), (30, '30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40, Inciso I, Reda\xe7\xe3o Original, CF'), (31, '31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40, \xa7 1\xba, Inciso I da CF com Reda\xe7\xe3o da EC 20/1998'), (32, '32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela m\xe9dia) - Art. 40, \xa7 1\xba, Inciso I da CF com Reda\xe7\xe3o da EC 41/2003'), (33, '33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na \xfaltima remunera\xe7\xe3o do cargo) - Art. 40 \xba 1\xba, Inciso I da CF C/C combinado com Art. 6\xaa- A da EC 70/2012'), (34, '34 - Reforma por invalidez'), (35, '35 - Reserva Remunerada Compuls\xf3ria'), (36, '36 - Reserva Remunerada Integral'), (37, '37 - Reserva Remunerada Proporcional'), (38, '38 - Aux\xedlio Doen\xe7a - Conforme lei do Ente'), (39, '39 - Aux\xedlio Reclus\xe3o - Art. 13 da EC 20/1998 c/c lei do Ente'), (4, '4 - Aposentadoria Compuls\xf3ria - Proventos proporcionais: Art. 40, II da CF reda\xe7\xe3o original, anterior \xe0 EC 20/1998 *'), (40, '40 - Pens\xe3o por Morte'), (41, '41 - Sal\xe1rio Fam\xedlia - Art. 13 da EC 20/1998 c/c lei do Ente'), (42, '42 - Sal\xe1rio Maternidade - Art. 7\xba, XVIII c/c art. 39, \xa7 3\xba da Constitui\xe7\xe3o Federal'), (43, '43 - Complementa\xe7\xe3o de Aposentadoria do Regime Geral de Previd\xeancia Social (RGPS)'), (44, '44 - Complementa\xe7\xe3o de Pens\xe3o por Morte do Regime Geral de Previd\xeancia Social (RGPS)'), (5, '5 - Aposentadoria por Tempo de Servi\xe7o Integral - Art. 40, III, a da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998 *'), (6, '6 - Aposentadoria por Tempo de Servi\xe7o Proporcional - Art. 40, III, a da CF reda\xe7\xe3o original - anterior \xe0 EC 20/1998 *'), (7, '7 - Aposentadoria Compuls\xf3ria Proporcional calculada sobre a \xfaltima remunera\xe7\xe3o- Art. 40, \xa7 1\xba, Inciso II da CF, Reda\xe7\xe3o EC 20/1998'), (8, '8 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03'), (9, '9 - Aposentadoria Compuls\xf3ria Proporcional calculada pela m\xe9dia - Art. 40, \xa7 1\xba Inciso II da CF, Reda\xe7\xe3o EC 41/03, c/c EC 88/2015'), (91, '91 - Aposentadoria sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (92, '92 - Aposentadoria com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (93, '93 - Aposentadoria por invalidez com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (94, '94 - Aposentadoria por invalidez sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (95, '95 - Transfer\xeancia para reserva concedida antes do in\xedcio de vig\xeancia do eSocial'), (96, '96 - Reforma concedida antes do in\xedcio de vig\xeancia do eSocial'), (97, '97 - Pens\xe3o por morte com paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (98, '98 - Pens\xe3o por morte sem paridade concedida antes do in\xedcio de vig\xeancia do eSocial'), (99, '99 - Outros Benef\xedcios previdenci\xe1rios concedidos antes do in\xedcio de vig\xeancia do eSocial')])),
                ('nrbenefic', models.CharField(max_length=20)),
                ('idedmdev', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207dmdev_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207dmdev_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_evtbenprrp', models.ForeignKey(related_name='s1207dmdev_s1207_evtbenprrp', to='esocial.s1207evtBenPrRP')),
            ],
            options={
                'ordering': ['s1207_evtbenprrp', 'tpbenef', 'nrbenefic', 'idedmdev'],
                'db_table': 's1207_dmdev',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1207itens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codrubr', models.CharField(max_length=30)),
                ('idetabrubr', models.CharField(max_length=8)),
                ('vrrubr', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1207itens_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1207itens_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1207_dmdev', models.ForeignKey(related_name='s1207itens_s1207_dmdev', to='s1207.s1207dmDev')),
            ],
            options={
                'ordering': ['s1207_dmdev', 'codrubr', 'idetabrubr', 'vrrubr'],
                'db_table': 's1207_itens',
                'managed': True,
            },
        ),
    ]
