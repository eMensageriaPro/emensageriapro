# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0002_auto_20181119_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2410homologtc',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='dthomol',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='nratolegal',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='s2410_evtcdbenin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2410homologtc_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn'),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='s2410_evtcdbenin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2410infopenmorte_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn'),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='tppenmorte',
            field=models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria')]),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='cpfinst',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='dtinst',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='intaposentado',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='s2410_infopenmorte',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2410instpenmorte_s2410_infopenmorte', to='s2410.s2410infoPenMorte'),
        ),
    ]
