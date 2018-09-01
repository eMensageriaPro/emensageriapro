# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0011_auto_20180822_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='ocorrencias',
            field=models.TextField(null=True, blank=True),
        ),
    ]
