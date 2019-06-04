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
from emensageriapro.s5013.choices import *
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





class s5013basePerAntE(SoftDeletionModel):

    s5013_infobaseperante = models.ForeignKey('s5013.s5013infoBasePerAntE', 
        related_name='%(class)s_s5013_infobaseperante', )
    
    def evento(self): 
        return self.s5013_infobaseperante.evento()
    tpvalore = models.IntegerField(choices=CHOICES_S5013_TPVALORE, null=True, )
    basefgtse = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infobaseperante),
            unicode(self.tpvalore),
            unicode(self.basefgtse),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre bases de cálculo do FGTS referentes à remuneração de períodos anteriores quando {tpAcConv} = [E]. Origem: S-1200 ou S-2299.'
        db_table = r's5013_baseperante'       
        managed = True # s5013_baseperante #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013basePerAntE", u"Pode ver listagem do modelo S5013BASEPERANTE"),
            ("can_see_data_s5013basePerAntE", u"Pode visualizar o conteúdo do modelo S5013BASEPERANTE"),
            ("can_see_menu_s5013basePerAntE", u"Pode visualizar no menu o modelo S5013BASEPERANTE"),
            ("can_print_list_s5013basePerAntE", u"Pode imprimir listagem do modelo S5013BASEPERANTE"),
            ("can_print_data_s5013basePerAntE", u"Pode imprimir o conteúdo do modelo S5013BASEPERANTE"), )
            
        ordering = [
            's5013_infobaseperante',
            'tpvalore',
            'basefgtse',]



class s5013basePerAntESerializer(ModelSerializer):

    class Meta:
    
        model = s5013basePerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013basePerApur(SoftDeletionModel):

    s5013_infobasefgts = models.ForeignKey('s5013.s5013infoBaseFGTS', 
        related_name='%(class)s_s5013_infobasefgts', )
    
    def evento(self): 
        return self.s5013_infobasefgts.evento()
    tpvalor = models.IntegerField(null=True, )
    basefgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infobasefgts),
            unicode(self.tpvalor),
            unicode(self.basefgts),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre bases de cálculo do FGTS referentes à remuneração do período de apuração e de períodos anteriores, exceto se {tpAcConv} = [E]. Origem: S-1200, S-2299 ou S-2399.'
        db_table = r's5013_baseperapur'       
        managed = True # s5013_baseperapur #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013basePerApur", u"Pode ver listagem do modelo S5013BASEPERAPUR"),
            ("can_see_data_s5013basePerApur", u"Pode visualizar o conteúdo do modelo S5013BASEPERAPUR"),
            ("can_see_menu_s5013basePerApur", u"Pode visualizar no menu o modelo S5013BASEPERAPUR"),
            ("can_print_list_s5013basePerApur", u"Pode imprimir listagem do modelo S5013BASEPERAPUR"),
            ("can_print_data_s5013basePerApur", u"Pode imprimir o conteúdo do modelo S5013BASEPERAPUR"), )
            
        ordering = [
            's5013_infobasefgts',
            'tpvalor',
            'basefgts',]



class s5013basePerApurSerializer(ModelSerializer):

    class Meta:
    
        model = s5013basePerApur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013dpsPerAntE(SoftDeletionModel):

    s5013_infodpsperante = models.ForeignKey('s5013.s5013infoDpsPerAntE', 
        related_name='%(class)s_s5013_infodpsperante', )
    
    def evento(self): 
        return self.s5013_infodpsperante.evento()
    tpdpse = models.IntegerField(choices=CHOICES_S5013_TPDPSE, null=True, )
    vrfgtse = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infodpsperante),
            unicode(self.tpdpse),
            unicode(self.vrfgtse),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Cálculo dos valores de FGTS a serem depositados, incidentes sobre a remuneração de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5013_dpsperante'       
        managed = True # s5013_dpsperante #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013dpsPerAntE", u"Pode ver listagem do modelo S5013DPSPERANTE"),
            ("can_see_data_s5013dpsPerAntE", u"Pode visualizar o conteúdo do modelo S5013DPSPERANTE"),
            ("can_see_menu_s5013dpsPerAntE", u"Pode visualizar no menu o modelo S5013DPSPERANTE"),
            ("can_print_list_s5013dpsPerAntE", u"Pode imprimir listagem do modelo S5013DPSPERANTE"),
            ("can_print_data_s5013dpsPerAntE", u"Pode imprimir o conteúdo do modelo S5013DPSPERANTE"), )
            
        ordering = [
            's5013_infodpsperante',
            'tpdpse',
            'vrfgtse',]



class s5013dpsPerAntESerializer(ModelSerializer):

    class Meta:
    
        model = s5013dpsPerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013dpsPerApur(SoftDeletionModel):

    s5013_infodpsfgts = models.ForeignKey('s5013.s5013infoDpsFGTS', 
        related_name='%(class)s_s5013_infodpsfgts', )
    
    def evento(self): 
        return self.s5013_infodpsfgts.evento()
    tpdps = models.IntegerField(choices=CHOICES_S5013_TPDPS, null=True, )
    vrfgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infodpsfgts),
            unicode(self.tpdps),
            unicode(self.vrfgts),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Cálculo dos valores de FGTS a serem depositados, incidentes sobre a remuneração do período de apuração e de períodos anteriores, exceto se {tpAcConv} = [E].'
        db_table = r's5013_dpsperapur'       
        managed = True # s5013_dpsperapur #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013dpsPerApur", u"Pode ver listagem do modelo S5013DPSPERAPUR"),
            ("can_see_data_s5013dpsPerApur", u"Pode visualizar o conteúdo do modelo S5013DPSPERAPUR"),
            ("can_see_menu_s5013dpsPerApur", u"Pode visualizar no menu o modelo S5013DPSPERAPUR"),
            ("can_print_list_s5013dpsPerApur", u"Pode imprimir listagem do modelo S5013DPSPERAPUR"),
            ("can_print_data_s5013dpsPerApur", u"Pode imprimir o conteúdo do modelo S5013DPSPERAPUR"), )
            
        ordering = [
            's5013_infodpsfgts',
            'tpdps',
            'vrfgts',]



class s5013dpsPerApurSerializer(ModelSerializer):

    class Meta:
    
        model = s5013dpsPerApur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013infoBaseFGTS(SoftDeletionModel):

    s5013_evtfgts = models.ForeignKey('esocial.s5013evtFGTS', 
        related_name='%(class)s_s5013_evtfgts', )
    
    def evento(self): 
        return self.s5013_evtfgts.evento()
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_evtfgts),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações referentes a bases de cálculo do FGTS.'
        db_table = r's5013_infobasefgts'       
        managed = True # s5013_infobasefgts #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013infoBaseFGTS", u"Pode ver listagem do modelo S5013INFOBASEFGTS"),
            ("can_see_data_s5013infoBaseFGTS", u"Pode visualizar o conteúdo do modelo S5013INFOBASEFGTS"),
            ("can_see_menu_s5013infoBaseFGTS", u"Pode visualizar no menu o modelo S5013INFOBASEFGTS"),
            ("can_print_list_s5013infoBaseFGTS", u"Pode imprimir listagem do modelo S5013INFOBASEFGTS"),
            ("can_print_data_s5013infoBaseFGTS", u"Pode imprimir o conteúdo do modelo S5013INFOBASEFGTS"), )
            
        ordering = [
            's5013_evtfgts',]



class s5013infoBaseFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s5013infoBaseFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013infoBasePerAntE(SoftDeletionModel):

    s5013_infobasefgts = models.ForeignKey('s5013.s5013infoBaseFGTS', 
        related_name='%(class)s_s5013_infobasefgts', )
    
    def evento(self): 
        return self.s5013_infobasefgts.evento()
    perref = models.CharField(max_length=7, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infobasefgts),
            unicode(self.perref),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações referentes a bases de cálculo do FGTS de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5013_infobaseperante'       
        managed = True # s5013_infobaseperante #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013infoBasePerAntE", u"Pode ver listagem do modelo S5013INFOBASEPERANTE"),
            ("can_see_data_s5013infoBasePerAntE", u"Pode visualizar o conteúdo do modelo S5013INFOBASEPERANTE"),
            ("can_see_menu_s5013infoBasePerAntE", u"Pode visualizar no menu o modelo S5013INFOBASEPERANTE"),
            ("can_print_list_s5013infoBasePerAntE", u"Pode imprimir listagem do modelo S5013INFOBASEPERANTE"),
            ("can_print_data_s5013infoBasePerAntE", u"Pode imprimir o conteúdo do modelo S5013INFOBASEPERANTE"), )
            
        ordering = [
            's5013_infobasefgts',
            'perref',]



class s5013infoBasePerAntESerializer(ModelSerializer):

    class Meta:
    
        model = s5013infoBasePerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013infoDpsFGTS(SoftDeletionModel):

    s5013_evtfgts = models.ForeignKey('esocial.s5013evtFGTS', 
        related_name='%(class)s_s5013_evtfgts', )
    
    def evento(self): 
        return self.s5013_evtfgts.evento()
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_evtfgts),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre valores de FGTS.'
        db_table = r's5013_infodpsfgts'       
        managed = True # s5013_infodpsfgts #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013infoDpsFGTS", u"Pode ver listagem do modelo S5013INFODPSFGTS"),
            ("can_see_data_s5013infoDpsFGTS", u"Pode visualizar o conteúdo do modelo S5013INFODPSFGTS"),
            ("can_see_menu_s5013infoDpsFGTS", u"Pode visualizar no menu o modelo S5013INFODPSFGTS"),
            ("can_print_list_s5013infoDpsFGTS", u"Pode imprimir listagem do modelo S5013INFODPSFGTS"),
            ("can_print_data_s5013infoDpsFGTS", u"Pode imprimir o conteúdo do modelo S5013INFODPSFGTS"), )
            
        ordering = [
            's5013_evtfgts',]



class s5013infoDpsFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s5013infoDpsFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5013infoDpsPerAntE(SoftDeletionModel):

    s5013_infodpsfgts = models.ForeignKey('s5013.s5013infoDpsFGTS', 
        related_name='%(class)s_s5013_infodpsfgts', )
    
    def evento(self): 
        return self.s5013_infodpsfgts.evento()
    perref = models.CharField(max_length=7, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5013_infodpsfgts),
            unicode(self.perref),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações referentes ao cálculo dos valores de FGTS de períodos anteriores quando {tpAcConv} = [E].'
        db_table = r's5013_infodpsperante'       
        managed = True # s5013_infodpsperante #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013infoDpsPerAntE", u"Pode ver listagem do modelo S5013INFODPSPERANTE"),
            ("can_see_data_s5013infoDpsPerAntE", u"Pode visualizar o conteúdo do modelo S5013INFODPSPERANTE"),
            ("can_see_menu_s5013infoDpsPerAntE", u"Pode visualizar no menu o modelo S5013INFODPSPERANTE"),
            ("can_print_list_s5013infoDpsPerAntE", u"Pode imprimir listagem do modelo S5013INFODPSPERANTE"),
            ("can_print_data_s5013infoDpsPerAntE", u"Pode imprimir o conteúdo do modelo S5013INFODPSPERANTE"), )
            
        ordering = [
            's5013_infodpsfgts',
            'perref',]



class s5013infoDpsPerAntESerializer(ModelSerializer):

    class Meta:
    
        model = s5013infoDpsPerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()