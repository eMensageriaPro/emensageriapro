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
from emensageriapro.s5002.choices import *
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





class s5002basesIrrf(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf', 
        related_name='%(class)s_s5002_infoirrf', )
    
    def evento(self): 
        return self.s5002_infoirrf.evento()
    tpvalor = models.IntegerField(null=True, )
    valor = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5002_infoirrf),
            unicode(self.tpvalor),
            unicode(self.valor),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Bases, deduções, isenções e retenções do IRRF'
        db_table = r's5002_basesirrf'       
        managed = True # s5002_basesirrf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s5002basesIrrf", "Can view S5002BASESIRRF"),
            ("can_view_menu_s5002basesIrrf", "Can view menu S5002BASESIRRF"),)
            
        ordering = [
            's5002_infoirrf',
            'tpvalor',
            'valor',]



class s5002basesIrrfSerializer(ModelSerializer):

    class Meta:
    
        model = s5002basesIrrf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5002idePgtoExt(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf', 
        related_name='%(class)s_s5002_infoirrf', )
    
    def evento(self): 
        return self.s5002_infoirrf.evento()
    codpais = models.TextField(null=True, )
    indnif = models.IntegerField(choices=CHOICES_S5002_INDNIF, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5002_infoirrf),
            unicode(self.codpais),
            unicode(self.indnif),
            unicode(self.dsclograd),
            unicode(self.nmcid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares relativas a pagamentos efetuados a beneficiário residente fiscal no exterior.'
        db_table = r's5002_idepgtoext'       
        managed = True # s5002_idepgtoext #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s5002idePgtoExt", "Can view S5002IDEPGTOEXT"),
            ("can_view_menu_s5002idePgtoExt", "Can view menu S5002IDEPGTOEXT"),)
            
        ordering = [
            's5002_infoirrf',
            'codpais',
            'indnif',
            'dsclograd',
            'nmcid',]



class s5002idePgtoExtSerializer(ModelSerializer):

    class Meta:
    
        model = s5002idePgtoExt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5002infoDep(SoftDeletionModel):

    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef', 
        related_name='%(class)s_s5002_evtirrfbenef', )
    
    def evento(self): 
        return self.s5002_evtirrfbenef.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5002_evtirrfbenef),
            unicode(self.vrdeddep),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas a existência de dependentes do beneficiário do pagamento. Origem: S-1210 - registro {deps}'
        db_table = r's5002_infodep'       
        managed = True # s5002_infodep #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s5002infoDep", "Can view S5002INFODEP"),
            ("can_view_menu_s5002infoDep", "Can view menu S5002INFODEP"),)
            
        ordering = [
            's5002_evtirrfbenef',
            'vrdeddep',]



class s5002infoDepSerializer(ModelSerializer):

    class Meta:
    
        model = s5002infoDep
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5002infoIrrf(SoftDeletionModel):

    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef', 
        related_name='%(class)s_s5002_evtirrfbenef', )
    
    def evento(self): 
        return self.s5002_evtirrfbenef.evento()
    codcateg = models.IntegerField(blank=True, null=True, )
    indresbr = models.CharField(choices=CHOICES_S5002_INDRESBR, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5002_evtirrfbenef),
            unicode(self.indresbr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao Imposto de Renda Retido na Fonte do Trabalhador e suas bases de cálculo'
        db_table = r's5002_infoirrf'       
        managed = True # s5002_infoirrf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s5002infoIrrf", "Can view S5002INFOIRRF"),
            ("can_view_menu_s5002infoIrrf", "Can view menu S5002INFOIRRF"),)
            
        ordering = [
            's5002_evtirrfbenef',
            'indresbr',]



class s5002infoIrrfSerializer(ModelSerializer):

    class Meta:
    
        model = s5002infoIrrf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s5002irrf(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf', 
        related_name='%(class)s_s5002_infoirrf', )
    
    def evento(self): 
        return self.s5002_infoirrf.evento()
    tpcr = models.CharField(choices=CHOICES_S5002_TPCR, max_length=6, null=True, )
    vrirrfdesc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s5002_infoirrf),
            unicode(self.tpcr),
            unicode(self.vrirrfdesc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao Imposto de Renda Retido na Fonte'
        db_table = r's5002_irrf'       
        managed = True # s5002_irrf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s5002irrf", "Can view S5002IRRF"),
            ("can_view_menu_s5002irrf", "Can view menu S5002IRRF"),)
            
        ordering = [
            's5002_infoirrf',
            'tpcr',
            'vrirrfdesc',]



class s5002irrfSerializer(ModelSerializer):

    class Meta:
    
        model = s5002irrf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()