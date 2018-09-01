# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0002_auto_20180816_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200dmdev',
            name='codcateg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='codcateg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1200remunoutrempr',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
