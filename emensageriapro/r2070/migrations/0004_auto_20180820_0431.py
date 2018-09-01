# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0003_auto_20180819_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070ideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF')]),
        ),
    ]
