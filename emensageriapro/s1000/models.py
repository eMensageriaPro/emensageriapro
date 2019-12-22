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
from emensageriapro.s1000.choices import *
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





class s1000alteracao(SoftDeletionModel):

    s1000_evtinfoempregador = models.ForeignKey('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador', )

    def evento(self):
        return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    nmrazao = models.CharField(max_length=100, blank=True, null=True, )
    classtrib = models.CharField(choices=CHOICES_ESOCIALCLASSIFICACOESTRIBUTARIAS, max_length=2, null=True, )
    natjurid = models.TextField(blank=True, null=True, )
    indcoop = models.IntegerField(choices=CHOICES_S1000_INDCOOP_ALTERACAO, blank=True, null=True, )
    indconstr = models.IntegerField(choices=CHOICES_S1000_INDCONSTR_ALTERACAO, blank=True, null=True, )
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_INDDESFOLHA_ALTERACAO, null=True, )
    indopccp = models.IntegerField(choices=CHOICES_S1000_INDOPCCP_ALTERACAO, blank=True, null=True, )
    indporte = models.CharField(choices=CHOICES_S1000_INDPORTE_ALTERACAO, max_length=1, blank=True, null=True, )
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_INDOPTREGELETRON_ALTERACAO, null=True, )
    indented = models.CharField(choices=CHOICES_S1000_INDENTED_ALTERACAO, max_length=1, blank=True, null=True, )
    indett = models.CharField(choices=CHOICES_S1000_INDETT_ALTERACAO, max_length=1, blank=True, null=True, )
    nrregett = models.CharField(max_length=30, blank=True, null=True, )
    nmctt = models.CharField(max_length=70, null=True, )
    cpfctt = models.CharField(max_length=11, null=True, )
    fonefixo = models.CharField(max_length=13, blank=True, null=True, )
    fonecel = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)

    class Meta:

        # verbose_name = u'Alteração das informações'
        db_table = r's1000_alteracao'
        managed = True # s1000_alteracao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracao", u"Pode ver listagem do modelo S1000ALTERACAO"),
            ("can_see_data_s1000alteracao", u"Pode visualizar o conteúdo do modelo S1000ALTERACAO"),
            ("can_see_menu_s1000alteracao", u"Pode visualizar no menu o modelo S1000ALTERACAO"),
            ("can_print_list_s1000alteracao", u"Pode imprimir listagem do modelo S1000ALTERACAO"),
            ("can_print_data_s1000alteracao", u"Pode imprimir o conteúdo do modelo S1000ALTERACAO"), )

        ordering = [
            's1000_evtinfoempregador',
            'inivalid',
            'classtrib',
            'inddesfolha',
            'indoptregeletron',
            'nmctt',
            'cpfctt',]



class s1000alteracaoSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaodadosIsencao(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    ideminlei = models.CharField(max_length=70, null=True, )
    nrcertif = models.CharField(max_length=40, null=True, )
    dtemiscertif = models.DateField(null=True, )
    dtvenccertif = models.DateField(null=True, )
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True, )
    dtprotrenov = models.DateField(blank=True, null=True, )
    dtdou = models.DateField(blank=True, null=True, )
    pagdou = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif)

    class Meta:

        # verbose_name = u'Informações Complementares - Empresas Isentas - Dados da Isenção'
        db_table = r's1000_alteracao_dadosisencao'
        managed = True # s1000_alteracao_dadosisencao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaodadosIsencao", u"Pode ver listagem do modelo S1000ALTERACAODADOSISENCAO"),
            ("can_see_data_s1000alteracaodadosIsencao", u"Pode visualizar o conteúdo do modelo S1000ALTERACAODADOSISENCAO"),
            ("can_see_menu_s1000alteracaodadosIsencao", u"Pode visualizar no menu o modelo S1000ALTERACAODADOSISENCAO"),
            ("can_print_list_s1000alteracaodadosIsencao", u"Pode imprimir listagem do modelo S1000ALTERACAODADOSISENCAO"),
            ("can_print_data_s1000alteracaodadosIsencao", u"Pode imprimir o conteúdo do modelo S1000ALTERACAODADOSISENCAO"), )

        ordering = [
            's1000_alteracao',
            'ideminlei',
            'nrcertif',
            'dtemiscertif',
            'dtvenccertif',]



class s1000alteracaodadosIsencaoSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaodadosIsencao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaoinfoEFR(SoftDeletionModel):

    s1000_alteracao_infoop = models.ForeignKey('s1000.s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop', )

    def evento(self):
        return self.s1000_alteracao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_IDEEFR_ALTERACAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    indrpps = models.CharField(choices=CHOICES_S1000_INDRPPS_ALTERACAO, max_length=1, null=True, )
    prevcomp = models.CharField(choices=CHOICES_S1000_PREVCOMP_ALTERACAO, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.prevcomp)

    class Meta:

        # verbose_name = u'Informações relativas a Ente Federativo Responsável - EFR'
        db_table = r's1000_alteracao_infoefr'
        managed = True # s1000_alteracao_infoefr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaoinfoEFR", u"Pode ver listagem do modelo S1000ALTERACAOINFOEFR"),
            ("can_see_data_s1000alteracaoinfoEFR", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOINFOEFR"),
            ("can_see_menu_s1000alteracaoinfoEFR", u"Pode visualizar no menu o modelo S1000ALTERACAOINFOEFR"),
            ("can_print_list_s1000alteracaoinfoEFR", u"Pode imprimir listagem do modelo S1000ALTERACAOINFOEFR"),
            ("can_print_data_s1000alteracaoinfoEFR", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOINFOEFR"), )

        ordering = [
            's1000_alteracao_infoop',
            'ideefr',
            'indrpps',
            'prevcomp',]



class s1000alteracaoinfoEFRSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaoinfoEFR
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaoinfoEnte(SoftDeletionModel):

    s1000_alteracao_infoop = models.ForeignKey('s1000.s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop', )

    def evento(self):
        return self.s1000_alteracao_infoop.evento()
    nmente = models.CharField(max_length=100, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.IntegerField(blank=True, null=True, )
    indrpps = models.CharField(choices=CHOICES_S1000_INDRPPS_ALTERACAO, max_length=1, null=True, )
    subteto = models.IntegerField(choices=CHOICES_S1000_SUBTETO_ALTERACAO, null=True, )
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)

    class Meta:

        # verbose_name = u'Informações relativas ao ente federativo estadual, distrital ou municipal'
        db_table = r's1000_alteracao_infoente'
        managed = True # s1000_alteracao_infoente #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaoinfoEnte", u"Pode ver listagem do modelo S1000ALTERACAOINFOENTE"),
            ("can_see_data_s1000alteracaoinfoEnte", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOINFOENTE"),
            ("can_see_menu_s1000alteracaoinfoEnte", u"Pode visualizar no menu o modelo S1000ALTERACAOINFOENTE"),
            ("can_print_list_s1000alteracaoinfoEnte", u"Pode imprimir listagem do modelo S1000ALTERACAOINFOENTE"),
            ("can_print_data_s1000alteracaoinfoEnte", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOINFOENTE"), )

        ordering = [
            's1000_alteracao_infoop',
            'nmente',
            'uf',
            'indrpps',
            'subteto',
            'vrsubteto',]



class s1000alteracaoinfoEnteSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaoinfoEnte
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaoinfoOP(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    nrsiafi = models.CharField(max_length=6, null=True, )
    indugrpps = models.CharField(choices=CHOICES_S1000_INDUGRPPS_ALTERACAO, max_length=1, null=True, )
    esferaop = models.IntegerField(choices=CHOICES_S1000_ESFERAOP_ALTERACAO, blank=True, null=True, )
    poderop = models.IntegerField(choices=CHOICES_S1000_PODEROP_ALTERACAO, null=True, )
    vrtetorem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    ideefr = models.CharField(choices=CHOICES_S1000_IDEEFR_ALTERACAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.nrsiafi) + ' - ' + unicode(self.indugrpps) + ' - ' + unicode(self.poderop) + ' - ' + unicode(self.vrtetorem) + ' - ' + unicode(self.ideefr)

    class Meta:

        # verbose_name = u'Informações relativas a Órgãos Públicos'
        db_table = r's1000_alteracao_infoop'
        managed = True # s1000_alteracao_infoop #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaoinfoOP", u"Pode ver listagem do modelo S1000ALTERACAOINFOOP"),
            ("can_see_data_s1000alteracaoinfoOP", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOINFOOP"),
            ("can_see_menu_s1000alteracaoinfoOP", u"Pode visualizar no menu o modelo S1000ALTERACAOINFOOP"),
            ("can_print_list_s1000alteracaoinfoOP", u"Pode imprimir listagem do modelo S1000ALTERACAOINFOOP"),
            ("can_print_data_s1000alteracaoinfoOP", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOINFOOP"), )

        ordering = [
            's1000_alteracao',
            'nrsiafi',
            'indugrpps',
            'poderop',
            'vrtetorem',
            'ideefr',]



class s1000alteracaoinfoOPSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaoinfoOP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaoinfoOrgInternacional(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_INDACORDOISENMULTA_ALTERACAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indacordoisenmulta)

    class Meta:

        # verbose_name = u'Informações exclusivas de organismos internacionais e outras instituições extraterritoriais'
        db_table = r's1000_alteracao_infoorginternacional'
        managed = True # s1000_alteracao_infoorginternacional #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaoinfoOrgInternacional", u"Pode ver listagem do modelo S1000ALTERACAOINFOORGINTERNACIONAL"),
            ("can_see_data_s1000alteracaoinfoOrgInternacional", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOINFOORGINTERNACIONAL"),
            ("can_see_menu_s1000alteracaoinfoOrgInternacional", u"Pode visualizar no menu o modelo S1000ALTERACAOINFOORGINTERNACIONAL"),
            ("can_print_list_s1000alteracaoinfoOrgInternacional", u"Pode imprimir listagem do modelo S1000ALTERACAOINFOORGINTERNACIONAL"),
            ("can_print_data_s1000alteracaoinfoOrgInternacional", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOINFOORGINTERNACIONAL"), )

        ordering = [
            's1000_alteracao',
            'indacordoisenmulta',]



class s1000alteracaoinfoOrgInternacionalSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaoinfoOrgInternacional
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaonovaValidade(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1000_alteracao_novavalidade'
        managed = True # s1000_alteracao_novavalidade #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaonovaValidade", u"Pode ver listagem do modelo S1000ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1000alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1000ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1000alteracaonovaValidade", u"Pode visualizar no menu o modelo S1000ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1000alteracaonovaValidade", u"Pode imprimir listagem do modelo S1000ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1000alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1000ALTERACAONOVAVALIDADE"), )

        ordering = [
            's1000_alteracao',
            'inivalid',]



class s1000alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaosituacaoPF(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_INDSITPF_ALTERACAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpf)

    class Meta:

        # verbose_name = u'Informações Complementares - Pessoa Física'
        db_table = r's1000_alteracao_situacaopf'
        managed = True # s1000_alteracao_situacaopf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaosituacaoPF", u"Pode ver listagem do modelo S1000ALTERACAOSITUACAOPF"),
            ("can_see_data_s1000alteracaosituacaoPF", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOSITUACAOPF"),
            ("can_see_menu_s1000alteracaosituacaoPF", u"Pode visualizar no menu o modelo S1000ALTERACAOSITUACAOPF"),
            ("can_print_list_s1000alteracaosituacaoPF", u"Pode imprimir listagem do modelo S1000ALTERACAOSITUACAOPF"),
            ("can_print_data_s1000alteracaosituacaoPF", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOSITUACAOPF"), )

        ordering = [
            's1000_alteracao',
            'indsitpf',]



class s1000alteracaosituacaoPFSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaosituacaoPF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaosituacaoPJ(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_INDSITPJ_ALTERACAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpj)

    class Meta:

        # verbose_name = u'Informações Complementares - Pessoa Jurídica'
        db_table = r's1000_alteracao_situacaopj'
        managed = True # s1000_alteracao_situacaopj #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaosituacaoPJ", u"Pode ver listagem do modelo S1000ALTERACAOSITUACAOPJ"),
            ("can_see_data_s1000alteracaosituacaoPJ", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOSITUACAOPJ"),
            ("can_see_menu_s1000alteracaosituacaoPJ", u"Pode visualizar no menu o modelo S1000ALTERACAOSITUACAOPJ"),
            ("can_print_list_s1000alteracaosituacaoPJ", u"Pode imprimir listagem do modelo S1000ALTERACAOSITUACAOPJ"),
            ("can_print_data_s1000alteracaosituacaoPJ", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOSITUACAOPJ"), )

        ordering = [
            's1000_alteracao',
            'indsitpj',]



class s1000alteracaosituacaoPJSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaosituacaoPJ
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000alteracaosoftwareHouse(SoftDeletionModel):

    s1000_alteracao = models.ForeignKey('s1000.s1000alteracao',
        related_name='%(class)s_s1000_alteracao', )

    def evento(self):
        return self.s1000_alteracao.evento()
    cnpjsofthouse = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=100, blank=True, null=True, )
    nmcont = models.CharField(max_length=70, null=True, )
    telefone = models.CharField(max_length=13, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone)

    class Meta:

        # verbose_name = u'Informações relativas ao desenvolvedor do software que gerou o arquivo xml.'
        db_table = r's1000_alteracao_softwarehouse'
        managed = True # s1000_alteracao_softwarehouse #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000alteracaosoftwareHouse", u"Pode ver listagem do modelo S1000ALTERACAOSOFTWAREHOUSE"),
            ("can_see_data_s1000alteracaosoftwareHouse", u"Pode visualizar o conteúdo do modelo S1000ALTERACAOSOFTWAREHOUSE"),
            ("can_see_menu_s1000alteracaosoftwareHouse", u"Pode visualizar no menu o modelo S1000ALTERACAOSOFTWAREHOUSE"),
            ("can_print_list_s1000alteracaosoftwareHouse", u"Pode imprimir listagem do modelo S1000ALTERACAOSOFTWAREHOUSE"),
            ("can_print_data_s1000alteracaosoftwareHouse", u"Pode imprimir o conteúdo do modelo S1000ALTERACAOSOFTWAREHOUSE"), )

        ordering = [
            's1000_alteracao',
            'cnpjsofthouse',
            'nmcont',
            'telefone',]



class s1000alteracaosoftwareHouseSerializer(ModelSerializer):

    class Meta:

        model = s1000alteracaosoftwareHouse
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000exclusao(SoftDeletionModel):

    s1000_evtinfoempregador = models.ForeignKey('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador', )

    def evento(self):
        return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Exclusão das informações'
        db_table = r's1000_exclusao'
        managed = True # s1000_exclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000exclusao", u"Pode ver listagem do modelo S1000EXCLUSAO"),
            ("can_see_data_s1000exclusao", u"Pode visualizar o conteúdo do modelo S1000EXCLUSAO"),
            ("can_see_menu_s1000exclusao", u"Pode visualizar no menu o modelo S1000EXCLUSAO"),
            ("can_print_list_s1000exclusao", u"Pode imprimir listagem do modelo S1000EXCLUSAO"),
            ("can_print_data_s1000exclusao", u"Pode imprimir o conteúdo do modelo S1000EXCLUSAO"), )

        ordering = [
            's1000_evtinfoempregador',
            'inivalid',]



class s1000exclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1000exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusao(SoftDeletionModel):

    s1000_evtinfoempregador = models.ForeignKey('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador', )

    def evento(self):
        return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    nmrazao = models.CharField(max_length=100, blank=True, null=True, )
    classtrib = models.CharField(choices=CHOICES_ESOCIALCLASSIFICACOESTRIBUTARIAS, max_length=2, null=True, )
    natjurid = models.TextField(blank=True, null=True, )
    indcoop = models.IntegerField(choices=CHOICES_S1000_INDCOOP_INCLUSAO, blank=True, null=True, )
    indconstr = models.IntegerField(choices=CHOICES_S1000_INDCONSTR_INCLUSAO, blank=True, null=True, )
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_INDDESFOLHA_INCLUSAO, null=True, )
    indopccp = models.IntegerField(choices=CHOICES_S1000_INDOPCCP_INCLUSAO, blank=True, null=True, )
    indporte = models.CharField(choices=CHOICES_S1000_INDPORTE_INCLUSAO, max_length=1, blank=True, null=True, )
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_INDOPTREGELETRON_INCLUSAO, null=True, )
    indented = models.CharField(choices=CHOICES_S1000_INDENTED_INCLUSAO, max_length=1, blank=True, null=True, )
    indett = models.CharField(choices=CHOICES_S1000_INDETT_INCLUSAO, max_length=1, blank=True, null=True, )
    nrregett = models.CharField(max_length=30, blank=True, null=True, )
    nmctt = models.CharField(max_length=70, null=True, )
    cpfctt = models.CharField(max_length=11, null=True, )
    fonefixo = models.CharField(max_length=13, blank=True, null=True, )
    fonecel = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)

    class Meta:

        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1000_inclusao'
        managed = True # s1000_inclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusao", u"Pode ver listagem do modelo S1000INCLUSAO"),
            ("can_see_data_s1000inclusao", u"Pode visualizar o conteúdo do modelo S1000INCLUSAO"),
            ("can_see_menu_s1000inclusao", u"Pode visualizar no menu o modelo S1000INCLUSAO"),
            ("can_print_list_s1000inclusao", u"Pode imprimir listagem do modelo S1000INCLUSAO"),
            ("can_print_data_s1000inclusao", u"Pode imprimir o conteúdo do modelo S1000INCLUSAO"), )

        ordering = [
            's1000_evtinfoempregador',
            'inivalid',
            'classtrib',
            'inddesfolha',
            'indoptregeletron',
            'nmctt',
            'cpfctt',]



class s1000inclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaodadosIsencao(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    ideminlei = models.CharField(max_length=70, null=True, )
    nrcertif = models.CharField(max_length=40, null=True, )
    dtemiscertif = models.DateField(null=True, )
    dtvenccertif = models.DateField(null=True, )
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True, )
    dtprotrenov = models.DateField(blank=True, null=True, )
    dtdou = models.DateField(blank=True, null=True, )
    pagdou = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif)

    class Meta:

        # verbose_name = u'Informações Complementares - Empresas Isentas - Dados da Isenção'
        db_table = r's1000_inclusao_dadosisencao'
        managed = True # s1000_inclusao_dadosisencao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaodadosIsencao", u"Pode ver listagem do modelo S1000INCLUSAODADOSISENCAO"),
            ("can_see_data_s1000inclusaodadosIsencao", u"Pode visualizar o conteúdo do modelo S1000INCLUSAODADOSISENCAO"),
            ("can_see_menu_s1000inclusaodadosIsencao", u"Pode visualizar no menu o modelo S1000INCLUSAODADOSISENCAO"),
            ("can_print_list_s1000inclusaodadosIsencao", u"Pode imprimir listagem do modelo S1000INCLUSAODADOSISENCAO"),
            ("can_print_data_s1000inclusaodadosIsencao", u"Pode imprimir o conteúdo do modelo S1000INCLUSAODADOSISENCAO"), )

        ordering = [
            's1000_inclusao',
            'ideminlei',
            'nrcertif',
            'dtemiscertif',
            'dtvenccertif',]



class s1000inclusaodadosIsencaoSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaodadosIsencao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaoinfoEFR(SoftDeletionModel):

    s1000_inclusao_infoop = models.ForeignKey('s1000.s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop', )

    def evento(self):
        return self.s1000_inclusao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_IDEEFR_INCLUSAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    indrpps = models.CharField(choices=CHOICES_S1000_INDRPPS_INCLUSAO, max_length=1, null=True, )
    prevcomp = models.CharField(choices=CHOICES_S1000_PREVCOMP_INCLUSAO, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.prevcomp)

    class Meta:

        # verbose_name = u'Informações relativas a Ente Federativo Responsável - EFR'
        db_table = r's1000_inclusao_infoefr'
        managed = True # s1000_inclusao_infoefr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaoinfoEFR", u"Pode ver listagem do modelo S1000INCLUSAOINFOEFR"),
            ("can_see_data_s1000inclusaoinfoEFR", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOINFOEFR"),
            ("can_see_menu_s1000inclusaoinfoEFR", u"Pode visualizar no menu o modelo S1000INCLUSAOINFOEFR"),
            ("can_print_list_s1000inclusaoinfoEFR", u"Pode imprimir listagem do modelo S1000INCLUSAOINFOEFR"),
            ("can_print_data_s1000inclusaoinfoEFR", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOINFOEFR"), )

        ordering = [
            's1000_inclusao_infoop',
            'ideefr',
            'indrpps',
            'prevcomp',]



class s1000inclusaoinfoEFRSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaoinfoEFR
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaoinfoEnte(SoftDeletionModel):

    s1000_inclusao_infoop = models.ForeignKey('s1000.s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop', )

    def evento(self):
        return self.s1000_inclusao_infoop.evento()
    nmente = models.CharField(max_length=100, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.IntegerField(blank=True, null=True, )
    indrpps = models.CharField(choices=CHOICES_S1000_INDRPPS_INCLUSAO, max_length=1, null=True, )
    subteto = models.IntegerField(choices=CHOICES_S1000_SUBTETO_INCLUSAO, null=True, )
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)

    class Meta:

        # verbose_name = u'Informações relativas ao ente federativo estadual, distrital ou municipal'
        db_table = r's1000_inclusao_infoente'
        managed = True # s1000_inclusao_infoente #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaoinfoEnte", u"Pode ver listagem do modelo S1000INCLUSAOINFOENTE"),
            ("can_see_data_s1000inclusaoinfoEnte", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOINFOENTE"),
            ("can_see_menu_s1000inclusaoinfoEnte", u"Pode visualizar no menu o modelo S1000INCLUSAOINFOENTE"),
            ("can_print_list_s1000inclusaoinfoEnte", u"Pode imprimir listagem do modelo S1000INCLUSAOINFOENTE"),
            ("can_print_data_s1000inclusaoinfoEnte", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOINFOENTE"), )

        ordering = [
            's1000_inclusao_infoop',
            'nmente',
            'uf',
            'indrpps',
            'subteto',
            'vrsubteto',]



class s1000inclusaoinfoEnteSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaoinfoEnte
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaoinfoOP(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    nrsiafi = models.CharField(max_length=6, null=True, )
    indugrpps = models.CharField(choices=CHOICES_S1000_INDUGRPPS_INCLUSAO, max_length=1, null=True, )
    esferaop = models.IntegerField(choices=CHOICES_S1000_ESFERAOP_INCLUSAO, blank=True, null=True, )
    poderop = models.IntegerField(choices=CHOICES_S1000_PODEROP_INCLUSAO, null=True, )
    vrtetorem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    ideefr = models.CharField(choices=CHOICES_S1000_IDEEFR_INCLUSAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.nrsiafi) + ' - ' + unicode(self.indugrpps) + ' - ' + unicode(self.poderop) + ' - ' + unicode(self.vrtetorem) + ' - ' + unicode(self.ideefr)

    class Meta:

        # verbose_name = u'Informações relativas a Órgãos Públicos'
        db_table = r's1000_inclusao_infoop'
        managed = True # s1000_inclusao_infoop #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaoinfoOP", u"Pode ver listagem do modelo S1000INCLUSAOINFOOP"),
            ("can_see_data_s1000inclusaoinfoOP", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOINFOOP"),
            ("can_see_menu_s1000inclusaoinfoOP", u"Pode visualizar no menu o modelo S1000INCLUSAOINFOOP"),
            ("can_print_list_s1000inclusaoinfoOP", u"Pode imprimir listagem do modelo S1000INCLUSAOINFOOP"),
            ("can_print_data_s1000inclusaoinfoOP", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOINFOOP"), )

        ordering = [
            's1000_inclusao',
            'nrsiafi',
            'indugrpps',
            'poderop',
            'vrtetorem',
            'ideefr',]



class s1000inclusaoinfoOPSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaoinfoOP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaoinfoOrgInternacional(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_INDACORDOISENMULTA_INCLUSAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indacordoisenmulta)

    class Meta:

        # verbose_name = u'Informações exclusivas de organismos internacionais e outras instituições extraterritoriais'
        db_table = r's1000_inclusao_infoorginternacional'
        managed = True # s1000_inclusao_infoorginternacional #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaoinfoOrgInternacional", u"Pode ver listagem do modelo S1000INCLUSAOINFOORGINTERNACIONAL"),
            ("can_see_data_s1000inclusaoinfoOrgInternacional", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOINFOORGINTERNACIONAL"),
            ("can_see_menu_s1000inclusaoinfoOrgInternacional", u"Pode visualizar no menu o modelo S1000INCLUSAOINFOORGINTERNACIONAL"),
            ("can_print_list_s1000inclusaoinfoOrgInternacional", u"Pode imprimir listagem do modelo S1000INCLUSAOINFOORGINTERNACIONAL"),
            ("can_print_data_s1000inclusaoinfoOrgInternacional", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOINFOORGINTERNACIONAL"), )

        ordering = [
            's1000_inclusao',
            'indacordoisenmulta',]



class s1000inclusaoinfoOrgInternacionalSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaoinfoOrgInternacional
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaosituacaoPF(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_INDSITPF_INCLUSAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpf)

    class Meta:

        # verbose_name = u'Informações Complementares - Pessoa Física'
        db_table = r's1000_inclusao_situacaopf'
        managed = True # s1000_inclusao_situacaopf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaosituacaoPF", u"Pode ver listagem do modelo S1000INCLUSAOSITUACAOPF"),
            ("can_see_data_s1000inclusaosituacaoPF", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOSITUACAOPF"),
            ("can_see_menu_s1000inclusaosituacaoPF", u"Pode visualizar no menu o modelo S1000INCLUSAOSITUACAOPF"),
            ("can_print_list_s1000inclusaosituacaoPF", u"Pode imprimir listagem do modelo S1000INCLUSAOSITUACAOPF"),
            ("can_print_data_s1000inclusaosituacaoPF", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOSITUACAOPF"), )

        ordering = [
            's1000_inclusao',
            'indsitpf',]



class s1000inclusaosituacaoPFSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaosituacaoPF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaosituacaoPJ(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_INDSITPJ_INCLUSAO, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpj)

    class Meta:

        # verbose_name = u'Informações Complementares - Pessoa Jurídica'
        db_table = r's1000_inclusao_situacaopj'
        managed = True # s1000_inclusao_situacaopj #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaosituacaoPJ", u"Pode ver listagem do modelo S1000INCLUSAOSITUACAOPJ"),
            ("can_see_data_s1000inclusaosituacaoPJ", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOSITUACAOPJ"),
            ("can_see_menu_s1000inclusaosituacaoPJ", u"Pode visualizar no menu o modelo S1000INCLUSAOSITUACAOPJ"),
            ("can_print_list_s1000inclusaosituacaoPJ", u"Pode imprimir listagem do modelo S1000INCLUSAOSITUACAOPJ"),
            ("can_print_data_s1000inclusaosituacaoPJ", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOSITUACAOPJ"), )

        ordering = [
            's1000_inclusao',
            'indsitpj',]



class s1000inclusaosituacaoPJSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaosituacaoPJ
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1000inclusaosoftwareHouse(SoftDeletionModel):

    s1000_inclusao = models.ForeignKey('s1000.s1000inclusao',
        related_name='%(class)s_s1000_inclusao', )

    def evento(self):
        return self.s1000_inclusao.evento()
    cnpjsofthouse = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=100, blank=True, null=True, )
    nmcont = models.CharField(max_length=70, null=True, )
    telefone = models.CharField(max_length=13, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone)

    class Meta:

        # verbose_name = u'Informações relativas ao desenvolvedor do software que gerou o arquivo xml.'
        db_table = r's1000_inclusao_softwarehouse'
        managed = True # s1000_inclusao_softwarehouse #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1000inclusaosoftwareHouse", u"Pode ver listagem do modelo S1000INCLUSAOSOFTWAREHOUSE"),
            ("can_see_data_s1000inclusaosoftwareHouse", u"Pode visualizar o conteúdo do modelo S1000INCLUSAOSOFTWAREHOUSE"),
            ("can_see_menu_s1000inclusaosoftwareHouse", u"Pode visualizar no menu o modelo S1000INCLUSAOSOFTWAREHOUSE"),
            ("can_print_list_s1000inclusaosoftwareHouse", u"Pode imprimir listagem do modelo S1000INCLUSAOSOFTWAREHOUSE"),
            ("can_print_data_s1000inclusaosoftwareHouse", u"Pode imprimir o conteúdo do modelo S1000INCLUSAOSOFTWAREHOUSE"), )

        ordering = [
            's1000_inclusao',
            'cnpjsofthouse',
            'nmcont',
            'telefone',]



class s1000inclusaosoftwareHouseSerializer(ModelSerializer):

    class Meta:

        model = s1000inclusaosoftwareHouse
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')