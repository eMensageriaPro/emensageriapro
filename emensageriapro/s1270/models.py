# eMensageriaAI #
#coding:utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s1270.choices import *
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





class s1270remunAvNP(SoftDeletionModel):

    s1270_evtcontratavnp = models.ForeignKey('esocial.s1270evtContratAvNP',
        related_name='%(class)s_s1270_evtcontratavnp', )

    def evento(self):
        return self.s1270_evtcontratavnp.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp13 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbcfgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1270_evtcontratavnp) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrbccp13) + ' - ' + unicode(self.vrbcfgts) + ' - ' + unicode(self.vrdesccp)

    class Meta:

        # verbose_name = u'Registro que apresenta a remuneração dos trabalhadores avulsos não portuários, de forma totalizada por estabelecimento contratante.'
        db_table = r's1270_remunavnp'
        managed = True # s1270_remunavnp #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1270remunAvNP", u"Pode ver listagem do modelo S1270REMUNAVNP"),
            ("can_see_data_s1270remunAvNP", u"Pode visualizar o conteúdo do modelo S1270REMUNAVNP"),
            ("can_see_menu_s1270remunAvNP", u"Pode visualizar no menu o modelo S1270REMUNAVNP"),
            ("can_print_list_s1270remunAvNP", u"Pode imprimir listagem do modelo S1270REMUNAVNP"),
            ("can_print_data_s1270remunAvNP", u"Pode imprimir o conteúdo do modelo S1270REMUNAVNP"), )

        ordering = [
            's1270_evtcontratavnp',
            'tpinsc',
            'nrinsc',
            'codlotacao',
            'vrbccp00',
            'vrbccp15',
            'vrbccp20',
            'vrbccp25',
            'vrbccp13',
            'vrbcfgts',
            'vrdesccp',]



class s1270remunAvNPSerializer(ModelSerializer):

    class Meta:

        model = s1270remunAvNP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')