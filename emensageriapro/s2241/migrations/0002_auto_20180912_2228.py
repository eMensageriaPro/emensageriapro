# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2241', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='codfatris',
            field=models.TextField(max_length=10),
        ),
    ]
