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
            name='s2416homologTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nratolegal', models.CharField(max_length=20)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2416homologtc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2416homologtc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2416_evtcdbenalt', models.OneToOneField(related_name='s2416homologtc_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt')),
            ],
            options={
                'ordering': ['s2416_evtcdbenalt', 'nratolegal'],
                'db_table': 's2416_homologtc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2416infoPenMorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tppenmorte', models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2416infopenmorte_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2416infopenmorte_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2416_evtcdbenalt', models.OneToOneField(related_name='s2416infopenmorte_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt')),
            ],
            options={
                'ordering': ['s2416_evtcdbenalt', 'tppenmorte'],
                'db_table': 's2416_infopenmorte',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2416suspensao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mtvsuspensao', models.CharField(max_length=2, choices=[(b'01', '01 - Suspens\xe3o por n\xe3o recadastramento'), (b'99', '99 - Outros motivos de suspens\xe3o')])),
                ('dscsuspensao', models.CharField(max_length=255, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2416suspensao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2416suspensao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2416_evtcdbenalt', models.OneToOneField(related_name='s2416suspensao_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt')),
            ],
            options={
                'ordering': ['s2416_evtcdbenalt', 'mtvsuspensao', 'dscsuspensao'],
                'db_table': 's2416_suspensao',
                'managed': True,
            },
        ),
    ]
