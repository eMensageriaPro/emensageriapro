# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1030', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1030alteracaocargopublico',
            options={'ordering': ['s1030_alteracao', 'acumcargo', 'contagemesp', 'dedicexcl', 'codcarreira', 'nrlei', 'dtlei', 'sitcargo'], 'managed': True},
        ),
        migrations.AlterModelOptions(
            name='s1030inclusaocargopublico',
            options={'ordering': ['s1030_inclusao', 'acumcargo', 'contagemesp', 'dedicexcl', 'codcarreira', 'nrlei', 'dtlei', 'sitcargo'], 'managed': True},
        ),
        migrations.AddField(
            model_name='s1030alteracaocargopublico',
            name='codcarreira',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='s1030inclusaocargopublico',
            name='codcarreira',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='dtlei',
            field=models.DateField(default='2018-09-10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='s1030alteracaocargopublico',
            name='nrlei',
            field=models.CharField(default=999, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='dtlei',
            field=models.DateField(default='2018-09-10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='s1030inclusaocargopublico',
            name='nrlei',
            field=models.CharField(default=999, max_length=12),
            preserve_default=False,
        ),
    ]
