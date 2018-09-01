# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0006_auto_20180811_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_certificado',
            new_name='efdreinf_certificado',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_intervalo',
            new_name='efdreinf_intervalo',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_lote_max',
            new_name='efdreinf_lote_max',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_lote_min',
            new_name='efdreinf_lote_min',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_senha',
            new_name='efdreinf_senha',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_tempo_prox_envio',
            new_name='efdreinf_tempo_prox_envio',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='reinf_timeout',
            new_name='efdreinf_timeout',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='reinf_pasta',
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='efdreinf_pasta',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='esocial_pasta',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='logotipo',
            field=models.FileField(default='-', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado com sucesso'), (8, 'Erro na consulta'), (9, 'Consultado com sucesso')]),
        ),
    ]
