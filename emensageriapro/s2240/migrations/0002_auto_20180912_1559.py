# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0003_auto_20180912_1556'),
        ('s2240', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2240iniExpRiscoativPericInsal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codativ', models.CharField(max_length=6)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2240iniexpriscoativpericinsal_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2240iniexpriscoativpericinsal_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2240_iniexprisco_infoamb', models.ForeignKey(related_name='s2240iniexpriscoativpericinsal_s2240_iniexprisco_infoamb', to='s2240.s2240iniExpRiscoinfoAmb')),
            ],
            options={
                'ordering': ['s2240_iniexprisco_infoamb', 'codativ'],
                'db_table': 's2240_iniexprisco_ativpericinsal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2240iniExpRiscoobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meterg', models.CharField(max_length=999)),
                ('observacao', models.CharField(max_length=999)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2240iniexpriscoobs_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2240iniexpriscoobs_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2240_evtexprisco', models.OneToOneField(related_name='s2240iniexpriscoobs_s2240_evtexprisco', to='esocial.s2240evtExpRisco')),
            ],
            options={
                'ordering': ['s2240_evtexprisco', 'meterg', 'observacao'],
                'db_table': 's2240_iniexprisco_obs',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2240iniExpRiscorespReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpfresp', models.CharField(max_length=11)),
                ('nisresp', models.CharField(max_length=11)),
                ('nmresp', models.CharField(max_length=70)),
                ('ideoc', models.IntegerField(choices=[(1, '1 - Conselho Regional de Medicina (CRM)'), (2, '2 - Conselho Regional de Engenharia e Agronomia (CREA)'), (9, '9 - Outros')])),
                ('dscoc', models.CharField(max_length=20, null=True, blank=True)),
                ('nroc', models.CharField(max_length=14)),
                ('ufoc', models.CharField(max_length=2, choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2240iniexpriscorespreg_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2240iniexpriscorespreg_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2240_evtexprisco', models.ForeignKey(related_name='s2240iniexpriscorespreg_s2240_evtexprisco', to='esocial.s2240evtExpRisco')),
            ],
            options={
                'ordering': ['s2240_evtexprisco', 'cpfresp', 'nisresp', 'nmresp', 'ideoc', 'dscoc', 'nroc', 'ufoc'],
                'db_table': 's2240_iniexprisco_respreg',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoepc',
            options={'ordering': ['s2240_iniexprisco_fatrisco', 'codep', 'dscepc', 'eficepc', 'codep'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscoepi',
            options={'ordering': ['s2240_iniexprisco_fatrisco', 'caepi', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao', 'manutencao'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s2240iniexpriscofatrisco',
            options={'ordering': ['s2240_iniexprisco_infoamb', 'codfatris', 'tpaval', 'intconc', 'unmed', 'tecmedicao', 'insalubridade', 'periculosidade', 'aposentesp', 'utilizepc', 'hieruso', 'utilizepi'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepc',
            name='codep',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscoepi',
            name='manutencao',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='aposentesp',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='hieruso',
            field=models.IntegerField(default=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='insalubridade',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='periculosidade',
            field=models.CharField(default=1, max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='tpaval',
            field=models.IntegerField(default=1, choices=[(1, '1 - Crit\xe9rio quantitativo'), (2, '2 - Crit\xe9rio qualitativo')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s2240iniexpriscofatrisco',
            name='unmed',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '01 - Dose di\xe1ria de ru\xeddo (n\xfamero adimensional)'), (2, '02 - Decibel linear (dB (linear))'), (3, '03 - Decibel (C) (dB(C))'), (4, '04 - Decibel (A) (dB(A))'), (5, '05 - Quilocaloria por hora (kcal/h)'), (6, '06 - Gray (Gy)'), (7, '07 - Sievert (Sv)'), (8, '08 - Quilograma-for\xe7a por cent\xedmetro quadrado (kgf/cm2)'), (9, '09 - Metro por segundo ao quadrado (m/s2)'), (10, '10 - Metro por segundo elevado a 1,75 (m/s1,75)'), (11, '11 - Parte de vapor ou g\xe1s por milh\xe3o de partes de ar contaminado (ppm)'), (12, '12 - Miligrama por metro c\xfabico de ar (mg/m3)'), (13, '13 - Fibra por cent\xedmetro c\xfabico (f/cm3)'), (14, '14 - Grau cent\xedgrados (\xbaC)'), (15, '15 - Metro por segundo (m/s)'), (16, '16 - Percentual (%)'), (17, '17 - Lux (lx)'), (18, '18 - Unidade formadora de col\xf4nias por metro c\xfabico (ufc/m3)')]),
        ),
        migrations.AlterField(
            model_name='s2240altexpriscofatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2240iniexpriscofatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
    ]
