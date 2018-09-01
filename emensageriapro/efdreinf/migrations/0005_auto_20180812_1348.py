# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0004_auto_20180812_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r5001evttotal',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r5011evttotalcontrib',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='arquivo_original',
            field=models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
    ]
