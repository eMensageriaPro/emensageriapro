# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0002_auto_20180811_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='esocial_tempo_prox_envio',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='reinf_tempo_prox_envio',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
