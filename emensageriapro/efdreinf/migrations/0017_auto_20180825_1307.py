# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0016_auto_20180825_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='r5001evttotal',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r5001evttotal_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r5001evttotal_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r5011evttotalcontrib_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r5011evttotalcontrib_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='dhprocess',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
