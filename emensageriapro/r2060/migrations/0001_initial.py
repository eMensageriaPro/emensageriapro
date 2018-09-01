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
            name='r2060infoProc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpproc', models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')])),
                ('nrproc', models.CharField(max_length=21)),
                ('codsusp', models.IntegerField(null=True, blank=True)),
                ('vlrcprbsusp', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2060infoproc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2060infoproc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2060_tipocod', 'tpproc', 'nrproc', 'codsusp', 'vlrcprbsusp'],
                'db_table': 'r2060_infoproc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2060tipoAjuste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpajuste', models.IntegerField(choices=[(0, '0 - Ajuste de redu\xe7\xe3o'), (1, '1 - Ajuste de acr\xe9scimo')])),
                ('codajuste', models.IntegerField(choices=[(1, '1 - Ajuste da CPRB: Ado\xe7\xe3o do Regime de Caixa'), (10, '10 - O valor do aporte de recursos realizado nos termos do art 6 \xa73 inciso III da Lei 11.079/2004'), (11, '11 - Demais ajustes oriundos da Legisla\xe7\xe3o Tribut\xe1ria, estorno ou outras situa\xe7\xf5es'), (2, '2 - Ajuste da CPRB: Diferimento de Valores a recolher no per\xedodo'), (3, '3 - Adi\xe7\xe3o de valores Diferidos em Per\xedodo(s) Anteriores(es)'), (4, '4 - Exporta\xe7\xf5es diretas'), (5, '5 -Transporte internacional de cargas'), (6, '6 - Vendas canceladas e os descontos incondicionais concedidos'), (7, '7 - IPI, se inclu\xeddo na receita bruta'), (8, '8 - ICMS, quando cobrado pelo vendedor dos bens ou prestador dos servi\xe7os na condi\xe7\xe3o de substituto tribut\xe1rio'), (9, '9 - Receita bruta reconhecida pela constru\xe7\xe3o, recupera\xe7\xe3o, reforma, amplia\xe7\xe3o ou melhoramento da infraestrutura, cuja contrapartida seja ativo intang\xedvel representativo de direito de explora\xe7\xe3o, no caso de contratos de concess\xe3o de servi\xe7os p\xfablicos')])),
                ('vlrajuste', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('descajuste', models.CharField(max_length=20)),
                ('dtajuste', models.CharField(max_length=7)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2060tipoajuste_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2060tipoajuste_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['r2060_tipocod', 'tpajuste', 'codajuste', 'vlrajuste', 'descajuste', 'dtajuste'],
                'db_table': 'r2060_tipoajuste',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='r2060tipoCod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codativecon', models.CharField(max_length=8)),
                ('vlrrecbrutaativ', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrexcrecbruta', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlradicrecbruta', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrbccprb', models.DecimalField(max_length=14, max_digits=15, decimal_places=2)),
                ('vlrcprbapur', models.DecimalField(max_length=14, null=True, max_digits=15, decimal_places=2, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2060tipocod_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2060tipocod_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2060_evtcprb', models.ForeignKey(related_name='r2060tipocod_r2060_evtcprb', to='efdreinf.r2060evtCPRB')),
            ],
            options={
                'ordering': ['r2060_evtcprb', 'codativecon', 'vlrrecbrutaativ', 'vlrexcrecbruta', 'vlradicrecbruta', 'vlrbccprb', 'vlrcprbapur'],
                'db_table': 'r2060_tipocod',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='r2060tipoajuste',
            name='r2060_tipocod',
            field=models.ForeignKey(related_name='r2060tipoajuste_r2060_tipocod', to='r2060.r2060tipoCod'),
        ),
        migrations.AddField(
            model_name='r2060infoproc',
            name='r2060_tipocod',
            field=models.ForeignKey(related_name='r2060infoproc_r2060_tipocod', to='r2060.r2060tipoCod'),
        ),
    ]
