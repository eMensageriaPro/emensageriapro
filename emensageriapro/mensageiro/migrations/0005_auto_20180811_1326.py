# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0004_auto_20180811_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='logotipo',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
