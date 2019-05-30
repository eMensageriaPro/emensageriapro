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
from emensageriapro.r9002.choices import *
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





class r9002infoTotal(SoftDeletionModel):

    r9002_evtret = models.ForeignKey('efdreinf.r9002evtRet', 
        related_name='%(class)s_r9002_evtret', )
    
    def evento(self): 
        return self.r9002_evtret.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_evtret),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas a totalizadores de bases e tributos'
        db_table = r'r9002_infototal'       
        managed = True # r9002_infototal #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_infototal", "Can view r9002_infototal"), )
            
        ordering = [
            'r9002_evtret',
            'tpinsc',
            'nrinsc',]



class r9002infoTotalSerializer(ModelSerializer):

    class Meta:
    
        model = r9002infoTotal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002regOcorrs(SoftDeletionModel):

    r9002_evtret = models.ForeignKey('efdreinf.r9002evtRet', 
        related_name='%(class)s_r9002_evtret', )
    
    def evento(self): 
        return self.r9002_evtret.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R9002_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_evtret),
            unicode(self.tpocorr),
            unicode(self.localerroaviso),
            unicode(self.codresp),
            unicode(self.dscresp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r9002_regocorrs'       
        managed = True # r9002_regocorrs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_regocorrs", "Can view r9002_regocorrs"), )
            
        ordering = [
            'r9002_evtret',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r9002regOcorrsSerializer(ModelSerializer):

    class Meta:
    
        model = r9002regOcorrs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002totApurDec(SoftDeletionModel):

    r9002_infototal = models.ForeignKey('r9002.r9002infoTotal', 
        related_name='%(class)s_r9002_infototal', )
    
    def evento(self): 
        return self.r9002_infototal.evento()
    perapurdec = models.IntegerField(choices=CHOICES_R9002_PERAPURDEC, null=True, )
    crdec = models.CharField(max_length=6, null=True, )
    vlrbasecrdec = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrdec = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrdecsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrdecsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_infototal),
            unicode(self.perapurdec),
            unicode(self.crdec),
            unicode(self.vlrbasecrdec),
            unicode(self.vlrcrdec),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração decendial'
        db_table = r'r9002_totapurdec'       
        managed = True # r9002_totapurdec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_totapurdec", "Can view r9002_totapurdec"), )
            
        ordering = [
            'r9002_infototal',
            'perapurdec',
            'crdec',
            'vlrbasecrdec',
            'vlrcrdec',]



class r9002totApurDecSerializer(ModelSerializer):

    class Meta:
    
        model = r9002totApurDec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002totApurDia(SoftDeletionModel):

    r9002_infototal = models.ForeignKey('r9002.r9002infoTotal', 
        related_name='%(class)s_r9002_infototal', )
    
    def evento(self): 
        return self.r9002_infototal.evento()
    perapurdia = models.IntegerField(null=True, )
    crdia = models.CharField(max_length=6, null=True, )
    vlrbasecrdia = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrdia = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrdiasusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrdiasusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_infototal),
            unicode(self.perapurdia),
            unicode(self.crdia),
            unicode(self.vlrbasecrdia),
            unicode(self.vlrcrdia),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração diário'
        db_table = r'r9002_totapurdia'       
        managed = True # r9002_totapurdia #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_totapurdia", "Can view r9002_totapurdia"), )
            
        ordering = [
            'r9002_infototal',
            'perapurdia',
            'crdia',
            'vlrbasecrdia',
            'vlrcrdia',]



class r9002totApurDiaSerializer(ModelSerializer):

    class Meta:
    
        model = r9002totApurDia
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002totApurMen(SoftDeletionModel):

    r9002_infototal = models.ForeignKey('r9002.r9002infoTotal', 
        related_name='%(class)s_r9002_infototal', )
    
    def evento(self): 
        return self.r9002_infototal.evento()
    crmen = models.CharField(max_length=6, null=True, )
    vlrbasecrmen = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrmen = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrmensusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrmensusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_infototal),
            unicode(self.crmen),
            unicode(self.vlrbasecrmen),
            unicode(self.vlrcrmen),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração mensal'
        db_table = r'r9002_totapurmen'       
        managed = True # r9002_totapurmen #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_totapurmen", "Can view r9002_totapurmen"), )
            
        ordering = [
            'r9002_infototal',
            'crmen',
            'vlrbasecrmen',
            'vlrcrmen',]



class r9002totApurMenSerializer(ModelSerializer):

    class Meta:
    
        model = r9002totApurMen
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002totApurQui(SoftDeletionModel):

    r9002_infototal = models.ForeignKey('r9002.r9002infoTotal', 
        related_name='%(class)s_r9002_infototal', )
    
    def evento(self): 
        return self.r9002_infototal.evento()
    perapurqui = models.IntegerField(choices=CHOICES_R9002_PERAPURQUI, null=True, )
    crqui = models.CharField(max_length=6, null=True, )
    vlrbasecrqui = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrqui = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrquisusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrquisusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_infototal),
            unicode(self.perapurqui),
            unicode(self.crqui),
            unicode(self.vlrbasecrqui),
            unicode(self.vlrcrqui),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração quinzenal'
        db_table = r'r9002_totapurqui'       
        managed = True # r9002_totapurqui #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_totapurqui", "Can view r9002_totapurqui"), )
            
        ordering = [
            'r9002_infototal',
            'perapurqui',
            'crqui',
            'vlrbasecrqui',
            'vlrcrqui',]



class r9002totApurQuiSerializer(ModelSerializer):

    class Meta:
    
        model = r9002totApurQui
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002totApurSem(SoftDeletionModel):

    r9002_infototal = models.ForeignKey('r9002.r9002infoTotal', 
        related_name='%(class)s_r9002_infototal', )
    
    def evento(self): 
        return self.r9002_infototal.evento()
    perapursem = models.IntegerField(null=True, )
    crsem = models.CharField(max_length=6, null=True, )
    vlrbasecrsem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrsem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrsemsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrsemsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9002_infototal),
            unicode(self.perapursem),
            unicode(self.crsem),
            unicode(self.vlrbasecrsem),
            unicode(self.vlrcrsem),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com apuração semanal'
        db_table = r'r9002_totapursem'       
        managed = True # r9002_totapursem #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_totapursem", "Can view r9002_totapursem"), )
            
        ordering = [
            'r9002_infototal',
            'perapursem',
            'crsem',
            'vlrbasecrsem',
            'vlrcrsem',]



class r9002totApurSemSerializer(ModelSerializer):

    class Meta:
    
        model = r9002totApurSem
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()