# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0002_auto_20180816_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070ideestab',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
