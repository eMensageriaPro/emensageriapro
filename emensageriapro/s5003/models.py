#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s5003.choices import *
get_model = apps.get_model


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class s5003basePerAntE(SoftDeletionModel):

    s5003_infobaseperante = models.ForeignKey('s5003.s5003infoBasePerAntE',
        related_name='%(class)s_s5003_infobaseperante', )

    def evento(self):
        return self.s5003_infobaseperante.evento()
    tpvalore = models.IntegerField(choices=CHOICES_S5003_TPVALORE, null=True, )
    remfgtse = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infobaseperante), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre bases de cálculo do FGTS referentes à remuneração de períodos anteriores quando {tpAcConv} = [E]. Origem: S-1200 ou S-2299.'
        db_table = r's5003_baseperante'
        managed = True # s5003_baseperante #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003basePerAntE", u"Pode ver listagem do modelo S5003BASEPERANTE"),
            ("can_see_data_s5003basePerAntE", u"Pode visualizar o conteúdo do modelo S5003BASEPERANTE"),
            ("can_see_menu_s5003basePerAntE", u"Pode visualizar no menu o modelo S5003BASEPERANTE"),
            ("can_print_list_s5003basePerAntE", u"Pode imprimir listagem do modelo S5003BASEPERANTE"),
            ("can_print_data_s5003basePerAntE", u"Pode imprimir o conteúdo do modelo S5003BASEPERANTE"), )

        ordering = [
            's5003_infobaseperante',
            'tpvalore',
            'remfgtse',]



class s5003basePerAntESerializer(ModelSerializer):

    class Meta:

        model = s5003basePerAntE
        fields = '__all__'


class s5003basePerApur(SoftDeletionModel):

    s5003_infobasefgts = models.ForeignKey('s5003.s5003infoBaseFGTS',
        related_name='%(class)s_s5003_infobasefgts', )

    def evento(self):
        return self.s5003_infobasefgts.evento()
    tpvalor = models.IntegerField(null=True, )
    remfgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infobasefgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre bases de cálculo do FGTS referentes à remuneração do período de apuração e de períodos anteriores, exceto se {tpAcConv} = [E]. Origem: S-1200, S-2299 ou S-2399.'
        db_table = r's5003_baseperapur'
        managed = True # s5003_baseperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003basePerApur", u"Pode ver listagem do modelo S5003BASEPERAPUR"),
            ("can_see_data_s5003basePerApur", u"Pode visualizar o conteúdo do modelo S5003BASEPERAPUR"),
            ("can_see_menu_s5003basePerApur", u"Pode visualizar no menu o modelo S5003BASEPERAPUR"),
            ("can_print_list_s5003basePerApur", u"Pode imprimir listagem do modelo S5003BASEPERAPUR"),
            ("can_print_data_s5003basePerApur", u"Pode imprimir o conteúdo do modelo S5003BASEPERAPUR"), )

        ordering = [
            's5003_infobasefgts',
            'tpvalor',
            'remfgts',]



class s5003basePerApurSerializer(ModelSerializer):

    class Meta:

        model = s5003basePerApur
        fields = '__all__'


class s5003dpsPerAntE(SoftDeletionModel):

    s5003_infodpsperante = models.ForeignKey('s5003.s5003infoDpsPerAntE',
        related_name='%(class)s_s5003_infodpsperante', )

    def evento(self):
        return self.s5003_infodpsperante.evento()
    tpdpse = models.IntegerField(choices=CHOICES_S5003_TPDPSE, null=True, )
    dpsfgtse = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infodpsperante), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Cálculo dos valores de FGTS a serem depositados, incidentes sobre a remuneração de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5003_dpsperante'
        managed = True # s5003_dpsperante #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003dpsPerAntE", u"Pode ver listagem do modelo S5003DPSPERANTE"),
            ("can_see_data_s5003dpsPerAntE", u"Pode visualizar o conteúdo do modelo S5003DPSPERANTE"),
            ("can_see_menu_s5003dpsPerAntE", u"Pode visualizar no menu o modelo S5003DPSPERANTE"),
            ("can_print_list_s5003dpsPerAntE", u"Pode imprimir listagem do modelo S5003DPSPERANTE"),
            ("can_print_data_s5003dpsPerAntE", u"Pode imprimir o conteúdo do modelo S5003DPSPERANTE"), )

        ordering = [
            's5003_infodpsperante',
            'tpdpse',
            'dpsfgtse',]



class s5003dpsPerAntESerializer(ModelSerializer):

    class Meta:

        model = s5003dpsPerAntE
        fields = '__all__'


class s5003dpsPerApur(SoftDeletionModel):

    s5003_infotrabdps = models.ForeignKey('s5003.s5003infoTrabDps',
        related_name='%(class)s_s5003_infotrabdps', )

    def evento(self):
        return self.s5003_infotrabdps.evento()
    tpdps = models.IntegerField(choices=CHOICES_S5003_TPDPS, null=True, )
    dpsfgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infotrabdps), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Cálculo dos valores de FGTS a serem depositados, incidentes sobre a remuneração do período de apuração e de períodos anteriores, exceto se {tpAcConv} = [E].'
        db_table = r's5003_dpsperapur'
        managed = True # s5003_dpsperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003dpsPerApur", u"Pode ver listagem do modelo S5003DPSPERAPUR"),
            ("can_see_data_s5003dpsPerApur", u"Pode visualizar o conteúdo do modelo S5003DPSPERAPUR"),
            ("can_see_menu_s5003dpsPerApur", u"Pode visualizar no menu o modelo S5003DPSPERAPUR"),
            ("can_print_list_s5003dpsPerApur", u"Pode imprimir listagem do modelo S5003DPSPERAPUR"),
            ("can_print_data_s5003dpsPerApur", u"Pode imprimir o conteúdo do modelo S5003DPSPERAPUR"), )

        ordering = [
            's5003_infotrabdps',
            'tpdps',
            'dpsfgts',]



class s5003dpsPerApurSerializer(ModelSerializer):

    class Meta:

        model = s5003dpsPerApur
        fields = '__all__'


class s5003ideEstabLot(SoftDeletionModel):

    s5003_evtbasesfgts = models.ForeignKey('esocial.s5003evtBasesFGTS',
        related_name='%(class)s_s5003_evtbasesfgts', )

    def evento(self):
        return self.s5003_evtbasesfgts.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_evtbasesfgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's5003_ideestablot'
        managed = True # s5003_ideestablot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003ideEstabLot", u"Pode ver listagem do modelo S5003IDEESTABLOT"),
            ("can_see_data_s5003ideEstabLot", u"Pode visualizar o conteúdo do modelo S5003IDEESTABLOT"),
            ("can_see_menu_s5003ideEstabLot", u"Pode visualizar no menu o modelo S5003IDEESTABLOT"),
            ("can_print_list_s5003ideEstabLot", u"Pode imprimir listagem do modelo S5003IDEESTABLOT"),
            ("can_print_data_s5003ideEstabLot", u"Pode imprimir o conteúdo do modelo S5003IDEESTABLOT"), )

        ordering = [
            's5003_evtbasesfgts',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s5003ideEstabLotSerializer(ModelSerializer):

    class Meta:

        model = s5003ideEstabLot
        fields = '__all__'


class s5003infoBaseFGTS(SoftDeletionModel):

    s5003_infotrabfgts = models.ForeignKey('s5003.s5003infoTrabFGTS',
        related_name='%(class)s_s5003_infotrabfgts', )

    def evento(self):
        return self.s5003_infotrabfgts.evento()

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infotrabfgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações referentes a bases de cálculo do FGTS.'
        db_table = r's5003_infobasefgts'
        managed = True # s5003_infobasefgts #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoBaseFGTS", u"Pode ver listagem do modelo S5003INFOBASEFGTS"),
            ("can_see_data_s5003infoBaseFGTS", u"Pode visualizar o conteúdo do modelo S5003INFOBASEFGTS"),
            ("can_see_menu_s5003infoBaseFGTS", u"Pode visualizar no menu o modelo S5003INFOBASEFGTS"),
            ("can_print_list_s5003infoBaseFGTS", u"Pode imprimir listagem do modelo S5003INFOBASEFGTS"),
            ("can_print_data_s5003infoBaseFGTS", u"Pode imprimir o conteúdo do modelo S5003INFOBASEFGTS"), )

        ordering = [
            's5003_infotrabfgts',]



class s5003infoBaseFGTSSerializer(ModelSerializer):

    class Meta:

        model = s5003infoBaseFGTS
        fields = '__all__'


class s5003infoBasePerAntE(SoftDeletionModel):

    s5003_infobasefgts = models.ForeignKey('s5003.s5003infoBaseFGTS',
        related_name='%(class)s_s5003_infobasefgts', )

    def evento(self):
        return self.s5003_infobasefgts.evento()
    perref = models.CharField(max_length=7, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infobasefgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações referentes a bases de cálculo do FGTS de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5003_infobaseperante'
        managed = True # s5003_infobaseperante #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoBasePerAntE", u"Pode ver listagem do modelo S5003INFOBASEPERANTE"),
            ("can_see_data_s5003infoBasePerAntE", u"Pode visualizar o conteúdo do modelo S5003INFOBASEPERANTE"),
            ("can_see_menu_s5003infoBasePerAntE", u"Pode visualizar no menu o modelo S5003INFOBASEPERANTE"),
            ("can_print_list_s5003infoBasePerAntE", u"Pode imprimir listagem do modelo S5003INFOBASEPERANTE"),
            ("can_print_data_s5003infoBasePerAntE", u"Pode imprimir o conteúdo do modelo S5003INFOBASEPERANTE"), )

        ordering = [
            's5003_infobasefgts',
            'perref',]



class s5003infoBasePerAntESerializer(ModelSerializer):

    class Meta:

        model = s5003infoBasePerAntE
        fields = '__all__'


class s5003infoDpsFGTS(SoftDeletionModel):

    s5003_evtbasesfgts = models.ForeignKey('esocial.s5003evtBasesFGTS',
        related_name='%(class)s_s5003_evtbasesfgts', )

    def evento(self):
        return self.s5003_evtbasesfgts.evento()

    def __unicode__(self):

        lista = [
            unicode(self.s5003_evtbasesfgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre valores de FGTS.'
        db_table = r's5003_infodpsfgts'
        managed = True # s5003_infodpsfgts #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoDpsFGTS", u"Pode ver listagem do modelo S5003INFODPSFGTS"),
            ("can_see_data_s5003infoDpsFGTS", u"Pode visualizar o conteúdo do modelo S5003INFODPSFGTS"),
            ("can_see_menu_s5003infoDpsFGTS", u"Pode visualizar no menu o modelo S5003INFODPSFGTS"),
            ("can_print_list_s5003infoDpsFGTS", u"Pode imprimir listagem do modelo S5003INFODPSFGTS"),
            ("can_print_data_s5003infoDpsFGTS", u"Pode imprimir o conteúdo do modelo S5003INFODPSFGTS"), )

        ordering = [
            's5003_evtbasesfgts',]



class s5003infoDpsFGTSSerializer(ModelSerializer):

    class Meta:

        model = s5003infoDpsFGTS
        fields = '__all__'


class s5003infoDpsPerAntE(SoftDeletionModel):

    s5003_infotrabdps = models.ForeignKey('s5003.s5003infoTrabDps',
        related_name='%(class)s_s5003_infotrabdps', )

    def evento(self):
        return self.s5003_infotrabdps.evento()
    perref = models.CharField(max_length=7, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infotrabdps), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações referentes ao cálculo dos valores de FGTS de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5003_infodpsperante'
        managed = True # s5003_infodpsperante #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoDpsPerAntE", u"Pode ver listagem do modelo S5003INFODPSPERANTE"),
            ("can_see_data_s5003infoDpsPerAntE", u"Pode visualizar o conteúdo do modelo S5003INFODPSPERANTE"),
            ("can_see_menu_s5003infoDpsPerAntE", u"Pode visualizar no menu o modelo S5003INFODPSPERANTE"),
            ("can_print_list_s5003infoDpsPerAntE", u"Pode imprimir listagem do modelo S5003INFODPSPERANTE"),
            ("can_print_data_s5003infoDpsPerAntE", u"Pode imprimir o conteúdo do modelo S5003INFODPSPERANTE"), )

        ordering = [
            's5003_infotrabdps',
            'perref',]



class s5003infoDpsPerAntESerializer(ModelSerializer):

    class Meta:

        model = s5003infoDpsPerAntE
        fields = '__all__'


class s5003infoTrabDps(SoftDeletionModel):

    s5003_infodpsfgts = models.ForeignKey('s5003.s5003infoDpsFGTS',
        related_name='%(class)s_s5003_infodpsfgts', )

    def evento(self):
        return self.s5003_infodpsfgts.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_infodpsfgts), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas à matrícula e categoria do trabalhador.'
        db_table = r's5003_infotrabdps'
        managed = True # s5003_infotrabdps #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoTrabDps", u"Pode ver listagem do modelo S5003INFOTRABDPS"),
            ("can_see_data_s5003infoTrabDps", u"Pode visualizar o conteúdo do modelo S5003INFOTRABDPS"),
            ("can_see_menu_s5003infoTrabDps", u"Pode visualizar no menu o modelo S5003INFOTRABDPS"),
            ("can_print_list_s5003infoTrabDps", u"Pode imprimir listagem do modelo S5003INFOTRABDPS"),
            ("can_print_data_s5003infoTrabDps", u"Pode imprimir o conteúdo do modelo S5003INFOTRABDPS"), )

        ordering = [
            's5003_infodpsfgts',
            'codcateg',]



class s5003infoTrabDpsSerializer(ModelSerializer):

    class Meta:

        model = s5003infoTrabDps
        fields = '__all__'


class s5003infoTrabFGTS(SoftDeletionModel):

    s5003_ideestablot = models.ForeignKey('s5003.s5003ideEstabLot',
        related_name='%(class)s_s5003_ideestablot', )

    def evento(self):
        return self.s5003_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    dtadm = models.DateField(blank=True, null=True, )
    dtdeslig = models.DateField(blank=True, null=True, )
    dtinicio = models.DateField(blank=True, null=True, )
    mtvdeslig = models.TextField(blank=True, null=True, )
    dtterm = models.DateField(blank=True, null=True, )
    mtvdesligtsv = models.CharField(choices=CHOICES_S5003_MTVDESLIGTSV, max_length=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5003_ideestablot), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas à matrícula e categoria do trabalhador.'
        db_table = r's5003_infotrabfgts'
        managed = True # s5003_infotrabfgts #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5003infoTrabFGTS", u"Pode ver listagem do modelo S5003INFOTRABFGTS"),
            ("can_see_data_s5003infoTrabFGTS", u"Pode visualizar o conteúdo do modelo S5003INFOTRABFGTS"),
            ("can_see_menu_s5003infoTrabFGTS", u"Pode visualizar no menu o modelo S5003INFOTRABFGTS"),
            ("can_print_list_s5003infoTrabFGTS", u"Pode imprimir listagem do modelo S5003INFOTRABFGTS"),
            ("can_print_data_s5003infoTrabFGTS", u"Pode imprimir o conteúdo do modelo S5003INFOTRABFGTS"), )

        ordering = [
            's5003_ideestablot',
            'codcateg',]



class s5003infoTrabFGTSSerializer(ModelSerializer):

    class Meta:

        model = s5003infoTrabFGTS
        fields = '__all__'