# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0007_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r2070compjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070compjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070depjudicial',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070depjudicial',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070detcompet',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070detcompet',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070detdeducao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070detdeducao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070ideestab',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070ideestab',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infomolestia',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infomolestia',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjuddespprocjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjuddespprocjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjudideadvogado',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjudideadvogado',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjudorigemrecursos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070infoprocjudorigemrecursos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforesidext',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforesidext',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforra',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforra',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforradespprocjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforradespprocjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforraideadvogado',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070inforraideadvogado',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopf',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopf',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopj',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopj',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjdespprocjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjdespprocjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjideadvogado',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjideadvogado',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjinfoprocjud',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjinfoprocjud',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjorigemrecursos',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtopjorigemrecursos',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtoresidext',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070pgtoresidext',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r2070rendisento',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r2070rendisento',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='r2070compjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070compjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070depjudicial',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070depjudicial',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detcompet',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detcompet',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detdeducao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detdeducao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070ideestab',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070ideestab',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infomolestia',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infomolestia',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjuddespprocjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjuddespprocjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudideadvogado',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudideadvogado',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudorigemrecursos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudorigemrecursos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforra',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforra',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforradespprocjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforradespprocjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforraideadvogado',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforraideadvogado',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopj',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopj',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjdespprocjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjdespprocjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjideadvogado',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjideadvogado',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjinfoprocjud',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjinfoprocjud',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjorigemrecursos',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjorigemrecursos',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070rendisento',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='r2070rendisento',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
