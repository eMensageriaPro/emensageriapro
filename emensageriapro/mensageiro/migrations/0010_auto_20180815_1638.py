# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0009_auto_20180815_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='importacaoarquivoseventos',
            options={'ordering': ['importacao_arquivos', 'arquivo', 'evento', 'versao', 'identidade_evento', 'identidade'], 'managed': True},
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando extra\xe7\xe3o'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (4, 'Aguardando processamento'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Aguardando extra\xe7\xe3o'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (4, 'Aguardando processamento'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base')]),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='logotipo',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
