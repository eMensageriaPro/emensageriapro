#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



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
    ('2019-01', u'Janeiro/2019'),
    ('2019-02', u'Fevereiro/2019'),
    ('2019-03', u'Março/2019'),
    ('2019-04', u'Abril/2019'),
    ('2019-05', u'Maio/2019'),
    ('2019-06', u'Junho/2019'),
    ('2019-07', u'Julho/2019'),
    ('2019-08', u'Agosto/2019'),
    ('2019-09', u'Setembro/2019'),
    ('2019-10', u'Outubro/2019'),
    ('2019-11', u'Novembro/2019'),
    ('2019-12', u'Dezembro/2019'),
)

class s1020alteracao(SoftDeletionModel):
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
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs)
    #s1020_alteracao_custom#

    class Meta:
        db_table = r's1020_alteracao'       
        managed = True # s1020_alteracao #
        permissions = (
            ("can_view_s1020_alteracao", "Can view s1020_alteracao"),
            #custom_permissions_s1020_alteracao
        )
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'tplotacao', 'fpas', 'codtercs']



class s1020alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1020alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020alteracaoinfoEmprParcial(SoftDeletionModel):
    s1020_alteracao = models.OneToOneField('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_ALTERACAO_TPINSCCONTRAT)
    nrinsccontrat = models.CharField(max_length=14)
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_ALTERACAO_TPINSCPROP)
    nrinscprop = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)
    #s1020_alteracao_infoemprparcial_custom#

    class Meta:
        db_table = r's1020_alteracao_infoemprparcial'       
        managed = True # s1020_alteracao_infoemprparcial #
        permissions = (
            ("can_view_s1020_alteracao_infoemprparcial", "Can view s1020_alteracao_infoemprparcial"),
            #custom_permissions_s1020_alteracao_infoemprparcial
        )
        ordering = ['s1020_alteracao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop']



class s1020alteracaoinfoEmprParcialSerializer(ModelSerializer):
    class Meta:
        model = s1020alteracaoinfoEmprParcial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020alteracaonovaValidade(SoftDeletionModel):
    s1020_alteracao = models.OneToOneField('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.inivalid)
    #s1020_alteracao_novavalidade_custom#

    class Meta:
        db_table = r's1020_alteracao_novavalidade'       
        managed = True # s1020_alteracao_novavalidade #
        permissions = (
            ("can_view_s1020_alteracao_novavalidade", "Can view s1020_alteracao_novavalidade"),
            #custom_permissions_s1020_alteracao_novavalidade
        )
        ordering = ['s1020_alteracao', 'inivalid']



class s1020alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1020alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020alteracaoprocJudTerceiro(SoftDeletionModel):
    s1020_alteracao = models.ForeignKey('s1020alteracao',
        related_name='%(class)s_s1020_alteracao')
    def evento(self): return self.s1020_alteracao.evento()
    codterc = models.CharField(max_length=4)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_alteracao) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1020_alteracao_procjudterceiro_custom#

    class Meta:
        db_table = r's1020_alteracao_procjudterceiro'       
        managed = True # s1020_alteracao_procjudterceiro #
        permissions = (
            ("can_view_s1020_alteracao_procjudterceiro", "Can view s1020_alteracao_procjudterceiro"),
            #custom_permissions_s1020_alteracao_procjudterceiro
        )
        ordering = ['s1020_alteracao', 'codterc', 'nrprocjud', 'codsusp']



class s1020alteracaoprocJudTerceiroSerializer(ModelSerializer):
    class Meta:
        model = s1020alteracaoprocJudTerceiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020exclusao(SoftDeletionModel):
    s1020_evttablotacao = models.OneToOneField('esocial.s1020evtTabLotacao',
        related_name='%(class)s_s1020_evttablotacao')
    def evento(self): return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid)
    #s1020_exclusao_custom#

    class Meta:
        db_table = r's1020_exclusao'       
        managed = True # s1020_exclusao #
        permissions = (
            ("can_view_s1020_exclusao", "Can view s1020_exclusao"),
            #custom_permissions_s1020_exclusao
        )
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid']



class s1020exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1020exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020inclusao(SoftDeletionModel):
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
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_evttablotacao) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.tplotacao) + ' - ' + unicode(self.fpas) + ' - ' + unicode(self.codtercs)
    #s1020_inclusao_custom#

    class Meta:
        db_table = r's1020_inclusao'       
        managed = True # s1020_inclusao #
        permissions = (
            ("can_view_s1020_inclusao", "Can view s1020_inclusao"),
            #custom_permissions_s1020_inclusao
        )
        ordering = ['s1020_evttablotacao', 'codlotacao', 'inivalid', 'tplotacao', 'fpas', 'codtercs']



class s1020inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1020inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020inclusaoinfoEmprParcial(SoftDeletionModel):
    s1020_inclusao = models.OneToOneField('s1020inclusao',
        related_name='%(class)s_s1020_inclusao')
    def evento(self): return self.s1020_inclusao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_INCLUSAO_TPINSCCONTRAT)
    nrinsccontrat = models.CharField(max_length=14)
    tpinscprop = models.IntegerField(choices=CHOICES_S1020_INCLUSAO_TPINSCPROP)
    nrinscprop = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_inclusao) + ' - ' + unicode(self.tpinsccontrat) + ' - ' + unicode(self.nrinsccontrat) + ' - ' + unicode(self.tpinscprop) + ' - ' + unicode(self.nrinscprop)
    #s1020_inclusao_infoemprparcial_custom#

    class Meta:
        db_table = r's1020_inclusao_infoemprparcial'       
        managed = True # s1020_inclusao_infoemprparcial #
        permissions = (
            ("can_view_s1020_inclusao_infoemprparcial", "Can view s1020_inclusao_infoemprparcial"),
            #custom_permissions_s1020_inclusao_infoemprparcial
        )
        ordering = ['s1020_inclusao', 'tpinsccontrat', 'nrinsccontrat', 'tpinscprop', 'nrinscprop']



class s1020inclusaoinfoEmprParcialSerializer(ModelSerializer):
    class Meta:
        model = s1020inclusaoinfoEmprParcial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1020inclusaoprocJudTerceiro(SoftDeletionModel):
    s1020_inclusao = models.ForeignKey('s1020inclusao',
        related_name='%(class)s_s1020_inclusao')
    def evento(self): return self.s1020_inclusao.evento()
    codterc = models.CharField(max_length=4)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1020_inclusao) + ' - ' + unicode(self.codterc) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1020_inclusao_procjudterceiro_custom#

    class Meta:
        db_table = r's1020_inclusao_procjudterceiro'       
        managed = True # s1020_inclusao_procjudterceiro #
        permissions = (
            ("can_view_s1020_inclusao_procjudterceiro", "Can view s1020_inclusao_procjudterceiro"),
            #custom_permissions_s1020_inclusao_procjudterceiro
        )
        ordering = ['s1020_inclusao', 'codterc', 'nrprocjud', 'codsusp']



class s1020inclusaoprocJudTerceiroSerializer(ModelSerializer):
    class Meta:
        model = s1020inclusaoprocJudTerceiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
