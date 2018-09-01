# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0024_auto_20180822_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retornoseventoshorarios',
            name='perhorflexivel',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')]),
        ),
    ]
