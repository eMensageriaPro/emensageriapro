# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0013_auto_20180824_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='s1040evttabfuncao',
            name='recepcao_data_hora',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1050evttabhortur',
            name='recepcao_data_hora',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1060evttabambiente',
            name='recepcao_data_hora',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1070evttabprocesso',
            name='recepcao_data_hora',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
