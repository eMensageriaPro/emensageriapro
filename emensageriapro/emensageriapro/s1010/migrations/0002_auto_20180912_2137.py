# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('s1010', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1010alteracaoideProcessoCPRP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1010alteracaoideprocessocprp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1010alteracaoideprocessocprp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1010_alteracao'],
                'db_table': 's1010_alteracao_ideprocessocprp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1010inclusaoideProcessoCPRP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1010inclusaoideprocessocprp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1010inclusaoideprocessocprp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s1010_inclusao'],
                'db_table': 's1010_inclusao_ideprocessocprp',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='s1010alteracao',
            options={'ordering': ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'fimvalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind', 'codinccprp', 'tetoremun', 'observacao'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1010alteracaoideprocessocp',
            options={'ordering': ['s1010_alteracao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp', 'tpproc', 'nrproc', 'extdecisao'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1010inclusao',
            options={'ordering': ['s1010_evttabrubrica', 'codrubr', 'idetabrubr', 'inivalid', 'fimvalid', 'dscrubr', 'natrubr', 'tprubr', 'codinccp', 'codincirrf', 'codincfgts', 'codincsind', 'codinccprp', 'tetoremun', 'observacao'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1010inclusaoideprocessocp',
            options={'ordering': ['s1010_inclusao', 'tpproc', 'nrproc', 'extdecisao', 'codsusp', 'tpproc', 'nrproc', 'extdecisao'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s1010alteracao',
            name='codinccprp',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'00', '00 - N\xe3o comp\xf5e a apura\xe7\xe3o de contribui\xe7\xf5es devidas ao RPPS/regime militar: Sem incid\xeancia para RPPS/regime militar'), (b'01', '01 - N\xe3o comp\xf5e a apura\xe7\xe3o de contribui\xe7\xf5es devidas ao RPPS/regime militar: Sem incid\xeancia em fun\xe7\xe3o de acordos internacionais de previd\xeancia social'), (b'10', '10 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente p\xfablico - mensal'), (b'11', '11 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente p\xfablico - 13\xba sal\xe1rio'), (b'12', '12 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente para o ente p\xfablico - mensal'), (b'13', '13 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente para o ente p\xfablico - 13\xb0 sal\xe1rio'), (b'14', '14 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente do segurado - mensal'), (b'15', '15 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente do segurado - 13\xb0 sal\xe1rio'), (b'16', '16 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - mensal'), (b'17', '17 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - 13\xba sal\xe1rio'), (b'18', '18 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - mensal'), (b'19', '19 - Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - 13\xb0 sal\xe1rio'), (b'20', '20 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Provento/pens\xe3o considerado para apura\xe7\xe3o da parcela excedente a teto RGPS'), (b'21', '21 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Do segurado de RPPS/militar e a cargo do ente p\xfablico - mensal'), (b'22', '22 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Do segurado de RPPS/militar e a cargo do ente p\xfablico - 13\xba sal\xe1rio'), (b'23', '23 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Somente para o ente p\xfablico - mensal'), (b'24', '24 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Somente para o ente p\xfablico - 13\xb0 sal\xe1rio'), (b'25', '25 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - mensal'), (b'26', '26 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - 13\xba sal\xe1rio'), (b'27', '27 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - mensal'), (b'28', '28 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - 13\xb0 sal\xe1rio'), (b'31', '31 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do segurado ativo RPPS/militar - mensal'), (b'32', '32 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'33', '33 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do aposentado RPPS/reforma/reserva - mensal'), (b'34', '34 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do aposentado RPPS /reforma/reserva - 13\xba sal\xe1rio'), (b'35', '35 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do pensionista RPPS/militar - mensal'), (b'36', '36 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do pensionista RPPS/militar - 13\xba sal\xe1rio'), (b'41', '41 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Do segurado ativo RPPS/militar - mensal'), (b'42', '42 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'51', '51 - Isen\xe7\xe3o de contribui\xe7\xe3o: Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - mensal'), (b'52', '52 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xba sal\xe1rio'), (b'91', '91 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do segurado ativo RPPS/militar - mensal'), (b'92', '92 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'93', '93 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do aposentado/reforma/reserva - mensal'), (b'94', '94 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do aposentado/reforma/reserva - 13\xba sal\xe1rio'), (b'95', '95 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do pensionista - mensal'), (b'96', '96 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do pensionista - 13\xba sal\xe1rio')]),
        ),
        migrations.AddField(
            model_name='s1010alteracao',
            name='tetoremun',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AddField(
            model_name='s1010inclusao',
            name='codinccprp',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'00', '00 - N\xe3o comp\xf5e a apura\xe7\xe3o de contribui\xe7\xf5es devidas ao RPPS/regime militar: Sem incid\xeancia para RPPS/regime militar'), (b'01', '01 - N\xe3o comp\xf5e a apura\xe7\xe3o de contribui\xe7\xf5es devidas ao RPPS/regime militar: Sem incid\xeancia em fun\xe7\xe3o de acordos internacionais de previd\xeancia social'), (b'10', '10 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente p\xfablico - mensal'), (b'11', '11 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Do segurado de RPPS/militar e a cargo do ente p\xfablico - 13\xba sal\xe1rio'), (b'12', '12 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente para o ente p\xfablico - mensal'), (b'13', '13 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente para o ente p\xfablico - 13\xb0 sal\xe1rio'), (b'14', '14 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente do segurado - mensal'), (b'15', '15 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Somente do segurado - 13\xb0 sal\xe1rio'), (b'16', '16 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - mensal'), (b'17', '17 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - 13\xba sal\xe1rio'), (b'18', '18 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - mensal'), (b'19', '19 - Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - 13\xb0 sal\xe1rio'), (b'20', '20 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o para o RPPS/regime militar): Provento/pens\xe3o considerado para apura\xe7\xe3o da parcela excedente a teto RGPS'), (b'21', '21 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Do segurado de RPPS/militar e a cargo do ente p\xfablico - mensal'), (b'22', '22 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Do segurado de RPPS/militar e a cargo do ente p\xfablico - 13\xba sal\xe1rio'), (b'23', '23 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Somente para o ente p\xfablico - mensal'), (b'24', '24 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Somente para o ente p\xfablico - 13\xb0 sal\xe1rio'), (b'25', '25 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - mensal'), (b'26', '26 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o do segurado e a cargo do ente - 13\xba sal\xe1rio'), (b'27', '27 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - mensal'), (b'28', '28 - Base de c\xe1lculo das contribui\xe7\xf5es (remunera\xe7\xe3o de contribui\xe7\xe3o) para o RPPS de outro ente p\xfablico: Verbas tempor\xe1rias - contribui\xe7\xe3o somente do segurado - 13\xb0 sal\xe1rio'), (b'31', '31 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do segurado ativo RPPS/militar - mensal'), (b'32', '32 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'33', '33 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do aposentado RPPS/reforma/reserva - mensal'), (b'34', '34 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do aposentado RPPS /reforma/reserva - 13\xba sal\xe1rio'), (b'35', '35 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do pensionista RPPS/militar - mensal'), (b'36', '36 - Contribui\xe7\xe3o descontada do segurado e benefici\xe1rio: Do pensionista RPPS/militar - 13\xba sal\xe1rio'), (b'41', '41 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Do segurado ativo RPPS/militar - mensal'), (b'42', '42 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'51', '51 - Isen\xe7\xe3o de contribui\xe7\xe3o: Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - mensal'), (b'52', '52 - Contribui\xe7\xe3o descontada para RPPS de outro ente p\xfablico: Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xba sal\xe1rio'), (b'91', '91 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do segurado ativo RPPS/militar - mensal'), (b'92', '92 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do segurado ativo RPPS/militar - 13\xba sal\xe1rio'), (b'93', '93 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do aposentado/reforma/reserva - mensal'), (b'94', '94 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do aposentado/reforma/reserva - 13\xba sal\xe1rio'), (b'95', '95 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do pensionista - mensal'), (b'96', '96 - Suspens\xe3o de incid\xeancia sobre Sal\xe1rio de Contribui\xe7\xe3o em decorr\xeancia de decis\xe3o judicial: Contribui\xe7\xe3o do pensionista - 13\xba sal\xe1rio')]),
        ),
        migrations.AddField(
            model_name='s1010inclusao',
            name='tetoremun',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracao',
            name='natrubr',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010alteracaoideprocessocp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusao',
            name='natrubr',
            field=models.TextField(max_length=4),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='extdecisao',
            field=models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico'), (1, '1 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria do Ente P\xfablico + Descontada dos Segurados'), (2, '2 - Contribui\xe7\xe3o Previdenci\xe1ria Patronal + Descontada dos Segurados'), (3, '3 - Contribui\xe7\xe3o Previdenci\xe1ria Descontada dos Segurados')]),
        ),
        migrations.AlterField(
            model_name='s1010inclusaoideprocessocp',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
        migrations.AddField(
            model_name='s1010inclusaoideprocessocprp',
            name='s1010_inclusao',
            field=models.ForeignKey(related_name='s1010inclusaoideprocessocprp_s1010_inclusao', to='s1010.s1010inclusao'),
        ),
        migrations.AddField(
            model_name='s1010alteracaoideprocessocprp',
            name='s1010_alteracao',
            field=models.ForeignKey(related_name='s1010alteracaoideprocessocprp_s1010_alteracao', to='s1010.s1010alteracao'),
        ),
    ]
