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
from emensageriapro.s1080.choices import *
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





class s1080alteracao(SoftDeletionModel):

    s1080_evttaboperport = models.ForeignKey('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport', )

    def evento(self):
        return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S1080_ALIQRAT_ALTERACAO, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)

    class Meta:

        # verbose_name = u'Alteração das informações'
        db_table = r's1080_alteracao'
        managed = True # s1080_alteracao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1080alteracao", u"Pode ver listagem do modelo S1080ALTERACAO"),
            ("can_see_data_s1080alteracao", u"Pode visualizar o conteúdo do modelo S1080ALTERACAO"),
            ("can_see_menu_s1080alteracao", u"Pode visualizar no menu o modelo S1080ALTERACAO"),
            ("can_print_list_s1080alteracao", u"Pode imprimir listagem do modelo S1080ALTERACAO"),
            ("can_print_data_s1080alteracao", u"Pode imprimir o conteúdo do modelo S1080ALTERACAO"), )

        ordering = [
            's1080_evttaboperport',
            'cnpjopportuario',
            'inivalid',
            'aliqrat',
            'fap',
            'aliqratajust',]



class s1080alteracaoSerializer(ModelSerializer):

    class Meta:

        model = s1080alteracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1080alteracaonovaValidade(SoftDeletionModel):

    s1080_alteracao = models.ForeignKey('s1080.s1080alteracao',
        related_name='%(class)s_s1080_alteracao', )

    def evento(self):
        return self.s1080_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1080_alteracao) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1080_alteracao_novavalidade'
        managed = True # s1080_alteracao_novavalidade #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1080alteracaonovaValidade", u"Pode ver listagem do modelo S1080ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1080alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1080ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1080alteracaonovaValidade", u"Pode visualizar no menu o modelo S1080ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1080alteracaonovaValidade", u"Pode imprimir listagem do modelo S1080ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1080alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1080ALTERACAONOVAVALIDADE"), )

        ordering = [
            's1080_alteracao',
            'inivalid',]



class s1080alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:

        model = s1080alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1080exclusao(SoftDeletionModel):

    s1080_evttaboperport = models.ForeignKey('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport', )

    def evento(self):
        return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Exclusão das informações'
        db_table = r's1080_exclusao'
        managed = True # s1080_exclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1080exclusao", u"Pode ver listagem do modelo S1080EXCLUSAO"),
            ("can_see_data_s1080exclusao", u"Pode visualizar o conteúdo do modelo S1080EXCLUSAO"),
            ("can_see_menu_s1080exclusao", u"Pode visualizar no menu o modelo S1080EXCLUSAO"),
            ("can_print_list_s1080exclusao", u"Pode imprimir listagem do modelo S1080EXCLUSAO"),
            ("can_print_data_s1080exclusao", u"Pode imprimir o conteúdo do modelo S1080EXCLUSAO"), )

        ordering = [
            's1080_evttaboperport',
            'cnpjopportuario',
            'inivalid',]



class s1080exclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1080exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1080inclusao(SoftDeletionModel):

    s1080_evttaboperport = models.ForeignKey('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport', )

    def evento(self):
        return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S1080_ALIQRAT_INCLUSAO, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)

    class Meta:

        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1080_inclusao'
        managed = True # s1080_inclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1080inclusao", u"Pode ver listagem do modelo S1080INCLUSAO"),
            ("can_see_data_s1080inclusao", u"Pode visualizar o conteúdo do modelo S1080INCLUSAO"),
            ("can_see_menu_s1080inclusao", u"Pode visualizar no menu o modelo S1080INCLUSAO"),
            ("can_print_list_s1080inclusao", u"Pode imprimir listagem do modelo S1080INCLUSAO"),
            ("can_print_data_s1080inclusao", u"Pode imprimir o conteúdo do modelo S1080INCLUSAO"), )

        ordering = [
            's1080_evttaboperport',
            'cnpjopportuario',
            'inivalid',
            'aliqrat',
            'fap',
            'aliqratajust',]



class s1080inclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1080inclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')