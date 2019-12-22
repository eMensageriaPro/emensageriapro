# eMensageriaAI #
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
from emensageriapro.r2050.choices import *
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





class r2050infoProc(SoftDeletionModel):

    r2050_tipocom = models.ForeignKey('r2050.r2050tipoCom',
        related_name='%(class)s_r2050_tipocom', )

    def evento(self):
        return self.r2050_tipocom.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2050_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrratsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r2050_tipocom) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc)

    class Meta:

        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r2050_infoproc'
        managed = True # r2050_infoproc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2050infoProc", u"Pode ver listagem do modelo R2050INFOPROC"),
            ("can_see_data_r2050infoProc", u"Pode visualizar o conteúdo do modelo R2050INFOPROC"),
            ("can_see_menu_r2050infoProc", u"Pode visualizar no menu o modelo R2050INFOPROC"),
            ("can_print_list_r2050infoProc", u"Pode imprimir listagem do modelo R2050INFOPROC"),
            ("can_print_data_r2050infoProc", u"Pode imprimir o conteúdo do modelo R2050INFOPROC"), )

        ordering = [
            'r2050_tipocom',
            'tpproc',
            'nrproc',]



class r2050infoProcSerializer(ModelSerializer):

    class Meta:

        model = r2050infoProc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r2050tipoCom(SoftDeletionModel):

    r2050_evtcomprod = models.ForeignKey('efdreinf.r2050evtComProd',
        related_name='%(class)s_r2050_evtcomprod', )

    def evento(self):
        return self.r2050_evtcomprod.evento()
    indcom = models.IntegerField(choices=CHOICES_R2050_INDCOM, null=True, )
    vlrrecbruta = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r2050_evtcomprod) + ' - ' + unicode(self.indcom) + ' - ' + unicode(self.vlrrecbruta)

    class Meta:

        # verbose_name = u'Registro que apresenta o valor total da Receita Bruta por 'tipo' de comercialização.'
        db_table = r'r2050_tipocom'
        managed = True # r2050_tipocom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r2050tipoCom", u"Pode ver listagem do modelo R2050TIPOCOM"),
            ("can_see_data_r2050tipoCom", u"Pode visualizar o conteúdo do modelo R2050TIPOCOM"),
            ("can_see_menu_r2050tipoCom", u"Pode visualizar no menu o modelo R2050TIPOCOM"),
            ("can_print_list_r2050tipoCom", u"Pode imprimir listagem do modelo R2050TIPOCOM"),
            ("can_print_data_r2050tipoCom", u"Pode imprimir o conteúdo do modelo R2050TIPOCOM"), )

        ordering = [
            'r2050_evtcomprod',
            'indcom',
            'vlrrecbruta',]



class r2050tipoComSerializer(ModelSerializer):

    class Meta:

        model = r2050tipoCom
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')