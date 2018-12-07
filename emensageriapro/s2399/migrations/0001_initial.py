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
            name='s2399detOper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjoper', models.CharField(max_length=14)),
                ('regans', models.CharField(max_length=6)),
                ('vrpgtit', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399detoper_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399detoper_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2399_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'],
                'db_table': 's2399_detoper',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399detPlano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpdep', models.CharField(max_length=2, choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')])),
                ('cpfdep', models.CharField(max_length=11, null=True, blank=True)),
                ('nmdep', models.CharField(max_length=70)),
                ('dtnascto', models.DateField()),
                ('vlrpgdep', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399detplano_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399detplano_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_detoper', models.ForeignKey(related_name='s2399detplano_s2399_detoper', to='s2399.s2399detOper')),
            ],
            options={
                'ordering': ['s2399_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep'],
                'db_table': 's2399_detplano',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399detVerbas',
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
                ('criado_por', models.ForeignKey(related_name='s2399detverbas_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399detverbas_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2399_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr'],
                'db_table': 's2399_detverbas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399dmDev',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idedmdev', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399dmdev_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399dmdev_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2399_verbasresc', 'idedmdev'],
                'db_table': 's2399_dmdev',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399ideEstabLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codlotacao', models.CharField(max_length=30)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399ideestablot_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399ideestablot_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_dmdev', models.ForeignKey(related_name='s2399ideestablot_s2399_dmdev', to='s2399.s2399dmDev')),
            ],
            options={
                'ordering': ['s2399_dmdev', 'tpinsc', 'nrinsc', 'codlotacao'],
                'db_table': 's2399_ideestablot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399infoAgNocivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grauexp', models.IntegerField(choices=[(1, '1 - N\xe3o ensejador de aposentadoria especial'), (2, '2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribui\xe7\xe3o e al\xedquota de 12%)'), (3, '3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribui\xe7\xe3o e al\xedquota de 9%)'), (4, '4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribui\xe7\xe3o e al\xedquota de 6%)')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399infoagnocivo_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399infoagnocivo_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_ideestablot', models.OneToOneField(related_name='s2399infoagnocivo_s2399_ideestablot', to='s2399.s2399ideEstabLot')),
            ],
            options={
                'ordering': ['s2399_ideestablot', 'grauexp'],
                'db_table': 's2399_infoagnocivo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399infoMV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indmv', models.IntegerField(choices=[(1, '1 - O declarante aplica a al\xedquota de desconto do segurado sobre a remunera\xe7\xe3o por ele informada (o percentual da al\xedquota ser\xe1 obtido considerando a remunera\xe7\xe3o total do trabalhador)'), (2, '2 - O declarante aplica a al\xedquota de desconto do segurado sobre a diferen\xe7a entre o limite m\xe1ximo do sal\xe1rio de contribui\xe7\xe3o e a remunera\xe7\xe3o de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'), (3, '3 - O declarante n\xe3o realiza desconto do segurado, uma vez que houve desconto sobre o limite m\xe1ximo de sal\xe1rio de contribui\xe7\xe3o em outra(s) empresa(s)')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399infomv_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399infomv_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2399_verbasresc', 'indmv'],
                'db_table': 's2399_infomv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399infoSaudeColet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399infosaudecolet_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399infosaudecolet_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_ideestablot', models.OneToOneField(related_name='s2399infosaudecolet_s2399_ideestablot', to='s2399.s2399ideEstabLot')),
            ],
            options={
                'ordering': ['s2399_ideestablot'],
                'db_table': 's2399_infosaudecolet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399infoSimples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indsimples', models.IntegerField(choices=[(1, '1 - Contribui\xe7\xe3o Substitu\xedda Integralmente'), (2, '2 - Contribui\xe7\xe3o n\xe3o substitu\xedda'), (3, '3 - Contribui\xe7\xe3o n\xe3o substitu\xedda concomitante com contribui\xe7\xe3o substitu\xedda')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399infosimples_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399infosimples_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_ideestablot', models.OneToOneField(related_name='s2399infosimples_s2399_ideestablot', to='s2399.s2399ideEstabLot')),
            ],
            options={
                'ordering': ['s2399_ideestablot', 'indsimples'],
                'db_table': 's2399_infosimples',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399procJudTrab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tptrib', models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - IRRF'), (4, '4 - Contribui\xe7\xe3o sindical')])),
                ('nrprocjud', models.CharField(max_length=20)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399procjudtrab_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399procjudtrab_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['s2399_verbasresc', 'tptrib', 'nrprocjud', 'codsusp'],
                'db_table': 's2399_procjudtrab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399quarentena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtfimquar', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399quarentena_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399quarentena_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_evttsvtermino', models.OneToOneField(related_name='s2399quarentena_s2399_evttsvtermino', to='esocial.s2399evtTSVTermino')),
            ],
            options={
                'ordering': ['s2399_evttsvtermino', 'dtfimquar'],
                'db_table': 's2399_quarentena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399remunOutrEmpr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpinsc', models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('codcateg', models.IntegerField()),
                ('vlrremunoe', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399remunoutrempr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399remunoutrempr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_infomv', models.ForeignKey(related_name='s2399remunoutrempr_s2399_infomv', to='s2399.s2399infoMV')),
            ],
            options={
                'ordering': ['s2399_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe'],
                'db_table': 's2399_remunoutrempr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2399verbasResc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2399verbasresc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2399verbasresc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2399_evttsvtermino', models.OneToOneField(related_name='s2399verbasresc_s2399_evttsvtermino', to='esocial.s2399evtTSVTermino')),
            ],
            options={
                'ordering': ['s2399_evttsvtermino'],
                'db_table': 's2399_verbasresc',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='s2399procjudtrab',
            name='s2399_verbasresc',
            field=models.ForeignKey(related_name='s2399procjudtrab_s2399_verbasresc', to='s2399.s2399verbasResc'),
        ),
        migrations.AddField(
            model_name='s2399infomv',
            name='s2399_verbasresc',
            field=models.OneToOneField(related_name='s2399infomv_s2399_verbasresc', to='s2399.s2399verbasResc'),
        ),
        migrations.AddField(
            model_name='s2399dmdev',
            name='s2399_verbasresc',
            field=models.ForeignKey(related_name='s2399dmdev_s2399_verbasresc', to='s2399.s2399verbasResc'),
        ),
        migrations.AddField(
            model_name='s2399detverbas',
            name='s2399_ideestablot',
            field=models.ForeignKey(related_name='s2399detverbas_s2399_ideestablot', to='s2399.s2399ideEstabLot'),
        ),
        migrations.AddField(
            model_name='s2399detoper',
            name='s2399_infosaudecolet',
            field=models.ForeignKey(related_name='s2399detoper_s2399_infosaudecolet', to='s2399.s2399infoSaudeColet'),
        ),
    ]
