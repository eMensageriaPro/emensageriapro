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



CHOICES_S1030_ALTERACAO_ACUMCARGO = (
    (1, u'1 - Não acumulável'),
    (2, u'2 - Profissional de Saúde'),
    (3, u'3 - Professor'),
    (4, u'4 - Técnico/Científico'),
)

CHOICES_S1030_ALTERACAO_CONTAGEMESP = (
    (1, u'1 - Não'),
    (2, u'2 - Professor (Infantil, Fundamental e Médio)'),
    (3, u'3 - Professor de Ensino Superior, Magistrado, Membro de Ministério Público, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'),
    (4, u'4 - Atividade de risco'),
)

CHOICES_S1030_ALTERACAO_DEDICEXCL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1030_ALTERACAO_SITCARGO = (
    (1, u'1 - Criação'),
    (2, u'2 - Extinção'),
    (3, u'3 - Reestruturação'),
)

CHOICES_S1030_INCLUSAO_ACUMCARGO = (
    (1, u'1 - Não acumulável'),
    (2, u'2 - Profissional de Saúde'),
    (3, u'3 - Professor'),
    (4, u'4 - Técnico/Científico'),
)

CHOICES_S1030_INCLUSAO_CONTAGEMESP = (
    (1, u'1 - Não'),
    (2, u'2 - Professor (Infantil, Fundamental e Médio)'),
    (3, u'3 - Professor de Ensino Superior, Magistrado, Membro de Ministério Público, Membro do Tribunal de Contas (com ingresso anterior a 16/12/1998 EC nr. 20/98)'),
    (4, u'4 - Atividade de risco'),
)

CHOICES_S1030_INCLUSAO_DEDICEXCL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1030_INCLUSAO_SITCARGO = (
    (1, u'1 - Criação'),
    (2, u'2 - Extinção'),
    (3, u'3 - Reestruturação'),
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

class s1030alteracao(models.Model):
    s1030_evttabcargo = models.OneToOneField('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo')
    def evento(self): return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmcargo = models.CharField(max_length=100)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1030_evttabcargo) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmcargo) + ' - ' + unicode(self.codcbo)
    #s1030_alteracao_custom#
    #s1030_alteracao_custom#
    class Meta:
        db_table = r's1030_alteracao'
        managed = True
        ordering = ['s1030_evttabcargo', 'codcargo', 'inivalid', 'nmcargo', 'codcbo']



class s1030alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1030alteracao
        fields = '__all__'
            

class s1030alteracaocargoPublico(models.Model):
    s1030_alteracao = models.OneToOneField('s1030alteracao',
        related_name='%(class)s_s1030_alteracao')
    def evento(self): return self.s1030_alteracao.evento()
    acumcargo = models.IntegerField(choices=CHOICES_S1030_ALTERACAO_ACUMCARGO)
    contagemesp = models.IntegerField(choices=CHOICES_S1030_ALTERACAO_CONTAGEMESP)
    dedicexcl = models.CharField(choices=CHOICES_S1030_ALTERACAO_DEDICEXCL, max_length=1)
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    nrlei = models.CharField(max_length=12)
    dtlei = models.DateField()
    sitcargo = models.IntegerField(choices=CHOICES_S1030_ALTERACAO_SITCARGO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1030_alteracao) + ' - ' + unicode(self.acumcargo) + ' - ' + unicode(self.contagemesp) + ' - ' + unicode(self.dedicexcl) + ' - ' + unicode(self.nrlei) + ' - ' + unicode(self.dtlei) + ' - ' + unicode(self.sitcargo)
    #s1030_alteracao_cargopublico_custom#
    #s1030_alteracao_cargopublico_custom#
    class Meta:
        db_table = r's1030_alteracao_cargopublico'
        managed = True
        ordering = ['s1030_alteracao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo']



class s1030alteracaocargoPublicoSerializer(ModelSerializer):
    class Meta:
        model = s1030alteracaocargoPublico
        fields = '__all__'
            

class s1030alteracaonovaValidade(models.Model):
    s1030_alteracao = models.OneToOneField('s1030alteracao',
        related_name='%(class)s_s1030_alteracao')
    def evento(self): return self.s1030_alteracao.evento()
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
        return unicode(self.s1030_alteracao) + ' - ' + unicode(self.inivalid)
    #s1030_alteracao_novavalidade_custom#
    #s1030_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1030_alteracao_novavalidade'
        managed = True
        ordering = ['s1030_alteracao', 'inivalid']



class s1030alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1030alteracaonovaValidade
        fields = '__all__'
            

class s1030exclusao(models.Model):
    s1030_evttabcargo = models.OneToOneField('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo')
    def evento(self): return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30)
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
        return unicode(self.s1030_evttabcargo) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.inivalid)
    #s1030_exclusao_custom#
    #s1030_exclusao_custom#
    class Meta:
        db_table = r's1030_exclusao'
        managed = True
        ordering = ['s1030_evttabcargo', 'codcargo', 'inivalid']



class s1030exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1030exclusao
        fields = '__all__'
            

class s1030inclusao(models.Model):
    s1030_evttabcargo = models.OneToOneField('esocial.s1030evtTabCargo',
        related_name='%(class)s_s1030_evttabcargo')
    def evento(self): return self.s1030_evttabcargo.evento()
    codcargo = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmcargo = models.CharField(max_length=100)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1030_evttabcargo) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmcargo) + ' - ' + unicode(self.codcbo)
    #s1030_inclusao_custom#
    #s1030_inclusao_custom#
    class Meta:
        db_table = r's1030_inclusao'
        managed = True
        ordering = ['s1030_evttabcargo', 'codcargo', 'inivalid', 'nmcargo', 'codcbo']



class s1030inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1030inclusao
        fields = '__all__'
            

class s1030inclusaocargoPublico(models.Model):
    s1030_inclusao = models.OneToOneField('s1030inclusao',
        related_name='%(class)s_s1030_inclusao')
    def evento(self): return self.s1030_inclusao.evento()
    acumcargo = models.IntegerField(choices=CHOICES_S1030_INCLUSAO_ACUMCARGO)
    contagemesp = models.IntegerField(choices=CHOICES_S1030_INCLUSAO_CONTAGEMESP)
    dedicexcl = models.CharField(choices=CHOICES_S1030_INCLUSAO_DEDICEXCL, max_length=1)
    codcarreira = models.CharField(max_length=30, blank=True, null=True)
    nrlei = models.CharField(max_length=12)
    dtlei = models.DateField()
    sitcargo = models.IntegerField(choices=CHOICES_S1030_INCLUSAO_SITCARGO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1030_inclusao) + ' - ' + unicode(self.acumcargo) + ' - ' + unicode(self.contagemesp) + ' - ' + unicode(self.dedicexcl) + ' - ' + unicode(self.nrlei) + ' - ' + unicode(self.dtlei) + ' - ' + unicode(self.sitcargo)
    #s1030_inclusao_cargopublico_custom#
    #s1030_inclusao_cargopublico_custom#
    class Meta:
        db_table = r's1030_inclusao_cargopublico'
        managed = True
        ordering = ['s1030_inclusao', 'acumcargo', 'contagemesp', 'dedicexcl', 'nrlei', 'dtlei', 'sitcargo']



class s1030inclusaocargoPublicoSerializer(ModelSerializer):
    class Meta:
        model = s1030inclusaocargoPublico
        fields = '__all__'
            

#VIEWS_MODELS
