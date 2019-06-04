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
from emensageriapro.s1300.choices import *
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





class s1300contribSind(SoftDeletionModel):

    s1300_evtcontrsindpatr = models.ForeignKey('esocial.s1300evtContrSindPatr', 
        related_name='%(class)s_s1300_evtcontrsindpatr', )
    
    def evento(self): 
        return self.s1300_evtcontrsindpatr.evento()
    cnpjsindic = models.CharField(max_length=14, null=True, )
    tpcontribsind = models.IntegerField(choices=CHOICES_S1300_TPCONTRIBSIND, null=True, )
    vlrcontribsind = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1300_evtcontrsindpatr),
            unicode(self.cnpjsindic),
            unicode(self.tpcontribsind),
            unicode(self.vlrcontribsind),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da contribuição sindical patronal'
        db_table = r's1300_contribsind'       
        managed = True # s1300_contribsind #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1300contribSind", u"Pode ver listagem do modelo S1300CONTRIBSIND"),
            ("can_see_data_s1300contribSind", u"Pode visualizar o conteúdo do modelo S1300CONTRIBSIND"),
            ("can_see_menu_s1300contribSind", u"Pode visualizar no menu o modelo S1300CONTRIBSIND"),
            ("can_print_list_s1300contribSind", u"Pode imprimir listagem do modelo S1300CONTRIBSIND"),
            ("can_print_data_s1300contribSind", u"Pode imprimir o conteúdo do modelo S1300CONTRIBSIND"), )
            
        ordering = [
            's1300_evtcontrsindpatr',
            'cnpjsindic',
            'tpcontribsind',
            'vlrcontribsind',]



class s1300contribSindSerializer(ModelSerializer):

    class Meta:
    
        model = s1300contribSind
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()