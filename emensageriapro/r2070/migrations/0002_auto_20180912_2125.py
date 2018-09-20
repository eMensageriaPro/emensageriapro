# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='paisresid',
            field=models.TextField(max_length=3),
        ),
    ]
