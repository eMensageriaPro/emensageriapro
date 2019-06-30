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
from emensageriapro.s5002.choices import *
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





class s5002basesIrrf(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf', )

    def evento(self):
        return self.s5002_infoirrf.evento()
    tpvalor = models.IntegerField(null=True, )
    valor = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5002_infoirrf), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Bases, deduções, isenções e retenções do IRRF'
        db_table = r's5002_basesirrf'
        managed = True # s5002_basesirrf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5002basesIrrf", u"Pode ver listagem do modelo S5002BASESIRRF"),
            ("can_see_data_s5002basesIrrf", u"Pode visualizar o conteúdo do modelo S5002BASESIRRF"),
            ("can_see_menu_s5002basesIrrf", u"Pode visualizar no menu o modelo S5002BASESIRRF"),
            ("can_print_list_s5002basesIrrf", u"Pode imprimir listagem do modelo S5002BASESIRRF"),
            ("can_print_data_s5002basesIrrf", u"Pode imprimir o conteúdo do modelo S5002BASESIRRF"), )

        ordering = [
            's5002_infoirrf',
            'tpvalor',
            'valor',]



class s5002basesIrrfSerializer(ModelSerializer):

    class Meta:

        model = s5002basesIrrf
        fields = '__all__'


class s5002idePgtoExt(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf', )

    def evento(self):
        return self.s5002_infoirrf.evento()
    codpais = models.TextField(null=True, )
    indnif = models.IntegerField(choices=CHOICES_S5002_INDNIF, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5002_infoirrf), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações complementares relativas a pagamentos efetuados a beneficiário residente fiscal no exterior.'
        db_table = r's5002_idepgtoext'
        managed = True # s5002_idepgtoext #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5002idePgtoExt", u"Pode ver listagem do modelo S5002IDEPGTOEXT"),
            ("can_see_data_s5002idePgtoExt", u"Pode visualizar o conteúdo do modelo S5002IDEPGTOEXT"),
            ("can_see_menu_s5002idePgtoExt", u"Pode visualizar no menu o modelo S5002IDEPGTOEXT"),
            ("can_print_list_s5002idePgtoExt", u"Pode imprimir listagem do modelo S5002IDEPGTOEXT"),
            ("can_print_data_s5002idePgtoExt", u"Pode imprimir o conteúdo do modelo S5002IDEPGTOEXT"), )

        ordering = [
            's5002_infoirrf',
            'codpais',
            'indnif',
            'dsclograd',
            'nmcid',]



class s5002idePgtoExtSerializer(ModelSerializer):

    class Meta:

        model = s5002idePgtoExt
        fields = '__all__'


class s5002infoDep(SoftDeletionModel):

    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef', )

    def evento(self):
        return self.s5002_evtirrfbenef.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5002_evtirrfbenef), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas a existência de dependentes do beneficiário do pagamento. Origem: S-1210 - registro {deps}'
        db_table = r's5002_infodep'
        managed = True # s5002_infodep #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5002infoDep", u"Pode ver listagem do modelo S5002INFODEP"),
            ("can_see_data_s5002infoDep", u"Pode visualizar o conteúdo do modelo S5002INFODEP"),
            ("can_see_menu_s5002infoDep", u"Pode visualizar no menu o modelo S5002INFODEP"),
            ("can_print_list_s5002infoDep", u"Pode imprimir listagem do modelo S5002INFODEP"),
            ("can_print_data_s5002infoDep", u"Pode imprimir o conteúdo do modelo S5002INFODEP"), )

        ordering = [
            's5002_evtirrfbenef',
            'vrdeddep',]



class s5002infoDepSerializer(ModelSerializer):

    class Meta:

        model = s5002infoDep
        fields = '__all__'


class s5002infoIrrf(SoftDeletionModel):

    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef', )

    def evento(self):
        return self.s5002_evtirrfbenef.evento()
    codcateg = models.IntegerField(blank=True, null=True, )
    indresbr = models.CharField(choices=CHOICES_S5002_INDRESBR, max_length=1, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5002_evtirrfbenef), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas ao Imposto de Renda Retido na Fonte do Trabalhador e suas bases de cálculo'
        db_table = r's5002_infoirrf'
        managed = True # s5002_infoirrf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5002infoIrrf", u"Pode ver listagem do modelo S5002INFOIRRF"),
            ("can_see_data_s5002infoIrrf", u"Pode visualizar o conteúdo do modelo S5002INFOIRRF"),
            ("can_see_menu_s5002infoIrrf", u"Pode visualizar no menu o modelo S5002INFOIRRF"),
            ("can_print_list_s5002infoIrrf", u"Pode imprimir listagem do modelo S5002INFOIRRF"),
            ("can_print_data_s5002infoIrrf", u"Pode imprimir o conteúdo do modelo S5002INFOIRRF"), )

        ordering = [
            's5002_evtirrfbenef',
            'indresbr',]



class s5002infoIrrfSerializer(ModelSerializer):

    class Meta:

        model = s5002infoIrrf
        fields = '__all__'


class s5002irrf(SoftDeletionModel):

    s5002_infoirrf = models.ForeignKey('s5002.s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf', )

    def evento(self):
        return self.s5002_infoirrf.evento()
    tpcr = models.CharField(choices=CHOICES_S5002_TPCR, max_length=6, null=True, )
    vrirrfdesc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5002_infoirrf), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas ao Imposto de Renda Retido na Fonte'
        db_table = r's5002_irrf'
        managed = True # s5002_irrf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5002irrf", u"Pode ver listagem do modelo S5002IRRF"),
            ("can_see_data_s5002irrf", u"Pode visualizar o conteúdo do modelo S5002IRRF"),
            ("can_see_menu_s5002irrf", u"Pode visualizar no menu o modelo S5002IRRF"),
            ("can_print_list_s5002irrf", u"Pode imprimir listagem do modelo S5002IRRF"),
            ("can_print_data_s5002irrf", u"Pode imprimir o conteúdo do modelo S5002IRRF"), )

        ordering = [
            's5002_infoirrf',
            'tpcr',
            'vrirrfdesc',]



class s5002irrfSerializer(ModelSerializer):

    class Meta:

        model = s5002irrf
        fields = '__all__'