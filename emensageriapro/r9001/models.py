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
from emensageriapro.r9001.choices import *
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





class r9001RCPRB(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    crcprb = models.IntegerField(null=True, )
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.crcprb),
            unicode(self.vlrcrcprb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB, apuradas no evento R-2060'
        db_table = r'r9001_rcprb'       
        managed = True # r9001_rcprb #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RCPRB", u"Pode ver listagem do modelo R9001RCPRB"),
            ("can_see_data_r9001RCPRB", u"Pode visualizar o conteúdo do modelo R9001RCPRB"),
            ("can_see_menu_r9001RCPRB", u"Pode visualizar no menu o modelo R9001RCPRB"),
            ("can_print_list_r9001RCPRB", u"Pode imprimir listagem do modelo R9001RCPRB"),
            ("can_print_data_r9001RCPRB", u"Pode imprimir o conteúdo do modelo R9001RCPRB"), )
            
        ordering = [
            'r9001_infototal',
            'crcprb',
            'vlrcrcprb',]



class r9001RCPRBSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RCPRB
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001RComl(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    crcoml = models.IntegerField(null=True, )
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.crcoml),
            unicode(self.vlrcrcoml),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria, apuradas no evento R-2050'
        db_table = r'r9001_rcoml'       
        managed = True # r9001_rcoml #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RComl", u"Pode ver listagem do modelo R9001RCOML"),
            ("can_see_data_r9001RComl", u"Pode visualizar o conteúdo do modelo R9001RCOML"),
            ("can_see_menu_r9001RComl", u"Pode visualizar no menu o modelo R9001RCOML"),
            ("can_print_list_r9001RComl", u"Pode imprimir listagem do modelo R9001RCOML"),
            ("can_print_data_r9001RComl", u"Pode imprimir o conteúdo do modelo R9001RCOML"), )
            
        ordering = [
            'r9001_infototal',
            'crcoml',
            'vlrcrcoml',]



class r9001RComlSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RComl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001RPrest(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    tpinsctomador = models.IntegerField(null=True, )
    nrinsctomador = models.CharField(max_length=14, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.tpinsctomador),
            unicode(self.nrinsctomador),
            unicode(self.vlrtotalbaseret),
            unicode(self.vlrtotalretprinc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados, apuradas no evento R-2020'
        db_table = r'r9001_rprest'       
        managed = True # r9001_rprest #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RPrest", u"Pode ver listagem do modelo R9001RPREST"),
            ("can_see_data_r9001RPrest", u"Pode visualizar o conteúdo do modelo R9001RPREST"),
            ("can_see_menu_r9001RPrest", u"Pode visualizar no menu o modelo R9001RPREST"),
            ("can_print_list_r9001RPrest", u"Pode imprimir listagem do modelo R9001RPREST"),
            ("can_print_data_r9001RPrest", u"Pode imprimir o conteúdo do modelo R9001RPREST"), )
            
        ordering = [
            'r9001_infototal',
            'tpinsctomador',
            'nrinsctomador',
            'vlrtotalbaseret',
            'vlrtotalretprinc',]



class r9001RPrestSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RPrest
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001RRecEspetDesp(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    crrecespetdesp = models.IntegerField(null=True, )
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecespetdesp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecespetdespsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.crrecespetdesp),
            unicode(self.vlrreceitatotal),
            unicode(self.vlrcrrecespetdesp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador da contribuição previdenciária incidente sobre Receitas de Espetáculos Desportivos, apuradas no evento R-3010.'
        db_table = r'r9001_rrecespetdesp'       
        managed = True # r9001_rrecespetdesp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RRecEspetDesp", u"Pode ver listagem do modelo R9001RRECESPETDESP"),
            ("can_see_data_r9001RRecEspetDesp", u"Pode visualizar o conteúdo do modelo R9001RRECESPETDESP"),
            ("can_see_menu_r9001RRecEspetDesp", u"Pode visualizar no menu o modelo R9001RRECESPETDESP"),
            ("can_print_list_r9001RRecEspetDesp", u"Pode imprimir listagem do modelo R9001RRECESPETDESP"),
            ("can_print_data_r9001RRecEspetDesp", u"Pode imprimir o conteúdo do modelo R9001RRECESPETDESP"), )
            
        ordering = [
            'r9001_infototal',
            'crrecespetdesp',
            'vlrreceitatotal',
            'vlrcrrecespetdesp',]



class r9001RRecEspetDespSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RRecEspetDesp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001RRecRepAD(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    cnpjassocdesp = models.CharField(max_length=14, null=True, )
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    crrecrepad = models.IntegerField(null=True, )
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.cnpjassocdesp),
            unicode(self.vlrtotalrep),
            unicode(self.crrecrepad),
            unicode(self.vlrcrrecrepad),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associações Desportivas que mantenham equipe de futebol profissional, apuradas no evento R-2040'
        db_table = r'r9001_rrecrepad'       
        managed = True # r9001_rrecrepad #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RRecRepAD", u"Pode ver listagem do modelo R9001RRECREPAD"),
            ("can_see_data_r9001RRecRepAD", u"Pode visualizar o conteúdo do modelo R9001RRECREPAD"),
            ("can_see_menu_r9001RRecRepAD", u"Pode visualizar no menu o modelo R9001RRECREPAD"),
            ("can_print_list_r9001RRecRepAD", u"Pode imprimir listagem do modelo R9001RRECREPAD"),
            ("can_print_data_r9001RRecRepAD", u"Pode imprimir o conteúdo do modelo R9001RRECREPAD"), )
            
        ordering = [
            'r9001_infototal',
            'cnpjassocdesp',
            'vlrtotalrep',
            'crrecrepad',
            'vlrcrrecrepad',]



class r9001RRecRepADSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RRecRepAD
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001RTom(SoftDeletionModel):

    r9001_infototal = models.ForeignKey('r9001.r9001infoTotal', 
        related_name='%(class)s_r9001_infototal', )
    
    def evento(self): 
        return self.r9001_infototal.evento()
    cnpjprestador = models.CharField(max_length=14, null=True, )
    cno = models.CharField(max_length=12, blank=True, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_infototal),
            unicode(self.cnpjprestador),
            unicode(self.vlrtotalbaseret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados, apuradas no evento R-2010'
        db_table = r'r9001_rtom'       
        managed = True # r9001_rtom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001RTom", u"Pode ver listagem do modelo R9001RTOM"),
            ("can_see_data_r9001RTom", u"Pode visualizar o conteúdo do modelo R9001RTOM"),
            ("can_see_menu_r9001RTom", u"Pode visualizar no menu o modelo R9001RTOM"),
            ("can_print_list_r9001RTom", u"Pode imprimir listagem do modelo R9001RTOM"),
            ("can_print_data_r9001RTom", u"Pode imprimir o conteúdo do modelo R9001RTOM"), )
            
        ordering = [
            'r9001_infototal',
            'cnpjprestador',
            'vlrtotalbaseret',]



class r9001RTomSerializer(ModelSerializer):

    class Meta:
    
        model = r9001RTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001infoCRTom(SoftDeletionModel):

    r9001_rtom = models.ForeignKey('r9001.r9001RTom', 
        related_name='%(class)s_r9001_rtom', )
    
    def evento(self): 
        return self.r9001_rtom.evento()
    crtom = models.IntegerField(null=True, )
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_rtom),
            unicode(self.crtom),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados'
        db_table = r'r9001_infocrtom'       
        managed = True # r9001_infocrtom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001infoCRTom", u"Pode ver listagem do modelo R9001INFOCRTOM"),
            ("can_see_data_r9001infoCRTom", u"Pode visualizar o conteúdo do modelo R9001INFOCRTOM"),
            ("can_see_menu_r9001infoCRTom", u"Pode visualizar no menu o modelo R9001INFOCRTOM"),
            ("can_print_list_r9001infoCRTom", u"Pode imprimir listagem do modelo R9001INFOCRTOM"),
            ("can_print_data_r9001infoCRTom", u"Pode imprimir o conteúdo do modelo R9001INFOCRTOM"), )
            
        ordering = [
            'r9001_rtom',
            'crtom',]



class r9001infoCRTomSerializer(ModelSerializer):

    class Meta:
    
        model = r9001infoCRTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001infoTotal(SoftDeletionModel):

    r9001_evttotal = models.ForeignKey('efdreinf.r9001evtTotal', 
        related_name='%(class)s_r9001_evttotal', )
    
    def evento(self): 
        return self.r9001_evttotal.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_evttotal),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas a totalizadores de bases e tributos'
        db_table = r'r9001_infototal'       
        managed = True # r9001_infototal #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001infoTotal", u"Pode ver listagem do modelo R9001INFOTOTAL"),
            ("can_see_data_r9001infoTotal", u"Pode visualizar o conteúdo do modelo R9001INFOTOTAL"),
            ("can_see_menu_r9001infoTotal", u"Pode visualizar no menu o modelo R9001INFOTOTAL"),
            ("can_print_list_r9001infoTotal", u"Pode imprimir listagem do modelo R9001INFOTOTAL"),
            ("can_print_data_r9001infoTotal", u"Pode imprimir o conteúdo do modelo R9001INFOTOTAL"), )
            
        ordering = [
            'r9001_evttotal',
            'tpinsc',
            'nrinsc',]



class r9001infoTotalSerializer(ModelSerializer):

    class Meta:
    
        model = r9001infoTotal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001regOcorrs(SoftDeletionModel):

    r9001_evttotal = models.ForeignKey('efdreinf.r9001evtTotal', 
        related_name='%(class)s_r9001_evttotal', )
    
    def evento(self): 
        return self.r9001_evttotal.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R9001_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9001_evttotal),
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
        db_table = r'r9001_regocorrs'       
        managed = True # r9001_regocorrs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001regOcorrs", u"Pode ver listagem do modelo R9001REGOCORRS"),
            ("can_see_data_r9001regOcorrs", u"Pode visualizar o conteúdo do modelo R9001REGOCORRS"),
            ("can_see_menu_r9001regOcorrs", u"Pode visualizar no menu o modelo R9001REGOCORRS"),
            ("can_print_list_r9001regOcorrs", u"Pode imprimir listagem do modelo R9001REGOCORRS"),
            ("can_print_data_r9001regOcorrs", u"Pode imprimir o conteúdo do modelo R9001REGOCORRS"), )
            
        ordering = [
            'r9001_evttotal',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r9001regOcorrsSerializer(ModelSerializer):

    class Meta:
    
        model = r9001regOcorrs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()