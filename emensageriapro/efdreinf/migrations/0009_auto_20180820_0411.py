# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0008_auto_20180819_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (1, '1 - CNPJ'), (2, '2 - CPF'), (2, '2 - CPF')]),
        ),
    ]
