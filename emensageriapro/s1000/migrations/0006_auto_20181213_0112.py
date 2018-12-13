# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1000', '0005_auto_20181120_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1000alteracao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaodadosisencao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoefr',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoente',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoop',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaoinfoorginternacional',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaonovavalidade',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopf',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosituacaopj',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000alteracaosoftwarehouse',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000exclusao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaodadosisencao',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoefr',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoente',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoop',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaoinfoorginternacional',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopf',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosituacaopj',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s1000inclusaosoftwarehouse',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
