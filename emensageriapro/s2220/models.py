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
from emensageriapro.s2220.choices import *
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





class s2220exame(SoftDeletionModel):

    s2220_evtmonit = models.ForeignKey('esocial.s2220evtMonit', 
        related_name='%(class)s_s2220_evtmonit', )
    
    def evento(self): 
        return self.s2220_evtmonit.evento()
    dtexm = models.DateField(null=True, )
    procrealizado = models.IntegerField(null=True, )
    obsproc = models.CharField(max_length=999, blank=True, null=True, )
    interprexm = models.IntegerField(choices=CHOICES_S2220_INTERPREXM, null=True, )
    ordexame = models.IntegerField(choices=CHOICES_S2220_ORDEXAME, null=True, )
    dtinimonit = models.DateField(null=True, )
    dtfimmonit = models.DateField(blank=True, null=True, )
    indresult = models.IntegerField(choices=CHOICES_S2220_INDRESULT, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro que detalha os exames complementares porventura realizados pelo trabalhador em virtude do determinado no Quadro II da NR 07 do MTE, além de outros solicitados pelo médico e os referentes ao ASO'
        db_table = r's2220_exame'       
        managed = True # s2220_exame #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2220exame", u"Pode ver listagem do modelo S2220EXAME"),
            ("can_see_data_s2220exame", u"Pode visualizar o conteúdo do modelo S2220EXAME"),
            ("can_see_menu_s2220exame", u"Pode visualizar no menu o modelo S2220EXAME"),
            ("can_print_list_s2220exame", u"Pode imprimir listagem do modelo S2220EXAME"),
            ("can_print_data_s2220exame", u"Pode imprimir o conteúdo do modelo S2220EXAME"), )
            
        ordering = [
            's2220_evtmonit',
            'dtexm',
            'procrealizado',
            'interprexm',
            'ordexame',
            'dtinimonit',]



class s2220exameSerializer(ModelSerializer):

    class Meta:
    
        model = s2220exame
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')