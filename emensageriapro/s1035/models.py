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
from emensageriapro.s1035.choices import *
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





class s1035alteracao(SoftDeletionModel):

    s1035_evttabcarreira = models.ForeignKey('esocial.s1035evtTabCarreira', 
        related_name='%(class)s_s1035_evttabcarreira', )
    
    def evento(self): 
        return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    dsccarreira = models.CharField(max_length=100, null=True, )
    leicarr = models.CharField(max_length=12, blank=True, null=True, )
    dtleicarr = models.DateField(null=True, )
    sitcarr = models.IntegerField(choices=CHOICES_S1035_SITCARR_ALTERACAO, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1035_evttabcarreira),
            unicode(self.codcarreira),
            unicode(self.inivalid),
            unicode(self.dsccarreira),
            unicode(self.dtleicarr),
            unicode(self.sitcarr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1035_alteracao'       
        managed = True # s1035_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1035alteracao", "Can view S1035ALTERACAO"),
            ("can_view_menu_s1035alteracao", "Can view menu S1035ALTERACAO"),)
            
        ordering = [
            's1035_evttabcarreira',
            'codcarreira',
            'inivalid',
            'dsccarreira',
            'dtleicarr',
            'sitcarr',]



class s1035alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1035alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1035alteracaonovaValidade(SoftDeletionModel):

    s1035_alteracao = models.ForeignKey('s1035.s1035alteracao', 
        related_name='%(class)s_s1035_alteracao', )
    
    def evento(self): 
        return self.s1035_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1035_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1035_alteracao_novavalidade'       
        managed = True # s1035_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1035alteracaonovaValidade", "Can view S1035ALTERACAONOVAVALIDADE"),
            ("can_view_menu_s1035alteracaonovaValidade", "Can view menu S1035ALTERACAONOVAVALIDADE"),)
            
        ordering = [
            's1035_alteracao',
            'inivalid',]



class s1035alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1035alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1035exclusao(SoftDeletionModel):

    s1035_evttabcarreira = models.ForeignKey('esocial.s1035evtTabCarreira', 
        related_name='%(class)s_s1035_evttabcarreira', )
    
    def evento(self): 
        return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1035_evttabcarreira),
            unicode(self.codcarreira),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1035_exclusao'       
        managed = True # s1035_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1035exclusao", "Can view S1035EXCLUSAO"),
            ("can_view_menu_s1035exclusao", "Can view menu S1035EXCLUSAO"),)
            
        ordering = [
            's1035_evttabcarreira',
            'codcarreira',
            'inivalid',]



class s1035exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1035exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1035inclusao(SoftDeletionModel):

    s1035_evttabcarreira = models.ForeignKey('esocial.s1035evtTabCarreira', 
        related_name='%(class)s_s1035_evttabcarreira', )
    
    def evento(self): 
        return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    dsccarreira = models.CharField(max_length=100, null=True, )
    leicarr = models.CharField(max_length=12, blank=True, null=True, )
    dtleicarr = models.DateField(null=True, )
    sitcarr = models.IntegerField(choices=CHOICES_S1035_SITCARR_INCLUSAO, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1035_evttabcarreira),
            unicode(self.codcarreira),
            unicode(self.inivalid),
            unicode(self.dsccarreira),
            unicode(self.dtleicarr),
            unicode(self.sitcarr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1035_inclusao'       
        managed = True # s1035_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1035inclusao", "Can view S1035INCLUSAO"),
            ("can_view_menu_s1035inclusao", "Can view menu S1035INCLUSAO"),)
            
        ordering = [
            's1035_evttabcarreira',
            'codcarreira',
            'inivalid',
            'dsccarreira',
            'dtleicarr',
            'sitcarr',]



class s1035inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1035inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()