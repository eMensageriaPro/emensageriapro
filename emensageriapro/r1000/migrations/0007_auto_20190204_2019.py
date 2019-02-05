# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r1000', '0006_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r1000alteracao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaoinfoefr',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaoinfoefr',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaonovavalidade',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaonovavalidade',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaosofthouse',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000alteracaosofthouse',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000exclusao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000exclusao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusaoinfoefr',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusaoinfoefr',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusaosofthouse',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r1000inclusaosofthouse',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaoinfoefr',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaonovavalidade',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaonovavalidade',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000exclusao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000exclusao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusaoinfoefr',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
