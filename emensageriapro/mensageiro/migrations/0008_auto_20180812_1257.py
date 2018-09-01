# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0002_auto_20180811_0801'),
        ('mensageiro', '0007_auto_20180811_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportacaoArquivosEventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=10, null=True, blank=True)),
                ('versao', models.CharField(max_length=30, null=True, blank=True)),
                ('identidade_evento', models.CharField(max_length=100, null=True, blank=True)),
                ('identidade', models.IntegerField(null=True, blank=True)),
                ('arquivo', models.CharField(max_length=200, null=True, blank=True)),
                ('status', models.IntegerField(blank=True, null=True, choices=[(1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!')])),
                ('data_hora', models.DateTimeField(null=True, blank=True)),
                ('validacoes', models.TextField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='importacaoarquivoseventos_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'ordering': ['importacao_arquivos', 'evento', 'versao', 'identidade_evento', 'identidade', 'arquivo'],
                'db_table': 'importacao_arquivos_eventos',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='importacaoarquivos',
            options={'ordering': ['arquivo'], 'managed': True},
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='identidade',
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='identidade_evento',
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='origem',
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='validacoes',
        ),
        migrations.RemoveField(
            model_name='importacaoarquivos',
            name='versao',
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='quant_aquardando',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='quant_error',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='quant_processado',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='importacaoarquivoseventos',
            name='importacao_arquivos',
            field=models.ForeignKey(related_name='importacaoarquivoseventos_importacao_arquivos', to='mensageiro.ImportacaoArquivos'),
        ),
        migrations.AddField(
            model_name='importacaoarquivoseventos',
            name='modificado_por',
            field=models.ForeignKey(related_name='importacaoarquivoseventos_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
    ]
