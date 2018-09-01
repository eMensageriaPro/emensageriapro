# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180813_0952'),
        ('mensageiro', '0033_auto_20180825_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('campos', models.CharField(max_length=500)),
                ('sql', models.TextField(null=True, blank=True)),
                ('criado_em', models.DateTimeField(blank=True)),
                ('modificado_em', models.DateTimeField(null=True, blank=True)),
                ('excluido', models.BooleanField()),
                ('criado_por', models.ForeignKey(related_name='relatorios_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
                ('modificado_por', models.ForeignKey(related_name='relatorios_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True)),
            ],
            options={
                'db_table': 'relatorios',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (14, 'Processado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
    ]
