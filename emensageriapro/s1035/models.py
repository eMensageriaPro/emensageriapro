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



CHOICES_S1035_ALTERACAO_SITCARR = (
    (1, u'1 - Criação'),
    (2, u'2 - Extinção'),
    (3, u'3 - Reestruturação'),
)

CHOICES_S1035_INCLUSAO_SITCARR = (
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

class s1035alteracao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dsccarreira = models.CharField(max_length=100)
    leicarr = models.CharField(max_length=12, blank=True, null=True)
    dtleicarr = models.DateField()
    sitcarr = models.IntegerField(choices=CHOICES_S1035_ALTERACAO_SITCARR)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.dsccarreira) + ' - ' + unicode(self.dtleicarr) + ' - ' + unicode(self.sitcarr)
    #s1035_alteracao_custom#
    class Meta:
        db_table = r's1035_alteracao'
        managed = True # s1035_alteracao #
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid', 'dsccarreira', 'dtleicarr', 'sitcarr']



class s1035alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1035alteracao
        fields = '__all__'
            

class s1035alteracaonovaValidade(models.Model):
    s1035_alteracao = models.OneToOneField('s1035alteracao',
        related_name='%(class)s_s1035_alteracao')
    def evento(self): return self.s1035_alteracao.evento()
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
        return unicode(self.s1035_alteracao) + ' - ' + unicode(self.inivalid)
    #s1035_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1035_alteracao_novavalidade'
        managed = True # s1035_alteracao_novavalidade #
        ordering = ['s1035_alteracao', 'inivalid']



class s1035alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1035alteracaonovaValidade
        fields = '__all__'
            

class s1035exclusao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
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
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid)
    #s1035_exclusao_custom#
    class Meta:
        db_table = r's1035_exclusao'
        managed = True # s1035_exclusao #
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid']



class s1035exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1035exclusao
        fields = '__all__'
            

class s1035inclusao(models.Model):
    s1035_evttabcarreira = models.OneToOneField('esocial.s1035evtTabCarreira',
        related_name='%(class)s_s1035_evttabcarreira')
    def evento(self): return self.s1035_evttabcarreira.evento()
    codcarreira = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dsccarreira = models.CharField(max_length=100)
    leicarr = models.CharField(max_length=12, blank=True, null=True)
    dtleicarr = models.DateField()
    sitcarr = models.IntegerField(choices=CHOICES_S1035_INCLUSAO_SITCARR)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1035_evttabcarreira) + ' - ' + unicode(self.codcarreira) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.dsccarreira) + ' - ' + unicode(self.dtleicarr) + ' - ' + unicode(self.sitcarr)
    #s1035_inclusao_custom#
    class Meta:
        db_table = r's1035_inclusao'
        managed = True # s1035_inclusao #
        ordering = ['s1035_evttabcarreira', 'codcarreira', 'inivalid', 'dsccarreira', 'dtleicarr', 'sitcarr']



class s1035inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1035inclusao
        fields = '__all__'
            

#VIEWS_MODELS
