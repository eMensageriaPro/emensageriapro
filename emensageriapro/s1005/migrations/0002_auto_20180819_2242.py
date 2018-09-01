# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1005', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1005alteracaoprocadmjudfap',
            name='tpproc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1005alteracaoprocadmjudrat',
            name='tpproc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1005inclusaoprocadmjudfap',
            name='tpproc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1005inclusaoprocadmjudrat',
            name='tpproc',
            field=models.IntegerField(),
        ),
    ]
