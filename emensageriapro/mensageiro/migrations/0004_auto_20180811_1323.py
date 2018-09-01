# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0003_auto_20180811_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='logotipo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
