# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1060', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1060alteracaofatorrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s1060inclusaofatorrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
    ]
