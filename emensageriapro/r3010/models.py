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
from emensageriapro.r3010.choices import *
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





class r3010boletim(SoftDeletionModel):

    r3010_evtespdesportivo = models.ForeignKey('efdreinf.r3010evtEspDesportivo', 
        related_name='%(class)s_r3010_evtespdesportivo', )
    
    def evento(self): 
        return self.r3010_evtespdesportivo.evento()
    nrboletim = models.CharField(max_length=4, null=True, )
    tpcompeticao = models.IntegerField(choices=CHOICES_R3010_TPCOMPETICAO, null=True, )
    categevento = models.IntegerField(choices=CHOICES_R3010_CATEGEVENTO, null=True, )
    moddesportiva = models.CharField(max_length=100, null=True, )
    nomecompeticao = models.CharField(max_length=100, null=True, )
    cnpjmandante = models.CharField(max_length=14, null=True, )
    cnpjvisitante = models.CharField(max_length=14, blank=True, null=True, )
    nomevisitante = models.CharField(max_length=80, blank=True, null=True, )
    pracadesportiva = models.CharField(max_length=100, null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    qtdepagantes = models.IntegerField(null=True, )
    qtdenaopagantes = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r3010_evtespdesportivo),
            unicode(self.nrboletim),
            unicode(self.tpcompeticao),
            unicode(self.categevento),
            unicode(self.moddesportiva),
            unicode(self.nomecompeticao),
            unicode(self.cnpjmandante),
            unicode(self.pracadesportiva),
            unicode(self.uf),
            unicode(self.qtdepagantes),
            unicode(self.qtdenaopagantes),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Boletim do Espetáculo Desportivo'
        db_table = r'r3010_boletim'       
        managed = True # r3010_boletim #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r3010_boletim", "Can view r3010_boletim"), )
            
        ordering = [
            'r3010_evtespdesportivo',
            'nrboletim',
            'tpcompeticao',
            'categevento',
            'moddesportiva',
            'nomecompeticao',
            'cnpjmandante',
            'pracadesportiva',
            'uf',
            'qtdepagantes',
            'qtdenaopagantes',]



class r3010boletimSerializer(ModelSerializer):

    class Meta:
    
        model = r3010boletim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r3010infoProc(SoftDeletionModel):

    r3010_evtespdesportivo = models.ForeignKey('efdreinf.r3010evtEspDesportivo', 
        related_name='%(class)s_r3010_evtespdesportivo', )
    
    def evento(self): 
        return self.r3010_evtespdesportivo.evento()
    tpproc = models.IntegerField(choices=CHOICES_R3010_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r3010_evtespdesportivo),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.vlrcpsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r3010_infoproc'       
        managed = True # r3010_infoproc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r3010_infoproc", "Can view r3010_infoproc"), )
            
        ordering = [
            'r3010_evtespdesportivo',
            'tpproc',
            'nrproc',
            'vlrcpsusp',]



class r3010infoProcSerializer(ModelSerializer):

    class Meta:
    
        model = r3010infoProc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r3010outrasReceitas(SoftDeletionModel):

    r3010_boletim = models.ForeignKey('r3010.r3010boletim', 
        related_name='%(class)s_r3010_boletim', )
    
    def evento(self): 
        return self.r3010_boletim.evento()
    tpreceita = models.IntegerField(choices=CHOICES_R3010_TPRECEITA, null=True, )
    vlrreceita = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    descreceita = models.CharField(max_length=20, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r3010_boletim),
            unicode(self.tpreceita),
            unicode(self.vlrreceita),
            unicode(self.descreceita),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Outras receitas do espetáculo'
        db_table = r'r3010_outrasreceitas'       
        managed = True # r3010_outrasreceitas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r3010_outrasreceitas", "Can view r3010_outrasreceitas"), )
            
        ordering = [
            'r3010_boletim',
            'tpreceita',
            'vlrreceita',
            'descreceita',]



class r3010outrasReceitasSerializer(ModelSerializer):

    class Meta:
    
        model = r3010outrasReceitas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r3010receitaIngressos(SoftDeletionModel):

    r3010_boletim = models.ForeignKey('r3010.r3010boletim', 
        related_name='%(class)s_r3010_boletim', )
    
    def evento(self): 
        return self.r3010_boletim.evento()
    tpingresso = models.IntegerField(choices=CHOICES_R3010_TPINGRESSO, null=True, )
    descingr = models.CharField(max_length=30, null=True, )
    qtdeingrvenda = models.IntegerField(null=True, )
    qtdeingrvendidos = models.IntegerField(null=True, )
    qtdeingrdev = models.IntegerField(null=True, )
    precoindiv = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r3010_boletim),
            unicode(self.tpingresso),
            unicode(self.descingr),
            unicode(self.qtdeingrvenda),
            unicode(self.qtdeingrvendidos),
            unicode(self.qtdeingrdev),
            unicode(self.precoindiv),
            unicode(self.vlrtotal),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Receita da Venda de Ingressos'
        db_table = r'r3010_receitaingressos'       
        managed = True # r3010_receitaingressos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r3010_receitaingressos", "Can view r3010_receitaingressos"), )
            
        ordering = [
            'r3010_boletim',
            'tpingresso',
            'descingr',
            'qtdeingrvenda',
            'qtdeingrvendidos',
            'qtdeingrdev',
            'precoindiv',
            'vlrtotal',]



class r3010receitaIngressosSerializer(ModelSerializer):

    class Meta:
    
        model = r3010receitaIngressos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()