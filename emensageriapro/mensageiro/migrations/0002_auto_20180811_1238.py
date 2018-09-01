# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0002_auto_20180811_0801'),
        ('mensageiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', models.CharField(max_length=300)),
                ('data_criacao', models.DateField()),
                ('permite_recuperacao', models.IntegerField(choices=[(0, 'N\xe3o'), (1, 'Sim')])),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='arquivos_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='arquivos_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'db_table': 'arquivos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='esocial_certificado',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='esocial_intervalo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='esocial_pasta',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='esocial_senha',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='esocial_tempo_prox_envio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='reinf_certificado',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='reinf_intervalo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='reinf_pasta',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='reinf_senha',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='reinf_tempo_prox_envio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
    ]
