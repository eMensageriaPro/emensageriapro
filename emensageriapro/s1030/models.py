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
from emensageriapro.s1030.choices import *
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





class s1030alteracao(SoftDeletionModel):

    s1030_evttabcargo = models.ForeignKey('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo', )

    def evento(self):
        return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    nmcargo = models.CharField(max_length=100, null=True, )
    codcbo = models.TextField(null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_evttabcargo), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Alteração das informações'
        db_table = r's1030_alteracao'
        managed = True # s1030_alteracao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030alteracao", u"Pode ver listagem do modelo S1030ALTERACAO"),
            ("can_see_data_s1030alteracao", u"Pode visualizar o conteúdo do modelo S1030ALTERACAO"),
            ("can_see_menu_s1030alteracao", u"Pode visualizar no menu o modelo S1030ALTERACAO"),
            ("can_print_list_s1030alteracao", u"Pode imprimir listagem do modelo S1030ALTERACAO"),
            ("can_print_data_s1030alteracao", u"Pode imprimir o conteúdo do modelo S1030ALTERACAO"), )

        ordering = [
            's1030_evttabcargo',
            'codcargo',
            'inivalid',
            'nmcargo',
            'codcbo',]



class s1030alteracaoSerializer(ModelSerializer):

    class Meta:

        model = s1030alteracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030alteracaocargoPublico(SoftDeletionModel):

    s1030_alteracao = models.ForeignKey('s1030.s1030alteracao',
        related_name='%(class)s_s1030_alteracao', )

    def evento(self):
        return self.s1030_alteracao.evento()
    acumcargo = models.IntegerField(choices=CHOICES_S1030_ACUMCARGO_ALTERACAO, null=True, )
    contagemesp = models.IntegerField(choices=CHOICES_S1030_CONTAGEMESP_ALTERACAO, null=True, )
    dedicexcl = models.CharField(choices=CHOICES_S1030_DEDICEXCL_ALTERACAO, max_length=1, null=True, )
    codcarreira = models.CharField(max_length=30, blank=True, null=True, )
    nrlei = models.CharField(max_length=12, null=True, )
    dtlei = models.DateField(null=True, )
    sitcargo = models.IntegerField(choices=CHOICES_S1030_SITCARGO_ALTERACAO, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_alteracao), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Detalhamento de informações exclusivas para Cargos e Empregos Públicos'
        db_table = r's1030_alteracao_cargopublico'
        managed = True # s1030_alteracao_cargopublico #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030alteracaocargoPublico", u"Pode ver listagem do modelo S1030ALTERACAOCARGOPUBLICO"),
            ("can_see_data_s1030alteracaocargoPublico", u"Pode visualizar o conteúdo do modelo S1030ALTERACAOCARGOPUBLICO"),
            ("can_see_menu_s1030alteracaocargoPublico", u"Pode visualizar no menu o modelo S1030ALTERACAOCARGOPUBLICO"),
            ("can_print_list_s1030alteracaocargoPublico", u"Pode imprimir listagem do modelo S1030ALTERACAOCARGOPUBLICO"),
            ("can_print_data_s1030alteracaocargoPublico", u"Pode imprimir o conteúdo do modelo S1030ALTERACAOCARGOPUBLICO"), )

        ordering = [
            's1030_alteracao',
            'acumcargo',
            'contagemesp',
            'dedicexcl',
            'nrlei',
            'dtlei',
            'sitcargo',]



class s1030alteracaocargoPublicoSerializer(ModelSerializer):

    class Meta:

        model = s1030alteracaocargoPublico
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030alteracaonovaValidade(SoftDeletionModel):

    s1030_alteracao = models.ForeignKey('s1030.s1030alteracao',
        related_name='%(class)s_s1030_alteracao', )

    def evento(self):
        return self.s1030_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_alteracao), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1030_alteracao_novavalidade'
        managed = True # s1030_alteracao_novavalidade #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030alteracaonovaValidade", u"Pode ver listagem do modelo S1030ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1030alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1030ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1030alteracaonovaValidade", u"Pode visualizar no menu o modelo S1030ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1030alteracaonovaValidade", u"Pode imprimir listagem do modelo S1030ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1030alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1030ALTERACAONOVAVALIDADE"), )

        ordering = [
            's1030_alteracao',
            'inivalid',]



class s1030alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:

        model = s1030alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030exclusao(SoftDeletionModel):

    s1030_evttabcargo = models.ForeignKey('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo', )

    def evento(self):
        return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_evttabcargo), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Exclusão das informações'
        db_table = r's1030_exclusao'
        managed = True # s1030_exclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030exclusao", u"Pode ver listagem do modelo S1030EXCLUSAO"),
            ("can_see_data_s1030exclusao", u"Pode visualizar o conteúdo do modelo S1030EXCLUSAO"),
            ("can_see_menu_s1030exclusao", u"Pode visualizar no menu o modelo S1030EXCLUSAO"),
            ("can_print_list_s1030exclusao", u"Pode imprimir listagem do modelo S1030EXCLUSAO"),
            ("can_print_data_s1030exclusao", u"Pode imprimir o conteúdo do modelo S1030EXCLUSAO"), )

        ordering = [
            's1030_evttabcargo',
            'codcargo',
            'inivalid',]



class s1030exclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1030exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030inclusao(SoftDeletionModel):

    s1030_evttabcargo = models.ForeignKey('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo', )

    def evento(self):
        return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    nmcargo = models.CharField(max_length=100, null=True, )
    codcbo = models.TextField(null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_evttabcargo), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1030_inclusao'
        managed = True # s1030_inclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030inclusao", u"Pode ver listagem do modelo S1030INCLUSAO"),
            ("can_see_data_s1030inclusao", u"Pode visualizar o conteúdo do modelo S1030INCLUSAO"),
            ("can_see_menu_s1030inclusao", u"Pode visualizar no menu o modelo S1030INCLUSAO"),
            ("can_print_list_s1030inclusao", u"Pode imprimir listagem do modelo S1030INCLUSAO"),
            ("can_print_data_s1030inclusao", u"Pode imprimir o conteúdo do modelo S1030INCLUSAO"), )

        ordering = [
            's1030_evttabcargo',
            'codcargo',
            'inivalid',
            'nmcargo',
            'codcbo',]



class s1030inclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1030inclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030inclusaocargoPublico(SoftDeletionModel):

    s1030_inclusao = models.ForeignKey('s1030.s1030inclusao',
        related_name='%(class)s_s1030_inclusao', )

    def evento(self):
        return self.s1030_inclusao.evento()
    acumcargo = models.IntegerField(choices=CHOICES_S1030_ACUMCARGO_INCLUSAO, null=True, )
    contagemesp = models.IntegerField(choices=CHOICES_S1030_CONTAGEMESP_INCLUSAO, null=True, )
    dedicexcl = models.CharField(choices=CHOICES_S1030_DEDICEXCL_INCLUSAO, max_length=1, null=True, )
    codcarreira = models.CharField(max_length=30, blank=True, null=True, )
    nrlei = models.CharField(max_length=12, null=True, )
    dtlei = models.DateField(null=True, )
    sitcargo = models.IntegerField(choices=CHOICES_S1030_SITCARGO_INCLUSAO, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s1030_inclusao), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Detalhamento de informações exclusivas para Cargos e Empregos Públicos'
        db_table = r's1030_inclusao_cargopublico'
        managed = True # s1030_inclusao_cargopublico #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1030inclusaocargoPublico", u"Pode ver listagem do modelo S1030INCLUSAOCARGOPUBLICO"),
            ("can_see_data_s1030inclusaocargoPublico", u"Pode visualizar o conteúdo do modelo S1030INCLUSAOCARGOPUBLICO"),
            ("can_see_menu_s1030inclusaocargoPublico", u"Pode visualizar no menu o modelo S1030INCLUSAOCARGOPUBLICO"),
            ("can_print_list_s1030inclusaocargoPublico", u"Pode imprimir listagem do modelo S1030INCLUSAOCARGOPUBLICO"),
            ("can_print_data_s1030inclusaocargoPublico", u"Pode imprimir o conteúdo do modelo S1030INCLUSAOCARGOPUBLICO"), )

        ordering = [
            's1030_inclusao',
            'acumcargo',
            'contagemesp',
            'dedicexcl',
            'nrlei',
            'dtlei',
            'sitcargo',]



class s1030inclusaocargoPublicoSerializer(ModelSerializer):

    class Meta:

        model = s1030inclusaocargoPublico
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')