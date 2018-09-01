# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0012_auto_20180822_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r1000evtinfocontri_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r1070evttabprocesso_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2010evtservtom_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2020evtservprest_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2030evtassocdesprec_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2040evtassocdesprep_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2050evtcomprod_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2060evtcprb_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2070evtpgtosdivs_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2098evtreabreevper_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r2099evtfechaevper_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r3010evtespdesportivo_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='r9000evtexclusao_retornos_eventos', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
    ]
