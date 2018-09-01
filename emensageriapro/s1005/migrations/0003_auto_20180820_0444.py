# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1005', '0002_auto_20180819_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1005alteracaoprocadmjudfap',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1005alteracaoprocadmjudrat',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1005inclusaoprocadmjudfap',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='s1005inclusaoprocadmjudrat',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (1, '1 - Administrativo'), (2, '2 - Judicial'), (2, '2 - Judicial')]),
        ),
    ]
