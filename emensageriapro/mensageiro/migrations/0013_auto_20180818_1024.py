# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0012_auto_20180816_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importacaoarquivos',
            old_name='quant_aquardando',
            new_name='quant_aguardando',
        ),
        migrations.RenameField(
            model_name='importacaoarquivos',
            old_name='quant_error',
            new_name='quant_erros',
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='quant_importado',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Aguardando processamento'), (1, 'Importa\xe7\xe3o realizada com sucesso!'), (2, 'Erro na importa\xe7\xe3o!'), (3, 'Arquivo xml inv\xe1lido!'), (5, 'ID do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
    ]
