# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1260', '0002_auto_20180816_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1260ideadquir',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
