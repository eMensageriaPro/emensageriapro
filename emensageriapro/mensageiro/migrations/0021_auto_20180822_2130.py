# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0020_auto_20180822_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retornoseventos',
            old_name='clauassec',
            new_name='clauasseg',
        ),
    ]
