#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S1270_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class s1270remunAvNP(SoftDeletionModel):
    s1270_evtcontratavnp = models.ForeignKey('esocial.s1270evtContratAvNP',
        related_name='%(class)s_s1270_evtcontratavnp')
    def evento(self): return self.s1270_evtcontratavnp.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1270_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbcfgts = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1270_evtcontratavnp) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrbccp13) + ' - ' + unicode(self.vrbcfgts) + ' - ' + unicode(self.vrdesccp)
    #s1270_remunavnp_custom#

    class Meta:
        db_table = r's1270_remunavnp'       
        managed = True # s1270_remunavnp #
        unique_together = (
            #custom_unique_together_s1270_remunavnp#
            
        )
        index_together = (
            #custom_index_together_s1270_remunavnp
            #index_together_s1270_remunavnp
        )
        permissions = (
            ("can_view_s1270_remunavnp", "Can view s1270_remunavnp"),
            #custom_permissions_s1270_remunavnp
        )
        ordering = ['s1270_evtcontratavnp', 'tpinsc', 'nrinsc', 'codlotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp']



class s1270remunAvNPSerializer(ModelSerializer):
    class Meta:
        model = s1270remunAvNP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
