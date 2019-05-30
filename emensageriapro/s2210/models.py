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
from emensageriapro.s2210.choices import *
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





class s2210agenteCausador(SoftDeletionModel):

    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT', 
        related_name='%(class)s_s2210_evtcat', )
    
    def evento(self): 
        return self.s2210_evtcat.evento()
    codagntcausador = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2210_evtcat),
            unicode(self.codagntcausador),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento do(s) agente(s) causador(es) do acidente de trabalho'
        db_table = r's2210_agentecausador'       
        managed = True # s2210_agentecausador #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2210_agentecausador", "Can view s2210_agentecausador"), )
            
        ordering = [
            's2210_evtcat',
            'codagntcausador',]



class s2210agenteCausadorSerializer(ModelSerializer):

    class Meta:
    
        model = s2210agenteCausador
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2210atestado(SoftDeletionModel):

    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT', 
        related_name='%(class)s_s2210_evtcat', )
    
    def evento(self): 
        return self.s2210_evtcat.evento()
    codcnes = models.CharField(max_length=7, blank=True, null=True, )
    dtatendimento = models.DateField(null=True, )
    hratendimento = models.CharField(max_length=4, null=True, )
    indinternacao = models.CharField(choices=CHOICES_S2210_INDINTERNACAO, max_length=1, null=True, )
    durtrat = models.IntegerField(null=True, )
    indafast = models.CharField(choices=CHOICES_S2210_INDAFAST, max_length=1, null=True, )
    dsclesao = models.IntegerField(null=True, )
    dsccomplesao = models.CharField(max_length=200, blank=True, null=True, )
    diagprovavel = models.CharField(max_length=100, blank=True, null=True, )
    codcid = models.CharField(max_length=4, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    nmemit = models.CharField(max_length=70, null=True, )
    ideoc = models.IntegerField(choices=CHOICES_S2210_IDEOC, null=True, )
    nroc = models.CharField(max_length=14, null=True, )
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2210_evtcat),
            unicode(self.dtatendimento),
            unicode(self.hratendimento),
            unicode(self.indinternacao),
            unicode(self.durtrat),
            unicode(self.indafast),
            unicode(self.dsclesao),
            unicode(self.codcid),
            unicode(self.nmemit),
            unicode(self.ideoc),
            unicode(self.nroc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Atestado Médico'
        db_table = r's2210_atestado'       
        managed = True # s2210_atestado #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2210_atestado", "Can view s2210_atestado"), )
            
        ordering = [
            's2210_evtcat',
            'dtatendimento',
            'hratendimento',
            'indinternacao',
            'durtrat',
            'indafast',
            'dsclesao',
            'codcid',
            'nmemit',
            'ideoc',
            'nroc',]



class s2210atestadoSerializer(ModelSerializer):

    class Meta:
    
        model = s2210atestado
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2210catOrigem(SoftDeletionModel):

    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT', 
        related_name='%(class)s_s2210_evtcat', )
    
    def evento(self): 
        return self.s2210_evtcat.evento()
    dtcatorig = models.DateField(null=True, )
    nrreccatorig = models.CharField(max_length=40, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2210_evtcat),
            unicode(self.dtcatorig),
            unicode(self.nrreccatorig),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que indica a CAT anterior, no caso de CAT de reabertura ou de comunicação de óbito'
        db_table = r's2210_catorigem'       
        managed = True # s2210_catorigem #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2210_catorigem", "Can view s2210_catorigem"), )
            
        ordering = [
            's2210_evtcat',
            'dtcatorig',
            'nrreccatorig',]



class s2210catOrigemSerializer(ModelSerializer):

    class Meta:
    
        model = s2210catOrigem
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2210ideLocalAcid(SoftDeletionModel):

    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT', 
        related_name='%(class)s_s2210_evtcat', )
    
    def evento(self): 
        return self.s2210_evtcat.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2210_evtcat),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do local onde ocorreu o acidente'
        db_table = r's2210_idelocalacid'       
        managed = True # s2210_idelocalacid #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2210_idelocalacid", "Can view s2210_idelocalacid"), )
            
        ordering = [
            's2210_evtcat',
            'tpinsc',
            'nrinsc',]



class s2210ideLocalAcidSerializer(ModelSerializer):

    class Meta:
    
        model = s2210ideLocalAcid
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2210parteAtingida(SoftDeletionModel):

    s2210_evtcat = models.ForeignKey('esocial.s2210evtCAT', 
        related_name='%(class)s_s2210_evtcat', )
    
    def evento(self): 
        return self.s2210_evtcat.evento()
    codparteating = models.IntegerField(null=True, )
    lateralidade = models.IntegerField(choices=CHOICES_S2210_LATERALIDADE, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2210_evtcat),
            unicode(self.codparteating),
            unicode(self.lateralidade),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento da(s) parte(s) atingida(s) pelo acidente de trabalho.'
        db_table = r's2210_parteatingida'       
        managed = True # s2210_parteatingida #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2210_parteatingida", "Can view s2210_parteatingida"), )
            
        ordering = [
            's2210_evtcat',
            'codparteating',
            'lateralidade',]



class s2210parteAtingidaSerializer(ModelSerializer):

    class Meta:
    
        model = s2210parteAtingida
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()