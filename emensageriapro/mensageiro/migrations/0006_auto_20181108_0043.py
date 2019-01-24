# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0005_transmissorlote_verificar_predecessao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='efdreinf_certificado',
            field=models.FileField(blank=True, null=True, upload_to=b'efdreinf_certificado'),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='esocial_certificado',
            field=models.FileField(blank=True, null=True, upload_to=b'esocial_certificado'),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='logotipo',
            field=models.FileField(blank=True, null=True, upload_to=b'logotipo'),
        ),
    ]
