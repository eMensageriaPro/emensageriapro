# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1295', '0011_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='cpfresp',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='nmresp',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='s1295_evttotconting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s1295iderespinf_s1295_evttotconting', to='esocial.s1295evtTotConting'),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='telefone',
            field=models.CharField(max_length=13),
        ),
    ]
