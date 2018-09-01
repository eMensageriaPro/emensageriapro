# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0013_auto_20180824_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r1000evtinfocontri',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r1070evttabprocesso',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2010evtservtom',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2020evtservprest',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2030evtassocdesprec',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2040evtassocdesprep',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2050evtcomprod',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2060evtcprb',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2070evtpgtosdivs',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2098evtreabreevper',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r2099evtfechaevper',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r3010evtespdesportivo',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='r9000evtexclusao',
            name='retornos_eventos',
        ),
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r1000evtinfocontri_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r1000evtinfocontri_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r1070evttabprocesso_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r1070evttabprocesso_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2010evtservtom_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2010evtservtom_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2020evtservprest_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2020evtservprest_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2030evtassocdesprec_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2030evtassocdesprec_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2040evtassocdesprep_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2040evtassocdesprep_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2050evtcomprod_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2050evtcomprod_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2060evtcprb_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2060evtcprb_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2070evtpgtosdivs_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2070evtpgtosdivs_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2098evtreabreevper_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2098evtreabreevper_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r2099evtfechaevper_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r2099evtfechaevper_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r3010evtespdesportivo_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r3010evtespdesportivo_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='retornos_evttotal',
            field=models.ForeignKey(related_name='r9000evtexclusao_retornos_evttotal', blank=True, to='efdreinf.r5001evtTotal', null=True),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='retornos_evttotalcontrib',
            field=models.ForeignKey(related_name='r9000evtexclusao_retornos_evttotalcontrib', blank=True, to='efdreinf.r5011evtTotalContrib', null=True),
        ),
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r5001evttotal',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r5011evttotalcontrib',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'Assinado'), (11, 'Gerado'), (12, 'Retorno'), (13, 'Erro - Ocorr\xeancias'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')]),
        ),
    ]
