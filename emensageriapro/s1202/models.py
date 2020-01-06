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
from emensageriapro.s1202.choices import *
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





class s1202dmDev(SoftDeletionModel):

    s1202_evtrmnrpps = models.ForeignKey('esocial.s1202evtRmnRPPS',
        related_name='%(class)s_s1202_evtrmnrpps', )

    def evento(self):
        return self.s1202_evtrmnrpps.evento()
    idedmdev = models.CharField(max_length=30, null=True, )
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1202_evtrmnrpps) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.codcateg)

    class Meta:

        # verbose_name = u'Identificação de cada um dos demonstrativos de valores devidos ao trabalhador antes das retenções de pensão alimentícia e IRRF'
        db_table = r's1202_dmdev'
        managed = True # s1202_dmdev #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202dmDev", u"Pode ver listagem do modelo S1202DMDEV"),
            ("can_see_data_s1202dmDev", u"Pode visualizar o conteúdo do modelo S1202DMDEV"),
            ("can_see_menu_s1202dmDev", u"Pode visualizar no menu o modelo S1202DMDEV"),
            ("can_print_list_s1202dmDev", u"Pode imprimir listagem do modelo S1202DMDEV"),
            ("can_print_data_s1202dmDev", u"Pode imprimir o conteúdo do modelo S1202DMDEV"), )

        ordering = [
            's1202_evtrmnrpps',
            'idedmdev',
            'codcateg',]



class s1202dmDevSerializer(ModelSerializer):

    class Meta:

        model = s1202dmDev
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAnt(SoftDeletionModel):

    s1202_dmdev = models.ForeignKey('s1202.s1202dmDev',
        related_name='%(class)s_s1202_dmdev', )

    def evento(self):
        return self.s1202_dmdev.evento()

    def __unicode__(self):
        return unicode(self.s1202_dmdev)

    class Meta:

        # verbose_name = u'Registro destinado ao registro de: a) remuneração relativa a diferenças salariais provenientes de acordos coletivos, convenção coletiva e dissídio; b) remuneração relativa a diferenças de vencimento provenientes de disposições legais (órgãos públicos); c) bases de cálculo para efeitos de apuração de FGTS resultantes de conversão de licença saúde em acidente de trabalho. d) verbas de natureza salarial ou não salarial devidas após o desligamento'
        db_table = r's1202_infoperant'
        managed = True # s1202_infoperant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAnt", u"Pode ver listagem do modelo S1202INFOPERANT"),
            ("can_see_data_s1202infoPerAnt", u"Pode visualizar o conteúdo do modelo S1202INFOPERANT"),
            ("can_see_menu_s1202infoPerAnt", u"Pode visualizar no menu o modelo S1202INFOPERANT"),
            ("can_print_list_s1202infoPerAnt", u"Pode imprimir listagem do modelo S1202INFOPERANT"),
            ("can_print_data_s1202infoPerAnt", u"Pode imprimir o conteúdo do modelo S1202INFOPERANT"), )

        ordering = [
            's1202_dmdev',]



class s1202infoPerAntSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAntideADC(SoftDeletionModel):

    s1202_infoperant = models.ForeignKey('s1202.s1202infoPerAnt',
        related_name='%(class)s_s1202_infoperant', )

    def evento(self):
        return self.s1202_infoperant.evento()
    dtlei = models.DateField(null=True, )
    nrlei = models.CharField(max_length=12, null=True, )
    dtef = models.DateField(blank=True, null=True, )
    dtacconv = models.DateField(blank=True, null=True, )
    tpacconv = models.CharField(choices=CHOICES_S1202_TPACCONV_INFOPERANT, max_length=1, null=True, )
    compacconv = models.CharField(max_length=7, blank=True, null=True, )
    dtefacconv = models.DateField(blank=True, null=True, )
    dsc = models.CharField(max_length=255, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperant) + ' - ' + unicode(self.dtlei) + ' - ' + unicode(self.nrlei) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dsc)

    class Meta:

        # verbose_name = u'Identificação do Instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores.'
        db_table = r's1202_infoperant_ideadc'
        managed = True # s1202_infoperant_ideadc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAntideADC", u"Pode ver listagem do modelo S1202INFOPERANTIDEADC"),
            ("can_see_data_s1202infoPerAntideADC", u"Pode visualizar o conteúdo do modelo S1202INFOPERANTIDEADC"),
            ("can_see_menu_s1202infoPerAntideADC", u"Pode visualizar no menu o modelo S1202INFOPERANTIDEADC"),
            ("can_print_list_s1202infoPerAntideADC", u"Pode imprimir listagem do modelo S1202INFOPERANTIDEADC"),
            ("can_print_data_s1202infoPerAntideADC", u"Pode imprimir o conteúdo do modelo S1202INFOPERANTIDEADC"), )

        ordering = [
            's1202_infoperant',
            'dtlei',
            'nrlei',
            'tpacconv',
            'dsc',]



class s1202infoPerAntideADCSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAntideADC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAntideEstab(SoftDeletionModel):

    s1202_infoperant_ideperiodo = models.ForeignKey('s1202.s1202infoPerAntidePeriodo',
        related_name='%(class)s_s1202_infoperant_ideperiodo', )

    def evento(self):
        return self.s1202_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)

    class Meta:

        # verbose_name = u'Informações de identificação do estabelecimento, obra ou órgão público e período de validade das informações que estão sendo incluídas'
        db_table = r's1202_infoperant_ideestab'
        managed = True # s1202_infoperant_ideestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAntideEstab", u"Pode ver listagem do modelo S1202INFOPERANTIDEESTAB"),
            ("can_see_data_s1202infoPerAntideEstab", u"Pode visualizar o conteúdo do modelo S1202INFOPERANTIDEESTAB"),
            ("can_see_menu_s1202infoPerAntideEstab", u"Pode visualizar no menu o modelo S1202INFOPERANTIDEESTAB"),
            ("can_print_list_s1202infoPerAntideEstab", u"Pode imprimir listagem do modelo S1202INFOPERANTIDEESTAB"),
            ("can_print_data_s1202infoPerAntideEstab", u"Pode imprimir o conteúdo do modelo S1202INFOPERANTIDEESTAB"), )

        ordering = [
            's1202_infoperant_ideperiodo',
            'tpinsc',
            'nrinsc',]



class s1202infoPerAntideEstabSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAntideEstab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAntidePeriodo(SoftDeletionModel):

    s1202_infoperant_ideadc = models.ForeignKey('s1202.s1202infoPerAntideADC',
        related_name='%(class)s_s1202_infoperant_ideadc', )

    def evento(self):
        return self.s1202_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideadc) + ' - ' + unicode(self.perref)

    class Meta:

        # verbose_name = u'Período de validade das informações incluídas'
        db_table = r's1202_infoperant_ideperiodo'
        managed = True # s1202_infoperant_ideperiodo #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAntidePeriodo", u"Pode ver listagem do modelo S1202INFOPERANTIDEPERIODO"),
            ("can_see_data_s1202infoPerAntidePeriodo", u"Pode visualizar o conteúdo do modelo S1202INFOPERANTIDEPERIODO"),
            ("can_see_menu_s1202infoPerAntidePeriodo", u"Pode visualizar no menu o modelo S1202INFOPERANTIDEPERIODO"),
            ("can_print_list_s1202infoPerAntidePeriodo", u"Pode imprimir listagem do modelo S1202INFOPERANTIDEPERIODO"),
            ("can_print_data_s1202infoPerAntidePeriodo", u"Pode imprimir o conteúdo do modelo S1202INFOPERANTIDEPERIODO"), )

        ordering = [
            's1202_infoperant_ideadc',
            'perref',]



class s1202infoPerAntidePeriodoSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAntidePeriodo
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAntitensRemun(SoftDeletionModel):

    s1202_infoperant_remunperant = models.ForeignKey('s1202.s1202infoPerAntremunPerAnt',
        related_name='%(class)s_s1202_infoperant_remunperant', )

    def evento(self):
        return self.s1202_infoperant_remunperant.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Registro que relaciona as rubricas que compõem a remuneração do trabalhador.'
        db_table = r's1202_infoperant_itensremun'
        managed = True # s1202_infoperant_itensremun #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAntitensRemun", u"Pode ver listagem do modelo S1202INFOPERANTITENSREMUN"),
            ("can_see_data_s1202infoPerAntitensRemun", u"Pode visualizar o conteúdo do modelo S1202INFOPERANTITENSREMUN"),
            ("can_see_menu_s1202infoPerAntitensRemun", u"Pode visualizar no menu o modelo S1202INFOPERANTITENSREMUN"),
            ("can_print_list_s1202infoPerAntitensRemun", u"Pode imprimir listagem do modelo S1202INFOPERANTITENSREMUN"),
            ("can_print_data_s1202infoPerAntitensRemun", u"Pode imprimir o conteúdo do modelo S1202INFOPERANTITENSREMUN"), )

        ordering = [
            's1202_infoperant_remunperant',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1202infoPerAntitensRemunSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAntitensRemun
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerAntremunPerAnt(SoftDeletionModel):

    s1202_infoperant_ideestab = models.ForeignKey('s1202.s1202infoPerAntideEstab',
        related_name='%(class)s_s1202_infoperant_ideestab', )

    def evento(self):
        return self.s1202_infoperant_ideestab.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideestab) + ' - ' + unicode(self.codcateg)

    class Meta:

        # verbose_name = u'Informações relativas a remuneração do trabalhador em períodos anteriores ao período de apuração'
        db_table = r's1202_infoperant_remunperant'
        managed = True # s1202_infoperant_remunperant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerAntremunPerAnt", u"Pode ver listagem do modelo S1202INFOPERANTREMUNPERANT"),
            ("can_see_data_s1202infoPerAntremunPerAnt", u"Pode visualizar o conteúdo do modelo S1202INFOPERANTREMUNPERANT"),
            ("can_see_menu_s1202infoPerAntremunPerAnt", u"Pode visualizar no menu o modelo S1202INFOPERANTREMUNPERANT"),
            ("can_print_list_s1202infoPerAntremunPerAnt", u"Pode imprimir listagem do modelo S1202INFOPERANTREMUNPERANT"),
            ("can_print_data_s1202infoPerAntremunPerAnt", u"Pode imprimir o conteúdo do modelo S1202INFOPERANTREMUNPERANT"), )

        ordering = [
            's1202_infoperant_ideestab',
            'codcateg',]



class s1202infoPerAntremunPerAntSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerAntremunPerAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApur(SoftDeletionModel):

    s1202_dmdev = models.ForeignKey('s1202.s1202dmDev',
        related_name='%(class)s_s1202_dmdev', )

    def evento(self):
        return self.s1202_dmdev.evento()

    def __unicode__(self):
        return unicode(self.s1202_dmdev)

    class Meta:

        # verbose_name = u'Remuneração no período de apuração'
        db_table = r's1202_infoperapur'
        managed = True # s1202_infoperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApur", u"Pode ver listagem do modelo S1202INFOPERAPUR"),
            ("can_see_data_s1202infoPerApur", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPUR"),
            ("can_see_menu_s1202infoPerApur", u"Pode visualizar no menu o modelo S1202INFOPERAPUR"),
            ("can_print_list_s1202infoPerApur", u"Pode imprimir listagem do modelo S1202INFOPERAPUR"),
            ("can_print_data_s1202infoPerApur", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPUR"), )

        ordering = [
            's1202_dmdev',]



class s1202infoPerApurSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApur
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApurdetOper(SoftDeletionModel):

    s1202_infoperapur_infosaudecolet = models.ForeignKey('s1202.s1202infoPerApurinfoSaudeColet',
        related_name='%(class)s_s1202_infoperapur_infosaudecolet', )

    def evento(self):
        return self.s1202_infoperapur_infosaudecolet.evento()
    cnpjoper = models.CharField(max_length=14, null=True, )
    regans = models.CharField(max_length=6, null=True, )
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperapur_infosaudecolet) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)

    class Meta:

        # verbose_name = u'Detalhamento dos valores pagos a Operadoras de Planos de Saúde.'
        db_table = r's1202_infoperapur_detoper'
        managed = True # s1202_infoperapur_detoper #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApurdetOper", u"Pode ver listagem do modelo S1202INFOPERAPURDETOPER"),
            ("can_see_data_s1202infoPerApurdetOper", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURDETOPER"),
            ("can_see_menu_s1202infoPerApurdetOper", u"Pode visualizar no menu o modelo S1202INFOPERAPURDETOPER"),
            ("can_print_list_s1202infoPerApurdetOper", u"Pode imprimir listagem do modelo S1202INFOPERAPURDETOPER"),
            ("can_print_data_s1202infoPerApurdetOper", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURDETOPER"), )

        ordering = [
            's1202_infoperapur_infosaudecolet',
            'cnpjoper',
            'regans',
            'vrpgtit',]



class s1202infoPerApurdetOperSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApurdetOper
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApurdetPlano(SoftDeletionModel):

    s1202_infoperapur_detoper = models.ForeignKey('s1202.s1202infoPerApurdetOper',
        related_name='%(class)s_s1202_infoperapur_detoper', )

    def evento(self):
        return self.s1202_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)

    class Meta:

        # verbose_name = u'Informações do dependente do plano privado de saúde.'
        db_table = r's1202_infoperapur_detplano'
        managed = True # s1202_infoperapur_detplano #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApurdetPlano", u"Pode ver listagem do modelo S1202INFOPERAPURDETPLANO"),
            ("can_see_data_s1202infoPerApurdetPlano", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURDETPLANO"),
            ("can_see_menu_s1202infoPerApurdetPlano", u"Pode visualizar no menu o modelo S1202INFOPERAPURDETPLANO"),
            ("can_print_list_s1202infoPerApurdetPlano", u"Pode imprimir listagem do modelo S1202INFOPERAPURDETPLANO"),
            ("can_print_data_s1202infoPerApurdetPlano", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURDETPLANO"), )

        ordering = [
            's1202_infoperapur_detoper',
            'tpdep',
            'nmdep',
            'dtnascto',
            'vlrpgdep',]



class s1202infoPerApurdetPlanoSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApurdetPlano
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApurideEstab(SoftDeletionModel):

    s1202_infoperapur = models.ForeignKey('s1202.s1202infoPerApur',
        related_name='%(class)s_s1202_infoperapur', )

    def evento(self):
        return self.s1202_infoperapur.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)

    class Meta:

        # verbose_name = u'Informações de identificação do estabelecimento, obra ou órgão público e período de validade das informações que estão sendo incluídas'
        db_table = r's1202_infoperapur_ideestab'
        managed = True # s1202_infoperapur_ideestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApurideEstab", u"Pode ver listagem do modelo S1202INFOPERAPURIDEESTAB"),
            ("can_see_data_s1202infoPerApurideEstab", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURIDEESTAB"),
            ("can_see_menu_s1202infoPerApurideEstab", u"Pode visualizar no menu o modelo S1202INFOPERAPURIDEESTAB"),
            ("can_print_list_s1202infoPerApurideEstab", u"Pode imprimir listagem do modelo S1202INFOPERAPURIDEESTAB"),
            ("can_print_data_s1202infoPerApurideEstab", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURIDEESTAB"), )

        ordering = [
            's1202_infoperapur',
            'tpinsc',
            'nrinsc',]



class s1202infoPerApurideEstabSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApurideEstab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApurinfoSaudeColet(SoftDeletionModel):

    s1202_infoperapur_remunperapur = models.ForeignKey('s1202.s1202infoPerApurremunPerApur',
        related_name='%(class)s_s1202_infoperapur_remunperapur', )

    def evento(self):
        return self.s1202_infoperapur_remunperapur.evento()

    def __unicode__(self):
        return unicode(self.s1202_infoperapur_remunperapur)

    class Meta:

        # verbose_name = u'Informações de plano privado coletivo empresarial de assistência à saúde'
        db_table = r's1202_infoperapur_infosaudecolet'
        managed = True # s1202_infoperapur_infosaudecolet #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApurinfoSaudeColet", u"Pode ver listagem do modelo S1202INFOPERAPURINFOSAUDECOLET"),
            ("can_see_data_s1202infoPerApurinfoSaudeColet", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURINFOSAUDECOLET"),
            ("can_see_menu_s1202infoPerApurinfoSaudeColet", u"Pode visualizar no menu o modelo S1202INFOPERAPURINFOSAUDECOLET"),
            ("can_print_list_s1202infoPerApurinfoSaudeColet", u"Pode imprimir listagem do modelo S1202INFOPERAPURINFOSAUDECOLET"),
            ("can_print_data_s1202infoPerApurinfoSaudeColet", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURINFOSAUDECOLET"), )

        ordering = [
            's1202_infoperapur_remunperapur',]



class s1202infoPerApurinfoSaudeColetSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApurinfoSaudeColet
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApuritensRemun(SoftDeletionModel):

    s1202_infoperapur_remunperapur = models.ForeignKey('s1202.s1202infoPerApurremunPerApur',
        related_name='%(class)s_s1202_infoperapur_remunperapur', )

    def evento(self):
        return self.s1202_infoperapur_remunperapur.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Registro que relaciona as rubricas que compõem a remuneração do trabalhador.'
        db_table = r's1202_infoperapur_itensremun'
        managed = True # s1202_infoperapur_itensremun #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApuritensRemun", u"Pode ver listagem do modelo S1202INFOPERAPURITENSREMUN"),
            ("can_see_data_s1202infoPerApuritensRemun", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURITENSREMUN"),
            ("can_see_menu_s1202infoPerApuritensRemun", u"Pode visualizar no menu o modelo S1202INFOPERAPURITENSREMUN"),
            ("can_print_list_s1202infoPerApuritensRemun", u"Pode imprimir listagem do modelo S1202INFOPERAPURITENSREMUN"),
            ("can_print_data_s1202infoPerApuritensRemun", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURITENSREMUN"), )

        ordering = [
            's1202_infoperapur_remunperapur',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1202infoPerApuritensRemunSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApuritensRemun
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202infoPerApurremunPerApur(SoftDeletionModel):

    s1202_infoperapur_ideestab = models.ForeignKey('s1202.s1202infoPerApurideEstab',
        related_name='%(class)s_s1202_infoperapur_ideestab', )

    def evento(self):
        return self.s1202_infoperapur_ideestab.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1202_infoperapur_ideestab) + ' - ' + unicode(self.codcateg)

    class Meta:

        # verbose_name = u'Informações relativas a remuneração do trabalhador no período de apuração'
        db_table = r's1202_infoperapur_remunperapur'
        managed = True # s1202_infoperapur_remunperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202infoPerApurremunPerApur", u"Pode ver listagem do modelo S1202INFOPERAPURREMUNPERAPUR"),
            ("can_see_data_s1202infoPerApurremunPerApur", u"Pode visualizar o conteúdo do modelo S1202INFOPERAPURREMUNPERAPUR"),
            ("can_see_menu_s1202infoPerApurremunPerApur", u"Pode visualizar no menu o modelo S1202INFOPERAPURREMUNPERAPUR"),
            ("can_print_list_s1202infoPerApurremunPerApur", u"Pode imprimir listagem do modelo S1202INFOPERAPURREMUNPERAPUR"),
            ("can_print_data_s1202infoPerApurremunPerApur", u"Pode imprimir o conteúdo do modelo S1202INFOPERAPURREMUNPERAPUR"), )

        ordering = [
            's1202_infoperapur_ideestab',
            'codcateg',]



class s1202infoPerApurremunPerApurSerializer(ModelSerializer):

    class Meta:

        model = s1202infoPerApurremunPerApur
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202procJudTrab(SoftDeletionModel):

    s1202_evtrmnrpps = models.ForeignKey('esocial.s1202evtRmnRPPS',
        related_name='%(class)s_s1202_evtrmnrpps', )

    def evento(self):
        return self.s1202_evtrmnrpps.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1202_TPTRIB, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1202_evtrmnrpps) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)

    class Meta:

        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's1202_procjudtrab'
        managed = True # s1202_procjudtrab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1202procJudTrab", u"Pode ver listagem do modelo S1202PROCJUDTRAB"),
            ("can_see_data_s1202procJudTrab", u"Pode visualizar o conteúdo do modelo S1202PROCJUDTRAB"),
            ("can_see_menu_s1202procJudTrab", u"Pode visualizar no menu o modelo S1202PROCJUDTRAB"),
            ("can_print_list_s1202procJudTrab", u"Pode imprimir listagem do modelo S1202PROCJUDTRAB"),
            ("can_print_data_s1202procJudTrab", u"Pode imprimir o conteúdo do modelo S1202PROCJUDTRAB"), )

        ordering = [
            's1202_evtrmnrpps',
            'tptrib',
            'nrprocjud',]



class s1202procJudTrabSerializer(ModelSerializer):

    class Meta:

        model = s1202procJudTrab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')