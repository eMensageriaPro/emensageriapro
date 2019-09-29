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
from emensageriapro.s2205.choices import *
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





class s2205CNH(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nrregcnh = models.CharField(max_length=12, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    ufcnh = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    dtvalid = models.DateField(null=True, )
    dtprihab = models.DateField(blank=True, null=True, )
    categoriacnh = models.CharField(choices=CHOICES_S2205_CATEGORIACNH, max_length=2, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.categoriacnh)

    class Meta:

        # verbose_name = u'Informações da Carteira Nacional de Habilitação (CNH)'
        db_table = r's2205_cnh'
        managed = True # s2205_cnh #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205CNH", u"Pode ver listagem do modelo S2205CNH"),
            ("can_see_data_s2205CNH", u"Pode visualizar o conteúdo do modelo S2205CNH"),
            ("can_see_menu_s2205CNH", u"Pode visualizar no menu o modelo S2205CNH"),
            ("can_print_list_s2205CNH", u"Pode imprimir listagem do modelo S2205CNH"),
            ("can_print_data_s2205CNH", u"Pode imprimir o conteúdo do modelo S2205CNH"), )

        ordering = [
            's2205_documentos',
            'nrregcnh',
            'ufcnh',
            'dtvalid',
            'categoriacnh',]



class s2205CNHSerializer(ModelSerializer):

    class Meta:

        model = s2205CNH
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205CTPS(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nrctps = models.CharField(max_length=11, null=True, )
    seriectps = models.CharField(max_length=5, null=True, )
    ufctps = models.CharField(choices=ESTADOS, max_length=2, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)

    class Meta:

        # verbose_name = u'Informações da Carteira de Trabalho e Previdência Social'
        db_table = r's2205_ctps'
        managed = True # s2205_ctps #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205CTPS", u"Pode ver listagem do modelo S2205CTPS"),
            ("can_see_data_s2205CTPS", u"Pode visualizar o conteúdo do modelo S2205CTPS"),
            ("can_see_menu_s2205CTPS", u"Pode visualizar no menu o modelo S2205CTPS"),
            ("can_print_list_s2205CTPS", u"Pode imprimir listagem do modelo S2205CTPS"),
            ("can_print_data_s2205CTPS", u"Pode imprimir o conteúdo do modelo S2205CTPS"), )

        ordering = [
            's2205_documentos',
            'nrctps',
            'seriectps',
            'ufctps',]



class s2205CTPSSerializer(ModelSerializer):

    class Meta:

        model = s2205CTPS
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205OC(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nroc = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    dtvalid = models.DateField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor)

    class Meta:

        # verbose_name = u'Informações do número de registro em Órgão de Classe (OC)'
        db_table = r's2205_oc'
        managed = True # s2205_oc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205OC", u"Pode ver listagem do modelo S2205OC"),
            ("can_see_data_s2205OC", u"Pode visualizar o conteúdo do modelo S2205OC"),
            ("can_see_menu_s2205OC", u"Pode visualizar no menu o modelo S2205OC"),
            ("can_print_list_s2205OC", u"Pode imprimir listagem do modelo S2205OC"),
            ("can_print_data_s2205OC", u"Pode imprimir o conteúdo do modelo S2205OC"), )

        ordering = [
            's2205_documentos',
            'nroc',
            'orgaoemissor',]



class s2205OCSerializer(ModelSerializer):

    class Meta:

        model = s2205OC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205RG(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nrrg = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor)

    class Meta:

        # verbose_name = u'Informações do Registro Geral (RG)'
        db_table = r's2205_rg'
        managed = True # s2205_rg #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205RG", u"Pode ver listagem do modelo S2205RG"),
            ("can_see_data_s2205RG", u"Pode visualizar o conteúdo do modelo S2205RG"),
            ("can_see_menu_s2205RG", u"Pode visualizar no menu o modelo S2205RG"),
            ("can_print_list_s2205RG", u"Pode imprimir listagem do modelo S2205RG"),
            ("can_print_data_s2205RG", u"Pode imprimir o conteúdo do modelo S2205RG"), )

        ordering = [
            's2205_documentos',
            'nrrg',
            'orgaoemissor',]



class s2205RGSerializer(ModelSerializer):

    class Meta:

        model = s2205RG
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205RIC(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nrric = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor)

    class Meta:

        # verbose_name = u'Informações do Documento Nacional de Identidade - DNI (Registro de Identificação Civil - RIC)'
        db_table = r's2205_ric'
        managed = True # s2205_ric #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205RIC", u"Pode ver listagem do modelo S2205RIC"),
            ("can_see_data_s2205RIC", u"Pode visualizar o conteúdo do modelo S2205RIC"),
            ("can_see_menu_s2205RIC", u"Pode visualizar no menu o modelo S2205RIC"),
            ("can_print_list_s2205RIC", u"Pode imprimir listagem do modelo S2205RIC"),
            ("can_print_data_s2205RIC", u"Pode imprimir o conteúdo do modelo S2205RIC"), )

        ordering = [
            's2205_documentos',
            'nrric',
            'orgaoemissor',]



class s2205RICSerializer(ModelSerializer):

    class Meta:

        model = s2205RIC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205RNE(SoftDeletionModel):

    s2205_documentos = models.ForeignKey('s2205.s2205documentos',
        related_name='%(class)s_s2205_documentos', )

    def evento(self):
        return self.s2205_documentos.evento()
    nrrne = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor)

    class Meta:

        # verbose_name = u'Informações do Registro Nacional de Estrangeiro'
        db_table = r's2205_rne'
        managed = True # s2205_rne #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205RNE", u"Pode ver listagem do modelo S2205RNE"),
            ("can_see_data_s2205RNE", u"Pode visualizar o conteúdo do modelo S2205RNE"),
            ("can_see_menu_s2205RNE", u"Pode visualizar no menu o modelo S2205RNE"),
            ("can_print_list_s2205RNE", u"Pode imprimir listagem do modelo S2205RNE"),
            ("can_print_data_s2205RNE", u"Pode imprimir o conteúdo do modelo S2205RNE"), )

        ordering = [
            's2205_documentos',
            'nrrne',
            'orgaoemissor',]



class s2205RNESerializer(ModelSerializer):

    class Meta:

        model = s2205RNE
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205aposentadoria(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    trabaposent = models.CharField(choices=CHOICES_S2205_TRABAPOSENT, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.trabaposent)

    class Meta:

        # verbose_name = u'Informação de aposentadoria do trabalhador'
        db_table = r's2205_aposentadoria'
        managed = True # s2205_aposentadoria #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205aposentadoria", u"Pode ver listagem do modelo S2205APOSENTADORIA"),
            ("can_see_data_s2205aposentadoria", u"Pode visualizar o conteúdo do modelo S2205APOSENTADORIA"),
            ("can_see_menu_s2205aposentadoria", u"Pode visualizar no menu o modelo S2205APOSENTADORIA"),
            ("can_print_list_s2205aposentadoria", u"Pode imprimir listagem do modelo S2205APOSENTADORIA"),
            ("can_print_data_s2205aposentadoria", u"Pode imprimir o conteúdo do modelo S2205APOSENTADORIA"), )

        ordering = [
            's2205_evtaltcadastral',
            'trabaposent',]



class s2205aposentadoriaSerializer(ModelSerializer):

    class Meta:

        model = s2205aposentadoria
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205brasil(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    tplograd = models.TextField(blank=True, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.IntegerField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)

    class Meta:

        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2205_brasil'
        managed = True # s2205_brasil #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205brasil", u"Pode ver listagem do modelo S2205BRASIL"),
            ("can_see_data_s2205brasil", u"Pode visualizar o conteúdo do modelo S2205BRASIL"),
            ("can_see_menu_s2205brasil", u"Pode visualizar no menu o modelo S2205BRASIL"),
            ("can_print_list_s2205brasil", u"Pode imprimir listagem do modelo S2205BRASIL"),
            ("can_print_data_s2205brasil", u"Pode imprimir o conteúdo do modelo S2205BRASIL"), )

        ordering = [
            's2205_evtaltcadastral',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2205brasilSerializer(ModelSerializer):

    class Meta:

        model = s2205brasil
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205contato(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True, )
    fonealternat = models.CharField(max_length=13, blank=True, null=True, )
    emailprinc = models.CharField(max_length=60, blank=True, null=True, )
    emailalternat = models.CharField(max_length=60, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral)

    class Meta:

        # verbose_name = u'Informações de contato'
        db_table = r's2205_contato'
        managed = True # s2205_contato #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205contato", u"Pode ver listagem do modelo S2205CONTATO"),
            ("can_see_data_s2205contato", u"Pode visualizar o conteúdo do modelo S2205CONTATO"),
            ("can_see_menu_s2205contato", u"Pode visualizar no menu o modelo S2205CONTATO"),
            ("can_print_list_s2205contato", u"Pode imprimir listagem do modelo S2205CONTATO"),
            ("can_print_data_s2205contato", u"Pode imprimir o conteúdo do modelo S2205CONTATO"), )

        ordering = [
            's2205_evtaltcadastral',]



class s2205contatoSerializer(ModelSerializer):

    class Meta:

        model = s2205contato
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205dependente(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    sexodep = models.CharField(choices=CHOICES_S2205_SEXODEP, max_length=1, blank=True, null=True, )
    depirrf = models.CharField(choices=CHOICES_S2205_DEPIRRF, max_length=1, null=True, )
    depsf = models.CharField(choices=CHOICES_S2205_DEPSF, max_length=1, null=True, )
    inctrab = models.CharField(choices=CHOICES_S2205_INCTRAB, max_length=1, null=True, )
    depfinsprev = models.CharField(choices=CHOICES_S2205_DEPFINSPREV, max_length=1, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab)

    class Meta:

        # verbose_name = u'Informações dos dependentes'
        db_table = r's2205_dependente'
        managed = True # s2205_dependente #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205dependente", u"Pode ver listagem do modelo S2205DEPENDENTE"),
            ("can_see_data_s2205dependente", u"Pode visualizar o conteúdo do modelo S2205DEPENDENTE"),
            ("can_see_menu_s2205dependente", u"Pode visualizar no menu o modelo S2205DEPENDENTE"),
            ("can_print_list_s2205dependente", u"Pode imprimir listagem do modelo S2205DEPENDENTE"),
            ("can_print_data_s2205dependente", u"Pode imprimir o conteúdo do modelo S2205DEPENDENTE"), )

        ordering = [
            's2205_evtaltcadastral',
            'tpdep',
            'nmdep',
            'dtnascto',
            'depirrf',
            'depsf',
            'inctrab',]



class s2205dependenteSerializer(ModelSerializer):

    class Meta:

        model = s2205dependente
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205documentos(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral)

    class Meta:

        # verbose_name = u'Informações dos documentos pessoais do trabalhador'
        db_table = r's2205_documentos'
        managed = True # s2205_documentos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205documentos", u"Pode ver listagem do modelo S2205DOCUMENTOS"),
            ("can_see_data_s2205documentos", u"Pode visualizar o conteúdo do modelo S2205DOCUMENTOS"),
            ("can_see_menu_s2205documentos", u"Pode visualizar no menu o modelo S2205DOCUMENTOS"),
            ("can_print_list_s2205documentos", u"Pode imprimir listagem do modelo S2205DOCUMENTOS"),
            ("can_print_data_s2205documentos", u"Pode imprimir o conteúdo do modelo S2205DOCUMENTOS"), )

        ordering = [
            's2205_evtaltcadastral',]



class s2205documentosSerializer(ModelSerializer):

    class Meta:

        model = s2205documentos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205exterior(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)

    class Meta:

        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2205_exterior'
        managed = True # s2205_exterior #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205exterior", u"Pode ver listagem do modelo S2205EXTERIOR"),
            ("can_see_data_s2205exterior", u"Pode visualizar o conteúdo do modelo S2205EXTERIOR"),
            ("can_see_menu_s2205exterior", u"Pode visualizar no menu o modelo S2205EXTERIOR"),
            ("can_print_list_s2205exterior", u"Pode imprimir listagem do modelo S2205EXTERIOR"),
            ("can_print_data_s2205exterior", u"Pode imprimir o conteúdo do modelo S2205EXTERIOR"), )

        ordering = [
            's2205_evtaltcadastral',
            'paisresid',
            'dsclograd',
            'nrlograd',
            'nmcid',]



class s2205exteriorSerializer(ModelSerializer):

    class Meta:

        model = s2205exterior
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205infoDeficiencia(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    deffisica = models.CharField(choices=CHOICES_S2205_DEFFISICA, max_length=1, null=True, )
    defvisual = models.CharField(choices=CHOICES_S2205_DEFVISUAL, max_length=1, null=True, )
    defauditiva = models.CharField(choices=CHOICES_S2205_DEFAUDITIVA, max_length=1, null=True, )
    defmental = models.CharField(choices=CHOICES_S2205_DEFMENTAL, max_length=1, null=True, )
    defintelectual = models.CharField(choices=CHOICES_S2205_DEFINTELECTUAL, max_length=1, null=True, )
    reabreadap = models.CharField(choices=CHOICES_S2205_REABREADAP, max_length=1, null=True, )
    infocota = models.CharField(choices=CHOICES_S2205_INFOCOTA, max_length=1, blank=True, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap)

    class Meta:

        # verbose_name = u'Pessoa com Deficiência'
        db_table = r's2205_infodeficiencia'
        managed = True # s2205_infodeficiencia #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205infoDeficiencia", u"Pode ver listagem do modelo S2205INFODEFICIENCIA"),
            ("can_see_data_s2205infoDeficiencia", u"Pode visualizar o conteúdo do modelo S2205INFODEFICIENCIA"),
            ("can_see_menu_s2205infoDeficiencia", u"Pode visualizar no menu o modelo S2205INFODEFICIENCIA"),
            ("can_print_list_s2205infoDeficiencia", u"Pode imprimir listagem do modelo S2205INFODEFICIENCIA"),
            ("can_print_data_s2205infoDeficiencia", u"Pode imprimir o conteúdo do modelo S2205INFODEFICIENCIA"), )

        ordering = [
            's2205_evtaltcadastral',
            'deffisica',
            'defvisual',
            'defauditiva',
            'defmental',
            'defintelectual',
            'reabreadap',]



class s2205infoDeficienciaSerializer(ModelSerializer):

    class Meta:

        model = s2205infoDeficiencia
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205trabEstrangeiro(SoftDeletionModel):

    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral', )

    def evento(self):
        return self.s2205_evtaltcadastral.evento()
    dtchegada = models.DateField(blank=True, null=True, )
    classtrabestrang = models.IntegerField(choices=CHOICES_S2205_CLASSTRABESTRANG, null=True, )
    casadobr = models.CharField(choices=CHOICES_S2205_CASADOBR, max_length=1, null=True, )
    filhosbr = models.CharField(choices=CHOICES_S2205_FILHOSBR, max_length=1, null=True, )

    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)

    class Meta:

        # verbose_name = u'Grupo de informações do Trabalhador Estrangeiro'
        db_table = r's2205_trabestrangeiro'
        managed = True # s2205_trabestrangeiro #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s2205trabEstrangeiro", u"Pode ver listagem do modelo S2205TRABESTRANGEIRO"),
            ("can_see_data_s2205trabEstrangeiro", u"Pode visualizar o conteúdo do modelo S2205TRABESTRANGEIRO"),
            ("can_see_menu_s2205trabEstrangeiro", u"Pode visualizar no menu o modelo S2205TRABESTRANGEIRO"),
            ("can_print_list_s2205trabEstrangeiro", u"Pode imprimir listagem do modelo S2205TRABESTRANGEIRO"),
            ("can_print_data_s2205trabEstrangeiro", u"Pode imprimir o conteúdo do modelo S2205TRABESTRANGEIRO"), )

        ordering = [
            's2205_evtaltcadastral',
            'classtrabestrang',
            'casadobr',
            'filhosbr',]



class s2205trabEstrangeiroSerializer(ModelSerializer):

    class Meta:

        model = s2205trabEstrangeiro
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')