# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0010_auto_20180815_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransmissorEventosEfdreinfTotalizacoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=10)),
                ('identidade', models.CharField(max_length=36)),
                ('grupo', models.IntegerField(choices=[(1, '1 - Eventos de Tabelas'), (2, '2 - Eventos N\xe3o Peri\xf3dicos'), (3, '3 - Eventos Peri\xf3dicos')])),
                ('tabela', models.CharField(max_length=50)),
                ('tabela_salvar', models.CharField(max_length=50)),
                ('ordem', models.IntegerField()),
                ('tpinsc', models.CharField(max_length=1, choices=[(b'1', '1 - CNPJ'), (b'2', '2 - CPF'), (b'3', '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (b'4', '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('processamento_codigo_resposta', models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (101, '101 - Lote Aguardando Processamento'), (201, '201 - Lote Processado com Sucesso'), (202, '202 - Lote Processado com Advert\xeancias'), (301, '301 - Erro Servidor eSocial'), (401, '401 - Lote Incorreto - Erro preenchimento'), (402, '402 - Lote Incorreto - schema Inv\xe1lido'), (403, '403 - Lote Incorreto - Vers\xe3o do Schema n\xe3o permitida'), (404, '404 - Lote Incorreto - Erro Certificado'), (405, '405 - Lote Incorreto - Lote nulo ou vazio'), (501, '501 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Preenchimento'), (502, '502 - Solicita\xe7\xe3o de Consulta Incorreta - Schema Inv\xe1lido.'), (503, '503 - Solicita\xe7\xe3o de Consulta Incorreta - Vers\xe3o do Schema N\xe3o Permitida.'), (504, '504 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Certificado.'), (505, '505 - Solicita\xe7\xe3o de Consulta Incorreta - Consulta nula ou vazia.')])),
                ('processamento_descricao_resposta', models.TextField(null=True, blank=True)),
                ('recibo_numero', models.CharField(max_length=100, null=True, blank=True)),
                ('recibo_hash', models.CharField(max_length=100, null=True, blank=True)),
                ('url_recibo', models.CharField(max_length=100, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
            ],
            options={
                'db_table': 'transmissor_eventos_efdreinf_totalizacoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransmissorEventosEsocialTotalizacoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=10)),
                ('identidade', models.CharField(max_length=36)),
                ('grupo', models.IntegerField(choices=[(1, '1 - Eventos de Tabelas'), (2, '2 - Eventos N\xe3o Peri\xf3dicos'), (3, '3 - Eventos Peri\xf3dicos')])),
                ('tabela', models.CharField(max_length=50)),
                ('tabela_salvar', models.CharField(max_length=50)),
                ('ordem', models.IntegerField()),
                ('tpinsc', models.CharField(max_length=1, choices=[(b'1', '1 - CNPJ'), (b'2', '2 - CPF'), (b'3', '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (b'4', '4 - CNO (Cadastro Nacional de Obra)')])),
                ('nrinsc', models.CharField(max_length=15)),
                ('processamento_codigo_resposta', models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (101, '101 - Lote Aguardando Processamento'), (201, '201 - Lote Processado com Sucesso'), (202, '202 - Lote Processado com Advert\xeancias'), (301, '301 - Erro Servidor eSocial'), (401, '401 - Lote Incorreto - Erro preenchimento'), (402, '402 - Lote Incorreto - schema Inv\xe1lido'), (403, '403 - Lote Incorreto - Vers\xe3o do Schema n\xe3o permitida'), (404, '404 - Lote Incorreto - Erro Certificado'), (405, '405 - Lote Incorreto - Lote nulo ou vazio'), (501, '501 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Preenchimento'), (502, '502 - Solicita\xe7\xe3o de Consulta Incorreta - Schema Inv\xe1lido.'), (503, '503 - Solicita\xe7\xe3o de Consulta Incorreta - Vers\xe3o do Schema N\xe3o Permitida.'), (504, '504 - Solicita\xe7\xe3o de Consulta Incorreta - Erro Certificado.'), (505, '505 - Solicita\xe7\xe3o de Consulta Incorreta - Consulta nula ou vazia.')])),
                ('processamento_descricao_resposta', models.TextField(null=True, blank=True)),
                ('recibo_numero', models.CharField(max_length=100, null=True, blank=True)),
                ('recibo_hash', models.CharField(max_length=100, null=True, blank=True)),
                ('url_recibo', models.CharField(max_length=100, null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
            ],
            options={
                'db_table': 'transmissor_eventos_esocial_totalizacoes',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='quant_total',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado com sucesso'), (7, 'Processando')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado com sucesso'), (7, 'Processando')]),
        ),
    ]
