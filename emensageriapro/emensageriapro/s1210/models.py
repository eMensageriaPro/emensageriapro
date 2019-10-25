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
from emensageriapro.s1210.choices import *
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





class s1210deps(SoftDeletionModel):

    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos', )

    def evento(self):
        return self.s1210_evtpgtos.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.vrdeddep)

    class Meta:

        # verbose_name = u'Informações de dependentes do beneficiário do pagamento'
        db_table = r's1210_deps'
        managed = True # s1210_deps #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210deps", u"Pode ver listagem do modelo S1210DEPS"),
            ("can_see_data_s1210deps", u"Pode visualizar o conteúdo do modelo S1210DEPS"),
            ("can_see_menu_s1210deps", u"Pode visualizar no menu o modelo S1210DEPS"),
            ("can_print_list_s1210deps", u"Pode imprimir listagem do modelo S1210DEPS"),
            ("can_print_data_s1210deps", u"Pode imprimir o conteúdo do modelo S1210DEPS"), )

        ordering = [
            's1210_evtpgtos',
            'vrdeddep',]



class s1210depsSerializer(ModelSerializer):

    class Meta:

        model = s1210deps
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoAnt(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto',
        related_name='%(class)s_s1210_infopgto', )

    def evento(self):
        return self.s1210_infopgto.evento()
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg)

    class Meta:

        # verbose_name = u'Pagamento relativo a competências anteriores ao início de obrigatoriedade do eSocial'
        db_table = r's1210_detpgtoant'
        managed = True # s1210_detpgtoant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoAnt", u"Pode ver listagem do modelo S1210DETPGTOANT"),
            ("can_see_data_s1210detPgtoAnt", u"Pode visualizar o conteúdo do modelo S1210DETPGTOANT"),
            ("can_see_menu_s1210detPgtoAnt", u"Pode visualizar no menu o modelo S1210DETPGTOANT"),
            ("can_print_list_s1210detPgtoAnt", u"Pode imprimir listagem do modelo S1210DETPGTOANT"),
            ("can_print_data_s1210detPgtoAnt", u"Pode imprimir o conteúdo do modelo S1210DETPGTOANT"), )

        ordering = [
            's1210_infopgto',
            'codcateg',]



class s1210detPgtoAntSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoAntinfoPgtoAnt(SoftDeletionModel):

    s1210_detpgtoant = models.ForeignKey('s1210.s1210detPgtoAnt',
        related_name='%(class)s_s1210_detpgtoant', )

    def evento(self):
        return self.s1210_detpgtoant.evento()
    tpbcirrf = models.TextField(null=True, )
    vrbcirrf = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtoant) + ' - ' + unicode(self.tpbcirrf) + ' - ' + unicode(self.vrbcirrf)

    class Meta:

        # verbose_name = u'Detalhamento do pagamento'
        db_table = r's1210_detpgtoant_infopgtoant'
        managed = True # s1210_detpgtoant_infopgtoant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoAntinfoPgtoAnt", u"Pode ver listagem do modelo S1210DETPGTOANTINFOPGTOANT"),
            ("can_see_data_s1210detPgtoAntinfoPgtoAnt", u"Pode visualizar o conteúdo do modelo S1210DETPGTOANTINFOPGTOANT"),
            ("can_see_menu_s1210detPgtoAntinfoPgtoAnt", u"Pode visualizar no menu o modelo S1210DETPGTOANTINFOPGTOANT"),
            ("can_print_list_s1210detPgtoAntinfoPgtoAnt", u"Pode imprimir listagem do modelo S1210DETPGTOANTINFOPGTOANT"),
            ("can_print_data_s1210detPgtoAntinfoPgtoAnt", u"Pode imprimir o conteúdo do modelo S1210DETPGTOANTINFOPGTOANT"), )

        ordering = [
            's1210_detpgtoant',
            'tpbcirrf',
            'vrbcirrf',]



class s1210detPgtoAntinfoPgtoAntSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoAntinfoPgtoAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoBenPr(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto',
        related_name='%(class)s_s1210_infopgto', )

    def evento(self):
        return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7, null=True, )
    idedmdev = models.CharField(max_length=30, null=True, )
    indpgtott = models.CharField(choices=CHOICES_S1210_INDPGTOTT_DETPGTOBENPR, max_length=1, null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.perref) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq)

    class Meta:

        # verbose_name = u'Detalhamento de pagamentos relativos a benefícios previdenciários'
        db_table = r's1210_detpgtobenpr'
        managed = True # s1210_detpgtobenpr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoBenPr", u"Pode ver listagem do modelo S1210DETPGTOBENPR"),
            ("can_see_data_s1210detPgtoBenPr", u"Pode visualizar o conteúdo do modelo S1210DETPGTOBENPR"),
            ("can_see_menu_s1210detPgtoBenPr", u"Pode visualizar no menu o modelo S1210DETPGTOBENPR"),
            ("can_print_list_s1210detPgtoBenPr", u"Pode imprimir listagem do modelo S1210DETPGTOBENPR"),
            ("can_print_data_s1210detPgtoBenPr", u"Pode imprimir o conteúdo do modelo S1210DETPGTOBENPR"), )

        ordering = [
            's1210_infopgto',
            'perref',
            'idedmdev',
            'indpgtott',
            'vrliq',]



class s1210detPgtoBenPrSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoBenPr
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoBenPrinfoPgtoParc(SoftDeletionModel):

    s1210_detpgtobenpr = models.ForeignKey('s1210.s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr', )

    def evento(self):
        return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Informações complentares relacionadas ao pagamento efetuado em valor menor que o apurado no demonstrativo.'
        db_table = r's1210_detpgtobenpr_infopgtoparc'
        managed = True # s1210_detpgtobenpr_infopgtoparc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoBenPrinfoPgtoParc", u"Pode ver listagem do modelo S1210DETPGTOBENPRINFOPGTOPARC"),
            ("can_see_data_s1210detPgtoBenPrinfoPgtoParc", u"Pode visualizar o conteúdo do modelo S1210DETPGTOBENPRINFOPGTOPARC"),
            ("can_see_menu_s1210detPgtoBenPrinfoPgtoParc", u"Pode visualizar no menu o modelo S1210DETPGTOBENPRINFOPGTOPARC"),
            ("can_print_list_s1210detPgtoBenPrinfoPgtoParc", u"Pode imprimir listagem do modelo S1210DETPGTOBENPRINFOPGTOPARC"),
            ("can_print_data_s1210detPgtoBenPrinfoPgtoParc", u"Pode imprimir o conteúdo do modelo S1210DETPGTOBENPRINFOPGTOPARC"), )

        ordering = [
            's1210_detpgtobenpr',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoBenPrinfoPgtoParcSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoBenPrinfoPgtoParc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoBenPrretPgtoTot(SoftDeletionModel):

    s1210_detpgtobenpr = models.ForeignKey('s1210.s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr', )

    def evento(self):
        return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Retenções efetuadas no ato do pagamento pelo valor total do demonstrativo.'
        db_table = r's1210_detpgtobenpr_retpgtotot'
        managed = True # s1210_detpgtobenpr_retpgtotot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoBenPrretPgtoTot", u"Pode ver listagem do modelo S1210DETPGTOBENPRRETPGTOTOT"),
            ("can_see_data_s1210detPgtoBenPrretPgtoTot", u"Pode visualizar o conteúdo do modelo S1210DETPGTOBENPRRETPGTOTOT"),
            ("can_see_menu_s1210detPgtoBenPrretPgtoTot", u"Pode visualizar no menu o modelo S1210DETPGTOBENPRRETPGTOTOT"),
            ("can_print_list_s1210detPgtoBenPrretPgtoTot", u"Pode imprimir listagem do modelo S1210DETPGTOBENPRRETPGTOTOT"),
            ("can_print_data_s1210detPgtoBenPrretPgtoTot", u"Pode imprimir o conteúdo do modelo S1210DETPGTOBENPRRETPGTOTOT"), )

        ordering = [
            's1210_detpgtobenpr',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoBenPrretPgtoTotSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoBenPrretPgtoTot
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFer(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto',
        related_name='%(class)s_s1210_infopgto', )

    def evento(self):
        return self.s1210_infopgto.evento()
    codcateg = models.IntegerField(null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    dtinigoz = models.DateField(null=True, )
    qtdias = models.IntegerField(null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtinigoz) + ' - ' + unicode(self.qtdias) + ' - ' + unicode(self.vrliq)

    class Meta:

        # verbose_name = u'Detalhamento dos pagamentos efetuados relativos a férias'
        db_table = r's1210_detpgtofer'
        managed = True # s1210_detpgtofer #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFer", u"Pode ver listagem do modelo S1210DETPGTOFER"),
            ("can_see_data_s1210detPgtoFer", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFER"),
            ("can_see_menu_s1210detPgtoFer", u"Pode visualizar no menu o modelo S1210DETPGTOFER"),
            ("can_print_list_s1210detPgtoFer", u"Pode imprimir listagem do modelo S1210DETPGTOFER"),
            ("can_print_data_s1210detPgtoFer", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFER"), )

        ordering = [
            's1210_infopgto',
            'codcateg',
            'dtinigoz',
            'qtdias',
            'vrliq',]



class s1210detPgtoFerSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFer
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFerdetRubrFer(SoftDeletionModel):

    s1210_detpgtofer = models.ForeignKey('s1210.s1210detPgtoFer',
        related_name='%(class)s_s1210_detpgtofer', )

    def evento(self):
        return self.s1210_detpgtofer.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtofer) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Detalhamento das rubricas do Recibo Antecipado de Férias'
        db_table = r's1210_detpgtofer_detrubrfer'
        managed = True # s1210_detpgtofer_detrubrfer #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFerdetRubrFer", u"Pode ver listagem do modelo S1210DETPGTOFERDETRUBRFER"),
            ("can_see_data_s1210detPgtoFerdetRubrFer", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFERDETRUBRFER"),
            ("can_see_menu_s1210detPgtoFerdetRubrFer", u"Pode visualizar no menu o modelo S1210DETPGTOFERDETRUBRFER"),
            ("can_print_list_s1210detPgtoFerdetRubrFer", u"Pode imprimir listagem do modelo S1210DETPGTOFERDETRUBRFER"),
            ("can_print_data_s1210detPgtoFerdetRubrFer", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFERDETRUBRFER"), )

        ordering = [
            's1210_detpgtofer',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFerdetRubrFerSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFerdetRubrFer
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFerpenAlim(SoftDeletionModel):

    s1210_detpgtofer_detrubrfer = models.ForeignKey('s1210.s1210detPgtoFerdetRubrFer',
        related_name='%(class)s_s1210_detpgtofer_detrubrfer', )

    def evento(self):
        return self.s1210_detpgtofer_detrubrfer.evento()
    cpfbenef = models.CharField(max_length=11, null=True, )
    dtnasctobenef = models.DateField(blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtofer_detrubrfer) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)

    class Meta:

        # verbose_name = u'Informações sobre beneficiários de pensão alimentícia.'
        db_table = r's1210_detpgtofer_penalim'
        managed = True # s1210_detpgtofer_penalim #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFerpenAlim", u"Pode ver listagem do modelo S1210DETPGTOFERPENALIM"),
            ("can_see_data_s1210detPgtoFerpenAlim", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFERPENALIM"),
            ("can_see_menu_s1210detPgtoFerpenAlim", u"Pode visualizar no menu o modelo S1210DETPGTOFERPENALIM"),
            ("can_print_list_s1210detPgtoFerpenAlim", u"Pode imprimir listagem do modelo S1210DETPGTOFERPENALIM"),
            ("can_print_data_s1210detPgtoFerpenAlim", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFERPENALIM"), )

        ordering = [
            's1210_detpgtofer_detrubrfer',
            'cpfbenef',
            'nmbenefic',
            'vlrpensao',]



class s1210detPgtoFerpenAlimSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFerpenAlim
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFl(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto',
        related_name='%(class)s_s1210_infopgto', )

    def evento(self):
        return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7, blank=True, null=True, )
    idedmdev = models.CharField(max_length=30, null=True, )
    indpgtott = models.CharField(choices=CHOICES_S1210_INDPGTOTT_DETPGTOFL, max_length=1, null=True, )
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    nrrecarq = models.CharField(max_length=40, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq)

    class Meta:

        # verbose_name = u'Detalhamento dos pagamentos efetuados, relativos a folha de pagamento e rescisões contratuais, apurados em S-1200, S-1202, S-2299 e S-2399'
        db_table = r's1210_detpgtofl'
        managed = True # s1210_detpgtofl #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFl", u"Pode ver listagem do modelo S1210DETPGTOFL"),
            ("can_see_data_s1210detPgtoFl", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFL"),
            ("can_see_menu_s1210detPgtoFl", u"Pode visualizar no menu o modelo S1210DETPGTOFL"),
            ("can_print_list_s1210detPgtoFl", u"Pode imprimir listagem do modelo S1210DETPGTOFL"),
            ("can_print_data_s1210detPgtoFl", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFL"), )

        ordering = [
            's1210_infopgto',
            'idedmdev',
            'indpgtott',
            'vrliq',]



class s1210detPgtoFlSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFl
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFlinfoPgtoParc(SoftDeletionModel):

    s1210_detpgtofl = models.ForeignKey('s1210.s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl', )

    def evento(self):
        return self.s1210_detpgtofl.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Informações complentares relacionadas ao pagamento efetuado em valor menor que o apurado no demonstrativo.'
        db_table = r's1210_detpgtofl_infopgtoparc'
        managed = True # s1210_detpgtofl_infopgtoparc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFlinfoPgtoParc", u"Pode ver listagem do modelo S1210DETPGTOFLINFOPGTOPARC"),
            ("can_see_data_s1210detPgtoFlinfoPgtoParc", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFLINFOPGTOPARC"),
            ("can_see_menu_s1210detPgtoFlinfoPgtoParc", u"Pode visualizar no menu o modelo S1210DETPGTOFLINFOPGTOPARC"),
            ("can_print_list_s1210detPgtoFlinfoPgtoParc", u"Pode imprimir listagem do modelo S1210DETPGTOFLINFOPGTOPARC"),
            ("can_print_data_s1210detPgtoFlinfoPgtoParc", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFLINFOPGTOPARC"), )

        ordering = [
            's1210_detpgtofl',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFlinfoPgtoParcSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFlinfoPgtoParc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFlpenAlim(SoftDeletionModel):

    s1210_detpgtofl_retpgtotot = models.ForeignKey('s1210.s1210detPgtoFlretPgtoTot',
        related_name='%(class)s_s1210_detpgtofl_retpgtotot', )

    def evento(self):
        return self.s1210_detpgtofl_retpgtotot.evento()
    cpfbenef = models.CharField(max_length=11, null=True, )
    dtnasctobenef = models.DateField(blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtofl_retpgtotot) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)

    class Meta:

        # verbose_name = u'Informações sobre beneficiários de pensão alimentícia.'
        db_table = r's1210_detpgtofl_penalim'
        managed = True # s1210_detpgtofl_penalim #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFlpenAlim", u"Pode ver listagem do modelo S1210DETPGTOFLPENALIM"),
            ("can_see_data_s1210detPgtoFlpenAlim", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFLPENALIM"),
            ("can_see_menu_s1210detPgtoFlpenAlim", u"Pode visualizar no menu o modelo S1210DETPGTOFLPENALIM"),
            ("can_print_list_s1210detPgtoFlpenAlim", u"Pode imprimir listagem do modelo S1210DETPGTOFLPENALIM"),
            ("can_print_data_s1210detPgtoFlpenAlim", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFLPENALIM"), )

        ordering = [
            's1210_detpgtofl_retpgtotot',
            'cpfbenef',
            'nmbenefic',
            'vlrpensao',]



class s1210detPgtoFlpenAlimSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFlpenAlim
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210detPgtoFlretPgtoTot(SoftDeletionModel):

    s1210_detpgtofl = models.ForeignKey('s1210.s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl', )

    def evento(self):
        return self.s1210_detpgtofl.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Retenções efetuadas no ato do pagamento pelo valor total do demonstrativo.'
        db_table = r's1210_detpgtofl_retpgtotot'
        managed = True # s1210_detpgtofl_retpgtotot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210detPgtoFlretPgtoTot", u"Pode ver listagem do modelo S1210DETPGTOFLRETPGTOTOT"),
            ("can_see_data_s1210detPgtoFlretPgtoTot", u"Pode visualizar o conteúdo do modelo S1210DETPGTOFLRETPGTOTOT"),
            ("can_see_menu_s1210detPgtoFlretPgtoTot", u"Pode visualizar no menu o modelo S1210DETPGTOFLRETPGTOTOT"),
            ("can_print_list_s1210detPgtoFlretPgtoTot", u"Pode imprimir listagem do modelo S1210DETPGTOFLRETPGTOTOT"),
            ("can_print_data_s1210detPgtoFlretPgtoTot", u"Pode imprimir o conteúdo do modelo S1210DETPGTOFLRETPGTOTOT"), )

        ordering = [
            's1210_detpgtofl',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1210detPgtoFlretPgtoTotSerializer(ModelSerializer):

    class Meta:

        model = s1210detPgtoFlretPgtoTot
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210idePgtoExt(SoftDeletionModel):

    s1210_infopgto = models.ForeignKey('s1210.s1210infoPgto',
        related_name='%(class)s_s1210_infopgto', )

    def evento(self):
        return self.s1210_infopgto.evento()
    codpais = models.TextField(null=True, )
    indnif = models.IntegerField(choices=CHOICES_S1210_INDNIF_IDEPGTOEXT, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codpais) + ' - ' + unicode(self.indnif) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nmcid)

    class Meta:

        # verbose_name = u'Informações complementares relativas a pagamentos efetuados a beneficiário residente fiscal no exterior.'
        db_table = r's1210_idepgtoext'
        managed = True # s1210_idepgtoext #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210idePgtoExt", u"Pode ver listagem do modelo S1210IDEPGTOEXT"),
            ("can_see_data_s1210idePgtoExt", u"Pode visualizar o conteúdo do modelo S1210IDEPGTOEXT"),
            ("can_see_menu_s1210idePgtoExt", u"Pode visualizar no menu o modelo S1210IDEPGTOEXT"),
            ("can_print_list_s1210idePgtoExt", u"Pode imprimir listagem do modelo S1210IDEPGTOEXT"),
            ("can_print_data_s1210idePgtoExt", u"Pode imprimir o conteúdo do modelo S1210IDEPGTOEXT"), )

        ordering = [
            's1210_infopgto',
            'codpais',
            'indnif',
            'dsclograd',
            'nmcid',]



class s1210idePgtoExtSerializer(ModelSerializer):

    class Meta:

        model = s1210idePgtoExt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210infoPgto(SoftDeletionModel):

    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos', )

    def evento(self):
        return self.s1210_evtpgtos.evento()
    dtpgto = models.DateField(null=True, )
    tppgto = models.IntegerField(choices=CHOICES_S1210_TPPGTO, null=True, )
    indresbr = models.CharField(choices=CHOICES_S1210_INDRESBR, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.dtpgto) + ' - ' + unicode(self.tppgto) + ' - ' + unicode(self.indresbr)

    class Meta:

        # verbose_name = u'Informações dos pagamentos efetuados'
        db_table = r's1210_infopgto'
        managed = True # s1210_infopgto #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1210infoPgto", u"Pode ver listagem do modelo S1210INFOPGTO"),
            ("can_see_data_s1210infoPgto", u"Pode visualizar o conteúdo do modelo S1210INFOPGTO"),
            ("can_see_menu_s1210infoPgto", u"Pode visualizar no menu o modelo S1210INFOPGTO"),
            ("can_print_list_s1210infoPgto", u"Pode imprimir listagem do modelo S1210INFOPGTO"),
            ("can_print_data_s1210infoPgto", u"Pode imprimir o conteúdo do modelo S1210INFOPGTO"), )

        ordering = [
            's1210_evtpgtos',
            'dtpgto',
            'tppgto',
            'indresbr',]



class s1210infoPgtoSerializer(ModelSerializer):

    class Meta:

        model = s1210infoPgto
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')