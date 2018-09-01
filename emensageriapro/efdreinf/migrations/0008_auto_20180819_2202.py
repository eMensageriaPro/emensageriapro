# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0007_auto_20180818_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
