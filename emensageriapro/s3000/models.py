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
from emensageriapro.s3000.choices import *
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





class s3000ideFolhaPagto(SoftDeletionModel):

    s3000_evtexclusao = models.ForeignKey('esocial.s3000evtExclusao', 
        related_name='%(class)s_s3000_evtexclusao', )
    
    def evento(self): 
        return self.s3000_evtexclusao.evento()
    indapuracao = models.IntegerField(choices=CHOICES_S3000_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s3000_evtexclusao),
            unicode(self.indapuracao),
            unicode(self.perapur),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica a qual folha de pagamento pertence o evento que será excluído'
        db_table = r's3000_idefolhapagto'       
        managed = True # s3000_idefolhapagto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s3000_idefolhapagto", "Can view s3000_idefolhapagto"), )
            
        ordering = [
            's3000_evtexclusao',
            'indapuracao',
            'perapur',]



class s3000ideFolhaPagtoSerializer(ModelSerializer):

    class Meta:
    
        model = s3000ideFolhaPagto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s3000ideTrabalhador(SoftDeletionModel):

    s3000_evtexclusao = models.ForeignKey('esocial.s3000evtExclusao', 
        related_name='%(class)s_s3000_evtexclusao', )
    
    def evento(self): 
        return self.s3000_evtexclusao.evento()
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s3000_evtexclusao),
            unicode(self.cpftrab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta a identificação básica do trabalhador ao qual se refere o evento de remuneração.'
        db_table = r's3000_idetrabalhador'       
        managed = True # s3000_idetrabalhador #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s3000_idetrabalhador", "Can view s3000_idetrabalhador"), )
            
        ordering = [
            's3000_evtexclusao',
            'cpftrab',]



class s3000ideTrabalhadorSerializer(ModelSerializer):

    class Meta:
    
        model = s3000ideTrabalhador
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()