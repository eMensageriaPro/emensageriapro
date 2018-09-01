# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0005_auto_20180811_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='esocial_senha',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='reinf_senha',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
