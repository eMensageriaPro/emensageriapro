# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0003_auto_20180912_1359'),
        ('esocial', '0002_auto_20180912_1556'),
        ('s2400', '0002_auto_20180912_1556'),
        ('mensageiro', '0003_auto_20180911_2127'),
    ]

    operations = [
        migrations.DeleteModel(
            name='s2400evtCdBenPrRP',
        ),
        migrations.AddField(
            model_name='s2420evtcdbenterm',
            name='criado_por',
            field=models.ForeignKey(related_name='s2420evtcdbenterm_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2420evtcdbenterm',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2420evtcdbenterm_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2420evtcdbenterm',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2420evtcdbenterm_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2420evtcdbenterm',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2420evtcdbenterm_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2416evtcdbenalt',
            name='criado_por',
            field=models.ForeignKey(related_name='s2416evtcdbenalt_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2416evtcdbenalt',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2416evtcdbenalt_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2416evtcdbenalt',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2416evtcdbenalt_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2416evtcdbenalt',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2416evtcdbenalt_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2410evtcdbenin',
            name='criado_por',
            field=models.ForeignKey(related_name='s2410evtcdbenin_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2410evtcdbenin',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2410evtcdbenin_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2410evtcdbenin',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2410evtcdbenin_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2410evtcdbenin',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2410evtcdbenin_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2405evtcdbenefalt',
            name='criado_por',
            field=models.ForeignKey(related_name='s2405evtcdbenefalt_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2405evtcdbenefalt',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2405evtcdbenefalt_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2405evtcdbenefalt',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2405evtcdbenefalt_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2405evtcdbenefalt',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2405evtcdbenefalt_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenefin',
            name='criado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenefin_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenefin',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2400evtcdbenefin_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenefin',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2400evtcdbenefin_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2400evtcdbenefin',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2400evtcdbenefin_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2245evttreicap',
            name='criado_por',
            field=models.ForeignKey(related_name='s2245evttreicap_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2245evttreicap',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2245evttreicap_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2245evttreicap',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s2245evttreicap_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s2245evttreicap',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s2245evttreicap_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='criado_por',
            field=models.ForeignKey(related_name='s2231evtcessao_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='modificado_por',
            field=models.ForeignKey(related_name='s2231evtcessao_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1065evttabequipamento',
            name='criado_por',
            field=models.ForeignKey(related_name='s1065evttabequipamento_criado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1065evttabequipamento',
            name='modificado_por',
            field=models.ForeignKey(related_name='s1065evttabequipamento_modificado_por', blank=True, to='controle_de_acesso.Usuarios', null=True),
        ),
        migrations.AddField(
            model_name='s1065evttabequipamento',
            name='retornos_eventos',
            field=models.ForeignKey(related_name='s1065evttabequipamento_retornos_eventos', blank=True, to='mensageiro.RetornosEventos', null=True),
        ),
        migrations.AddField(
            model_name='s1065evttabequipamento',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(related_name='s1065evttabequipamento_transmissor_lote_esocial', blank=True, to='mensageiro.TransmissorLoteEsocial', null=True),
        ),
    ]
