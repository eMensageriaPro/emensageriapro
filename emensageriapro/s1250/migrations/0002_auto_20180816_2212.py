# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1250', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1250tpaquis',
            name='indaquis',
            field=models.IntegerField(choices=[(1, '1 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral'), (2, '2 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA'), (3, '3 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA. Evento de origem (S- 1250)'), (4, '4 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (5, '5 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa f\xedsica ou segurado especial em geral por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)'), (6, '6 - Aquisi\xe7\xe3o da produ\xe7\xe3o de produtor rural pessoa jur\xeddica por Entidade do PAA - Produ\xe7\xe3o Isenta (Lei 13.606/2018)')]),
        ),
    ]
