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



CHOICES_S1080_ALTERACAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
)

CHOICES_S1080_INCLUSAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
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

class s1080alteracao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    aliqrat = models.IntegerField(choices=CHOICES_S1080_ALTERACAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s1080_alteracao_custom#
    class Meta:
        db_table = r's1080_alteracao'
        managed = True # s1080_alteracao #
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'aliqrat', 'fap', 'aliqratajust']



class s1080alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1080alteracao
        fields = '__all__'
            

class s1080alteracaonovaValidade(models.Model):
    s1080_alteracao = models.OneToOneField('s1080alteracao',
        related_name='%(class)s_s1080_alteracao')
    def evento(self): return self.s1080_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1080_alteracao) + ' - ' + unicode(self.inivalid)
    #s1080_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1080_alteracao_novavalidade'
        managed = True # s1080_alteracao_novavalidade #
        ordering = ['s1080_alteracao', 'inivalid']



class s1080alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1080alteracaonovaValidade
        fields = '__all__'
            

class s1080exclusao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid)
    #s1080_exclusao_custom#
    class Meta:
        db_table = r's1080_exclusao'
        managed = True # s1080_exclusao #
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid']



class s1080exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1080exclusao
        fields = '__all__'
            

class s1080inclusao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    aliqrat = models.IntegerField(choices=CHOICES_S1080_INCLUSAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s1080_inclusao_custom#
    class Meta:
        db_table = r's1080_inclusao'
        managed = True # s1080_inclusao #
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'aliqrat', 'fap', 'aliqratajust']



class s1080inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1080inclusao
        fields = '__all__'
            

#VIEWS_MODELS
