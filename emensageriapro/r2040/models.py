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
from emensageriapro.r2040.choices import *
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





class r2040infoProc(SoftDeletionModel):

    r2040_recursosrep = models.ForeignKey('r2040.r2040recursosRep', 
        related_name='%(class)s_r2040_recursosrep', )
    
    def evento(self): 
        return self.r2040_recursosrep.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2040_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2040_recursosrep),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.vlrnret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r2040_infoproc'       
        managed = True # r2040_infoproc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2040infoProc", u"Pode ver listagem do modelo R2040INFOPROC"),
            ("can_see_data_r2040infoProc", u"Pode visualizar o conteúdo do modelo R2040INFOPROC"),
            ("can_see_menu_r2040infoProc", u"Pode visualizar no menu o modelo R2040INFOPROC"),
            ("can_print_list_r2040infoProc", u"Pode imprimir listagem do modelo R2040INFOPROC"),
            ("can_print_data_r2040infoProc", u"Pode imprimir o conteúdo do modelo R2040INFOPROC"), )
            
        ordering = [
            'r2040_recursosrep',
            'tpproc',
            'nrproc',
            'vlrnret',]



class r2040infoProcSerializer(ModelSerializer):

    class Meta:
    
        model = r2040infoProc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class r2040infoRecurso(SoftDeletionModel):

    r2040_recursosrep = models.ForeignKey('r2040.r2040recursosRep', 
        related_name='%(class)s_r2040_recursosrep', )
    
    def evento(self): 
        return self.r2040_recursosrep.evento()
    tprepasse = models.IntegerField(choices=CHOICES_R2040_TPREPASSE, null=True, )
    descrecurso = models.CharField(max_length=20, null=True, )
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrretapur = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2040_recursosrep),
            unicode(self.tprepasse),
            unicode(self.descrecurso),
            unicode(self.vlrbruto),
            unicode(self.vlrretapur),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos recursos recebidos.'
        db_table = r'r2040_inforecurso'       
        managed = True # r2040_inforecurso #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2040infoRecurso", u"Pode ver listagem do modelo R2040INFORECURSO"),
            ("can_see_data_r2040infoRecurso", u"Pode visualizar o conteúdo do modelo R2040INFORECURSO"),
            ("can_see_menu_r2040infoRecurso", u"Pode visualizar no menu o modelo R2040INFORECURSO"),
            ("can_print_list_r2040infoRecurso", u"Pode imprimir listagem do modelo R2040INFORECURSO"),
            ("can_print_data_r2040infoRecurso", u"Pode imprimir o conteúdo do modelo R2040INFORECURSO"), )
            
        ordering = [
            'r2040_recursosrep',
            'tprepasse',
            'descrecurso',
            'vlrbruto',
            'vlrretapur',]



class r2040infoRecursoSerializer(ModelSerializer):

    class Meta:
    
        model = r2040infoRecurso
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class r2040recursosRep(SoftDeletionModel):

    r2040_evtassocdesprep = models.ForeignKey('efdreinf.r2040evtAssocDespRep', 
        related_name='%(class)s_r2040_evtassocdesprep', )
    
    def evento(self): 
        return self.r2040_evtassocdesprep.evento()
    cnpjassocdesp = models.CharField(max_length=14, null=True, )
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalnret = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2040_evtassocdesprep),
            unicode(self.cnpjassocdesp),
            unicode(self.vlrtotalrep),
            unicode(self.vlrtotalret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos repasses efetuados pelo estabelecimento indicado em {ideEstab} a Associação Desportiva que mantenha equipe de futebol profissional.'
        db_table = r'r2040_recursosrep'       
        managed = True # r2040_recursosrep #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2040recursosRep", u"Pode ver listagem do modelo R2040RECURSOSREP"),
            ("can_see_data_r2040recursosRep", u"Pode visualizar o conteúdo do modelo R2040RECURSOSREP"),
            ("can_see_menu_r2040recursosRep", u"Pode visualizar no menu o modelo R2040RECURSOSREP"),
            ("can_print_list_r2040recursosRep", u"Pode imprimir listagem do modelo R2040RECURSOSREP"),
            ("can_print_data_r2040recursosRep", u"Pode imprimir o conteúdo do modelo R2040RECURSOSREP"), )
            
        ordering = [
            'r2040_evtassocdesprep',
            'cnpjassocdesp',
            'vlrtotalrep',
            'vlrtotalret',]



class r2040recursosRepSerializer(ModelSerializer):

    class Meta:
    
        model = r2040recursosRep
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')