# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0019_auto_20180822_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='retornoseventos',
            name='empregador_nrinsc',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='retornoseventos',
            name='empregador_tpinsc',
            field=models.IntegerField(blank=True, null=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
    ]
