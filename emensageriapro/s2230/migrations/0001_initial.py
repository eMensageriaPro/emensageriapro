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
            name='s2230emitente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nmemit', models.CharField(max_length=70)),
                ('ideoc', models.IntegerField(choices=[(1, '1 - Conselho Regional de Medicina (CRM)'), (2, '2 - Conselho Regional de Odontologia (CRO)'), (3, '3 - Registro do Minist\xe9rio da Sa\xfade (RMS)')])),
                ('nroc', models.CharField(max_length=14)),
                ('ufoc', models.CharField(blank=True, max_length=2, null=True, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230emitente_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230emitente_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2230_infoatestado', 'nmemit', 'ideoc', 'nroc', 'ufoc'],
                'db_table': 's2230_emitente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230fimAfastamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dttermafast', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230fimafastamento_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230fimafastamento_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2230_evtafasttemp', models.OneToOneField(related_name='s2230fimafastamento_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp')),
            ],
            options={
                'ordering': ['s2230_evtafasttemp', 'dttermafast'],
                'db_table': 's2230_fimafastamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230infoAtestado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codcid', models.CharField(max_length=4, null=True, blank=True)),
                ('qtddiasafast', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230infoatestado_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230infoatestado_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2230_iniafastamento', 'codcid', 'qtddiasafast'],
                'db_table': 's2230_infoatestado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230infoCessao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjcess', models.CharField(max_length=14)),
                ('infonus', models.IntegerField(choices=[(1, '1 - \xd4nus do Cedente'), (2, '2 - \xd4nus do Cession\xe1rio'), (3, '3 - \xd4nus do Cedente e Cession\xe1rio')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230infocessao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230infocessao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2230_iniafastamento', 'cnpjcess', 'infonus'],
                'db_table': 's2230_infocessao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230infoMandSind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjsind', models.CharField(max_length=14)),
                ('infonusremun', models.IntegerField(choices=[(1, '1 - Apenas do Empregador'), (2, '2 - Apenas do Sindicato'), (3, '3 - Parte do Empregador, sendo a diferen\xe7a e/ou complementa\xe7\xe3o salarial paga pelo Sindicato')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230infomandsind_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230infomandsind_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2230_iniafastamento', 'cnpjsind', 'infonusremun'],
                'db_table': 's2230_infomandsind',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230infoRetif',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origretif', models.IntegerField(choices=[(1, '1 - Por iniciativa do empregador'), (2, '2 - Revis\xe3o Administrativa'), (3, '3 - Determina\xe7\xe3o Judicial')])),
                ('tpproc', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Administrativo'), (2, '2 - Judicial'), (3, '3 - N\xfamero de Benef\xedcio (NB) do INSS')])),
                ('nrproc', models.CharField(max_length=21, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230inforetif_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230inforetif_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2230_evtafasttemp', models.OneToOneField(related_name='s2230inforetif_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp')),
            ],
            options={
                'ordering': ['s2230_evtafasttemp', 'origretif', 'tpproc', 'nrproc'],
                'db_table': 's2230_inforetif',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2230iniAfastamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtiniafast', models.DateField()),
                ('codmotafast', models.CharField(max_length=2, choices=[(b'1', '01 - Acidente/Doen\xe7a do trabalho'), (b'10', '10 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), com remunera\xe7\xe3o'), (b'11', '11 - C\xe1rcere'), (b'12', '12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25\xb0, par\xe1grafo \xfanico - Celetistas em geral'), (b'13', '13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1\xb0, inciso II, al\xednea 1 - Servidor p\xfablico, estatut\xe1rio ou n\xe3o, dos \xf3rg\xe3os ou entidades da Administra\xe7\xe3o Direta ou Indireta da Uni\xe3o, dos Estados, do Distrito Federal, dos Muni (...)'), (b'14', '14 - Cess\xe3o / Requisi\xe7\xe3o'), (b'15', '15 - Gozo de f\xe9rias ou recesso - Afastamento tempor\xe1rio para o gozo de f\xe9rias ou recesso'), (b'16', '16 - Licen\xe7a remunerada - Lei, liberalidade da empresa ou Acordo/Conven\xe7\xe3o Coletiva de Trabalho'), (b'17', '17 - Licen\xe7a Maternidade - 120 dias e suas prorroga\xe7\xf5es/antecipa\xe7\xf5es, inclusive para o c\xf4njuge sobrevivente'), (b'18', '18 - Licen\xe7a Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidad\xe3), inclusive para o c\xf4njuge sobrevivente'), (b'19', '19 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de aborto n\xe3o criminoso'), (b'20', '20 - Licen\xe7a Maternidade - Afastamento tempor\xe1rio por motivo de licen\xe7a-maternidade decorrente de ado\xe7\xe3o ou guarda judicial de crian\xe7a, inclusive para o c\xf4njuge sobrevivente'), (b'21', '21 - Licen\xe7a n\xe3o remunerada ou Sem Vencimento'), (b'22', '22 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, sem remunera\xe7\xe3o'), (b'23', '23 - Mandato Eleitoral - Afastamento tempor\xe1rio para o exerc\xedcio de mandato eleitoral, com remunera\xe7\xe3o'), (b'24', '24 - Mandato Sindical - Afastamento tempor\xe1rio para exerc\xedcio de mandato sindical'), (b'25', '25 - Mulher v\xedtima de viol\xeancia - Lei 11.340/2006 - art. 9\xba \xa72o, II - Lei Maria da Penha'), (b'26', '26 - Participa\xe7\xe3o de empregado no Conselho Nacional de Previd\xeancia Social-CNPS (art. 3\xba, Lei 8.213/1991)'), (b'27', '27 - Qualifica\xe7\xe3o - Afastamento por suspens\xe3o do contrato de acordo com o art 476-A da CLT'), (b'28', '28 - Representante Sindical - Afastamento pelo tempo que se fizer necess\xe1rio, quando, na qualidade de representante de entidade sindical, estiver participando de reuni\xe3o oficial de organismo internacional do qual o Brasil seja membro'), (b'29', '29 - Servi\xe7o Militar - Afastamento tempor\xe1rio para prestar servi\xe7o militar obrigat\xf3rio;'), (b'3', '03 - Acidente/Doen\xe7a n\xe3o relacionada ao trabalho'), (b'30', '30 - Suspens\xe3o disciplinar - CLT, art. 474'), (b'31', '31 - Servidor P\xfablico em Disponibilidade'), (b'33', '33 - Licen\xe7a Maternidade - de 180 dias, Lei 13.301/2016.'), (b'34', '34 - Inatividade do trabalhador avulso (portu\xe1rio ou n\xe3o portu\xe1rio) por per\xedodo superior a 90 dias'), (b'5', '05 - Afastamento/licen\xe7a prevista em regime pr\xf3prio (estatuto), sem remunera\xe7\xe3o'), (b'6', '06 - Aposentadoria por invalidez'), (b'7', '07 - Acompanhamento - Licen\xe7a para acompanhamento de membro da fam\xedlia enfermo'), (b'8', '08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, \xa76\xba, Dec. 99.684/90 (Regulamento do FGTS)')])),
                ('infomesmomtv', models.CharField(blank=True, max_length=1, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('tpacidtransito', models.IntegerField(blank=True, null=True, choices=[(1, '1 - Atropelamento'), (2, '2 - Colis\xe3o'), (3, '3 - Outros')])),
                ('observacao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2230iniafastamento_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2230iniafastamento_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2230_evtafasttemp', models.OneToOneField(related_name='s2230iniafastamento_s2230_evtafasttemp', to='esocial.s2230evtAfastTemp')),
            ],
            options={
                'ordering': ['s2230_evtafasttemp', 'dtiniafast', 'codmotafast', 'infomesmomtv', 'tpacidtransito', 'observacao'],
                'db_table': 's2230_iniafastamento',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s2230infomandsind',
            name='s2230_iniafastamento',
            field=models.OneToOneField(related_name='s2230infomandsind_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AddField(
            model_name='s2230infocessao',
            name='s2230_iniafastamento',
            field=models.OneToOneField(related_name='s2230infocessao_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AddField(
            model_name='s2230infoatestado',
            name='s2230_iniafastamento',
            field=models.ForeignKey(related_name='s2230infoatestado_s2230_iniafastamento', to='s2230.s2230iniAfastamento'),
        ),
        migrations.AddField(
            model_name='s2230emitente',
            name='s2230_infoatestado',
            field=models.OneToOneField(related_name='s2230emitente_s2230_infoatestado', to='s2230.s2230infoAtestado'),
        ),
    ]
