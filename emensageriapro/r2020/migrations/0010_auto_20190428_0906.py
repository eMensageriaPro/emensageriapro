# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r2020', '0009_auto_20190427_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2020infoprocretad',
            name='nrprocretadic',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretad',
            name='r2020_evtservprest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2020infoprocretad_r2020_evtservprest', to='efdreinf.r2020evtServPrest'),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretad',
            name='tpprocretadic',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretad',
            name='valoradic',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretpr',
            name='nrprocretprinc',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretpr',
            name='r2020_evtservprest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2020infoprocretpr_r2020_evtservprest', to='efdreinf.r2020evtServPrest'),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretpr',
            name='tpprocretprinc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial')]),
        ),
        migrations.AlterField(
            model_name='r2020infoprocretpr',
            name='valorprinc',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2020infotpserv',
            name='r2020_nfs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2020infotpserv_r2020_nfs', to='r2020.r2020nfs'),
        ),
        migrations.AlterField(
            model_name='r2020infotpserv',
            name='tpservico',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r2020infotpserv',
            name='vlrbaseret',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2020infotpserv',
            name='vlrretencao',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r2020nfs',
            name='dtemissaonf',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='r2020nfs',
            name='numdocto',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='r2020nfs',
            name='r2020_evtservprest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r2020nfs_r2020_evtservprest', to='efdreinf.r2020evtServPrest'),
        ),
        migrations.AlterField(
            model_name='r2020nfs',
            name='serie',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='r2020nfs',
            name='vlrbruto',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
    ]