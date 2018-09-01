# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0018_auto_20180822_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retornoseventos',
            old_name='codcbo',
            new_name='codcbocargo',
        ),
        migrations.AddField(
            model_name='retornoseventos',
            name='codcbofuncao',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
