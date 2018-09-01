# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0021_auto_20180822_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retornoseventos',
            name='clauasseg',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
