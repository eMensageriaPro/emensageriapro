# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0003_auto_20181120_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r5001evttotal',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r5001evttotal',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r5011evttotalcontrib',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r5011evttotalcontrib',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v1_03_02', 'Vers\xe3o 1.03.02'), (b'v1_04', 'Vers\xe3o 1.04')], default=b'v1_03_02', max_length=20),
        ),
    ]