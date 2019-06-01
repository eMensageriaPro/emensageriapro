# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1280', '0008_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='fator13',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=5),
        ),
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='fatormes',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=5),
        ),
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='s1280_evtinfocomplper',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1280infoativconcom_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer'),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='indsubstpatr',
            field=models.IntegerField(choices=[(1, '1 - Integralmente substitu\xedda'), (2, '2 - Parcialmente substitu\xedda')], default=0),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='percredcontrib',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=5),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='s1280_evtinfocomplper',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1280infosubstpatr_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer'),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatropport',
            name='cnpjopportuario',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatropport',
            name='s1280_evtinfocomplper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1280infosubstpatropport_s1280_evtinfocomplper', to='esocial.s1280evtInfoComplPer'),
        ),
    ]