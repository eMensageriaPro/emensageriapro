# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0015_auto_20180824_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='cdretorno',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='descretorno',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='dhprocess',
            field=models.DateField(null=True, blank=True),
        ),
    ]
