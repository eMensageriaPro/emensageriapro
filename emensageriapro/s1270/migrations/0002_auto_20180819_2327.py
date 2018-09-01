# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1270', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1270remunavnp',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
