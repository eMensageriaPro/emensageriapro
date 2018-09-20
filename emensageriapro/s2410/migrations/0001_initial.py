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
            name='s2410homologTC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dthomol', models.DateField()),
                ('nratolegal', models.CharField(max_length=20)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2410homologtc_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2410homologtc_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2410_evtcdbenin', models.OneToOneField(related_name='s2410homologtc_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn')),
            ],
            options={
                'ordering': ['s2410_evtcdbenin', 'dthomol', 'nratolegal'],
                'db_table': 's2410_homologtc',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2410infoPenMorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tppenmorte', models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2410infopenmorte_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2410infopenmorte_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2410_evtcdbenin', models.OneToOneField(related_name='s2410infopenmorte_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn')),
            ],
            options={
                'ordering': ['s2410_evtcdbenin', 'tppenmorte'],
                'db_table': 's2410_infopenmorte',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s2410instPenMorte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpfinst', models.CharField(max_length=11)),
                ('dtinst', models.DateField()),
                ('intaposentado', models.CharField(max_length=1, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s2410instpenmorte_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s2410instpenmorte_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s2410_infopenmorte', models.OneToOneField(related_name='s2410instpenmorte_s2410_infopenmorte', to='s2410.s2410infoPenMorte')),
            ],
            options={
                'ordering': ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado'],
                'db_table': 's2410_instpenmorte',
                'managed': True,
            },
        ),
    ]
