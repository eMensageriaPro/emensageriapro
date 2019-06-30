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
from emensageriapro.s2231.choices import *
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





class s2231fimCessao(SoftDeletionModel):

    s2231_evtcessao = models.ForeignKey('esocial.s2231evtCessao',
        related_name='%(class)s_s2231_evtcessao', )

    def evento(self):
        return self.s2231_evtcessao.evento()
    dttermcessao = models.DateField(null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s2231_evtcessao), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações de término da cessão/exercício em outro órgão'
        db_table = r's2231_fimcessao'
        managed = True # s2231_fimcessao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2231fimCessao", u"Pode ver listagem do modelo S2231FIMCESSAO"),
            ("can_see_data_s2231fimCessao", u"Pode visualizar o conteúdo do modelo S2231FIMCESSAO"),
            ("can_see_menu_s2231fimCessao", u"Pode visualizar no menu o modelo S2231FIMCESSAO"),
            ("can_print_list_s2231fimCessao", u"Pode imprimir listagem do modelo S2231FIMCESSAO"),
            ("can_print_data_s2231fimCessao", u"Pode imprimir o conteúdo do modelo S2231FIMCESSAO"), )

        ordering = [
            's2231_evtcessao',
            'dttermcessao',]



class s2231fimCessaoSerializer(ModelSerializer):

    class Meta:

        model = s2231fimCessao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2231iniCessao(SoftDeletionModel):

    s2231_evtcessao = models.ForeignKey('esocial.s2231evtCessao',
        related_name='%(class)s_s2231_evtcessao', )

    def evento(self):
        return self.s2231_evtcessao.evento()
    dtinicessao = models.DateField(null=True, )
    cnpjcess = models.CharField(max_length=14, null=True, )
    infonus = models.IntegerField(choices=CHOICES_S2231_INFONUS, null=True, )
    indcessao = models.IntegerField(choices=CHOICES_S2231_INDCESSAO, null=True, )
    dscsituacao = models.CharField(max_length=255, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s2231_evtcessao), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações de início da cessão/exercício em outro órgão'
        db_table = r's2231_inicessao'
        managed = True # s2231_inicessao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2231iniCessao", u"Pode ver listagem do modelo S2231INICESSAO"),
            ("can_see_data_s2231iniCessao", u"Pode visualizar o conteúdo do modelo S2231INICESSAO"),
            ("can_see_menu_s2231iniCessao", u"Pode visualizar no menu o modelo S2231INICESSAO"),
            ("can_print_list_s2231iniCessao", u"Pode imprimir listagem do modelo S2231INICESSAO"),
            ("can_print_data_s2231iniCessao", u"Pode imprimir o conteúdo do modelo S2231INICESSAO"), )

        ordering = [
            's2231_evtcessao',
            'dtinicessao',
            'cnpjcess',
            'infonus',
            'indcessao',]



class s2231iniCessaoSerializer(ModelSerializer):

    class Meta:

        model = s2231iniCessao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')