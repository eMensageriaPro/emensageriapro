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
            name='s1299ideRespInf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nmresp', models.CharField(max_length=70)),
                ('cpfresp', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1299iderespinf_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1299iderespinf_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1299_evtfechaevper', models.OneToOneField(related_name='s1299iderespinf_s1299_evtfechaevper', to='esocial.s1299evtFechaEvPer')),
            ],
            options={
                'ordering': ['s1299_evtfechaevper', 'nmresp', 'cpfresp', 'telefone', 'email'],
                'db_table': 's1299_iderespinf',
                'managed': True,
            },
        ),
    ]
