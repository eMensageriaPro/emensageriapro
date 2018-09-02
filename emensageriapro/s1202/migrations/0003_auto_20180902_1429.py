# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1202', '0002_auto_20180816_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - IRRF'), (2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')]),
        ),
    ]
