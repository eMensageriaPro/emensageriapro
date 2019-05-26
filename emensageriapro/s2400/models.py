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
from emensageriapro.s2400.choices import *
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





class s2400brasil(SoftDeletionModel):

    s2400_endereco = models.ForeignKey('s2400.s2400endereco', 
        related_name='%(class)s_s2400_endereco', )
    
    def evento(self): 
        return self.s2400_endereco.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2400_endereco),
            unicode(self.tplograd),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.cep),
            unicode(self.codmunic),
            unicode(self.uf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2400_brasil'       
        managed = True # s2400_brasil #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2400_brasil", "Can view s2400_brasil"), )
            
        ordering = [
            's2400_endereco',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2400brasilSerializer(ModelSerializer):

    class Meta:
    
        model = s2400brasil
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2400dependente(SoftDeletionModel):

    s2400_evtcdbenefin = models.ForeignKey('esocial.s2400evtCdBenefIn', 
        related_name='%(class)s_s2400_evtcdbenefin', )
    
    def evento(self): 
        return self.s2400_evtcdbenefin.evento()
    tpdep = models.CharField(choices=CHOICES_S2400_TPDEP, max_length=2, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    sexodep = models.CharField(choices=CHOICES_S2400_SEXODEP, max_length=1, null=True, )
    depirrf = models.CharField(choices=CHOICES_S2400_DEPIRRF, max_length=1, null=True, )
    incfismen = models.CharField(choices=CHOICES_S2400_INCFISMEN, max_length=1, null=True, )
    depfinsprev = models.CharField(choices=CHOICES_S2400_DEPFINSPREV, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2400_evtcdbenefin),
            unicode(self.tpdep),
            unicode(self.nmdep),
            unicode(self.dtnascto),
            unicode(self.sexodep),
            unicode(self.depirrf),
            unicode(self.incfismen),
            unicode(self.depfinsprev),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações dos dependentes'
        db_table = r's2400_dependente'       
        managed = True # s2400_dependente #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2400_dependente", "Can view s2400_dependente"), )
            
        ordering = [
            's2400_evtcdbenefin',
            'tpdep',
            'nmdep',
            'dtnascto',
            'sexodep',
            'depirrf',
            'incfismen',
            'depfinsprev',]



class s2400dependenteSerializer(ModelSerializer):

    class Meta:
    
        model = s2400dependente
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2400endereco(SoftDeletionModel):

    s2400_evtcdbenefin = models.ForeignKey('esocial.s2400evtCdBenefIn', 
        related_name='%(class)s_s2400_evtcdbenefin', )
    
    def evento(self): 
        return self.s2400_evtcdbenefin.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2400_evtcdbenefin),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Grupo de informações do endereço do Trabalhador'
        db_table = r's2400_endereco'       
        managed = True # s2400_endereco #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2400_endereco", "Can view s2400_endereco"), )
            
        ordering = [
            's2400_evtcdbenefin',]



class s2400enderecoSerializer(ModelSerializer):

    class Meta:
    
        model = s2400endereco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2400exterior(SoftDeletionModel):

    s2400_endereco = models.ForeignKey('s2400.s2400endereco', 
        related_name='%(class)s_s2400_endereco', )
    
    def evento(self): 
        return self.s2400_endereco.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2400_endereco),
            unicode(self.paisresid),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.nmcid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2400_exterior'       
        managed = True # s2400_exterior #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2400_exterior", "Can view s2400_exterior"), )
            
        ordering = [
            's2400_endereco',
            'paisresid',
            'dsclograd',
            'nrlograd',
            'nmcid',]



class s2400exteriorSerializer(ModelSerializer):

    class Meta:
    
        model = s2400exterior
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()