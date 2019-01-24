# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0002_auto_20180904_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='cpf_cnpj',
            new_name='transmissor_nrinsc',
        ),
        migrations.RenameField(
            model_name='transmissorlote',
            old_name='tipo_inscricao',
            new_name='transmissor_tpinsc',
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='contribuinte_nrinsc',
            field=models.IntegerField(default=0, choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='contribuinte_tpinsc',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='empregador_nrinsc',
            field=models.IntegerField(default=0, choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='empregador_tpinsc',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
