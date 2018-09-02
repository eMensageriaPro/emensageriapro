# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2299', '0002_auto_20180816_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2299infotrabintermprocjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - IRRF'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')]),
        ),
    ]
