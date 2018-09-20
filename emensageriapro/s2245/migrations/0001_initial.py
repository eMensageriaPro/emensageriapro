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
            name='s2245ideProfResp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpfprof', models.CharField(max_length=11)),
                ('nmprof', models.CharField(max_length=70)),
                ('tpprof', models.IntegerField(choices=[(1, '1 - Profissional empregado do declarante'), (2, '2 - Profissional sem v\xednculo de emprego/estatut\xe1rio com o declarante')])),
                ('matricula', models.CharField(max_length=30, null=True, blank=True)),
                ('formprof', models.CharField(max_length=255)),
                ('codcbo', models.CharField(max_length=6)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2245ideprofresp_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2245ideprofresp_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2245_evttreicap', models.ForeignKey(related_name='s2245ideprofresp_s2245_evttreicap', to='esocial.s2245evtTreiCap')),
            ],
            options={
                'ordering': ['s2245_evttreicap', 'cpfprof', 'nmprof', 'tpprof', 'matricula', 'formprof', 'codcbo'],
                'db_table': 's2245_ideprofresp',
                'managed': True,
            },
        ),
    ]
