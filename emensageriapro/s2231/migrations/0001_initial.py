# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0003_auto_20180912_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2231fimCessao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dttermcessao', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2231fimcessao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2231fimcessao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2231_evtcessao', models.OneToOneField(related_name='s2231fimcessao_s2231_evtcessao', to='esocial.s2231evtCessao')),
            ],
            options={
                'ordering': ['s2231_evtcessao', 'dttermcessao'],
                'db_table': 's2231_fimcessao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2231iniCessao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dtinicessao', models.DateField()),
                ('cnpjcess', models.CharField(max_length=14)),
                ('infonus', models.IntegerField(choices=[(1, '1 - Pagamento exclusivamente pelo cedente/origem'), (2, '2 - Pagamento exclusivamente pelo cession\xe1rio/destino'), (3, '3 - Pagamento pelo cedente/origem e pelo cession\xe1rio/destino'), (4, '4 - Pagamento pelo cedente/origem com ressarcimento pelo cession\xe1rio/destino')])),
                ('indcessao', models.IntegerField(choices=[(1, '1 - Cess\xe3o'), (2, '2 - Agente p\xfablico \xe0 disposi\xe7\xe3o da Justi\xe7a Eleitoral'), (3, '3 - Exerc\xedcio em outro \xf3rg\xe3o, em caso diferente de cess\xe3o')])),
                ('dscsituacao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2231inicessao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2231inicessao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2231_evtcessao', models.OneToOneField(related_name='s2231inicessao_s2231_evtcessao', to='esocial.s2231evtCessao')),
            ],
            options={
                'ordering': ['s2231_evtcessao', 'dtinicessao', 'cnpjcess', 'infonus', 'indcessao', 'dscsituacao'],
                'db_table': 's2231_inicessao',
                'managed': True,
            },
        ),
    ]
