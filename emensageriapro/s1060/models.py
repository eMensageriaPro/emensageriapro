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
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S1060_ALTERACAO_LOCALAMB = (
    (1, u'1 - Estabelecimento do próprio empregador'),
    (2, u'2 - Estabelecimento de terceiros'),
    (3, u'3 - Prestação de serviços em instalações de terceiros não consideradas como lotações dos tipos 03 a 09 da Tabela 10'),
)

CHOICES_S1060_ALTERACAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1060_INCLUSAO_LOCALAMB = (
    (1, u'1 - Estabelecimento do próprio empregador'),
    (2, u'2 - Estabelecimento de terceiros'),
    (3, u'3 - Prestação de serviços em instalações de terceiros não consideradas como lotações dos tipos 03 a 09 da Tabela 10'),
)

CHOICES_S1060_INCLUSAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
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

class s1060alteracao(models.Model):
    s1060_evttabambiente = models.OneToOneField('esocial.s1060evtTabAmbiente',
        related_name='%(class)s_s1060_evttabambiente')
    def evento(self): return self.s1060_evttabambiente.evento()
    codamb = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmamb = models.CharField(max_length=100)
    dscamb = models.CharField(max_length=8000)
    localamb = models.IntegerField(choices=CHOICES_S1060_ALTERACAO_LOCALAMB)
    tpinsc = models.IntegerField(choices=CHOICES_S1060_ALTERACAO_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
    codlotacao = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1060_evttabambiente) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmamb) + ' - ' + unicode(self.dscamb) + ' - ' + unicode(self.localamb)
    #s1060_alteracao_custom#
    #s1060_alteracao_custom#
    class Meta:
        db_table = r's1060_alteracao'
        managed = True
        ordering = ['s1060_evttabambiente', 'codamb', 'inivalid', 'nmamb', 'dscamb', 'localamb']



class s1060alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1060alteracao
        fields = '__all__'
            

class s1060alteracaonovaValidade(models.Model):
    s1060_alteracao = models.OneToOneField('s1060alteracao',
        related_name='%(class)s_s1060_alteracao')
    def evento(self): return self.s1060_alteracao.evento()
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
        return unicode(self.s1060_alteracao) + ' - ' + unicode(self.inivalid)
    #s1060_alteracao_novavalidade_custom#
    #s1060_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1060_alteracao_novavalidade'
        managed = True
        ordering = ['s1060_alteracao', 'inivalid']



class s1060alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1060alteracaonovaValidade
        fields = '__all__'
            

class s1060exclusao(models.Model):
    s1060_evttabambiente = models.OneToOneField('esocial.s1060evtTabAmbiente',
        related_name='%(class)s_s1060_evttabambiente')
    def evento(self): return self.s1060_evttabambiente.evento()
    codamb = models.CharField(max_length=30)
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
        return unicode(self.s1060_evttabambiente) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.inivalid)
    #s1060_exclusao_custom#
    #s1060_exclusao_custom#
    class Meta:
        db_table = r's1060_exclusao'
        managed = True
        ordering = ['s1060_evttabambiente', 'codamb', 'inivalid']



class s1060exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1060exclusao
        fields = '__all__'
            

class s1060inclusao(models.Model):
    s1060_evttabambiente = models.OneToOneField('esocial.s1060evtTabAmbiente',
        related_name='%(class)s_s1060_evttabambiente')
    def evento(self): return self.s1060_evttabambiente.evento()
    codamb = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmamb = models.CharField(max_length=100)
    dscamb = models.CharField(max_length=8000)
    localamb = models.IntegerField(choices=CHOICES_S1060_INCLUSAO_LOCALAMB)
    tpinsc = models.IntegerField(choices=CHOICES_S1060_INCLUSAO_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
    codlotacao = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1060_evttabambiente) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmamb) + ' - ' + unicode(self.dscamb) + ' - ' + unicode(self.localamb)
    #s1060_inclusao_custom#
    #s1060_inclusao_custom#
    class Meta:
        db_table = r's1060_inclusao'
        managed = True
        ordering = ['s1060_evttabambiente', 'codamb', 'inivalid', 'nmamb', 'dscamb', 'localamb']



class s1060inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1060inclusao
        fields = '__all__'
            

#VIEWS_MODELS
