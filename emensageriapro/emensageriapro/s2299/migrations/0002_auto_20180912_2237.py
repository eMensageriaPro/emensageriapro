# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2299', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2299infotrabintermprocjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (3, '3 - IRRF'), (4, '4 - Contribui\xe7\xe3o sindical')]),
        ),
        migrations.AlterField(
            model_name='s2299infotrabintermremunoutrempr',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
    ]
