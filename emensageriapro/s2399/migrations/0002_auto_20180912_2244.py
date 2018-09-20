# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2399', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2399procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical'), (4, '4 - IRRF')]),
        ),
        migrations.AlterField(
            model_name='s2399remunoutrempr',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
    ]
