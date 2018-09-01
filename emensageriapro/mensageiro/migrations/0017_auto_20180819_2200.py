# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0016_auto_20180818_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros'), (9, 'Vers\xe3o incompat\xedvel')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo inv\xe1lido!'), (4, 'Validado'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros'), (9, 'Vers\xe3o incompat\xedvel')]),
        ),
        
    ]
