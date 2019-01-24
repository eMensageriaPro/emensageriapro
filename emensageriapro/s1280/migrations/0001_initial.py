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
            name='s1280infoAtivConcom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fatormes', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('fator13', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1280infoativconcom_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1280infoativconcom_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1280_evtinfocomplper', models.OneToOneField(related_name='s1280infoativconcom_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer')),
            ],
            options={
                'ordering': ['s1280_evtinfocomplper', 'fatormes', 'fator13'],
                'db_table': 's1280_infoativconcom',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1280infoSubstPatr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indsubstpatr', models.IntegerField(choices=[(1, '1 - Integralmente substitu\xedda'), (2, '2 - Parcialmente substitu\xedda')])),
                ('percredcontrib', models.DecimalField(max_length=5, max_digits=15, decimal_places=2)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1280infosubstpatr_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1280infosubstpatr_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1280_evtinfocomplper', models.OneToOneField(related_name='s1280infosubstpatr_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer')),
            ],
            options={
                'ordering': ['s1280_evtinfocomplper', 'indsubstpatr', 'percredcontrib'],
                'db_table': 's1280_infosubstpatr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s1280infoSubstPatrOpPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnpjopportuario', models.CharField(max_length=14)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s1280infosubstpatropport_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s1280infosubstpatropport_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s1280_evtinfocomplper', models.ForeignKey(related_name='s1280infosubstpatropport_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer')),
            ],
            options={
                'ordering': ['s1280_evtinfocomplper', 'cnpjopportuario'],
                'db_table': 's1280_infosubstpatropport',
                'managed': True,
            },
        ),
    ]
