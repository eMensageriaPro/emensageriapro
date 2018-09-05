#coding: utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S5011_TPINSC = (
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5011_ALIQRAT = (
    (1, u'1 - 1'),
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
    (3, u'3 - 3'),
)

CHOICES_S5011_INDAQUIS = (
    (1, u'1 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral'),
    (2, u'2 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA'),
    (3, u'3 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA. Evento de origem (S- 1250)'),
    (4, u'4 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral - Produção Isenta (Lei 13.606/2018)'),
    (5, u'5 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA - Produção Isenta (Lei 13.606/2018)'),
    (6, u'6 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA - Produção Isenta (Lei 13.606/2018)'),
)

CHOICES_S5011_INDCOMERC = (
    (2, u'2 - Comercialização da Produção efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa física por Produtor Rural Pessoa Física, inclusive por Segurado Especial ou por Pessoa Física não produtor rural'),
    (3, u'3 - Comercialização da Produção por Prod. Rural PF/Seg. Especia - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisição de Alimentos - PAA) ou a Intermediário PF'),
    (7, u'7 - Comercialização da Produção Isenta de acordo com a Lei no 13.606/2018'),
    (8, u'8 - Comercialização da Produção da Pessoa Física/Segurado Especial para Entidade inscrita no Programa de Aquisição de Alimentos - PAA'),
    (9, u'9 - Comercialização da Produção no Mercado Externo'),
)

CHOICES_S5011_INDCOOP = (
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas'),
)

CHOICES_S5011_TPINSCCONTRAT = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5011_TPINSCPROP = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5011_INDINCID = (
    (1, u'1 - Normal'),
    (2, u'2 - Ativ. Concomitante'),
    (9, u'9 - Substituída ou Isenta'),
)

CHOICES_S5011_INDCONSTR = (
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora'),
)

CHOICES_S5011_INDSUBSTPATR = (
    (1, u'1 - Integralmente substituída'),
    (2, u'2 - Parcialmente substituída'),
)

CHOICES_S5011_INDSUBSTPATROBRA = (
    (1, u'1 - Contribuição Patronal Substituída'),
    (2, u'2 - Contribuição Patronal Não Substituída'),
)

class s5011basesAquis(models.Model):
    s5011_ideestab = models.ForeignKey('s5011ideEstab',
        related_name='%(class)s_s5011_ideestab')
    def evento(self): return self.s5011_ideestab.evento()
    indaquis = models.IntegerField(choices=CHOICES_S5011_INDAQUIS)
    vlraquis = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpcalcpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratcalcpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenarcalc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.indaquis) + ' - ' + unicode(self.vlraquis) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrcpnret) + ' - ' + unicode(self.vrratnret) + ' - ' + unicode(self.vrsenarnret) + ' - ' + unicode(self.vrcpcalcpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrratcalcpr) + ' - ' + unicode(self.vrsenardesc) + ' - ' + unicode(self.vrsenarcalc)
    #s5011_basesaquis_custom#
    #s5011_basesaquis_custom#
    class Meta:
        db_table = r's5011_basesaquis'
        managed = True
        ordering = ['s5011_ideestab', 'indaquis', 'vlraquis', 'vrcpdescpr', 'vrcpnret', 'vrratnret', 'vrsenarnret', 'vrcpcalcpr', 'vrratdescpr', 'vrratcalcpr', 'vrsenardesc', 'vrsenarcalc']


class s5011basesAvNPort(models.Model):
    s5011_idelotacao = models.OneToOneField('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbcfgts = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrbccp13) + ' - ' + unicode(self.vrbcfgts) + ' - ' + unicode(self.vrdesccp)
    #s5011_basesavnport_custom#
    #s5011_basesavnport_custom#
    class Meta:
        db_table = r's5011_basesavnport'
        managed = True
        ordering = ['s5011_idelotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp']


class s5011basesComerc(models.Model):
    s5011_ideestab = models.ForeignKey('s5011ideEstab',
        related_name='%(class)s_s5011_ideestab')
    def evento(self): return self.s5011_ideestab.evento()
    indcomerc = models.IntegerField(choices=CHOICES_S5011_INDCOMERC)
    vrbccompr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrratsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.indcomerc) + ' - ' + unicode(self.vrbccompr) + ' - ' + unicode(self.vrcpsusp) + ' - ' + unicode(self.vrratsusp) + ' - ' + unicode(self.vrsenarsusp)
    #s5011_basescomerc_custom#
    #s5011_basescomerc_custom#
    class Meta:
        db_table = r's5011_basescomerc'
        managed = True
        ordering = ['s5011_ideestab', 'indcomerc', 'vrbccompr', 'vrcpsusp', 'vrratsusp', 'vrsenarsusp']


class s5011basesRemun(models.Model):
    s5011_idelotacao = models.ForeignKey('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    indincid = models.IntegerField(choices=CHOICES_S5011_INDINCID)
    codcateg = models.IntegerField()
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsuspbccp00 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsuspbccp15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsuspbccp20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsuspbccp25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescsest = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcalcsest = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescsenat = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcalcsenat = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsalfam = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsalmat = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.indincid) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrsuspbccp00) + ' - ' + unicode(self.vrsuspbccp15) + ' - ' + unicode(self.vrsuspbccp20) + ' - ' + unicode(self.vrsuspbccp25) + ' - ' + unicode(self.vrdescsest) + ' - ' + unicode(self.vrcalcsest) + ' - ' + unicode(self.vrdescsenat) + ' - ' + unicode(self.vrcalcsenat) + ' - ' + unicode(self.vrsalfam) + ' - ' + unicode(self.vrsalmat)
    #s5011_basesremun_custom#
    #s5011_basesremun_custom#
    class Meta:
        db_table = r's5011_basesremun'
        managed = True
        ordering = ['s5011_idelotacao', 'indincid', 'codcateg', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrsuspbccp00', 'vrsuspbccp15', 'vrsuspbccp20', 'vrsuspbccp25', 'vrdescsest', 'vrcalcsest', 'vrdescsenat', 'vrcalcsenat', 'vrsalfam', 'vrsalmat']


class s5011dadosOpPort(models.Model):
    s5011_idelotacao = models.OneToOneField('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    cnpjopportuario = models.CharField(max_length=14)
    aliqrat = models.IntegerField(choices=CHOICES_S5011_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s5011_dadosopport_custom#
    #s5011_dadosopport_custom#
    class Meta:
        db_table = r's5011_dadosopport'
        managed = True
        ordering = ['s5011_idelotacao', 'cnpjopportuario', 'aliqrat', 'fap', 'aliqratajust']


class s5011ideEstab(models.Model):
    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs')
    def evento(self): return self.s5011_evtcs.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S5011_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s5011_ideestab_custom#
    #s5011_ideestab_custom#
    class Meta:
        db_table = r's5011_ideestab'
        managed = True
        ordering = ['s5011_evtcs', 'tpinsc', 'nrinsc']


class s5011ideLotacao(models.Model):
    s5011_ideestab = models.ForeignKey('s5011ideEstab',
        related_name='%(class)s_s5011_ideestab')
    def evento(self): return self.s5011_ideestab.evento()
    codlotacao = models.CharField(max_length=30)
    fpas = models.IntegerField()
    codtercs = models.CharField(max_length=4)
    codtercssusp = models.CharField(max_length=4, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs) + ' - ' + unicode(self.codtercssusp)
    #s5011_idelotacao_custom#
    #s5011_idelotacao_custom#
    class Meta:
        db_table = r's5011_idelotacao'
        managed = True
        ordering = ['s5011_ideestab', 'codlotacao', 'fpas', 'codtercs', 'codtercssusp']


class s5011infoAtConc(models.Model):
    s5011_infopj = models.OneToOneField('s5011infoPJ',
        related_name='%(class)s_s5011_infopj')
    def evento(self): return self.s5011_infopj.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_infopj) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)
    #s5011_infoatconc_custom#
    #s5011_infoatconc_custom#
    class Meta:
        db_table = r's5011_infoatconc'
        managed = True
        ordering = ['s5011_infopj', 'fatormes', 'fator13']


class s5011infoCPSeg(models.Model):
    s5011_evtcs = models.OneToOneField('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs')
    def evento(self): return self.s5011_evtcs.evento()
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpseg = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.vrdesccp) + ' - ' + unicode(self.vrcpseg)
    #s5011_infocpseg_custom#
    #s5011_infocpseg_custom#
    class Meta:
        db_table = r's5011_infocpseg'
        managed = True
        ordering = ['s5011_evtcs', 'vrdesccp', 'vrcpseg']


class s5011infoCRContrib(models.Model):
    s5011_evtcs = models.ForeignKey('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs')
    def evento(self): return self.s5011_evtcs.evento()
    tpcr = models.IntegerField()
    vrcr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcrsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcr) + ' - ' + unicode(self.vrcrsusp)
    #s5011_infocrcontrib_custom#
    #s5011_infocrcontrib_custom#
    class Meta:
        db_table = r's5011_infocrcontrib'
        managed = True
        ordering = ['s5011_evtcs', 'tpcr', 'vrcr', 'vrcrsusp']


class s5011infoCREstab(models.Model):
    s5011_ideestab = models.ForeignKey('s5011ideEstab',
        related_name='%(class)s_s5011_ideestab')
    def evento(self): return self.s5011_ideestab.evento()
    tpcr = models.IntegerField()
    vrcr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsuspcr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcr) + ' - ' + unicode(self.vrsuspcr)
    #s5011_infocrestab_custom#
    #s5011_infocrestab_custom#
    class Meta:
        db_table = r's5011_infocrestab'
        managed = True
        ordering = ['s5011_ideestab', 'tpcr', 'vrcr', 'vrsuspcr']


class s5011infoComplObra(models.Model):
    s5011_infoestab = models.OneToOneField('s5011infoEstab',
        related_name='%(class)s_s5011_infoestab')
    def evento(self): return self.s5011_infoestab.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S5011_INDSUBSTPATROBRA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_infoestab) + ' - ' + unicode(self.indsubstpatrobra)
    #s5011_infocomplobra_custom#
    #s5011_infocomplobra_custom#
    class Meta:
        db_table = r's5011_infocomplobra'
        managed = True
        ordering = ['s5011_infoestab', 'indsubstpatrobra']


class s5011infoEmprParcial(models.Model):
    s5011_idelotacao = models.OneToOneField('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S5011_TPINSCCONTRAT)
    nrinsccontrat = models.CharField(max_length=14)
    tpinscprop = models.IntegerField(choices=CHOICES_S5011_TPINSCPROP)
    nrinscprop = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)
    #s5011_infoemprparcial_custom#
    #s5011_infoemprparcial_custom#
    class Meta:
        db_table = r's5011_infoemprparcial'
        managed = True
        ordering = ['s5011_idelotacao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop']


class s5011infoEstab(models.Model):
    s5011_ideestab = models.OneToOneField('s5011ideEstab',
        related_name='%(class)s_s5011_ideestab')
    def evento(self): return self.s5011_ideestab.evento()
    cnaeprep = models.IntegerField()
    aliqrat = models.IntegerField(choices=CHOICES_S5011_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_ideestab) + ' - ' + unicode(self.cnaeprep) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s5011_infoestab_custom#
    #s5011_infoestab_custom#
    class Meta:
        db_table = r's5011_infoestab'
        managed = True
        ordering = ['s5011_ideestab', 'cnaeprep', 'aliqrat', 'fap', 'aliqratajust']


class s5011infoPJ(models.Model):
    s5011_evtcs = models.OneToOneField('esocial.s5011evtCS',
        related_name='%(class)s_s5011_evtcs')
    def evento(self): return self.s5011_evtcs.evento()
    indcoop = models.IntegerField(choices=CHOICES_S5011_INDCOOP, blank=True, null=True)
    indconstr = models.IntegerField(choices=CHOICES_S5011_INDCONSTR)
    indsubstpatr = models.IntegerField(choices=CHOICES_S5011_INDSUBSTPATR, blank=True, null=True)
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_evtcs) + ' - ' + unicode(self.indcoop) + ' - ' + unicode(self.indconstr) + ' - ' + unicode(self.indsubstpatr) + ' - ' + unicode(self.percredcontrib)
    #s5011_infopj_custom#
    #s5011_infopj_custom#
    class Meta:
        db_table = r's5011_infopj'
        managed = True
        ordering = ['s5011_evtcs', 'indcoop', 'indconstr', 'indsubstpatr', 'percredcontrib']


class s5011infoSubstPatrOpPort(models.Model):
    s5011_idelotacao = models.ForeignKey('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    cnpjopportuario = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.cnpjopportuario)
    #s5011_infosubstpatropport_custom#
    #s5011_infosubstpatropport_custom#
    class Meta:
        db_table = r's5011_infosubstpatropport'
        managed = True
        ordering = ['s5011_idelotacao', 'cnpjopportuario']


class s5011infoTercSusp(models.Model):
    s5011_idelotacao = models.ForeignKey('s5011ideLotacao',
        related_name='%(class)s_s5011_idelotacao')
    def evento(self): return self.s5011_idelotacao.evento()
    codterc = models.CharField(max_length=4)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5011_idelotacao) + ' - ' + unicode(self.codterc)
    #s5011_infotercsusp_custom#
    #s5011_infotercsusp_custom#
    class Meta:
        db_table = r's5011_infotercsusp'
        managed = True
        ordering = ['s5011_idelotacao', 'codterc']


#VIEWS_MODELS
