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
from emensageriapro.s2410.choices import *
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





class s2410homologTC(SoftDeletionModel):

    s2410_evtcdbenin = models.ForeignKey('esocial.s2410evtCdBenIn', 
        related_name='%(class)s_s2410_evtcdbenin', )
    
    def evento(self): 
        return self.s2410_evtcdbenin.evento()
    dthomol = models.DateField(null=True, )
    nratolegal = models.CharField(max_length=20, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2410_evtcdbenin), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta as informações de homologação do benefício pelo Tribunal de Contas'
        db_table = r's2410_homologtc'       
        managed = True # s2410_homologtc #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2410homologTC", u"Pode ver listagem do modelo S2410HOMOLOGTC"),
            ("can_see_data_s2410homologTC", u"Pode visualizar o conteúdo do modelo S2410HOMOLOGTC"),
            ("can_see_menu_s2410homologTC", u"Pode visualizar no menu o modelo S2410HOMOLOGTC"),
            ("can_print_list_s2410homologTC", u"Pode imprimir listagem do modelo S2410HOMOLOGTC"),
            ("can_print_data_s2410homologTC", u"Pode imprimir o conteúdo do modelo S2410HOMOLOGTC"), )
            
        ordering = [
            's2410_evtcdbenin',
            'dthomol',
            'nratolegal',]



class s2410homologTCSerializer(ModelSerializer):

    class Meta:
    
        model = s2410homologTC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2410infoPenMorte(SoftDeletionModel):

    s2410_evtcdbenin = models.ForeignKey('esocial.s2410evtCdBenIn', 
        related_name='%(class)s_s2410_evtcdbenin', )
    
    def evento(self): 
        return self.s2410_evtcdbenin.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2410_TPPENMORTE, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2410_evtcdbenin), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas a pensão por morte'
        db_table = r's2410_infopenmorte'       
        managed = True # s2410_infopenmorte #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2410infoPenMorte", u"Pode ver listagem do modelo S2410INFOPENMORTE"),
            ("can_see_data_s2410infoPenMorte", u"Pode visualizar o conteúdo do modelo S2410INFOPENMORTE"),
            ("can_see_menu_s2410infoPenMorte", u"Pode visualizar no menu o modelo S2410INFOPENMORTE"),
            ("can_print_list_s2410infoPenMorte", u"Pode imprimir listagem do modelo S2410INFOPENMORTE"),
            ("can_print_data_s2410infoPenMorte", u"Pode imprimir o conteúdo do modelo S2410INFOPENMORTE"), )
            
        ordering = [
            's2410_evtcdbenin',
            'tppenmorte',]



class s2410infoPenMorteSerializer(ModelSerializer):

    class Meta:
    
        model = s2410infoPenMorte
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2410instPenMorte(SoftDeletionModel):

    s2410_infopenmorte = models.ForeignKey('s2410.s2410infoPenMorte', 
        related_name='%(class)s_s2410_infopenmorte', )
    
    def evento(self): 
        return self.s2410_infopenmorte.evento()
    cpfinst = models.CharField(max_length=11, null=True, )
    dtinst = models.DateField(null=True, )
    intaposentado = models.CharField(choices=CHOICES_S2410_INTAPOSENTADO, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2410_infopenmorte), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do instituidor da pensão por morte'
        db_table = r's2410_instpenmorte'       
        managed = True # s2410_instpenmorte #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2410instPenMorte", u"Pode ver listagem do modelo S2410INSTPENMORTE"),
            ("can_see_data_s2410instPenMorte", u"Pode visualizar o conteúdo do modelo S2410INSTPENMORTE"),
            ("can_see_menu_s2410instPenMorte", u"Pode visualizar no menu o modelo S2410INSTPENMORTE"),
            ("can_print_list_s2410instPenMorte", u"Pode imprimir listagem do modelo S2410INSTPENMORTE"),
            ("can_print_data_s2410instPenMorte", u"Pode imprimir o conteúdo do modelo S2410INSTPENMORTE"), )
            
        ordering = [
            's2410_infopenmorte',
            'cpfinst',
            'dtinst',
            'intaposentado',]



class s2410instPenMorteSerializer(ModelSerializer):

    class Meta:
    
        model = s2410instPenMorte
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')