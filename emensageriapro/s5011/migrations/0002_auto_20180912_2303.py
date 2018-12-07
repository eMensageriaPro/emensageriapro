# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5011basesremun',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
    ]
