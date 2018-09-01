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
            name='s5001calcTerc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpcr', models.IntegerField(choices=[(108201, '108201 - Contribui\xe7\xe3o previdenci\xe1ria (CP) descontada do segurado empregado/avulso, al\xedquotas 8%, 9% ou 11%'), (108202, '108202 - CP descontada do segurado empregado rural curto prazo, al\xedquota de 8%, lei 11718/2008'), (108203, '108203 - CP descontada do segurado empregado dom\xe9stico ou segurado especial, al\xedquota de 8%, 9% ou 11%'), (108204, '108204 - CP descontada do segurado especial curto prazo, al\xedquota de 8%, lei 11718/2008'), (108221, '108221 - CP descontada do segurado empregado/avulso 13\xb0 sal\xe1rio, al\xedquotas 8%, 9% ou 11% (codIncCP = [12, 16])'), (108222, '108222 - CP descontada do segurado empregado rural curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (108223, '108223 - CP descontada do segurado empregado dom\xe9stico ou segurado especial 13\xb0 sal\xe1rio, al\xedquota de 8%, 9% ou 11%(codIncCP = [12, 16])'), (108224, '108224 - CP descontada do segurado especial curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (1099, '1099-01 - CP descontada do contribuinte individual, al\xedquota de 11%'), (109902, '109902 - CP descontada do contribuinte individual, al\xedquota de 20%'), (1218, '1218-02 - Contribui\xe7\xe3o ao SEST, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,5%'), (1221, '1221-02 - Contribui\xe7\xe3o ao SENAT, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,0%')])),
                ('vrcssegterc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdescterc', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001calcterc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001calcterc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5001_infocategincid', 'tpcr', 'vrcssegterc', 'vrdescterc'],
                'db_table': 's5001_calcterc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001ideEstabLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codlotacao', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001ideestablot_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001ideestablot_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5001_infocp', 'tpinsc', 'nrinsc', 'codlotacao'],
                'db_table': 's5001_ideestablot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001infoBaseCS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ind13', models.IntegerField(choices=[(0, '0 - Mensal'), (1, '1 - 13\xb0 sal\xe1rio - {codIncCP} = [12, 14, 16, 22, 26, 32, 92, 94]')])),
                ('tpvalor', models.IntegerField(choices=[(11, '11 - Base de c\xe1lculo da Contribui\xe7\xe3o Previdenci\xe1ria normal'), (12, '12 - Base de c\xe1lculo da Contribui\xe7\xe3o Previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 15 anos de contribui\xe7\xe3o'), (13, '13 - Base de c\xe1lculo da Contribui\xe7\xe3o Previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 20 anos de contribui\xe7\xe3o'), (14, '14 - Base de c\xe1lculo da Contribui\xe7\xe3o Previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 25 anos de contribui\xe7\xe3o'), (15, '15 - Base de c\xe1lculo da contribui\xe7\xe3o previdenci\xe1ria adicional normal - exclusiva do empregador'), (16, '16 - Base de c\xe1lculo da contribui\xe7\xe3o previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 15 anos de contribui\xe7\xe3o - exclusiva do empregador'), (17, '17 - Base de c\xe1lculo da contribui\xe7\xe3o previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 20 anos de contribui\xe7\xe3o - exclusiva do empregador'), (18, '18 - Base de c\xe1lculo da contribui\xe7\xe3o previdenci\xe1ria adicional para o financiamento dos benef\xedcios de aposentadoria especial ap\xf3s 25 anos de contribui\xe7\xe3o - exclusiva do empregador'), (19, '19 - Base de c\xe1lculo da contribui\xe7\xe3o previdenci\xe1ria exclusiva do empregado'), (21, '21 - Valor total descontado do trabalhador para recolhimento \xe0 Previd\xeancia Social'), (22, '22 - Valor descontado do trabalhador para recolhimento ao Sest'), (23, '23 - Valor descontado do trabalhador para recolhimento ao Senat'), (31, '31 - Valor pago ao trabalhador a t\xedtulo de sal\xe1rio-fam\xedlia'), (32, '32 - Valor pago ao trabalhador a t\xedtulo de sal\xe1rio-maternidade'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial - Base de c\xe1lculo (BC) da Contribui\xe7\xe3o Previdenci\xe1ria (CP) Normal'), (92, '92 - Incid. suspensa em decorr\xeancia de decis\xe3o judicial - BC CP Aposentadoria Especial aos 15 anos de trabalho'), (93, '93 - Incid. suspensa em decorr\xeancia de decis\xe3o judicial - BC CP Aposentadoria Especial aos 20 anos de trabalho'), (94, '94 - Incid. suspensa em decorr\xeancia de decis\xe3o judicial - BC CP Aposentadoria Especial aos 25 anos de trabalho')])),
                ('valor', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001infobasecs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001infobasecs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s5001_infocategincid', 'ind13', 'tpvalor', 'valor'],
                'db_table': 's5001_infobasecs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001infoCategIncid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.CharField(max_length=30, null=True, blank=True)),
                ('codcateg', models.IntegerField(choices=[(101, '101 - Empregado - Geral, inclusive o empregado p\xfablico da administra\xe7\xe3o direta ou indireta contratado pela CLT.'), (102, '102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008'), (103, '103 - Empregado - Aprendiz'), (104, '104 - Empregado - Dom\xe9stico'), (105, '105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98'), (106, '106 - Trabalhador Tempor\xe1rio - contrato por prazo determinado nos termos da Lei 6019/74'), (111, '111 - Empregado - contrato de trabalho intermitente'), (201, '201 - Trabalhador Avulso Portu\xe1rio'), (202, '202 - Trabalhador Avulso N\xe3o Portu\xe1rio'), (301, '301 - Servidor P\xfablico Titular de Cargo Efetivo, Magistrado, Ministro de Tribunal de Contas, Conselheiro de Tribunal de Contas e Membro do Minist\xe9rio P\xfablico'), (302, '302 - Servidor P\xfablico Ocupante de Cargo exclusivo em comiss\xe3o'), (303, '303 - Agente Pol\xedtico'), (305, '305 - Servidor P\xfablico indicado para conselho ou \xf3rg\xe3o deliberativo, na condi\xe7\xe3o de representante do governo, \xf3rg\xe3o ou entidade da administra\xe7\xe3o p\xfablica.'), (306, '306 - Servidor P\xfablico Tempor\xe1rio, sujeito a regime administrativo especial definido em lei pr\xf3pria'), (307, '307 - Militar efetivo'), (308, '308 - Conscrito'), (309, '309 - Agente P\xfablico - Outros'), (401, '401 - Dirigente Sindical - informa\xe7\xe3o prestada pelo Sindicato'), (410, '410 - Trabalhador cedido - informa\xe7\xe3o prestada pelo Cession\xe1rio'), (701, '701 - Contribuinte individual - Aut\xf4nomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual'), (711, '711 - Contribuinte individual - Transportador aut\xf4nomo de passageiros'), (712, '712 - Contribuinte individual - Transportador aut\xf4nomo de carga'), (721, '721 - Contribuinte individual - Diretor n\xe3o empregado, com FGTS'), (722, '722 - Contribuinte individual - Diretor n\xe3o empregado, sem FGTS'), (723, '723 - Contribuinte individual - empres\xe1rios, s\xf3cios e membro de conselho de administra\xe7\xe3o ou fiscal'), (731, '731 - Contribuinte individual - Cooperado que presta servi\xe7os por interm\xe9dio de Cooperativa de Trabalho'), (734, '734 - Contribuinte individual - Transportador Cooperado que presta servi\xe7os por interm\xe9dio de cooperativa de trabalho'), (738, '738 - Contribuinte individual - Cooperado filiado a Cooperativa de Produ\xe7\xe3o'), (741, '741 - Contribuinte individual - Microempreendedor Individual'), (751, '751 - Contribuinte individual - magistrado classista tempor\xe1rio da Justi\xe7a do Trabalho ou da Justi\xe7a Eleitoral que seja aposentado de qualquer regime previdenci\xe1rio'), (761, '761 - Contribuinte individual - Associado eleito para dire\xe7\xe3o de Cooperativa, associa\xe7\xe3o ou entidade de classe de qualquer natureza ou finalidade, bem como o s\xedndico ou administrador eleito para exercer atividade de dire\xe7\xe3o condominial, desde que recebam r (...)'), (771, '771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei n\xba 8.069, de 13 de julho de 1990'), (781, '781 - Ministro de confiss\xe3o religiosa ou membro de vida consagrada, de congrega\xe7\xe3o ou de ordem religiosa'), (901, '901 - Estagi\xe1rio'), (902, '902 - M\xe9dico Residente'), (903, '903 - Bolsista, nos termos da lei 8958/1994'), (904, '904 - Participante de curso de forma\xe7\xe3o, como etapa de concurso p\xfablico, sem v\xednculo de emprego/estatut\xe1rio'), (905, '905 - Atleta n\xe3o profissional em forma\xe7\xe3o que receba bolsa')])),
                ('indsimples', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Contribui\xe7\xe3o Substitu\xedda Integralmente'), (2, '2 - Contribui\xe7\xe3o n\xe3o substitu\xedda'), (3, '3 - Contribui\xe7\xe3o n\xe3o substitu\xedda concomitante com contribui\xe7\xe3o substitu\xedda')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001infocategincid_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001infocategincid_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5001_ideestablot', models.ForeignKey(related_name='s5001infocategincid_s5001_ideestablot', to='s5001.s5001ideEstabLot')),
            ],
            options={
                'ordering': ['s5001_ideestablot', 'matricula', 'codcateg', 'indsimples'],
                'db_table': 's5001_infocategincid',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001infoCp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001infocp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001infocp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5001_evtbasestrab', models.OneToOneField(related_name='s5001infocp_s5001_evtbasestrab', to='esocial.s5001evtBasesTrab')),
            ],
            options={
                'ordering': ['s5001_evtbasestrab'],
                'db_table': 's5001_infocp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001infoCpCalc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpcr', models.IntegerField(choices=[(108201, '108201 - Contribui\xe7\xe3o previdenci\xe1ria (CP) descontada do segurado empregado/avulso, al\xedquotas 8%, 9% ou 11%'), (108202, '108202 - CP descontada do segurado empregado rural curto prazo, al\xedquota de 8%, lei 11718/2008'), (108203, '108203 - CP descontada do segurado empregado dom\xe9stico ou segurado especial, al\xedquota de 8%, 9% ou 11%'), (108204, '108204 - CP descontada do segurado especial curto prazo, al\xedquota de 8%, lei 11718/2008'), (108221, '108221 - CP descontada do segurado empregado/avulso 13\xb0 sal\xe1rio, al\xedquotas 8%, 9% ou 11% (codIncCP = [12, 16])'), (108222, '108222 - CP descontada do segurado empregado rural curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (108223, '108223 - CP descontada do segurado empregado dom\xe9stico ou segurado especial 13\xb0 sal\xe1rio, al\xedquota de 8%, 9% ou 11%(codIncCP = [12, 16])'), (108224, '108224 - CP descontada do segurado especial curto prazo 13\xb0 sal\xe1rio, al\xedquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'), (1099, '1099-01 - CP descontada do contribuinte individual, al\xedquota de 11%'), (109902, '109902 - CP descontada do contribuinte individual, al\xedquota de 20%'), (1218, '1218-02 - Contribui\xe7\xe3o ao SEST, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,5%'), (1221, '1221-02 - Contribui\xe7\xe3o ao SENAT, descontada do transportador aut\xf4nomo, \xe0 al\xedquota de 1,0%')])),
                ('vrcpseg', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vrdescseg', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001infocpcalc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001infocpcalc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5001_evtbasestrab', models.ForeignKey(related_name='s5001infocpcalc_s5001_evtbasestrab', to='esocial.s5001evtBasesTrab')),
            ],
            options={
                'ordering': ['s5001_evtbasestrab', 'tpcr', 'vrcpseg', 'vrdescseg'],
                'db_table': 's5001_infocpcalc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s5001procJudTrab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s5001procjudtrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s5001procjudtrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s5001_evtbasestrab', models.ForeignKey(related_name='s5001procjudtrab_s5001_evtbasestrab', to='esocial.s5001evtBasesTrab')),
            ],
            options={
                'ordering': ['s5001_evtbasestrab', 'nrprocjud', 'codsusp'],
                'db_table': 's5001_procjudtrab',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s5001infobasecs',
            name='s5001_infocategincid',
            field=models.ForeignKey(related_name='s5001infobasecs_s5001_infocategincid', to='s5001.s5001infoCategIncid'),
        ),
        migrations.AddField(
            model_name='s5001ideestablot',
            name='s5001_infocp',
            field=models.ForeignKey(related_name='s5001ideestablot_s5001_infocp', to='s5001.s5001infoCp'),
        ),
        migrations.AddField(
            model_name='s5001calcterc',
            name='s5001_infocategincid',
            field=models.ForeignKey(related_name='s5001calcterc_s5001_infocategincid', to='s5001.s5001infoCategIncid'),
        ),
    ]
