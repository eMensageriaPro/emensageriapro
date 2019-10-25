# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='username',
        ),
    ]
