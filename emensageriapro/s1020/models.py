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



CHOICES_S1020_ALTERACAO_TPLOTACAO = (
    ('01', u'01 - Classificação da atividade econômica exercida pela Pessoa Jurídica para fins de atribuição de código FPAS, inclusive obras de construção civil própria, exceto: a) empreitada parcial ou sub-empreitada de obra de construção civil (utilizar opção 02); b) (...)'),
    ('02', u'02 - Obra de Construção Civil - Empreitada Parcial ou Sub- empreitada'),
    ('03', u'03 - Pessoa Física Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa'),
    ('04', u'04 - Pessoa Jurídica Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'),
    ('05', u'05 - Pessoa Jurídica Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'),
    ('06', u'06 - Entidade beneficente/isenta Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho'),
    ('07', u'07 - Pessoa Física tomadora de Serviços prestados por Cooperados por intermédio de Cooperativa de Trabalho'),
    ('08', u'08 - Operador Portuário tomador de serviços de trabalhadores avulsos'),
    ('09', u'09 - Contratante de trabalhadores avulsos não portuários por intermédio de Sindicato'),
    ('10', u'10 - Embarcação inscrita no Registro Especial Brasileiro - REB'),
    ('21', u'21 - Classificação da atividade econômica ou obra própria de construção civil da Pessoa Física'),
    ('24', u'24 - Empregador Doméstico'),
    ('90', u'90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previdência Social (expatriados)'),
    ('91', u'91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previdência Social Estrangeiro'),
)

CHOICES_S1020_INCLUSAO_TPLOTACAO = (
    ('01', u'01 - Classificação da atividade econômica exercida pela Pessoa Jurídica para fins de atribuição de código FPAS, inclusive obras de construção civil própria, exceto: a) empreitada parcial ou sub-empreitada de obra de construção civil (utilizar opção 02); b) (...)'),
    ('02', u'02 - Obra de Construção Civil - Empreitada Parcial ou Sub- empreitada'),
    ('03', u'03 - Pessoa Física Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa'),
    ('04', u'04 - Pessoa Jurídica Tomadora de Serviços prestados mediante cessão de mão de obra, exceto contratante de cooperativa, nos termos da lei 8.212/1991'),
    ('05', u'05 - Pessoa Jurídica Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho, exceto aqueles prestados a entidade beneficente/isenta'),
    ('06', u'06 - Entidade beneficente/isenta Tomadora de Serviços prestados por cooperados por intermédio de cooperativa de trabalho'),
    ('07', u'07 - Pessoa Física tomadora de Serviços prestados por Cooperados por intermédio de Cooperativa de Trabalho'),
    ('08', u'08 - Operador Portuário tomador de serviços de trabalhadores avulsos'),
    ('09', u'09 - Contratante de trabalhadores avulsos não portuários por intermédio de Sindicato'),
    ('10', u'10 - Embarcação inscrita no Registro Especial Brasileiro - REB'),
    ('21', u'21 - Classificação da atividade econômica ou obra própria de construção civil da Pessoa Física'),
    ('24', u'24 - Empregador Doméstico'),
    ('90', u'90 - Atividades desenvolvidas no exterior por trabalhador vinculado ao Regime Geral de Previdência Social (expatriados)'),
    ('91', u'91 - Atividades desenvolvidas por trabalhador estrangeiro vinculado a Regime de Previdência Social Estrangeiro'),
)

PERIODOS = (
    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
)

CHOICES_S1020_ALTERACAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_ALTERACAO_TPINSCCONTRAT = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_ALTERACAO_TPINSCPROP = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_INCLUSAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_INCLUSAO_TPINSCCONTRAT = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1020_INCLUSAO_TPINSCPROP = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class s1020alteracao(models.Model):
    s1020_evttablotacao = models.OneToOneField('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao')
    def evento(self): return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    tplotacao = models.CharField(choices=CHOICES_S1020_ALTERACAO_TPLOTACAO, max_length=2)
    tpinsc = models.IntegerField(choices=CHOICES_S1020_ALTERACAO_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
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
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs) + ' - ' + unicode(self.codtercssusp)
    #s1020_alteracao_custom#
    #s1020_alteracao_custom#
    class Meta:
        db_table = r's1020_alteracao'
        managed = True
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid', 'tplotacao', 'tpinsc', 'nrinsc', 'fpas', 'codtercs', 'codtercssusp']


class s1020alteracaoinfoEmprParcial(models.Model):
    s1020_alteracao = models.OneToOneField('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_ALTERACAO_TPINSCCONTRAT)
    nrinsccontrat = models.CharField(max_length=14)
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_ALTERACAO_TPINSCPROP)
    nrinscprop = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)
    #s1020_alteracao_infoemprparcial_custom#
    #s1020_alteracao_infoemprparcial_custom#
    class Meta:
        db_table = r's1020_alteracao_infoemprparcial'
        managed = True
        ordering = ['s1020_alteracao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop']


class s1020alteracaoinfoProcJudTerceiros(models.Model):
    s1020_alteracao = models.OneToOneField('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_alteracao)
    #s1020_alteracao_infoprocjudterceiros_custom#
    #s1020_alteracao_infoprocjudterceiros_custom#
    class Meta:
        db_table = r's1020_alteracao_infoprocjudterceiros'
        managed = True
        ordering = ['s1020_alteracao']


class s1020alteracaonovaValidade(models.Model):
    s1020_alteracao = models.OneToOneField('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1020_alteracao_novavalidade_custom#
    #s1020_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1020_alteracao_novavalidade'
        managed = True
        ordering = ['s1020_alteracao', 'inivalid', 'fimvalid']


class s1020alteracaoprocJudTerceiro(models.Model):
    s1020_alteracao_infoprocjudterceiros = models.ForeignKey('s1020alteracaoinfoProcJudTerceiros',
        related_name='%(class)s_s1020_alteracao_infoprocjudterceiros')
    def evento(self): return self.s1020_alteracao_infoprocjudterceiros.evento()
    codterc = models.CharField(max_length=4)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_alteracao_infoprocjudterceiros) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1020_alteracao_procjudterceiro_custom#
    #s1020_alteracao_procjudterceiro_custom#
    class Meta:
        db_table = r's1020_alteracao_procjudterceiro'
        managed = True
        ordering = ['s1020_alteracao_infoprocjudterceiros', 'codterc', 'nrprocjud', 'codsusp']


class s1020exclusao(models.Model):
    s1020_evttablotacao = models.OneToOneField('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao')
    def evento(self): return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1020_exclusao_custom#
    #s1020_exclusao_custom#
    class Meta:
        db_table = r's1020_exclusao'
        managed = True
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid']


class s1020inclusao(models.Model):
    s1020_evttablotacao = models.OneToOneField('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao')
    def evento(self): return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    tplotacao = models.CharField(choices=CHOICES_S1020_INCLUSAO_TPLOTACAO, max_length=2)
    tpinsc = models.IntegerField(choices=CHOICES_S1020_INCLUSAO_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
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
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs) + ' - ' + unicode(self.codtercssusp)
    #s1020_inclusao_custom#
    #s1020_inclusao_custom#
    class Meta:
        db_table = r's1020_inclusao'
        managed = True
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'fimvalid', 'tplotacao', 'tpinsc', 'nrinsc', 'fpas', 'codtercs', 'codtercssusp']


class s1020inclusaoinfoEmprParcial(models.Model):
    s1020_inclusao = models.OneToOneField('s1020inclusao',
        related_name='%(class)s_s1020_inclusao')
    def evento(self): return self.s1020_inclusao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_INCLUSAO_TPINSCCONTRAT)
    nrinsccontrat = models.CharField(max_length=14)
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_INCLUSAO_TPINSCPROP)
    nrinscprop = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_inclusao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)
    #s1020_inclusao_infoemprparcial_custom#
    #s1020_inclusao_infoemprparcial_custom#
    class Meta:
        db_table = r's1020_inclusao_infoemprparcial'
        managed = True
        ordering = ['s1020_inclusao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop']


class s1020inclusaoinfoProcJudTerceiros(models.Model):
    s1020_inclusao = models.OneToOneField('s1020inclusao',
        related_name='%(class)s_s1020_inclusao')
    def evento(self): return self.s1020_inclusao.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_inclusao)
    #s1020_inclusao_infoprocjudterceiros_custom#
    #s1020_inclusao_infoprocjudterceiros_custom#
    class Meta:
        db_table = r's1020_inclusao_infoprocjudterceiros'
        managed = True
        ordering = ['s1020_inclusao']


class s1020inclusaoprocJudTerceiro(models.Model):
    s1020_inclusao_infoprocjudterceiros = models.ForeignKey('s1020inclusaoinfoProcJudTerceiros',
        related_name='%(class)s_s1020_inclusao_infoprocjudterceiros')
    def evento(self): return self.s1020_inclusao_infoprocjudterceiros.evento()
    codterc = models.CharField(max_length=4)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1020_inclusao_infoprocjudterceiros) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1020_inclusao_procjudterceiro_custom#
    #s1020_inclusao_procjudterceiro_custom#
    class Meta:
        db_table = r's1020_inclusao_procjudterceiro'
        managed = True
        ordering = ['s1020_inclusao_infoprocjudterceiros', 'codterc', 'nrprocjud', 'codsusp']


#VIEWS_MODELS
