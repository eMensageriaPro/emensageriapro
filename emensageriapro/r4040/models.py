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
from emensageriapro.r4040.choices import *
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





class r4040ideNat(SoftDeletionModel):

    r4040_evtbenefnid = models.ForeignKey('efdreinf.r4040evtBenefNId', 
        related_name='%(class)s_r4040_evtbenefnid', )
    
    def evento(self): 
        return self.r4040_evtbenefnid.evento()
    natrendim = models.IntegerField(choices=CHOICES_R4040_NATRENDIM, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4040_evtbenefnid),
            unicode(self.natrendim),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação da natureza do rendimento'
        db_table = r'r4040_idenat'       
        managed = True # r4040_idenat #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4040_idenat", "Can view r4040_idenat"), )
            
        ordering = [
            'r4040_evtbenefnid',
            'natrendim',]



class r4040ideNatSerializer(ModelSerializer):

    class Meta:
    
        model = r4040ideNat
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4040infoPgto(SoftDeletionModel):

    r4040_idenat = models.ForeignKey('r4040.r4040ideNat', 
        related_name='%(class)s_r4040_idenat', )
    
    def evento(self): 
        return self.r4040_idenat.evento()
    dtfg = models.DateField(null=True, )
    vlrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrreaj = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrir = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    descr = models.CharField(max_length=200, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4040_idenat),
            unicode(self.dtfg),
            unicode(self.vlrliq),
            unicode(self.vlrreaj),
            unicode(self.vlrir),
            unicode(self.descr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Pagamento'
        db_table = r'r4040_infopgto'       
        managed = True # r4040_infopgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4040_infopgto", "Can view r4040_infopgto"), )
            
        ordering = [
            'r4040_idenat',
            'dtfg',
            'vlrliq',
            'vlrreaj',
            'vlrir',
            'descr',]



class r4040infoPgtoSerializer(ModelSerializer):

    class Meta:
    
        model = r4040infoPgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()