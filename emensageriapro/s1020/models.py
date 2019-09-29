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
from emensageriapro.s1020.choices import *
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





class s1020alteracao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao', )

    def evento(self):
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    tplotacao = models.CharField(choices=CHOICES_ESOCIALLOTACOESTRIBUTARIASTIPOS, max_length=2, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, blank=True, null=True, )
    nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    fpas = models.IntegerField(null=True, )
    codtercs = models.TextField(null=True, )
    codtercssusp = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs)

    class Meta:

        # verbose_name = u'Alteração das informações'
        db_table = r's1020_alteracao'
        managed = True # s1020_alteracao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020alteracao", u"Pode ver listagem do modelo S1020ALTERACAO"),
            ("can_see_data_s1020alteracao", u"Pode visualizar o conteúdo do modelo S1020ALTERACAO"),
            ("can_see_menu_s1020alteracao", u"Pode visualizar no menu o modelo S1020ALTERACAO"),
            ("can_print_list_s1020alteracao", u"Pode imprimir listagem do modelo S1020ALTERACAO"),
            ("can_print_data_s1020alteracao", u"Pode imprimir o conteúdo do modelo S1020ALTERACAO"), )

        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',
            'tplotacao',
            'fpas',
            'codtercs',]



class s1020alteracaoSerializer(ModelSerializer):

    class Meta:

        model = s1020alteracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020alteracaoinfoEmprParcial(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao',
        related_name='%(class)s_s1020_alteracao', )

    def evento(self):
        return self.s1020_alteracao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_TPINSCCONTRAT_ALTERACAO, null=True, )
    nrinsccontrat = models.CharField(max_length=14, null=True, )
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_TPINSCPROP_ALTERACAO, null=True, )
    nrinscprop = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)

    class Meta:

        # verbose_name = u'Informação complementar que apresenta identificação do contratante e do proprietário de obra de construção civil contratada sob regime de empreitada parcial ou subempreitada'
        db_table = r's1020_alteracao_infoemprparcial'
        managed = True # s1020_alteracao_infoemprparcial #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020alteracaoinfoEmprParcial", u"Pode ver listagem do modelo S1020ALTERACAOINFOEMPRPARCIAL"),
            ("can_see_data_s1020alteracaoinfoEmprParcial", u"Pode visualizar o conteúdo do modelo S1020ALTERACAOINFOEMPRPARCIAL"),
            ("can_see_menu_s1020alteracaoinfoEmprParcial", u"Pode visualizar no menu o modelo S1020ALTERACAOINFOEMPRPARCIAL"),
            ("can_print_list_s1020alteracaoinfoEmprParcial", u"Pode imprimir listagem do modelo S1020ALTERACAOINFOEMPRPARCIAL"),
            ("can_print_data_s1020alteracaoinfoEmprParcial", u"Pode imprimir o conteúdo do modelo S1020ALTERACAOINFOEMPRPARCIAL"), )

        ordering = [
            's1020_alteracao',
            'tpinsccontrat',
            'nrinsccontrat',
            'tpinscprop',
            'nrinscprop',]



class s1020alteracaoinfoEmprParcialSerializer(ModelSerializer):

    class Meta:

        model = s1020alteracaoinfoEmprParcial
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020alteracaoinfoProcJudTerceiros(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao',
        related_name='%(class)s_s1020_alteracao', )

    def evento(self):
        return self.s1020_alteracao.evento()

    def __unicode__(self):
        return unicode(self.s1020_alteracao)

    class Meta:

        # verbose_name = u'Informações sobre a existência de processos judiciais, com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos.'
        db_table = r's1020_alteracao_infoprocjudterceiros'
        managed = True # s1020_alteracao_infoprocjudterceiros #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020alteracaoinfoProcJudTerceiros", u"Pode ver listagem do modelo S1020ALTERACAOINFOPROCJUDTERCEIROS"),
            ("can_see_data_s1020alteracaoinfoProcJudTerceiros", u"Pode visualizar o conteúdo do modelo S1020ALTERACAOINFOPROCJUDTERCEIROS"),
            ("can_see_menu_s1020alteracaoinfoProcJudTerceiros", u"Pode visualizar no menu o modelo S1020ALTERACAOINFOPROCJUDTERCEIROS"),
            ("can_print_list_s1020alteracaoinfoProcJudTerceiros", u"Pode imprimir listagem do modelo S1020ALTERACAOINFOPROCJUDTERCEIROS"),
            ("can_print_data_s1020alteracaoinfoProcJudTerceiros", u"Pode imprimir o conteúdo do modelo S1020ALTERACAOINFOPROCJUDTERCEIROS"), )

        ordering = [
            's1020_alteracao',]



class s1020alteracaoinfoProcJudTerceirosSerializer(ModelSerializer):

    class Meta:

        model = s1020alteracaoinfoProcJudTerceiros
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020alteracaonovaValidade(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao',
        related_name='%(class)s_s1020_alteracao', )

    def evento(self):
        return self.s1020_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1020_alteracao_novavalidade'
        managed = True # s1020_alteracao_novavalidade #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020alteracaonovaValidade", u"Pode ver listagem do modelo S1020ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1020alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1020ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1020alteracaonovaValidade", u"Pode visualizar no menu o modelo S1020ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1020alteracaonovaValidade", u"Pode imprimir listagem do modelo S1020ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1020alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1020ALTERACAONOVAVALIDADE"), )

        ordering = [
            's1020_alteracao',
            'inivalid',]



class s1020alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:

        model = s1020alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020alteracaoprocJudTerceiro(SoftDeletionModel):

    s1020_alteracao_infoprocjudterceiros = models.ForeignKey('s1020.s1020alteracaoinfoProcJudTerceiros',
        related_name='%(class)s_s1020_alteracao_infoprocjudterceiros', )

    def evento(self):
        return self.s1020_alteracao_infoprocjudterceiros.evento()
    codterc = models.TextField(null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1020_alteracao_infoprocjudterceiros) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)

    class Meta:

        # verbose_name = u'Identificação do Processo Judicial'
        db_table = r's1020_alteracao_procjudterceiro'
        managed = True # s1020_alteracao_procjudterceiro #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020alteracaoprocJudTerceiro", u"Pode ver listagem do modelo S1020ALTERACAOPROCJUDTERCEIRO"),
            ("can_see_data_s1020alteracaoprocJudTerceiro", u"Pode visualizar o conteúdo do modelo S1020ALTERACAOPROCJUDTERCEIRO"),
            ("can_see_menu_s1020alteracaoprocJudTerceiro", u"Pode visualizar no menu o modelo S1020ALTERACAOPROCJUDTERCEIRO"),
            ("can_print_list_s1020alteracaoprocJudTerceiro", u"Pode imprimir listagem do modelo S1020ALTERACAOPROCJUDTERCEIRO"),
            ("can_print_data_s1020alteracaoprocJudTerceiro", u"Pode imprimir o conteúdo do modelo S1020ALTERACAOPROCJUDTERCEIRO"), )

        ordering = [
            's1020_alteracao_infoprocjudterceiros',
            'codterc',
            'nrprocjud',
            'codsusp',]



class s1020alteracaoprocJudTerceiroSerializer(ModelSerializer):

    class Meta:

        model = s1020alteracaoprocJudTerceiro
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020exclusao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao', )

    def evento(self):
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid)

    class Meta:

        # verbose_name = u'Exclusão das informações'
        db_table = r's1020_exclusao'
        managed = True # s1020_exclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020exclusao", u"Pode ver listagem do modelo S1020EXCLUSAO"),
            ("can_see_data_s1020exclusao", u"Pode visualizar o conteúdo do modelo S1020EXCLUSAO"),
            ("can_see_menu_s1020exclusao", u"Pode visualizar no menu o modelo S1020EXCLUSAO"),
            ("can_print_list_s1020exclusao", u"Pode imprimir listagem do modelo S1020EXCLUSAO"),
            ("can_print_data_s1020exclusao", u"Pode imprimir o conteúdo do modelo S1020EXCLUSAO"), )

        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',]



class s1020exclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1020exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020inclusao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao', )

    def evento(self):
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    tplotacao = models.CharField(choices=CHOICES_ESOCIALLOTACOESTRIBUTARIASTIPOS, max_length=2, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, blank=True, null=True, )
    nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    fpas = models.IntegerField(null=True, )
    codtercs = models.TextField(null=True, )
    codtercssusp = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs)

    class Meta:

        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1020_inclusao'
        managed = True # s1020_inclusao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020inclusao", u"Pode ver listagem do modelo S1020INCLUSAO"),
            ("can_see_data_s1020inclusao", u"Pode visualizar o conteúdo do modelo S1020INCLUSAO"),
            ("can_see_menu_s1020inclusao", u"Pode visualizar no menu o modelo S1020INCLUSAO"),
            ("can_print_list_s1020inclusao", u"Pode imprimir listagem do modelo S1020INCLUSAO"),
            ("can_print_data_s1020inclusao", u"Pode imprimir o conteúdo do modelo S1020INCLUSAO"), )

        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',
            'tplotacao',
            'fpas',
            'codtercs',]



class s1020inclusaoSerializer(ModelSerializer):

    class Meta:

        model = s1020inclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020inclusaoinfoEmprParcial(SoftDeletionModel):

    s1020_inclusao = models.ForeignKey('s1020.s1020inclusao',
        related_name='%(class)s_s1020_inclusao', )

    def evento(self):
        return self.s1020_inclusao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_TPINSCCONTRAT_INCLUSAO, null=True, )
    nrinsccontrat = models.CharField(max_length=14, null=True, )
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_TPINSCPROP_INCLUSAO, null=True, )
    nrinscprop = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.s1020_inclusao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)

    class Meta:

        # verbose_name = u'Informação complementar que apresenta identificação do contratante e do proprietário de obra de construção civil contratada sob regime de empreitada parcial ou subempreitada'
        db_table = r's1020_inclusao_infoemprparcial'
        managed = True # s1020_inclusao_infoemprparcial #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020inclusaoinfoEmprParcial", u"Pode ver listagem do modelo S1020INCLUSAOINFOEMPRPARCIAL"),
            ("can_see_data_s1020inclusaoinfoEmprParcial", u"Pode visualizar o conteúdo do modelo S1020INCLUSAOINFOEMPRPARCIAL"),
            ("can_see_menu_s1020inclusaoinfoEmprParcial", u"Pode visualizar no menu o modelo S1020INCLUSAOINFOEMPRPARCIAL"),
            ("can_print_list_s1020inclusaoinfoEmprParcial", u"Pode imprimir listagem do modelo S1020INCLUSAOINFOEMPRPARCIAL"),
            ("can_print_data_s1020inclusaoinfoEmprParcial", u"Pode imprimir o conteúdo do modelo S1020INCLUSAOINFOEMPRPARCIAL"), )

        ordering = [
            's1020_inclusao',
            'tpinsccontrat',
            'nrinsccontrat',
            'tpinscprop',
            'nrinscprop',]



class s1020inclusaoinfoEmprParcialSerializer(ModelSerializer):

    class Meta:

        model = s1020inclusaoinfoEmprParcial
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020inclusaoinfoProcJudTerceiros(SoftDeletionModel):

    s1020_inclusao = models.ForeignKey('s1020.s1020inclusao',
        related_name='%(class)s_s1020_inclusao', )

    def evento(self):
        return self.s1020_inclusao.evento()

    def __unicode__(self):
        return unicode(self.s1020_inclusao)

    class Meta:

        # verbose_name = u'Informações sobre a existência de processos judiciais, com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos.'
        db_table = r's1020_inclusao_infoprocjudterceiros'
        managed = True # s1020_inclusao_infoprocjudterceiros #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020inclusaoinfoProcJudTerceiros", u"Pode ver listagem do modelo S1020INCLUSAOINFOPROCJUDTERCEIROS"),
            ("can_see_data_s1020inclusaoinfoProcJudTerceiros", u"Pode visualizar o conteúdo do modelo S1020INCLUSAOINFOPROCJUDTERCEIROS"),
            ("can_see_menu_s1020inclusaoinfoProcJudTerceiros", u"Pode visualizar no menu o modelo S1020INCLUSAOINFOPROCJUDTERCEIROS"),
            ("can_print_list_s1020inclusaoinfoProcJudTerceiros", u"Pode imprimir listagem do modelo S1020INCLUSAOINFOPROCJUDTERCEIROS"),
            ("can_print_data_s1020inclusaoinfoProcJudTerceiros", u"Pode imprimir o conteúdo do modelo S1020INCLUSAOINFOPROCJUDTERCEIROS"), )

        ordering = [
            's1020_inclusao',]



class s1020inclusaoinfoProcJudTerceirosSerializer(ModelSerializer):

    class Meta:

        model = s1020inclusaoinfoProcJudTerceiros
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020inclusaoprocJudTerceiro(SoftDeletionModel):

    s1020_inclusao_infoprocjudterceiros = models.ForeignKey('s1020.s1020inclusaoinfoProcJudTerceiros',
        related_name='%(class)s_s1020_inclusao_infoprocjudterceiros', )

    def evento(self):
        return self.s1020_inclusao_infoprocjudterceiros.evento()
    codterc = models.TextField(null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1020_inclusao_infoprocjudterceiros) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)

    class Meta:

        # verbose_name = u'Identificação do Processo Judicial'
        db_table = r's1020_inclusao_procjudterceiro'
        managed = True # s1020_inclusao_procjudterceiro #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1020inclusaoprocJudTerceiro", u"Pode ver listagem do modelo S1020INCLUSAOPROCJUDTERCEIRO"),
            ("can_see_data_s1020inclusaoprocJudTerceiro", u"Pode visualizar o conteúdo do modelo S1020INCLUSAOPROCJUDTERCEIRO"),
            ("can_see_menu_s1020inclusaoprocJudTerceiro", u"Pode visualizar no menu o modelo S1020INCLUSAOPROCJUDTERCEIRO"),
            ("can_print_list_s1020inclusaoprocJudTerceiro", u"Pode imprimir listagem do modelo S1020INCLUSAOPROCJUDTERCEIRO"),
            ("can_print_data_s1020inclusaoprocJudTerceiro", u"Pode imprimir o conteúdo do modelo S1020INCLUSAOPROCJUDTERCEIRO"), )

        ordering = [
            's1020_inclusao_infoprocjudterceiros',
            'codterc',
            'nrprocjud',
            'codsusp',]



class s1020inclusaoprocJudTerceiroSerializer(ModelSerializer):

    class Meta:

        model = s1020inclusaoprocJudTerceiro
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')