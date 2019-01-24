# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200dmdev',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='codcateg',
            field=models.TextField(max_length=3),
        ),
    ]
