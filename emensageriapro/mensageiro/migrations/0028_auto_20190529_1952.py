# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 19:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0027_auto_20190523_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificados',
            options={'managed': True, 'ordering': ['nome'], 'permissions': (('can_view_certificados', 'Can view certificados'),), 'verbose_name': 'Certificados'},
        ),
    ]
