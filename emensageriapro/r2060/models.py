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
from emensageriapro.r2060.choices import *
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





class r2060infoProc(SoftDeletionModel):

    r2060_tipocod = models.ForeignKey('r2060.r2060tipoCod', 
        related_name='%(class)s_r2060_tipocod', )
    
    def evento(self): 
        return self.r2060_tipocod.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2060_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2060_tipocod),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.vlrcprbsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r2060_infoproc'       
        managed = True # r2060_infoproc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2060_infoproc", "Can view r2060_infoproc"), )
            
        ordering = [
            'r2060_tipocod',
            'tpproc',
            'nrproc',
            'vlrcprbsusp',]



class r2060infoProcSerializer(ModelSerializer):

    class Meta:
    
        model = r2060infoProc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2060tipoAjuste(SoftDeletionModel):

    r2060_tipocod = models.ForeignKey('r2060.r2060tipoCod', 
        related_name='%(class)s_r2060_tipocod', )
    
    def evento(self): 
        return self.r2060_tipocod.evento()
    tpajuste = models.IntegerField(choices=CHOICES_R2060_TPAJUSTE, null=True, )
    codajuste = models.IntegerField(choices=CHOICES_R2060_CODAJUSTE, null=True, )
    vlrajuste = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    descajuste = models.CharField(max_length=20, null=True, )
    dtajuste = models.CharField(max_length=7, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2060_tipocod),
            unicode(self.tpajuste),
            unicode(self.codajuste),
            unicode(self.vlrajuste),
            unicode(self.descajuste),
            unicode(self.dtajuste),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro a ser preenchido caso a pessoa jurídica tenha de proceder a ajustes da contribuição apurada no período, decorrentes da legislação tributária da contribuição, de estorno ou de outras situações.'
        db_table = r'r2060_tipoajuste'       
        managed = True # r2060_tipoajuste #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2060_tipoajuste", "Can view r2060_tipoajuste"), )
            
        ordering = [
            'r2060_tipocod',
            'tpajuste',
            'codajuste',
            'vlrajuste',
            'descajuste',
            'dtajuste',]



class r2060tipoAjusteSerializer(ModelSerializer):

    class Meta:
    
        model = r2060tipoAjuste
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2060tipoCod(SoftDeletionModel):

    r2060_evtcprb = models.ForeignKey('efdreinf.r2060evtCPRB', 
        related_name='%(class)s_r2060_evtcprb', )
    
    def evento(self): 
        return self.r2060_evtcprb.evento()
    codativecon = models.TextField(null=True, )
    vlrrecbrutaativ = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrexcrecbruta = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlradicrecbruta = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbccprb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcprbapur = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    observ = models.CharField(max_length=200, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2060_evtcprb),
            unicode(self.codativecon),
            unicode(self.vlrrecbrutaativ),
            unicode(self.vlrexcrecbruta),
            unicode(self.vlradicrecbruta),
            unicode(self.vlrbccprb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta o valor total da receita por tipo de código de atividade econômica.'
        db_table = r'r2060_tipocod'       
        managed = True # r2060_tipocod #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2060_tipocod", "Can view r2060_tipocod"), )
            
        ordering = [
            'r2060_evtcprb',
            'codativecon',
            'vlrrecbrutaativ',
            'vlrexcrecbruta',
            'vlradicrecbruta',
            'vlrbccprb',]



class r2060tipoCodSerializer(ModelSerializer):

    class Meta:
    
        model = r2060tipoCod
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()