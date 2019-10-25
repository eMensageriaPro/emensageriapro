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
            name='r2099ideRespInf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nmresp', models.CharField(max_length=70)),
                ('cpfresp', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=13, null=True, blank=True)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='r2099iderespinf_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='r2099iderespinf_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('r2099_evtfechaevper', models.OneToOneField(related_name='r2099iderespinf_r2099_evtfechaevper', to='efdreinf.r2099evtFechaEvPer')),
            ],
            options={
                'ordering': ['r2099_evtfechaevper', 'nmresp', 'cpfresp', 'telefone', 'email'],
                'db_table': 'r2099_iderespinf',
                'managed': True,
            },
        ),
    ]
