# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1270', '0002_auto_20180819_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (4, '4 - CNO (Cadastro Nacional de Obra)')]),
        ),
    ]
