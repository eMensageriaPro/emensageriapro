# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0017_auto_20190205_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Enviado'), (2, 'Erro no envio'), (3, 'Consultado'), (4, 'Erro na consulta')], default=0),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Enviado'), (2, 'Erro no envio'), (3, 'Consultado'), (4, 'Erro na consulta')], default=0),
        ),
    ]