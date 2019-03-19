#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S1280_INDSUBSTPATR = (
    (1, u'1 - Integralmente substituída'),
    (2, u'2 - Parcialmente substituída'),
)

class s1280infoAtivConcom(SoftDeletionModel):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)
    #s1280_infoativconcom_custom#

    class Meta:
        # verbose_name = u'Registro preenchido por empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída.'
        db_table = r's1280_infoativconcom'       
        managed = True # s1280_infoativconcom #
        unique_together = (
            #custom_unique_together_s1280_infoativconcom#
            
        )
        index_together = (
            #custom_index_together_s1280_infoativconcom
            #index_together_s1280_infoativconcom
        )
        permissions = (
            ("can_view_s1280_infoativconcom", "Can view s1280_infoativconcom"),
            #custom_permissions_s1280_infoativconcom
        )
        ordering = ['s1280_evtinfocomplper', 'fatormes', 'fator13']



class s1280infoAtivConcomSerializer(ModelSerializer):
    class Meta:
        model = s1280infoAtivConcom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1280infoSubstPatr(SoftDeletionModel):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    indsubstpatr = models.IntegerField(choices=CHOICES_S1280_INDSUBSTPATR)
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.indsubstpatr) + ' - ' + unicode(self.percredcontrib)
    #s1280_infosubstpatr_custom#

    class Meta:
        # verbose_name = u'Registro preenchido exclusivamente por empresa enquadrada nos artigos 7 a 9 da Lei 12.546/2011, conforme classificação tributária indicada no evento de Informações Cadastrais do Empregador.'
        db_table = r's1280_infosubstpatr'       
        managed = True # s1280_infosubstpatr #
        unique_together = (
            #custom_unique_together_s1280_infosubstpatr#
            
        )
        index_together = (
            #custom_index_together_s1280_infosubstpatr
            #index_together_s1280_infosubstpatr
        )
        permissions = (
            ("can_view_s1280_infosubstpatr", "Can view s1280_infosubstpatr"),
            #custom_permissions_s1280_infosubstpatr
        )
        ordering = ['s1280_evtinfocomplper', 'indsubstpatr', 'percredcontrib']



class s1280infoSubstPatrSerializer(ModelSerializer):
    class Meta:
        model = s1280infoSubstPatr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1280infoSubstPatrOpPort(SoftDeletionModel):
    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    cnpjopportuario = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.cnpjopportuario)
    #s1280_infosubstpatropport_custom#

    class Meta:
        # verbose_name = u'Registro preenchido exclusivamente pelo OGMO ({classTrib}=[09]) listando apenas seus Operadores Portuários enquadrados nos artigos 7 a 9 da Lei 12.546/2011.'
        db_table = r's1280_infosubstpatropport'       
        managed = True # s1280_infosubstpatropport #
        unique_together = (
            #custom_unique_together_s1280_infosubstpatropport#
            
        )
        index_together = (
            #custom_index_together_s1280_infosubstpatropport
            #index_together_s1280_infosubstpatropport
        )
        permissions = (
            ("can_view_s1280_infosubstpatropport", "Can view s1280_infosubstpatropport"),
            #custom_permissions_s1280_infosubstpatropport
        )
        ordering = ['s1280_evtinfocomplper', 'cnpjopportuario']



class s1280infoSubstPatrOpPortSerializer(ModelSerializer):
    class Meta:
        model = s1280infoSubstPatrOpPort
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
