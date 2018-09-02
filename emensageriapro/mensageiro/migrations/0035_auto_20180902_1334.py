# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0034_auto_20180829_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando!'), (1, 'Sucesso!'), (2, 'Erro!'), (3, 'Arquivo inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros'), (9, 'Vers\xe3o incompat\xedvel')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Aguardando!'), (1, 'Sucesso!'), (2, 'Erro!'), (3, 'Arquivo inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros'), (9, 'Vers\xe3o incompat\xedvel')]),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='efdreinf_timeout',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='esocial_timeout',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
