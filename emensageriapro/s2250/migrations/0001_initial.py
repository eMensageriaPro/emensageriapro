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
            name='s2250cancAvPrevio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtcancavprv', models.DateField()),
                ('observacao', models.CharField(max_length=255, null=True, blank=True)),
                ('mtvcancavprevio', models.IntegerField(choices=[(1, '1 - Reconsidera\xe7\xe3o prevista no artigo 489 da CLT'), (2, '2 - Determina\xe7\xe3o Judicial'), (3, '3 - Cumprimento de norma legal'), (9, '9 - Outros')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2250cancavprevio_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2250cancavprevio_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2250_evtavprevio', models.OneToOneField(related_name='s2250cancavprevio_s2250_evtavprevio', to='esocial.s2250evtAvPrevio')),
            ],
            options={
                'ordering': ['s2250_evtavprevio', 'dtcancavprv', 'observacao', 'mtvcancavprevio'],
                'db_table': 's2250_cancavprevio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2250detAvPrevio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtavprv', models.DateField()),
                ('dtprevdeslig', models.DateField()),
                ('tpavprevio', models.IntegerField(choices=[(1, '1 - Aviso pr\xe9vio trabalhado dado pelo empregador ao empregado, que optou pela redu\xe7\xe3o de duas horas di\xe1rias [caput do art. 488 da CLT]'), (2, '2 - Aviso pr\xe9vio trabalhado dado pelo empregador ao empregado, que optou pela redu\xe7\xe3o de dias corridos [par\xe1grafo \xfanico do art. 488 da CLT]'), (4, '4 - Aviso pr\xe9vio dado pelo empregado (pedido de demiss\xe3o), n\xe3o dispensado de seu cumprimento, sob pena de desconto, pelo empregador, dos sal\xe1rios correspondentes ao prazo respectivo (\xa72\xba do art. 487 da CLT)'), (5, '5 - Aviso pr\xe9vio trabalhado dado pelo empregador rural ao empregado, com redu\xe7\xe3o de um dia por semana ( art. 15 da Lei n\xba 5889/73)')])),
                ('observacao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2250detavprevio_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2250detavprevio_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2250_evtavprevio', models.OneToOneField(related_name='s2250detavprevio_s2250_evtavprevio', to='esocial.s2250evtAvPrevio')),
            ],
            options={
                'ordering': ['s2250_evtavprevio', 'dtavprv', 'dtprevdeslig', 'tpavprevio', 'observacao'],
                'db_table': 's2250_detavprevio',
                'managed': True,
            },
        ),
    ]
