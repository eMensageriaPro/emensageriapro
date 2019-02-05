# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2206', '0008_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s2206alvarajudicial',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206alvarajudicial',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206aprend',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206aprend',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206filiacaosindical',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206filiacaosindical',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206horario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206horario',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206horcontratual',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206horcontratual',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206infoceletista',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206infoceletista',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206infoestatutario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206infoestatutario',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabdom',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabdom',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabgeral',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206localtrabgeral',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206observacoes',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206observacoes',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206servpubl',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206servpubl',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s2206trabtemp',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s2206trabtemp',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s2206alvarajudicial',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206alvarajudicial',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206aprend',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206filiacaosindical',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206filiacaosindical',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206horario',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206horcontratual',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206infoceletista',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206infoestatutario',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206infoestatutario',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabdom',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206localtrabgeral',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206observacoes',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206observacoes',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206servpubl',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206servpubl',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206trabtemp',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s2206trabtemp',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
