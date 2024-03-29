# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-28 20:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0044_auto_20191228_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmissorloteefdreinf',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='transmissorloteesocial',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinfocorrencias',
            name='localizacao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocialocorrencias',
            name='localizacao',
            field=models.TextField(),
        ),
    ]
