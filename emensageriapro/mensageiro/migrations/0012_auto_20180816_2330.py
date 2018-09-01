# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0011_auto_20180816_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='evento',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
