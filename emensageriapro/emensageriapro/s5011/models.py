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
from emensageriapro.s5011.choices import *
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





class s5011basesAquis(SoftDeletionModel):

    s5011_ideestab = models.ForeignKey('s5011.s5011ideEstab',
        related_name='%(class)s_s5011_ideestab', )

    def evento(self):
        return self.s5011_ideestab.evento()
    indaquis = models.IntegerField(choices=CHOICES_S5011_INDAQUIS, null=True, )
    vlraquis = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpcalcpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrratcalcpr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsenarcalc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.indaquis) + ' - ' + unicode(self.vlraquis) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrcpnret) + ' - ' + unicode(self.vrratnret) + ' - ' + unicode(self.vrsenarnret) + ' - ' + unicode(self.vrcpcalcpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrratcalcpr) + ' - ' + unicode(self.vrsenardesc) + ' - ' + unicode(self.vrsenarcalc)

    class Meta:

        # verbose_name = u'Informações de bases de cálculo relativas a aquisição de produção rural'
        db_table = r's5011_basesaquis'
        managed = True # s5011_basesaquis #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011basesAquis", u"Pode ver listagem do modelo S5011BASESAQUIS"),
            ("can_see_data_s5011basesAquis", u"Pode visualizar o conteúdo do modelo S5011BASESAQUIS"),
            ("can_see_menu_s5011basesAquis", u"Pode visualizar no menu o modelo S5011BASESAQUIS"),
            ("can_print_list_s5011basesAquis", u"Pode imprimir listagem do modelo S5011BASESAQUIS"),
            ("can_print_data_s5011basesAquis", u"Pode imprimir o conteúdo do modelo S5011BASESAQUIS"), )

        ordering = [
            's5011_ideestab',
            'indaquis',
            'vlraquis',
            'vrcpdescpr',
            'vrcpnret',
            'vrratnret',
            'vrsenarnret',
            'vrcpcalcpr',
            'vrratdescpr',
            'vrratcalcpr',
            'vrsenardesc',
            'vrsenarcalc',]



class s5011basesAquisSerializer(ModelSerializer):

    class Meta:

        model = s5011basesAquis
        fields = '__all__'


class s5011basesAvNPort(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp13 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbcfgts = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrbccp13) + ' - ' + unicode(self.vrbcfgts) + ' - ' + unicode(self.vrdesccp)

    class Meta:

        # verbose_name = u'Informações de bases de cálculo relativas à contratação de trabalhadores avulsos não portuários'
        db_table = r's5011_basesavnport'
        managed = True # s5011_basesavnport #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011basesAvNPort", u"Pode ver listagem do modelo S5011BASESAVNPORT"),
            ("can_see_data_s5011basesAvNPort", u"Pode visualizar o conteúdo do modelo S5011BASESAVNPORT"),
            ("can_see_menu_s5011basesAvNPort", u"Pode visualizar no menu o modelo S5011BASESAVNPORT"),
            ("can_print_list_s5011basesAvNPort", u"Pode imprimir listagem do modelo S5011BASESAVNPORT"),
            ("can_print_data_s5011basesAvNPort", u"Pode imprimir o conteúdo do modelo S5011BASESAVNPORT"), )

        ordering = [
            's5011_idelotacao',
            'vrbccp00',
            'vrbccp15',
            'vrbccp20',
            'vrbccp25',
            'vrbccp13',
            'vrbcfgts',
            'vrdesccp',]



class s5011basesAvNPortSerializer(ModelSerializer):

    class Meta:

        model = s5011basesAvNPort
        fields = '__all__'


class s5011basesComerc(SoftDeletionModel):

    s5011_ideestab = models.ForeignKey('s5011.s5011ideEstab',
        related_name='%(class)s_s5011_ideestab', )

    def evento(self):
        return self.s5011_ideestab.evento()
    indcomerc = models.IntegerField(choices=CHOICES_S5011_INDCOMERC, null=True, )
    vrbccompr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrratsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.indcomerc) + ' - ' + unicode(self.vrbccompr)

    class Meta:

        # verbose_name = u'Informações de bases de cálculo relativas à comercialização da produção rural da Pessoa Física. Informações desse grupo conforme informado pelo contribuinte em S-1260.'
        db_table = r's5011_basescomerc'
        managed = True # s5011_basescomerc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011basesComerc", u"Pode ver listagem do modelo S5011BASESCOMERC"),
            ("can_see_data_s5011basesComerc", u"Pode visualizar o conteúdo do modelo S5011BASESCOMERC"),
            ("can_see_menu_s5011basesComerc", u"Pode visualizar no menu o modelo S5011BASESCOMERC"),
            ("can_print_list_s5011basesComerc", u"Pode imprimir listagem do modelo S5011BASESCOMERC"),
            ("can_print_data_s5011basesComerc", u"Pode imprimir o conteúdo do modelo S5011BASESCOMERC"), )

        ordering = [
            's5011_ideestab',
            'indcomerc',
            'vrbccompr',]



class s5011basesComercSerializer(ModelSerializer):

    class Meta:

        model = s5011basesComerc
        fields = '__all__'


class s5011basesRemun(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    indincid = models.IntegerField(choices=CHOICES_S5011_INDINCID, null=True, )
    codcateg = models.IntegerField(null=True, )
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsuspbccp00 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsuspbccp15 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsuspbccp20 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsuspbccp25 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdescsest = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcalcsest = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdescsenat = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcalcsenat = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsalfam = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsalmat = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.indincid) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrsuspbccp00) + ' - ' + unicode(self.vrsuspbccp15) + ' - ' + unicode(self.vrsuspbccp20) + ' - ' + unicode(self.vrsuspbccp25) + ' - ' + unicode(self.vrdescsest) + ' - ' + unicode(self.vrcalcsest) + ' - ' + unicode(self.vrdescsenat) + ' - ' + unicode(self.vrcalcsenat) + ' - ' + unicode(self.vrsalfam) + ' - ' + unicode(self.vrsalmat)

    class Meta:

        # verbose_name = u'Bases de cálculo da contribuição previdenciária incidente sobre remunerações, por categoria.'
        db_table = r's5011_basesremun'
        managed = True # s5011_basesremun #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011basesRemun", u"Pode ver listagem do modelo S5011BASESREMUN"),
            ("can_see_data_s5011basesRemun", u"Pode visualizar o conteúdo do modelo S5011BASESREMUN"),
            ("can_see_menu_s5011basesRemun", u"Pode visualizar no menu o modelo S5011BASESREMUN"),
            ("can_print_list_s5011basesRemun", u"Pode imprimir listagem do modelo S5011BASESREMUN"),
            ("can_print_data_s5011basesRemun", u"Pode imprimir o conteúdo do modelo S5011BASESREMUN"), )

        ordering = [
            's5011_idelotacao',
            'indincid',
            'codcateg',
            'vrbccp00',
            'vrbccp15',
            'vrbccp20',
            'vrbccp25',
            'vrsuspbccp00',
            'vrsuspbccp15',
            'vrsuspbccp20',
            'vrsuspbccp25',
            'vrdescsest',
            'vrcalcsest',
            'vrdescsenat',
            'vrcalcsenat',
            'vrsalfam',
            'vrsalmat',]



class s5011basesRemunSerializer(ModelSerializer):

    class Meta:

        model = s5011basesRemun
        fields = '__all__'


class s5011dadosOpPort(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S5011_ALIQRAT, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)

    class Meta:

        # verbose_name = u'Detalhamento das informações do Operador Portuário que está sendo incluído (origem S-1080).'
        db_table = r's5011_dadosopport'
        managed = True # s5011_dadosopport #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011dadosOpPort", u"Pode ver listagem do modelo S5011DADOSOPPORT"),
            ("can_see_data_s5011dadosOpPort", u"Pode visualizar o conteúdo do modelo S5011DADOSOPPORT"),
            ("can_see_menu_s5011dadosOpPort", u"Pode visualizar no menu o modelo S5011DADOSOPPORT"),
            ("can_print_list_s5011dadosOpPort", u"Pode imprimir listagem do modelo S5011DADOSOPPORT"),
            ("can_print_data_s5011dadosOpPort", u"Pode imprimir o conteúdo do modelo S5011DADOSOPPORT"), )

        ordering = [
            's5011_idelotacao',
            'cnpjopportuario',
            'aliqrat',
            'fap',
            'aliqratajust',]



class s5011dadosOpPortSerializer(ModelSerializer):

    class Meta:

        model = s5011dadosOpPort
        fields = '__all__'


class s5011ideEstab(SoftDeletionModel):

    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs', )

    def evento(self):
        return self.s5011_evtcs.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)

    class Meta:

        # verbose_name = u'Informações de identificação do estabelecimento, obra ou órgão público e período de validade das informações que estão sendo incluídas'
        db_table = r's5011_ideestab'
        managed = True # s5011_ideestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011ideEstab", u"Pode ver listagem do modelo S5011IDEESTAB"),
            ("can_see_data_s5011ideEstab", u"Pode visualizar o conteúdo do modelo S5011IDEESTAB"),
            ("can_see_menu_s5011ideEstab", u"Pode visualizar no menu o modelo S5011IDEESTAB"),
            ("can_print_list_s5011ideEstab", u"Pode imprimir listagem do modelo S5011IDEESTAB"),
            ("can_print_data_s5011ideEstab", u"Pode imprimir o conteúdo do modelo S5011IDEESTAB"), )

        ordering = [
            's5011_evtcs',
            'tpinsc',
            'nrinsc',]



class s5011ideEstabSerializer(ModelSerializer):

    class Meta:

        model = s5011ideEstab
        fields = '__all__'


class s5011ideLotacao(SoftDeletionModel):

    s5011_ideestab = models.ForeignKey('s5011.s5011ideEstab',
        related_name='%(class)s_s5011_ideestab', )

    def evento(self):
        return self.s5011_ideestab.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    fpas = models.IntegerField(null=True, )
    codtercs = models.TextField(null=True, )
    codtercssusp = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs)

    class Meta:

        # verbose_name = u'Informações de identificação da lotação e validade das informações que estão sendo incluídas'
        db_table = r's5011_idelotacao'
        managed = True # s5011_idelotacao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011ideLotacao", u"Pode ver listagem do modelo S5011IDELOTACAO"),
            ("can_see_data_s5011ideLotacao", u"Pode visualizar o conteúdo do modelo S5011IDELOTACAO"),
            ("can_see_menu_s5011ideLotacao", u"Pode visualizar no menu o modelo S5011IDELOTACAO"),
            ("can_print_list_s5011ideLotacao", u"Pode imprimir listagem do modelo S5011IDELOTACAO"),
            ("can_print_data_s5011ideLotacao", u"Pode imprimir o conteúdo do modelo S5011IDELOTACAO"), )

        ordering = [
            's5011_ideestab',
            'codlotacao',
            'fpas',
            'codtercs',]



class s5011ideLotacaoSerializer(ModelSerializer):

    class Meta:

        model = s5011ideLotacao
        fields = '__all__'


class s5011infoAtConc(SoftDeletionModel):

    s5011_infopj = models.ForeignKey('s5011.s5011infoPJ',
        related_name='%(class)s_s5011_infopj', )

    def evento(self):
        return self.s5011_infopj.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_infopj) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)

    class Meta:

        # verbose_name = u'Informações prestadas por empresa enquadrada no Regime de Tributação Simples Nacional com tributação previdenciária substituída e não substituída.'
        db_table = r's5011_infoatconc'
        managed = True # s5011_infoatconc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoAtConc", u"Pode ver listagem do modelo S5011INFOATCONC"),
            ("can_see_data_s5011infoAtConc", u"Pode visualizar o conteúdo do modelo S5011INFOATCONC"),
            ("can_see_menu_s5011infoAtConc", u"Pode visualizar no menu o modelo S5011INFOATCONC"),
            ("can_print_list_s5011infoAtConc", u"Pode imprimir listagem do modelo S5011INFOATCONC"),
            ("can_print_data_s5011infoAtConc", u"Pode imprimir o conteúdo do modelo S5011INFOATCONC"), )

        ordering = [
            's5011_infopj',
            'fatormes',
            'fator13',]



class s5011infoAtConcSerializer(ModelSerializer):

    class Meta:

        model = s5011infoAtConc
        fields = '__all__'


class s5011infoCPSeg(SoftDeletionModel):

    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs', )

    def evento(self):
        return self.s5011_evtcs.evento()
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcpseg = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.vrdesccp) + ' - ' + unicode(self.vrcpseg)

    class Meta:

        # verbose_name = u'Informações de contribuição previdenciária do Segurado'
        db_table = r's5011_infocpseg'
        managed = True # s5011_infocpseg #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoCPSeg", u"Pode ver listagem do modelo S5011INFOCPSEG"),
            ("can_see_data_s5011infoCPSeg", u"Pode visualizar o conteúdo do modelo S5011INFOCPSEG"),
            ("can_see_menu_s5011infoCPSeg", u"Pode visualizar no menu o modelo S5011INFOCPSEG"),
            ("can_print_list_s5011infoCPSeg", u"Pode imprimir listagem do modelo S5011INFOCPSEG"),
            ("can_print_data_s5011infoCPSeg", u"Pode imprimir o conteúdo do modelo S5011INFOCPSEG"), )

        ordering = [
            's5011_evtcs',
            'vrdesccp',
            'vrcpseg',]



class s5011infoCPSegSerializer(ModelSerializer):

    class Meta:

        model = s5011infoCPSeg
        fields = '__all__'


class s5011infoCRContrib(SoftDeletionModel):

    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs', )

    def evento(self):
        return self.s5011_evtcs.evento()
    tpcr = models.CharField(max_length=6, null=True, )
    vrcr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrcrsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcr)

    class Meta:

        # verbose_name = u'Informações consolidadas das contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, por código de Receita - CR.'
        db_table = r's5011_infocrcontrib'
        managed = True # s5011_infocrcontrib #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoCRContrib", u"Pode ver listagem do modelo S5011INFOCRCONTRIB"),
            ("can_see_data_s5011infoCRContrib", u"Pode visualizar o conteúdo do modelo S5011INFOCRCONTRIB"),
            ("can_see_menu_s5011infoCRContrib", u"Pode visualizar no menu o modelo S5011INFOCRCONTRIB"),
            ("can_print_list_s5011infoCRContrib", u"Pode imprimir listagem do modelo S5011INFOCRCONTRIB"),
            ("can_print_data_s5011infoCRContrib", u"Pode imprimir o conteúdo do modelo S5011INFOCRCONTRIB"), )

        ordering = [
            's5011_evtcs',
            'tpcr',
            'vrcr',]



class s5011infoCRContribSerializer(ModelSerializer):

    class Meta:

        model = s5011infoCRContrib
        fields = '__all__'


class s5011infoCREstab(SoftDeletionModel):

    s5011_ideestab = models.ForeignKey('s5011.s5011ideEstab',
        related_name='%(class)s_s5011_ideestab', )

    def evento(self):
        return self.s5011_ideestab.evento()
    tpcr = models.CharField(max_length=6, null=True, )
    vrcr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrsuspcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcr)

    class Meta:

        # verbose_name = u'Informações das contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, consolidadas por estabelecimento e por código de Receita - CR.'
        db_table = r's5011_infocrestab'
        managed = True # s5011_infocrestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoCREstab", u"Pode ver listagem do modelo S5011INFOCRESTAB"),
            ("can_see_data_s5011infoCREstab", u"Pode visualizar o conteúdo do modelo S5011INFOCRESTAB"),
            ("can_see_menu_s5011infoCREstab", u"Pode visualizar no menu o modelo S5011INFOCRESTAB"),
            ("can_print_list_s5011infoCREstab", u"Pode imprimir listagem do modelo S5011INFOCRESTAB"),
            ("can_print_data_s5011infoCREstab", u"Pode imprimir o conteúdo do modelo S5011INFOCRESTAB"), )

        ordering = [
            's5011_ideestab',
            'tpcr',
            'vrcr',]



class s5011infoCREstabSerializer(ModelSerializer):

    class Meta:

        model = s5011infoCREstab
        fields = '__all__'


class s5011infoComplObra(SoftDeletionModel):

    s5011_infoestab = models.ForeignKey('s5011.s5011infoEstab',
        related_name='%(class)s_s5011_infoestab', )

    def evento(self):
        return self.s5011_infoestab.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S5011_INDSUBSTPATROBRA, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_infoestab) + ' - ' + unicode(self.indsubstpatrobra)

    class Meta:

        # verbose_name = u'Informações complementares relativas a obras de construção civil'
        db_table = r's5011_infocomplobra'
        managed = True # s5011_infocomplobra #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoComplObra", u"Pode ver listagem do modelo S5011INFOCOMPLOBRA"),
            ("can_see_data_s5011infoComplObra", u"Pode visualizar o conteúdo do modelo S5011INFOCOMPLOBRA"),
            ("can_see_menu_s5011infoComplObra", u"Pode visualizar no menu o modelo S5011INFOCOMPLOBRA"),
            ("can_print_list_s5011infoComplObra", u"Pode imprimir listagem do modelo S5011INFOCOMPLOBRA"),
            ("can_print_data_s5011infoComplObra", u"Pode imprimir o conteúdo do modelo S5011INFOCOMPLOBRA"), )

        ordering = [
            's5011_infoestab',
            'indsubstpatrobra',]



class s5011infoComplObraSerializer(ModelSerializer):

    class Meta:

        model = s5011infoComplObra
        fields = '__all__'


class s5011infoEmprParcial(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S5011_TPINSCCONTRAT, null=True, )
    nrinsccontrat = models.CharField(max_length=14, null=True, )
    tpinscprop = models.IntegerField(choices=CHOICES_S5011_TPINSCPROP, null=True, )
    nrinscprop = models.CharField(max_length=14, null=True, )
    cnoobra = models.CharField(max_length=12, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop) + ' - ' + unicode(self.cnoobra)

    class Meta:

        # verbose_name = u'Informação complementar que apresenta identificação do contratante e do proprietário de obra de construção civil contratada sob regime de empreitada parcial ou subempreitada'
        db_table = r's5011_infoemprparcial'
        managed = True # s5011_infoemprparcial #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoEmprParcial", u"Pode ver listagem do modelo S5011INFOEMPRPARCIAL"),
            ("can_see_data_s5011infoEmprParcial", u"Pode visualizar o conteúdo do modelo S5011INFOEMPRPARCIAL"),
            ("can_see_menu_s5011infoEmprParcial", u"Pode visualizar no menu o modelo S5011INFOEMPRPARCIAL"),
            ("can_print_list_s5011infoEmprParcial", u"Pode imprimir listagem do modelo S5011INFOEMPRPARCIAL"),
            ("can_print_data_s5011infoEmprParcial", u"Pode imprimir o conteúdo do modelo S5011INFOEMPRPARCIAL"), )

        ordering = [
            's5011_idelotacao',
            'tpinsccontrat',
            'nrinsccontrat',
            'tpinscprop',
            'nrinscprop',
            'cnoobra',]



class s5011infoEmprParcialSerializer(ModelSerializer):

    class Meta:

        model = s5011infoEmprParcial
        fields = '__all__'


class s5011infoEstab(SoftDeletionModel):

    s5011_ideestab = models.ForeignKey('s5011.s5011ideEstab',
        related_name='%(class)s_s5011_ideestab', )

    def evento(self):
        return self.s5011_ideestab.evento()
    cnaeprep = models.IntegerField(null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S5011_ALIQRAT, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.cnaeprep) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)

    class Meta:

        # verbose_name = u'Informações do Estabelecimento ou obra'
        db_table = r's5011_infoestab'
        managed = True # s5011_infoestab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoEstab", u"Pode ver listagem do modelo S5011INFOESTAB"),
            ("can_see_data_s5011infoEstab", u"Pode visualizar o conteúdo do modelo S5011INFOESTAB"),
            ("can_see_menu_s5011infoEstab", u"Pode visualizar no menu o modelo S5011INFOESTAB"),
            ("can_print_list_s5011infoEstab", u"Pode imprimir listagem do modelo S5011INFOESTAB"),
            ("can_print_data_s5011infoEstab", u"Pode imprimir o conteúdo do modelo S5011INFOESTAB"), )

        ordering = [
            's5011_ideestab',
            'cnaeprep',
            'aliqrat',
            'fap',
            'aliqratajust',]



class s5011infoEstabSerializer(ModelSerializer):

    class Meta:

        model = s5011infoEstab
        fields = '__all__'


class s5011infoPJ(SoftDeletionModel):

    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs', )

    def evento(self):
        return self.s5011_evtcs.evento()
    indcoop = models.IntegerField(choices=CHOICES_S5011_INDCOOP, blank=True, null=True, )
    indconstr = models.IntegerField(choices=CHOICES_S5011_INDCONSTR, null=True, )
    indsubstpatr = models.IntegerField(choices=CHOICES_S5011_INDSUBSTPATR, blank=True, null=True, )
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.indconstr)

    class Meta:

        # verbose_name = u'Informações complementares, exclusivas da Pessoa Jurídica.'
        db_table = r's5011_infopj'
        managed = True # s5011_infopj #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoPJ", u"Pode ver listagem do modelo S5011INFOPJ"),
            ("can_see_data_s5011infoPJ", u"Pode visualizar o conteúdo do modelo S5011INFOPJ"),
            ("can_see_menu_s5011infoPJ", u"Pode visualizar no menu o modelo S5011INFOPJ"),
            ("can_print_list_s5011infoPJ", u"Pode imprimir listagem do modelo S5011INFOPJ"),
            ("can_print_data_s5011infoPJ", u"Pode imprimir o conteúdo do modelo S5011INFOPJ"), )

        ordering = [
            's5011_evtcs',
            'indconstr',]



class s5011infoPJSerializer(ModelSerializer):

    class Meta:

        model = s5011infoPJ
        fields = '__all__'


class s5011infoSubstPatrOpPort(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    cnpjopportuario = models.CharField(max_length=14, null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.cnpjopportuario)

    class Meta:

        # verbose_name = u'Registro preenchido exclusivamente pelo OGMO ({classTrib}=[09]) listando apenas seus Operadores Portuários enquadrados nos artigos 7 a 9 da Lei 12.546/2011.'
        db_table = r's5011_infosubstpatropport'
        managed = True # s5011_infosubstpatropport #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoSubstPatrOpPort", u"Pode ver listagem do modelo S5011INFOSUBSTPATROPPORT"),
            ("can_see_data_s5011infoSubstPatrOpPort", u"Pode visualizar o conteúdo do modelo S5011INFOSUBSTPATROPPORT"),
            ("can_see_menu_s5011infoSubstPatrOpPort", u"Pode visualizar no menu o modelo S5011INFOSUBSTPATROPPORT"),
            ("can_print_list_s5011infoSubstPatrOpPort", u"Pode imprimir listagem do modelo S5011INFOSUBSTPATROPPORT"),
            ("can_print_data_s5011infoSubstPatrOpPort", u"Pode imprimir o conteúdo do modelo S5011INFOSUBSTPATROPPORT"), )

        ordering = [
            's5011_idelotacao',
            'cnpjopportuario',]



class s5011infoSubstPatrOpPortSerializer(ModelSerializer):

    class Meta:

        model = s5011infoSubstPatrOpPort
        fields = '__all__'


class s5011infoTercSusp(SoftDeletionModel):

    s5011_idelotacao = models.ForeignKey('s5011.s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao', )

    def evento(self):
        return self.s5011_idelotacao.evento()
    codterc = models.TextField(null=True, )

    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.codterc)

    class Meta:

        # verbose_name = u'Informações de suspensão de contribuições destinadas a Outras Entidades e Fundos (Terceiros).'
        db_table = r's5011_infotercsusp'
        managed = True # s5011_infotercsusp #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5011infoTercSusp", u"Pode ver listagem do modelo S5011INFOTERCSUSP"),
            ("can_see_data_s5011infoTercSusp", u"Pode visualizar o conteúdo do modelo S5011INFOTERCSUSP"),
            ("can_see_menu_s5011infoTercSusp", u"Pode visualizar no menu o modelo S5011INFOTERCSUSP"),
            ("can_print_list_s5011infoTercSusp", u"Pode imprimir listagem do modelo S5011INFOTERCSUSP"),
            ("can_print_data_s5011infoTercSusp", u"Pode imprimir o conteúdo do modelo S5011INFOTERCSUSP"), )

        ordering = [
            's5011_idelotacao',
            'codterc',]



class s5011infoTercSuspSerializer(ModelSerializer):

    class Meta:

        model = s5011infoTercSusp
        fields = '__all__'