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
from emensageriapro.s2405.choices import *
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





class s2405brasil(SoftDeletionModel):

    s2405_endereco = models.ForeignKey('s2405.s2405endereco',
        related_name='%(class)s_s2405_endereco', )

    def evento(self):
        return self.s2405_endereco.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.IntegerField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )

    def __unicode__(self):
        return unicode(self.s2405_endereco) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)

    class Meta:

        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2405_brasil'
        managed = True # s2405_brasil #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2405brasil", u"Pode ver listagem do modelo S2405BRASIL"),
            ("can_see_data_s2405brasil", u"Pode visualizar o conteúdo do modelo S2405BRASIL"),
            ("can_see_menu_s2405brasil", u"Pode visualizar no menu o modelo S2405BRASIL"),
            ("can_print_list_s2405brasil", u"Pode imprimir listagem do modelo S2405BRASIL"),
            ("can_print_data_s2405brasil", u"Pode imprimir o conteúdo do modelo S2405BRASIL"), )

        ordering = [
            's2405_endereco',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2405brasilSerializer(ModelSerializer):

    class Meta:

        model = s2405brasil
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2405dependente(SoftDeletionModel):

    s2405_evtcdbenefalt = models.ForeignKey('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt', )

    def evento(self):
        return self.s2405_evtcdbenefalt.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    sexodep = models.CharField(choices=CHOICES_S2405_SEXODEP, max_length=1, null=True, )
    depirrf = models.CharField(choices=CHOICES_S2405_DEPIRRF, max_length=1, null=True, )
    incfismen = models.CharField(choices=CHOICES_S2405_INCFISMEN, max_length=1, null=True, )
    depfinsprev = models.CharField(choices=CHOICES_S2405_DEPFINSPREV, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.sexodep) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.incfismen) + ' - ' + unicode(self.depfinsprev)

    class Meta:

        # verbose_name = u'Informações dos dependentes'
        db_table = r's2405_dependente'
        managed = True # s2405_dependente #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2405dependente", u"Pode ver listagem do modelo S2405DEPENDENTE"),
            ("can_see_data_s2405dependente", u"Pode visualizar o conteúdo do modelo S2405DEPENDENTE"),
            ("can_see_menu_s2405dependente", u"Pode visualizar no menu o modelo S2405DEPENDENTE"),
            ("can_print_list_s2405dependente", u"Pode imprimir listagem do modelo S2405DEPENDENTE"),
            ("can_print_data_s2405dependente", u"Pode imprimir o conteúdo do modelo S2405DEPENDENTE"), )

        ordering = [
            's2405_evtcdbenefalt',
            'tpdep',
            'nmdep',
            'dtnascto',
            'sexodep',
            'depirrf',
            'incfismen',
            'depfinsprev',]



class s2405dependenteSerializer(ModelSerializer):

    class Meta:

        model = s2405dependente
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2405endereco(SoftDeletionModel):

    s2405_evtcdbenefalt = models.ForeignKey('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt', )

    def evento(self):
        return self.s2405_evtcdbenefalt.evento()

    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt)

    class Meta:

        # verbose_name = u'Grupo de informações do endereço do Trabalhador'
        db_table = r's2405_endereco'
        managed = True # s2405_endereco #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2405endereco", u"Pode ver listagem do modelo S2405ENDERECO"),
            ("can_see_data_s2405endereco", u"Pode visualizar o conteúdo do modelo S2405ENDERECO"),
            ("can_see_menu_s2405endereco", u"Pode visualizar no menu o modelo S2405ENDERECO"),
            ("can_print_list_s2405endereco", u"Pode imprimir listagem do modelo S2405ENDERECO"),
            ("can_print_data_s2405endereco", u"Pode imprimir o conteúdo do modelo S2405ENDERECO"), )

        ordering = [
            's2405_evtcdbenefalt',]



class s2405enderecoSerializer(ModelSerializer):

    class Meta:

        model = s2405endereco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2405exterior(SoftDeletionModel):

    s2405_endereco = models.ForeignKey('s2405.s2405endereco',
        related_name='%(class)s_s2405_endereco', )

    def evento(self):
        return self.s2405_endereco.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2405_endereco) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)

    class Meta:

        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2405_exterior'
        managed = True # s2405_exterior #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2405exterior", u"Pode ver listagem do modelo S2405EXTERIOR"),
            ("can_see_data_s2405exterior", u"Pode visualizar o conteúdo do modelo S2405EXTERIOR"),
            ("can_see_menu_s2405exterior", u"Pode visualizar no menu o modelo S2405EXTERIOR"),
            ("can_print_list_s2405exterior", u"Pode imprimir listagem do modelo S2405EXTERIOR"),
            ("can_print_data_s2405exterior", u"Pode imprimir o conteúdo do modelo S2405EXTERIOR"), )

        ordering = [
            's2405_endereco',
            'paisresid',
            'dsclograd',
            'nrlograd',
            'nmcid',]



class s2405exteriorSerializer(ModelSerializer):

    class Meta:

        model = s2405exterior
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')