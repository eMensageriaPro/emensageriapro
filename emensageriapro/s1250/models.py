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
from emensageriapro.s1250.choices import *
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





class s1250ideProdutor(SoftDeletionModel):

    s1250_tpaquis = models.ForeignKey('s1250.s1250tpAquis', 
        related_name='%(class)s_s1250_tpaquis', )
    
    def evento(self): 
        return self.s1250_tpaquis.evento()
    tpinscprod = models.IntegerField(null=True, )
    nrinscprod = models.CharField(max_length=14, null=True, )
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    indopccp = models.IntegerField(choices=CHOICES_S1250_INDOPCCP, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro que identifica os produtores rurais dos quais foi efetuada aquisição da produção pelo contribuinte declarante.'
        db_table = r's1250_ideprodutor'       
        managed = True # s1250_ideprodutor #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250ideProdutor", u"Pode ver listagem do modelo S1250IDEPRODUTOR"),
            ("can_see_data_s1250ideProdutor", u"Pode visualizar o conteúdo do modelo S1250IDEPRODUTOR"),
            ("can_see_menu_s1250ideProdutor", u"Pode visualizar no menu o modelo S1250IDEPRODUTOR"),
            ("can_print_list_s1250ideProdutor", u"Pode imprimir listagem do modelo S1250IDEPRODUTOR"),
            ("can_print_data_s1250ideProdutor", u"Pode imprimir o conteúdo do modelo S1250IDEPRODUTOR"), )
            
        ordering = [
            's1250_tpaquis',
            'tpinscprod',
            'nrinscprod',
            'vlrbruto',
            'vrcpdescpr',
            'vrratdescpr',
            'vrsenardesc',
            'indopccp',]



class s1250ideProdutorSerializer(ModelSerializer):

    class Meta:
    
        model = s1250ideProdutor
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1250infoProcJ(SoftDeletionModel):

    s1250_tpaquis = models.ForeignKey('s1250.s1250tpAquis', 
        related_name='%(class)s_s1250_tpaquis', )
    
    def evento(self): 
        return self.s1250_tpaquis.evento()
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro preenchido quando houver processo judicial do adquirente ou de terceiros e que abranja a totalidade dos produtores identificados em {ideProdutor} com decisão/sentença determinando a não retenção pelo adquirente, das contribuições incidentes sobre a aquisição de produção.'
        db_table = r's1250_infoprocj'       
        managed = True # s1250_infoprocj #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250infoProcJ", u"Pode ver listagem do modelo S1250INFOPROCJ"),
            ("can_see_data_s1250infoProcJ", u"Pode visualizar o conteúdo do modelo S1250INFOPROCJ"),
            ("can_see_menu_s1250infoProcJ", u"Pode visualizar no menu o modelo S1250INFOPROCJ"),
            ("can_print_list_s1250infoProcJ", u"Pode imprimir listagem do modelo S1250INFOPROCJ"),
            ("can_print_data_s1250infoProcJ", u"Pode imprimir o conteúdo do modelo S1250INFOPROCJ"), )
            
        ordering = [
            's1250_tpaquis',
            'nrprocjud',
            'codsusp',
            'vrcpnret',
            'vrratnret',
            'vrsenarnret',]



class s1250infoProcJSerializer(ModelSerializer):

    class Meta:
    
        model = s1250infoProcJ
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1250infoProcJud(SoftDeletionModel):

    s1250_ideprodutor = models.ForeignKey('s1250.s1250ideProdutor', 
        related_name='%(class)s_s1250_ideprodutor', )
    
    def evento(self): 
        return self.s1250_ideprodutor.evento()
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro preenchido quando o Produtor Rural (pessoa física ou segurado especial), identificado em {ideProdutor}, ou o próprio declarante, possuir processo judicial com decisão/sentença determinando a não retenção, pelo adquirente, das contribuições incidentes sobre a aquisição de produção.'
        db_table = r's1250_infoprocjud'       
        managed = True # s1250_infoprocjud #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250infoProcJud", u"Pode ver listagem do modelo S1250INFOPROCJUD"),
            ("can_see_data_s1250infoProcJud", u"Pode visualizar o conteúdo do modelo S1250INFOPROCJUD"),
            ("can_see_menu_s1250infoProcJud", u"Pode visualizar no menu o modelo S1250INFOPROCJUD"),
            ("can_print_list_s1250infoProcJud", u"Pode imprimir listagem do modelo S1250INFOPROCJUD"),
            ("can_print_data_s1250infoProcJud", u"Pode imprimir o conteúdo do modelo S1250INFOPROCJUD"), )
            
        ordering = [
            's1250_ideprodutor',
            'nrprocjud',
            'codsusp',
            'vrcpnret',
            'vrratnret',
            'vrsenarnret',]



class s1250infoProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = s1250infoProcJud
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1250nfs(SoftDeletionModel):

    s1250_ideprodutor = models.ForeignKey('s1250.s1250ideProdutor', 
        related_name='%(class)s_s1250_ideprodutor', )
    
    def evento(self): 
        return self.s1250_ideprodutor.evento()
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
        db_table = r's1250_nfs'       
        managed = True # s1250_nfs #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250nfs", u"Pode ver listagem do modelo S1250NFS"),
            ("can_see_data_s1250nfs", u"Pode visualizar o conteúdo do modelo S1250NFS"),
            ("can_see_menu_s1250nfs", u"Pode visualizar no menu o modelo S1250NFS"),
            ("can_print_list_s1250nfs", u"Pode imprimir listagem do modelo S1250NFS"),
            ("can_print_data_s1250nfs", u"Pode imprimir o conteúdo do modelo S1250NFS"), )
            
        ordering = [
            's1250_ideprodutor',
            'nrdocto',
            'dtemisnf',
            'vlrbruto',
            'vrcpdescpr',
            'vrratdescpr',
            'vrsenardesc',]



class s1250nfsSerializer(ModelSerializer):

    class Meta:
    
        model = s1250nfs
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1250tpAquis(SoftDeletionModel):

    s1250_evtaqprod = models.ForeignKey('esocial.s1250evtAqProd', 
        related_name='%(class)s_s1250_evtaqprod', )
    
    def evento(self): 
        return self.s1250_evtaqprod.evento()
    indaquis = models.IntegerField(choices=CHOICES_S1250_INDAQUIS, null=True, )
    vlrtotaquis = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro preenchido por Pessoa Jurídica em geral, quando o estabelecimento identificado no registro superior efetuar aquisição de produtos rurais de pessoa física'
        db_table = r's1250_tpaquis'       
        managed = True # s1250_tpaquis #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250tpAquis", u"Pode ver listagem do modelo S1250TPAQUIS"),
            ("can_see_data_s1250tpAquis", u"Pode visualizar o conteúdo do modelo S1250TPAQUIS"),
            ("can_see_menu_s1250tpAquis", u"Pode visualizar no menu o modelo S1250TPAQUIS"),
            ("can_print_list_s1250tpAquis", u"Pode imprimir listagem do modelo S1250TPAQUIS"),
            ("can_print_data_s1250tpAquis", u"Pode imprimir o conteúdo do modelo S1250TPAQUIS"), )
            
        ordering = [
            's1250_evtaqprod',
            'indaquis',
            'vlrtotaquis',]



class s1250tpAquisSerializer(ModelSerializer):

    class Meta:
    
        model = s1250tpAquis
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')