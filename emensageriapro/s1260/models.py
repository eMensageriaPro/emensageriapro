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
from emensageriapro.s1260.choices import *
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





class s1260ideAdquir(SoftDeletionModel):

    s1260_tpcomerc = models.ForeignKey('s1260.s1260tpComerc', 
        related_name='%(class)s_s1260_tpcomerc', )
    
    def evento(self): 
        return self.s1260_tpcomerc.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    vrcomerc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Identificação dos Adquirentes da Produção.'
        db_table = r's1260_ideadquir'       
        managed = True # s1260_ideadquir #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1260ideAdquir", u"Pode ver listagem do modelo S1260IDEADQUIR"),
            ("can_see_data_s1260ideAdquir", u"Pode visualizar o conteúdo do modelo S1260IDEADQUIR"),
            ("can_see_menu_s1260ideAdquir", u"Pode visualizar no menu o modelo S1260IDEADQUIR"),
            ("can_print_list_s1260ideAdquir", u"Pode imprimir listagem do modelo S1260IDEADQUIR"),
            ("can_print_data_s1260ideAdquir", u"Pode imprimir o conteúdo do modelo S1260IDEADQUIR"), )
            
        ordering = [
            's1260_tpcomerc',
            'tpinsc',
            'nrinsc',
            'vrcomerc',]



class s1260ideAdquirSerializer(ModelSerializer):

    class Meta:
    
        model = s1260ideAdquir
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1260infoProcJud(SoftDeletionModel):

    s1260_tpcomerc = models.ForeignKey('s1260.s1260tpComerc', 
        related_name='%(class)s_s1260_tpcomerc', )
    
    def evento(self): 
        return self.s1260_tpcomerc.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1260_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(null=True, )
    vrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrratsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro preenchido quando o Produtor Rural (pessoa física ou segurado especial), identificado em {ideProdutor}, ou o próprio declarante, possuir processo judicial com decisão/sentença determinando a não retenção, pelo adquirente, das contribuições incidentes sobre a aquisição de produção.'
        db_table = r's1260_infoprocjud'       
        managed = True # s1260_infoprocjud #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1260infoProcJud", u"Pode ver listagem do modelo S1260INFOPROCJUD"),
            ("can_see_data_s1260infoProcJud", u"Pode visualizar o conteúdo do modelo S1260INFOPROCJUD"),
            ("can_see_menu_s1260infoProcJud", u"Pode visualizar no menu o modelo S1260INFOPROCJUD"),
            ("can_print_list_s1260infoProcJud", u"Pode imprimir listagem do modelo S1260INFOPROCJUD"),
            ("can_print_data_s1260infoProcJud", u"Pode imprimir o conteúdo do modelo S1260INFOPROCJUD"), )
            
        ordering = [
            's1260_tpcomerc',
            'tpproc',
            'nrproc',
            'codsusp',]



class s1260infoProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = s1260infoProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1260nfs(SoftDeletionModel):

    s1260_ideadquir = models.ForeignKey('s1260.s1260ideAdquir', 
        related_name='%(class)s_s1260_ideadquir', )
    
    def evento(self): 
        return self.s1260_ideadquir.evento()
    serie = models.CharField(max_length=5, blank=True, null=True, )
    nrdocto = models.CharField(max_length=20, null=True, )
    dtemisnf = models.DateField(null=True, )
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Detalhamento das notas fiscais relativas a aquisição de produção do produtor rural identificado no registro superior, não sendo obrigatório nas aquisições de produção de pessoa física/segurado especial.'
        db_table = r's1260_nfs'       
        managed = True # s1260_nfs #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1260nfs", u"Pode ver listagem do modelo S1260NFS"),
            ("can_see_data_s1260nfs", u"Pode visualizar o conteúdo do modelo S1260NFS"),
            ("can_see_menu_s1260nfs", u"Pode visualizar no menu o modelo S1260NFS"),
            ("can_print_list_s1260nfs", u"Pode imprimir listagem do modelo S1260NFS"),
            ("can_print_data_s1260nfs", u"Pode imprimir o conteúdo do modelo S1260NFS"), )
            
        ordering = [
            's1260_ideadquir',
            'nrdocto',
            'dtemisnf',
            'vlrbruto',
            'vrcpdescpr',
            'vrratdescpr',
            'vrsenardesc',]



class s1260nfsSerializer(ModelSerializer):

    class Meta:
    
        model = s1260nfs
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1260tpComerc(SoftDeletionModel):

    s1260_evtcomprod = models.ForeignKey('esocial.s1260evtComProd', 
        related_name='%(class)s_s1260_evtcomprod', )
    
    def evento(self): 
        return self.s1260_evtcomprod.evento()
    indcomerc = models.IntegerField(choices=CHOICES_S1260_INDCOMERC, null=True, )
    vrtotcom = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta o valor total da comercialização por 'tipo' de comercialização'
        db_table = r's1260_tpcomerc'       
        managed = True # s1260_tpcomerc #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1260tpComerc", u"Pode ver listagem do modelo S1260TPCOMERC"),
            ("can_see_data_s1260tpComerc", u"Pode visualizar o conteúdo do modelo S1260TPCOMERC"),
            ("can_see_menu_s1260tpComerc", u"Pode visualizar no menu o modelo S1260TPCOMERC"),
            ("can_print_list_s1260tpComerc", u"Pode imprimir listagem do modelo S1260TPCOMERC"),
            ("can_print_data_s1260tpComerc", u"Pode imprimir o conteúdo do modelo S1260TPCOMERC"), )
            
        ordering = [
            's1260_evtcomprod',
            'indcomerc',
            'vrtotcom',]



class s1260tpComercSerializer(ModelSerializer):

    class Meta:
    
        model = s1260tpComerc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')