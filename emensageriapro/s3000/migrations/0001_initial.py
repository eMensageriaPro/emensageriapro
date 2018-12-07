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
            name='s3000ideFolhaPagto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indapuracao', models.IntegerField(choices=[(1, '1 - Mensal'), (2, '2 - Anual (13\xb0 sal\xe1rio)')])),
                ('perapur', models.CharField(max_length=7)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s3000idefolhapagto_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s3000idefolhapagto_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s3000_evtexclusao', models.OneToOneField(related_name='s3000idefolhapagto_s3000_evtexclusao', to='esocial.s3000evtExclusao')),
            ],
            options={
                'ordering': ['s3000_evtexclusao', 'indapuracao', 'perapur'],
                'db_table': 's3000_idefolhapagto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='s3000ideTrabalhador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpftrab', models.CharField(max_length=11)),
                ('nistrab', models.CharField(max_length=11, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='s3000idetrabalhador_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='s3000idetrabalhador_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('s3000_evtexclusao', models.OneToOneField(related_name='s3000idetrabalhador_s3000_evtexclusao', to='esocial.s3000evtExclusao')),
            ],
            options={
                'ordering': ['s3000_evtexclusao', 'cpftrab', 'nistrab'],
                'db_table': 's3000_idetrabalhador',
                'managed': True,
            },
        ),
    ]
