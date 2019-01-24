# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0005_auto_20180913_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined'], 'managed': True},
        ),
    ]
