# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r4020', '0011_auto_20191218_2214'),
        ('r4040', '0010_auto_20191218_2214'),
        ('r9002', '0012_auto_20191218_2214'),
        ('r9011', '0011_auto_20191218_2214'),
        ('r4010', '0012_auto_20191218_2214'),
        ('r9012', '0010_auto_20191218_2214'),
        ('r4099', '0010_auto_20191218_2214'),
        ('r9001', '0012_auto_20191218_2214'),
        ('efdreinf', '0030_auto_20190929_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r5001',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r5011',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r4010evtretpf',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r5001',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r5011',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r4020evtretpj',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r5001',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r5011',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r4040evtbenefnid',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r5001',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r5011',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r4098evtreab',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r5001',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r5011',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r4099evtfech',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r9001evttotal',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9001evttotal',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9001evttotal',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9001evttotal',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r9001evttotal',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r9002evtret',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002evtret',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002evtret',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002evtret',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r9002evtret',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r9011evttotalcontrib',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9011evttotalcontrib',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9011evttotalcontrib',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9011evttotalcontrib',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r9011evttotalcontrib',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r9012evtretcons',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9012evtretcons',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9012evtretcons',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9012evtretcons',
            name='transmissor_lote_efdreinf',
        ),
        migrations.RemoveField(
            model_name='r9012evtretcons',
            name='transmissor_lote_efdreinf_error',
        ),
        migrations.RemoveField(
            model_name='r1000evtinfocontri',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r1000evtinfocontri',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r1000evtinfocontri',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r1000evtinfocontri',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r1070evttabprocesso',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r1070evttabprocesso',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r1070evttabprocesso',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r1070evttabprocesso',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2010evtservtom',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2010evtservtom',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2010evtservtom',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2010evtservtom',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2020evtservprest',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2020evtservprest',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2020evtservprest',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2020evtservprest',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2030evtassocdesprec',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2030evtassocdesprec',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2030evtassocdesprec',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2030evtassocdesprec',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2040evtassocdesprep',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2040evtassocdesprep',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2040evtassocdesprep',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2040evtassocdesprep',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2050evtcomprod',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2050evtcomprod',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2050evtcomprod',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2050evtcomprod',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2060evtcprb',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2060evtcprb',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2060evtcprb',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2060evtcprb',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2070evtpgtosdivs',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2070evtpgtosdivs',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2070evtpgtosdivs',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2070evtpgtosdivs',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2098evtreabreevper',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2098evtreabreevper',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2098evtreabreevper',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2098evtreabreevper',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r2099evtfechaevper',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r2099evtfechaevper',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r2099evtfechaevper',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r2099evtfechaevper',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r3010evtespdesportivo',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r3010evtespdesportivo',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r3010evtespdesportivo',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r3010evtespdesportivo',
            name='retornos_r9012',
        ),
        migrations.RemoveField(
            model_name='r9000evtexclusao',
            name='retornos_r9001',
        ),
        migrations.RemoveField(
            model_name='r9000evtexclusao',
            name='retornos_r9002',
        ),
        migrations.RemoveField(
            model_name='r9000evtexclusao',
            name='retornos_r9011',
        ),
        migrations.RemoveField(
            model_name='r9000evtexclusao',
            name='retornos_r9012',
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='tpinscestabprest',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='tpinscestab',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='tpinscestab',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='r4010evtRetPF',
        ),
        migrations.DeleteModel(
            name='r4020evtRetPJ',
        ),
        migrations.DeleteModel(
            name='r4040evtBenefNId',
        ),
        migrations.DeleteModel(
            name='r4098evtReab',
        ),
        migrations.DeleteModel(
            name='r4099evtFech',
        ),
        migrations.DeleteModel(
            name='r9001evtTotal',
        ),
        migrations.DeleteModel(
            name='r9002evtRet',
        ),
        migrations.DeleteModel(
            name='r9011evtTotalContrib',
        ),
        migrations.DeleteModel(
            name='r9012evtRetCons',
        ),
    ]
