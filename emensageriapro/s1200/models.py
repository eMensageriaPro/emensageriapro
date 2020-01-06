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
from emensageriapro.s1200.choices import *
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





class s1200dmDev(SoftDeletionModel):

    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun', )

    def evento(self):
        return self.s1200_evtremun.evento()
    idedmdev = models.CharField(max_length=30, null=True, )
    codcateg = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.codcateg)

    class Meta:

        # verbose_name = u'Identificação de cada um dos demonstrativos de valores devidos ao trabalhador antes das retenções de pensão alimentícia e IRRF'
        db_table = r's1200_dmdev'
        managed = True # s1200_dmdev #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200dmDev", u"Pode ver listagem do modelo S1200DMDEV"),
            ("can_see_data_s1200dmDev", u"Pode visualizar o conteúdo do modelo S1200DMDEV"),
            ("can_see_menu_s1200dmDev", u"Pode visualizar no menu o modelo S1200DMDEV"),
            ("can_print_list_s1200dmDev", u"Pode imprimir listagem do modelo S1200DMDEV"),
            ("can_print_data_s1200dmDev", u"Pode imprimir o conteúdo do modelo S1200DMDEV"), )

        ordering = [
            's1200_evtremun',
            'idedmdev',
            'codcateg',]



class s1200dmDevSerializer(ModelSerializer):

    class Meta:

        model = s1200dmDev
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoComplem(SoftDeletionModel):

    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun', )

    def evento(self):
        return self.s1200_evtremun.evento()
    nmtrab = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )

    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.dtnascto)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente quando o evento de remuneração referir- se a trabalhador cuja categoria não está sujeita ao evento de admissão ou ao evento de início de 'trabalhador sem vínculo''
        db_table = r's1200_infocomplem'
        managed = True # s1200_infocomplem #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoComplem", u"Pode ver listagem do modelo S1200INFOCOMPLEM"),
            ("can_see_data_s1200infoComplem", u"Pode visualizar o conteúdo do modelo S1200INFOCOMPLEM"),
            ("can_see_menu_s1200infoComplem", u"Pode visualizar no menu o modelo S1200INFOCOMPLEM"),
            ("can_print_list_s1200infoComplem", u"Pode imprimir listagem do modelo S1200INFOCOMPLEM"),
            ("can_print_data_s1200infoComplem", u"Pode imprimir o conteúdo do modelo S1200INFOCOMPLEM"), )

        ordering = [
            's1200_evtremun',
            'nmtrab',
            'dtnascto',]



class s1200infoComplemSerializer(ModelSerializer):

    class Meta:

        model = s1200infoComplem
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoInterm(SoftDeletionModel):

    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun', )

    def evento(self):
        return self.s1200_evtremun.evento()
    qtddiasinterm = models.IntegerField(null=True, )

    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.qtddiasinterm)

    class Meta:

        # verbose_name = u'Informações relativas ao trabalho intermitente'
        db_table = r's1200_infointerm'
        managed = True # s1200_infointerm #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoInterm", u"Pode ver listagem do modelo S1200INFOINTERM"),
            ("can_see_data_s1200infoInterm", u"Pode visualizar o conteúdo do modelo S1200INFOINTERM"),
            ("can_see_menu_s1200infoInterm", u"Pode visualizar no menu o modelo S1200INFOINTERM"),
            ("can_print_list_s1200infoInterm", u"Pode imprimir listagem do modelo S1200INFOINTERM"),
            ("can_print_data_s1200infoInterm", u"Pode imprimir o conteúdo do modelo S1200INFOINTERM"), )

        ordering = [
            's1200_evtremun',
            'qtddiasinterm',]



class s1200infoIntermSerializer(ModelSerializer):

    class Meta:

        model = s1200infoInterm
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoMV(SoftDeletionModel):

    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun', )

    def evento(self):
        return self.s1200_evtremun.evento()
    indmv = models.IntegerField(choices=CHOICES_S1200_INDMV, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.indmv)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente em caso de trabalhador que possua outros vínculos/atividades para definição do limite do salário-de-contribuição e da alíquota a ser aplicada no desconto da contribuição previdenciária.'
        db_table = r's1200_infomv'
        managed = True # s1200_infomv #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoMV", u"Pode ver listagem do modelo S1200INFOMV"),
            ("can_see_data_s1200infoMV", u"Pode visualizar o conteúdo do modelo S1200INFOMV"),
            ("can_see_menu_s1200infoMV", u"Pode visualizar no menu o modelo S1200INFOMV"),
            ("can_print_list_s1200infoMV", u"Pode imprimir listagem do modelo S1200INFOMV"),
            ("can_print_data_s1200infoMV", u"Pode imprimir o conteúdo do modelo S1200INFOMV"), )

        ordering = [
            's1200_evtremun',
            'indmv',]



class s1200infoMVSerializer(ModelSerializer):

    class Meta:

        model = s1200infoMV
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAnt(SoftDeletionModel):

    s1200_dmdev = models.ForeignKey('s1200.s1200dmDev',
        related_name='%(class)s_s1200_dmdev', )

    def evento(self):
        return self.s1200_dmdev.evento()

    def __unicode__(self):
        return unicode(self.s1200_dmdev)

    class Meta:

        # verbose_name = u'Registro destinado ao registro de: a) remuneração relativa a diferenças salariais provenientes de acordos coletivos, convenção coletiva e dissídio; b) remuneração relativa a diferenças de vencimento provenientes de disposições legais (órgãos públicos); c) bases de cálculo para efeitos de apuração de FGTS resultantes de conversão de licença saúde em acidente de trabalho. d) verbas de natureza salarial ou não salarial devidas após o desligamento'
        db_table = r's1200_infoperant'
        managed = True # s1200_infoperant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAnt", u"Pode ver listagem do modelo S1200INFOPERANT"),
            ("can_see_data_s1200infoPerAnt", u"Pode visualizar o conteúdo do modelo S1200INFOPERANT"),
            ("can_see_menu_s1200infoPerAnt", u"Pode visualizar no menu o modelo S1200INFOPERANT"),
            ("can_print_list_s1200infoPerAnt", u"Pode imprimir listagem do modelo S1200INFOPERANT"),
            ("can_print_data_s1200infoPerAnt", u"Pode imprimir o conteúdo do modelo S1200INFOPERANT"), )

        ordering = [
            's1200_dmdev',]



class s1200infoPerAntSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntideADC(SoftDeletionModel):

    s1200_infoperant = models.ForeignKey('s1200.s1200infoPerAnt',
        related_name='%(class)s_s1200_infoperant', )

    def evento(self):
        return self.s1200_infoperant.evento()
    dtacconv = models.DateField(blank=True, null=True, )
    tpacconv = models.CharField(choices=CHOICES_S1200_TPACCONV_INFOPERANT, max_length=1, null=True, )
    compacconv = models.CharField(max_length=7, blank=True, null=True, )
    dtefacconv = models.DateField(blank=True, null=True, )
    dsc = models.CharField(max_length=255, null=True, )
    remunsuc = models.CharField(choices=CHOICES_S1200_REMUNSUC_INFOPERANT, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dsc) + ' - ' + unicode(self.remunsuc)

    class Meta:

        # verbose_name = u'Identificação do Instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores.'
        db_table = r's1200_infoperant_ideadc'
        managed = True # s1200_infoperant_ideadc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntideADC", u"Pode ver listagem do modelo S1200INFOPERANTIDEADC"),
            ("can_see_data_s1200infoPerAntideADC", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTIDEADC"),
            ("can_see_menu_s1200infoPerAntideADC", u"Pode visualizar no menu o modelo S1200INFOPERANTIDEADC"),
            ("can_print_list_s1200infoPerAntideADC", u"Pode imprimir listagem do modelo S1200INFOPERANTIDEADC"),
            ("can_print_data_s1200infoPerAntideADC", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTIDEADC"), )

        ordering = [
            's1200_infoperant',
            'tpacconv',
            'dsc',
            'remunsuc',]



class s1200infoPerAntideADCSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntideADC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntideEstabLot(SoftDeletionModel):

    s1200_infoperant_ideperiodo = models.ForeignKey('s1200.s1200infoPerAntidePeriodo',
        related_name='%(class)s_s1200_infoperant_ideperiodo', )

    def evento(self):
        return self.s1200_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)

    class Meta:

        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's1200_infoperant_ideestablot'
        managed = True # s1200_infoperant_ideestablot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntideEstabLot", u"Pode ver listagem do modelo S1200INFOPERANTIDEESTABLOT"),
            ("can_see_data_s1200infoPerAntideEstabLot", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTIDEESTABLOT"),
            ("can_see_menu_s1200infoPerAntideEstabLot", u"Pode visualizar no menu o modelo S1200INFOPERANTIDEESTABLOT"),
            ("can_print_list_s1200infoPerAntideEstabLot", u"Pode imprimir listagem do modelo S1200INFOPERANTIDEESTABLOT"),
            ("can_print_data_s1200infoPerAntideEstabLot", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTIDEESTABLOT"), )

        ordering = [
            's1200_infoperant_ideperiodo',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s1200infoPerAntideEstabLotSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntideEstabLot
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntidePeriodo(SoftDeletionModel):

    s1200_infoperant_ideadc = models.ForeignKey('s1200.s1200infoPerAntideADC',
        related_name='%(class)s_s1200_infoperant_ideadc', )

    def evento(self):
        return self.s1200_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideadc) + ' - ' + unicode(self.perref)

    class Meta:

        # verbose_name = u'Período de validade das informações incluídas'
        db_table = r's1200_infoperant_ideperiodo'
        managed = True # s1200_infoperant_ideperiodo #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntidePeriodo", u"Pode ver listagem do modelo S1200INFOPERANTIDEPERIODO"),
            ("can_see_data_s1200infoPerAntidePeriodo", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTIDEPERIODO"),
            ("can_see_menu_s1200infoPerAntidePeriodo", u"Pode visualizar no menu o modelo S1200INFOPERANTIDEPERIODO"),
            ("can_print_list_s1200infoPerAntidePeriodo", u"Pode imprimir listagem do modelo S1200INFOPERANTIDEPERIODO"),
            ("can_print_data_s1200infoPerAntidePeriodo", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTIDEPERIODO"), )

        ordering = [
            's1200_infoperant_ideadc',
            'perref',]



class s1200infoPerAntidePeriodoSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntidePeriodo
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntinfoAgNocivo(SoftDeletionModel):

    s1200_infoperant_remunperant = models.ForeignKey('s1200.s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant', )

    def evento(self):
        return self.s1200_infoperant_remunperant.evento()
    grauexp = models.IntegerField(choices=CHOICES_S1200_GRAUEXP_INFOPERANT, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.grauexp)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a cooperativa de trabalho que presta serviço a empresa [731, 734], permitindo o detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial.'
        db_table = r's1200_infoperant_infoagnocivo'
        managed = True # s1200_infoperant_infoagnocivo #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntinfoAgNocivo", u"Pode ver listagem do modelo S1200INFOPERANTINFOAGNOCIVO"),
            ("can_see_data_s1200infoPerAntinfoAgNocivo", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTINFOAGNOCIVO"),
            ("can_see_menu_s1200infoPerAntinfoAgNocivo", u"Pode visualizar no menu o modelo S1200INFOPERANTINFOAGNOCIVO"),
            ("can_print_list_s1200infoPerAntinfoAgNocivo", u"Pode imprimir listagem do modelo S1200INFOPERANTINFOAGNOCIVO"),
            ("can_print_data_s1200infoPerAntinfoAgNocivo", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTINFOAGNOCIVO"), )

        ordering = [
            's1200_infoperant_remunperant',
            'grauexp',]



class s1200infoPerAntinfoAgNocivoSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntinfoAgNocivo
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntinfoComplCont(SoftDeletionModel):

    s1200_dmdev = models.ForeignKey('s1200.s1200dmDev',
        related_name='%(class)s_s1200_dmdev', )

    def evento(self):
        return self.s1200_dmdev.evento()
    codcbo = models.TextField(null=True, )
    natatividade = models.IntegerField(choices=CHOICES_S1200_NATATIVIDADE_INFOPERANT, blank=True, null=True, )
    qtddiastrab = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_dmdev) + ' - ' + unicode(self.codcbo)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente quando o evento de remuneração se referir a trabalhador cuja categoria não estiver obrigada ao evento de início de TSVE e se não houver evento S-2300 correspondente (CPF + categoria).'
        db_table = r's1200_infoperant_infocomplcont'
        managed = True # s1200_infoperant_infocomplcont #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntinfoComplCont", u"Pode ver listagem do modelo S1200INFOPERANTINFOCOMPLCONT"),
            ("can_see_data_s1200infoPerAntinfoComplCont", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTINFOCOMPLCONT"),
            ("can_see_menu_s1200infoPerAntinfoComplCont", u"Pode visualizar no menu o modelo S1200INFOPERANTINFOCOMPLCONT"),
            ("can_print_list_s1200infoPerAntinfoComplCont", u"Pode imprimir listagem do modelo S1200INFOPERANTINFOCOMPLCONT"),
            ("can_print_data_s1200infoPerAntinfoComplCont", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTINFOCOMPLCONT"), )

        ordering = [
            's1200_dmdev',
            'codcbo',]



class s1200infoPerAntinfoComplContSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntinfoComplCont
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntinfoTrabInterm(SoftDeletionModel):

    s1200_infoperant_remunperant = models.ForeignKey('s1200.s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant', )

    def evento(self):
        return self.s1200_infoperant_remunperant.evento()
    codconv = models.CharField(max_length=30, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codconv)

    class Meta:

        # verbose_name = u'Informações da(s) convocação(ões) de trabalho intermitente'
        db_table = r's1200_infoperant_infotrabinterm'
        managed = True # s1200_infoperant_infotrabinterm #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntinfoTrabInterm", u"Pode ver listagem do modelo S1200INFOPERANTINFOTRABINTERM"),
            ("can_see_data_s1200infoPerAntinfoTrabInterm", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTINFOTRABINTERM"),
            ("can_see_menu_s1200infoPerAntinfoTrabInterm", u"Pode visualizar no menu o modelo S1200INFOPERANTINFOTRABINTERM"),
            ("can_print_list_s1200infoPerAntinfoTrabInterm", u"Pode imprimir listagem do modelo S1200INFOPERANTINFOTRABINTERM"),
            ("can_print_data_s1200infoPerAntinfoTrabInterm", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTINFOTRABINTERM"), )

        ordering = [
            's1200_infoperant_remunperant',
            'codconv',]



class s1200infoPerAntinfoTrabIntermSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntinfoTrabInterm
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntitensRemun(SoftDeletionModel):

    s1200_infoperant_remunperant = models.ForeignKey('s1200.s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant', )

    def evento(self):
        return self.s1200_infoperant_remunperant.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Registro que relaciona as rubricas que compõem a remuneração do trabalhador.'
        db_table = r's1200_infoperant_itensremun'
        managed = True # s1200_infoperant_itensremun #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntitensRemun", u"Pode ver listagem do modelo S1200INFOPERANTITENSREMUN"),
            ("can_see_data_s1200infoPerAntitensRemun", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTITENSREMUN"),
            ("can_see_menu_s1200infoPerAntitensRemun", u"Pode visualizar no menu o modelo S1200INFOPERANTITENSREMUN"),
            ("can_print_list_s1200infoPerAntitensRemun", u"Pode imprimir listagem do modelo S1200INFOPERANTITENSREMUN"),
            ("can_print_data_s1200infoPerAntitensRemun", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTITENSREMUN"), )

        ordering = [
            's1200_infoperant_remunperant',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1200infoPerAntitensRemunSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntitensRemun
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerAntremunPerAnt(SoftDeletionModel):

    s1200_infoperant_ideestablot = models.ForeignKey('s1200.s1200infoPerAntideEstabLot',
        related_name='%(class)s_s1200_infoperant_ideestablot', )

    def evento(self):
        return self.s1200_infoperant_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    indsimples = models.IntegerField(choices=CHOICES_S1200_INDSIMPLES_INFOPERANT, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideestablot)

    class Meta:

        # verbose_name = u'Informações relativas a remuneração do trabalhador em períodos anteriores ao período de apuração'
        db_table = r's1200_infoperant_remunperant'
        managed = True # s1200_infoperant_remunperant #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerAntremunPerAnt", u"Pode ver listagem do modelo S1200INFOPERANTREMUNPERANT"),
            ("can_see_data_s1200infoPerAntremunPerAnt", u"Pode visualizar o conteúdo do modelo S1200INFOPERANTREMUNPERANT"),
            ("can_see_menu_s1200infoPerAntremunPerAnt", u"Pode visualizar no menu o modelo S1200INFOPERANTREMUNPERANT"),
            ("can_print_list_s1200infoPerAntremunPerAnt", u"Pode imprimir listagem do modelo S1200INFOPERANTREMUNPERANT"),
            ("can_print_data_s1200infoPerAntremunPerAnt", u"Pode imprimir o conteúdo do modelo S1200INFOPERANTREMUNPERANT"), )

        ordering = [
            's1200_infoperant_ideestablot',]



class s1200infoPerAntremunPerAntSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerAntremunPerAnt
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApur(SoftDeletionModel):

    s1200_dmdev = models.ForeignKey('s1200.s1200dmDev',
        related_name='%(class)s_s1200_dmdev', )

    def evento(self):
        return self.s1200_dmdev.evento()

    def __unicode__(self):
        return unicode(self.s1200_dmdev)

    class Meta:

        # verbose_name = u'Remuneração no período de apuração'
        db_table = r's1200_infoperapur'
        managed = True # s1200_infoperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApur", u"Pode ver listagem do modelo S1200INFOPERAPUR"),
            ("can_see_data_s1200infoPerApur", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPUR"),
            ("can_see_menu_s1200infoPerApur", u"Pode visualizar no menu o modelo S1200INFOPERAPUR"),
            ("can_print_list_s1200infoPerApur", u"Pode imprimir listagem do modelo S1200INFOPERAPUR"),
            ("can_print_data_s1200infoPerApur", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPUR"), )

        ordering = [
            's1200_dmdev',]



class s1200infoPerApurSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApur
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurdetOper(SoftDeletionModel):

    s1200_infoperapur_infosaudecolet = models.ForeignKey('s1200.s1200infoPerApurinfoSaudeColet',
        related_name='%(class)s_s1200_infoperapur_infosaudecolet', )

    def evento(self):
        return self.s1200_infoperapur_infosaudecolet.evento()
    cnpjoper = models.CharField(max_length=14, null=True, )
    regans = models.CharField(max_length=6, null=True, )
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_infosaudecolet) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)

    class Meta:

        # verbose_name = u'Detalhamento dos valores pagos a Operadoras de Planos de Saúde.'
        db_table = r's1200_infoperapur_detoper'
        managed = True # s1200_infoperapur_detoper #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurdetOper", u"Pode ver listagem do modelo S1200INFOPERAPURDETOPER"),
            ("can_see_data_s1200infoPerApurdetOper", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURDETOPER"),
            ("can_see_menu_s1200infoPerApurdetOper", u"Pode visualizar no menu o modelo S1200INFOPERAPURDETOPER"),
            ("can_print_list_s1200infoPerApurdetOper", u"Pode imprimir listagem do modelo S1200INFOPERAPURDETOPER"),
            ("can_print_data_s1200infoPerApurdetOper", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURDETOPER"), )

        ordering = [
            's1200_infoperapur_infosaudecolet',
            'cnpjoper',
            'regans',
            'vrpgtit',]



class s1200infoPerApurdetOperSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurdetOper
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurdetPlano(SoftDeletionModel):

    s1200_infoperapur_detoper = models.ForeignKey('s1200.s1200infoPerApurdetOper',
        related_name='%(class)s_s1200_infoperapur_detoper', )

    def evento(self):
        return self.s1200_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)

    class Meta:

        # verbose_name = u'Informações do dependente do plano privado de saúde.'
        db_table = r's1200_infoperapur_detplano'
        managed = True # s1200_infoperapur_detplano #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurdetPlano", u"Pode ver listagem do modelo S1200INFOPERAPURDETPLANO"),
            ("can_see_data_s1200infoPerApurdetPlano", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURDETPLANO"),
            ("can_see_menu_s1200infoPerApurdetPlano", u"Pode visualizar no menu o modelo S1200INFOPERAPURDETPLANO"),
            ("can_print_list_s1200infoPerApurdetPlano", u"Pode imprimir listagem do modelo S1200INFOPERAPURDETPLANO"),
            ("can_print_data_s1200infoPerApurdetPlano", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURDETPLANO"), )

        ordering = [
            's1200_infoperapur_detoper',
            'tpdep',
            'nmdep',
            'dtnascto',
            'vlrpgdep',]



class s1200infoPerApurdetPlanoSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurdetPlano
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurideEstabLot(SoftDeletionModel):

    s1200_infoperapur = models.ForeignKey('s1200.s1200infoPerApur',
        related_name='%(class)s_s1200_infoperapur', )

    def evento(self):
        return self.s1200_infoperapur.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )
    qtddiasav = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)

    class Meta:

        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's1200_infoperapur_ideestablot'
        managed = True # s1200_infoperapur_ideestablot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurideEstabLot", u"Pode ver listagem do modelo S1200INFOPERAPURIDEESTABLOT"),
            ("can_see_data_s1200infoPerApurideEstabLot", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURIDEESTABLOT"),
            ("can_see_menu_s1200infoPerApurideEstabLot", u"Pode visualizar no menu o modelo S1200INFOPERAPURIDEESTABLOT"),
            ("can_print_list_s1200infoPerApurideEstabLot", u"Pode imprimir listagem do modelo S1200INFOPERAPURIDEESTABLOT"),
            ("can_print_data_s1200infoPerApurideEstabLot", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURIDEESTABLOT"), )

        ordering = [
            's1200_infoperapur',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s1200infoPerApurideEstabLotSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurideEstabLot
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurinfoAgNocivo(SoftDeletionModel):

    s1200_infoperapur_remunperapur = models.ForeignKey('s1200.s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur', )

    def evento(self):
        return self.s1200_infoperapur_remunperapur.evento()
    grauexp = models.IntegerField(choices=CHOICES_S1200_GRAUEXP_INFOPERAPUR, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.grauexp)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a cooperativa de trabalho que presta serviço a empresa [731, 734], permitindo o detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial.'
        db_table = r's1200_infoperapur_infoagnocivo'
        managed = True # s1200_infoperapur_infoagnocivo #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurinfoAgNocivo", u"Pode ver listagem do modelo S1200INFOPERAPURINFOAGNOCIVO"),
            ("can_see_data_s1200infoPerApurinfoAgNocivo", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURINFOAGNOCIVO"),
            ("can_see_menu_s1200infoPerApurinfoAgNocivo", u"Pode visualizar no menu o modelo S1200INFOPERAPURINFOAGNOCIVO"),
            ("can_print_list_s1200infoPerApurinfoAgNocivo", u"Pode imprimir listagem do modelo S1200INFOPERAPURINFOAGNOCIVO"),
            ("can_print_data_s1200infoPerApurinfoAgNocivo", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURINFOAGNOCIVO"), )

        ordering = [
            's1200_infoperapur_remunperapur',
            'grauexp',]



class s1200infoPerApurinfoAgNocivoSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurinfoAgNocivo
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurinfoSaudeColet(SoftDeletionModel):

    s1200_infoperapur_remunperapur = models.ForeignKey('s1200.s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur', )

    def evento(self):
        return self.s1200_infoperapur_remunperapur.evento()

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur)

    class Meta:

        # verbose_name = u'Informações de plano privado coletivo empresarial de assistência à saúde'
        db_table = r's1200_infoperapur_infosaudecolet'
        managed = True # s1200_infoperapur_infosaudecolet #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurinfoSaudeColet", u"Pode ver listagem do modelo S1200INFOPERAPURINFOSAUDECOLET"),
            ("can_see_data_s1200infoPerApurinfoSaudeColet", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURINFOSAUDECOLET"),
            ("can_see_menu_s1200infoPerApurinfoSaudeColet", u"Pode visualizar no menu o modelo S1200INFOPERAPURINFOSAUDECOLET"),
            ("can_print_list_s1200infoPerApurinfoSaudeColet", u"Pode imprimir listagem do modelo S1200INFOPERAPURINFOSAUDECOLET"),
            ("can_print_data_s1200infoPerApurinfoSaudeColet", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURINFOSAUDECOLET"), )

        ordering = [
            's1200_infoperapur_remunperapur',]



class s1200infoPerApurinfoSaudeColetSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurinfoSaudeColet
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurinfoTrabInterm(SoftDeletionModel):

    s1200_infoperapur_remunperapur = models.ForeignKey('s1200.s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur', )

    def evento(self):
        return self.s1200_infoperapur_remunperapur.evento()
    codconv = models.CharField(max_length=30, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codconv)

    class Meta:

        # verbose_name = u'Informações da(s) convocação(ões) de trabalho intermitente'
        db_table = r's1200_infoperapur_infotrabinterm'
        managed = True # s1200_infoperapur_infotrabinterm #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurinfoTrabInterm", u"Pode ver listagem do modelo S1200INFOPERAPURINFOTRABINTERM"),
            ("can_see_data_s1200infoPerApurinfoTrabInterm", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURINFOTRABINTERM"),
            ("can_see_menu_s1200infoPerApurinfoTrabInterm", u"Pode visualizar no menu o modelo S1200INFOPERAPURINFOTRABINTERM"),
            ("can_print_list_s1200infoPerApurinfoTrabInterm", u"Pode imprimir listagem do modelo S1200INFOPERAPURINFOTRABINTERM"),
            ("can_print_data_s1200infoPerApurinfoTrabInterm", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURINFOTRABINTERM"), )

        ordering = [
            's1200_infoperapur_remunperapur',
            'codconv',]



class s1200infoPerApurinfoTrabIntermSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurinfoTrabInterm
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApuritensRemun(SoftDeletionModel):

    s1200_infoperapur_remunperapur = models.ForeignKey('s1200.s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur', )

    def evento(self):
        return self.s1200_infoperapur_remunperapur.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)

    class Meta:

        # verbose_name = u'Registro que relaciona as rubricas que compõem a remuneração do trabalhador.'
        db_table = r's1200_infoperapur_itensremun'
        managed = True # s1200_infoperapur_itensremun #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApuritensRemun", u"Pode ver listagem do modelo S1200INFOPERAPURITENSREMUN"),
            ("can_see_data_s1200infoPerApuritensRemun", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURITENSREMUN"),
            ("can_see_menu_s1200infoPerApuritensRemun", u"Pode visualizar no menu o modelo S1200INFOPERAPURITENSREMUN"),
            ("can_print_list_s1200infoPerApuritensRemun", u"Pode imprimir listagem do modelo S1200INFOPERAPURITENSREMUN"),
            ("can_print_data_s1200infoPerApuritensRemun", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURITENSREMUN"), )

        ordering = [
            's1200_infoperapur_remunperapur',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s1200infoPerApuritensRemunSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApuritensRemun
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200infoPerApurremunPerApur(SoftDeletionModel):

    s1200_infoperapur_ideestablot = models.ForeignKey('s1200.s1200infoPerApurideEstabLot',
        related_name='%(class)s_s1200_infoperapur_ideestablot', )

    def evento(self):
        return self.s1200_infoperapur_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    indsimples = models.IntegerField(choices=CHOICES_S1200_INDSIMPLES_INFOPERAPUR, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infoperapur_ideestablot)

    class Meta:

        # verbose_name = u'Informações relativas a remuneração do trabalhador no período de apuração'
        db_table = r's1200_infoperapur_remunperapur'
        managed = True # s1200_infoperapur_remunperapur #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200infoPerApurremunPerApur", u"Pode ver listagem do modelo S1200INFOPERAPURREMUNPERAPUR"),
            ("can_see_data_s1200infoPerApurremunPerApur", u"Pode visualizar o conteúdo do modelo S1200INFOPERAPURREMUNPERAPUR"),
            ("can_see_menu_s1200infoPerApurremunPerApur", u"Pode visualizar no menu o modelo S1200INFOPERAPURREMUNPERAPUR"),
            ("can_print_list_s1200infoPerApurremunPerApur", u"Pode imprimir listagem do modelo S1200INFOPERAPURREMUNPERAPUR"),
            ("can_print_data_s1200infoPerApurremunPerApur", u"Pode imprimir o conteúdo do modelo S1200INFOPERAPURREMUNPERAPUR"), )

        ordering = [
            's1200_infoperapur_ideestablot',]



class s1200infoPerApurremunPerApurSerializer(ModelSerializer):

    class Meta:

        model = s1200infoPerApurremunPerApur
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200procJudTrab(SoftDeletionModel):

    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun', )

    def evento(self):
        return self.s1200_evtremun.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1200_TPTRIB, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)

    class Meta:

        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's1200_procjudtrab'
        managed = True # s1200_procjudtrab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200procJudTrab", u"Pode ver listagem do modelo S1200PROCJUDTRAB"),
            ("can_see_data_s1200procJudTrab", u"Pode visualizar o conteúdo do modelo S1200PROCJUDTRAB"),
            ("can_see_menu_s1200procJudTrab", u"Pode visualizar no menu o modelo S1200PROCJUDTRAB"),
            ("can_print_list_s1200procJudTrab", u"Pode imprimir listagem do modelo S1200PROCJUDTRAB"),
            ("can_print_data_s1200procJudTrab", u"Pode imprimir o conteúdo do modelo S1200PROCJUDTRAB"), )

        ordering = [
            's1200_evtremun',
            'tptrib',
            'nrprocjud',]



class s1200procJudTrabSerializer(ModelSerializer):

    class Meta:

        model = s1200procJudTrab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200remunOutrEmpr(SoftDeletionModel):

    s1200_infomv = models.ForeignKey('s1200.s1200infoMV',
        related_name='%(class)s_s1200_infomv', )

    def evento(self):
        return self.s1200_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codcateg = models.IntegerField(null=True, )
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)

    class Meta:

        # verbose_name = u'Informações relativas ao trabalhador que possui vínculo empregatício com outra(s) empresa(s) e/ou que exerce outras atividades como contribuinte individual, detalhando as empresas que efetuaram (ou efetuarão) desconto da contribuição, ou ainda valores recolhidos pelo próprio trabalhador como contribuinte individual'
        db_table = r's1200_remunoutrempr'
        managed = True # s1200_remunoutrempr #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200remunOutrEmpr", u"Pode ver listagem do modelo S1200REMUNOUTREMPR"),
            ("can_see_data_s1200remunOutrEmpr", u"Pode visualizar o conteúdo do modelo S1200REMUNOUTREMPR"),
            ("can_see_menu_s1200remunOutrEmpr", u"Pode visualizar no menu o modelo S1200REMUNOUTREMPR"),
            ("can_print_list_s1200remunOutrEmpr", u"Pode imprimir listagem do modelo S1200REMUNOUTREMPR"),
            ("can_print_data_s1200remunOutrEmpr", u"Pode imprimir o conteúdo do modelo S1200REMUNOUTREMPR"), )

        ordering = [
            's1200_infomv',
            'tpinsc',
            'nrinsc',
            'codcateg',
            'vlrremunoe',]



class s1200remunOutrEmprSerializer(ModelSerializer):

    class Meta:

        model = s1200remunOutrEmpr
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200sucessaoVinc(SoftDeletionModel):

    s1200_infocomplem = models.ForeignKey('s1200.s1200infoComplem',
        related_name='%(class)s_s1200_infocomplem', )

    def evento(self):
        return self.s1200_infocomplem.evento()
    tpinscant = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    cnpjempregant = models.CharField(max_length=14, null=True, )
    matricant = models.CharField(max_length=30, blank=True, null=True, )
    dtadm = models.DateField(null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s1200_infocomplem) + ' - ' + unicode(self.tpinscant) + ' - ' + unicode(self.cnpjempregant) + ' - ' + unicode(self.dtadm)

    class Meta:

        # verbose_name = u'Grupo de informações da sucessão de vínculo trabalhista/estatutário'
        db_table = r's1200_sucessaovinc'
        managed = True # s1200_sucessaovinc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s1200sucessaoVinc", u"Pode ver listagem do modelo S1200SUCESSAOVINC"),
            ("can_see_data_s1200sucessaoVinc", u"Pode visualizar o conteúdo do modelo S1200SUCESSAOVINC"),
            ("can_see_menu_s1200sucessaoVinc", u"Pode visualizar no menu o modelo S1200SUCESSAOVINC"),
            ("can_print_list_s1200sucessaoVinc", u"Pode imprimir listagem do modelo S1200SUCESSAOVINC"),
            ("can_print_data_s1200sucessaoVinc", u"Pode imprimir o conteúdo do modelo S1200SUCESSAOVINC"), )

        ordering = [
            's1200_infocomplem',
            'tpinscant',
            'cnpjempregant',
            'dtadm',]



class s1200sucessaoVincSerializer(ModelSerializer):

    class Meta:

        model = s1200sucessaoVinc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')