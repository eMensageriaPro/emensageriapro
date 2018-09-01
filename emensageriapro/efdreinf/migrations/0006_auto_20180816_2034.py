# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0005_auto_20180812_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='validacoes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='procemi',
            field=models.IntegerField(default=1, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
    ]
