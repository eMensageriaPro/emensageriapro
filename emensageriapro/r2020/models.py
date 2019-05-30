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
from emensageriapro.r2020.choices import *
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





class r2020infoProcRetAd(SoftDeletionModel):

    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest', 
        related_name='%(class)s_r2020_evtservprest', )
    
    def evento(self): 
        return self.r2020_evtservprest.evento()
    tpprocretadic = models.IntegerField(choices=CHOICES_R2020_TPPROCRETADIC, null=True, )
    nrprocretadic = models.CharField(max_length=21, null=True, )
    codsuspadic = models.IntegerField(blank=True, null=True, )
    valoradic = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2020_evtservprest),
            unicode(self.tpprocretadic),
            unicode(self.nrprocretadic),
            unicode(self.valoradic),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária adicional'
        db_table = r'r2020_infoprocretad'       
        managed = True # r2020_infoprocretad #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2020_infoprocretad", "Can view r2020_infoprocretad"), )
            
        ordering = [
            'r2020_evtservprest',
            'tpprocretadic',
            'nrprocretadic',
            'valoradic',]



class r2020infoProcRetAdSerializer(ModelSerializer):

    class Meta:
    
        model = r2020infoProcRetAd
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2020infoProcRetPr(SoftDeletionModel):

    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest', 
        related_name='%(class)s_r2020_evtservprest', )
    
    def evento(self): 
        return self.r2020_evtservprest.evento()
    tpprocretprinc = models.IntegerField(choices=CHOICES_R2020_TPPROCRETPRINC, null=True, )
    nrprocretprinc = models.CharField(max_length=21, null=True, )
    codsuspprinc = models.IntegerField(blank=True, null=True, )
    valorprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2020_evtservprest),
            unicode(self.tpprocretprinc),
            unicode(self.nrprocretprinc),
            unicode(self.valorprinc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r2020_infoprocretpr'       
        managed = True # r2020_infoprocretpr #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2020_infoprocretpr", "Can view r2020_infoprocretpr"), )
            
        ordering = [
            'r2020_evtservprest',
            'tpprocretprinc',
            'nrprocretprinc',
            'valorprinc',]



class r2020infoProcRetPrSerializer(ModelSerializer):

    class Meta:
    
        model = r2020infoProcRetPr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2020infoTpServ(SoftDeletionModel):

    r2020_nfs = models.ForeignKey('r2020.r2020nfs', 
        related_name='%(class)s_r2020_nfs', )
    
    def evento(self): 
        return self.r2020_nfs.evento()
    tpservico = models.IntegerField(null=True, )
    vlrbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrretencao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrretsub = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrservicos15 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrservicos20 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrservicos25 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlradicional = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2020_nfs),
            unicode(self.tpservico),
            unicode(self.vlrbaseret),
            unicode(self.vlrretencao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre os tipos de Serviços constantes da Nota Fiscal'
        db_table = r'r2020_infotpserv'       
        managed = True # r2020_infotpserv #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2020_infotpserv", "Can view r2020_infotpserv"), )
            
        ordering = [
            'r2020_nfs',
            'tpservico',
            'vlrbaseret',
            'vlrretencao',]



class r2020infoTpServSerializer(ModelSerializer):

    class Meta:
    
        model = r2020infoTpServ
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2020nfs(SoftDeletionModel):

    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest', 
        related_name='%(class)s_r2020_evtservprest', )
    
    def evento(self): 
        return self.r2020_evtservprest.evento()
    serie = models.CharField(max_length=5, null=True, )
    numdocto = models.CharField(max_length=15, null=True, )
    dtemissaonf = models.DateField(null=True, )
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    obs = models.CharField(max_length=250, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2020_evtservprest),
            unicode(self.serie),
            unicode(self.numdocto),
            unicode(self.dtemissaonf),
            unicode(self.vlrbruto),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das notas fiscais de serviços prestados pela empresa identificada no registro superior'
        db_table = r'r2020_nfs'       
        managed = True # r2020_nfs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2020_nfs", "Can view r2020_nfs"), )
            
        ordering = [
            'r2020_evtservprest',
            'serie',
            'numdocto',
            'dtemissaonf',
            'vlrbruto',]



class r2020nfsSerializer(ModelSerializer):

    class Meta:
    
        model = r2020nfs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()