# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070infoprocjud',
            name='indorigemrecursos',
            field=models.IntegerField(choices=[(1, '1 - Recursos do pr\xf3prio declarante'), (2, '2 - Recursos de terceiros -Declarante \xe9 a Institui\xe7\xe3o Financeira respons\xe1vel apenas pelo repasse dos valores')]),
        ),
    ]
