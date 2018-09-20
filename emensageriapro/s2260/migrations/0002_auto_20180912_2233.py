# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2260', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2260localtrabinterm',
            name='tplograd',
            field=models.TextField(max_length=4),
        ),
    ]
