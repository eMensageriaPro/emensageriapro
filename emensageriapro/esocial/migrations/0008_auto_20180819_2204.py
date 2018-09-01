# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0007_auto_20180818_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1200evtremun',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1260evtcomprod',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s1270evtcontratavnp',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s2200evtadmissao',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s2206evtaltcontratual',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s2210evtcat',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s2399evttsvtermino',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s5001evtbasestrab',
            name='tpinsc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='s5011evtcs',
            name='tpinsc',
            field=models.IntegerField(),
        ),
    ]
