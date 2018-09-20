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

CHOICES_S1050_ALTERACAO_PERHORFLEXIVEL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1050_ALTERACAO_TPINTERV = (
    (1, u'1 - Intervalo em Horário Fixo'),
    (2, u'2 - Intervalo em Horário Variável'),
)

CHOICES_S1050_INCLUSAO_PERHORFLEXIVEL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1050_INCLUSAO_TPINTERV = (
    (1, u'1 - Intervalo em Horário Fixo'),
    (2, u'2 - Intervalo em Horário Variável'),
)

class s1050alteracao(models.Model):
    s1050_evttabhortur = models.OneToOneField('esocial.s1050evtTabHorTur',
        related_name='%(class)s_s1050_evttabhortur')
    codhorcontrat = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    hrentr = models.CharField(max_length=4)
    hrsaida = models.CharField(max_length=4)
    durjornada = models.IntegerField()
    perhorflexivel = models.CharField(choices=CHOICES_S1050_ALTERACAO_PERHORFLEXIVEL, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1050_evttabhortur) + ' - ' + unicode(self.codhorcontrat) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.hrentr) + ' - ' + unicode(self.hrsaida) + ' - ' + unicode(self.durjornada) + ' - ' + unicode(self.perhorflexivel)
    #s1050_alteracao_custom#
    #s1050_alteracao_custom#
    class Meta:
        db_table = r's1050_alteracao'
        managed = True
        ordering = ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel']


class s1050alteracaohorarioIntervalo(models.Model):
    s1050_alteracao = models.ForeignKey('s1050alteracao',
        related_name='%(class)s_s1050_alteracao')
    tpinterv = models.IntegerField(choices=CHOICES_S1050_ALTERACAO_TPINTERV)
    durinterv = models.IntegerField()
    iniinterv = models.CharField(max_length=4, blank=True, null=True)
    terminterv = models.CharField(max_length=4, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1050_alteracao) + ' - ' + unicode(self.tpinterv) + ' - ' + unicode(self.durinterv) + ' - ' + unicode(self.iniinterv) + ' - ' + unicode(self.terminterv)
    #s1050_alteracao_horariointervalo_custom#
    #s1050_alteracao_horariointervalo_custom#
    class Meta:
        db_table = r's1050_alteracao_horariointervalo'
        managed = True
        ordering = ['s1050_alteracao', 'tpinterv', 'durinterv', 'iniinterv', 'terminterv']


class s1050alteracaonovaValidade(models.Model):
    s1050_alteracao = models.OneToOneField('s1050alteracao',
        related_name='%(class)s_s1050_alteracao')
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
        return unicode(self.s1050_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1050_alteracao_novavalidade_custom#
    #s1050_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1050_alteracao_novavalidade'
        managed = True
        ordering = ['s1050_alteracao', 'inivalid', 'fimvalid']


class s1050exclusao(models.Model):
    s1050_evttabhortur = models.OneToOneField('esocial.s1050evtTabHorTur',
        related_name='%(class)s_s1050_evttabhortur')
    codhorcontrat = models.CharField(max_length=30)
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
        return unicode(self.s1050_evttabhortur) + ' - ' + unicode(self.codhorcontrat) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1050_exclusao_custom#
    #s1050_exclusao_custom#
    class Meta:
        db_table = r's1050_exclusao'
        managed = True
        ordering = ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid']


class s1050inclusao(models.Model):
    s1050_evttabhortur = models.OneToOneField('esocial.s1050evtTabHorTur',
        related_name='%(class)s_s1050_evttabhortur')
    codhorcontrat = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    hrentr = models.CharField(max_length=4)
    hrsaida = models.CharField(max_length=4)
    durjornada = models.IntegerField()
    perhorflexivel = models.CharField(choices=CHOICES_S1050_INCLUSAO_PERHORFLEXIVEL, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1050_evttabhortur) + ' - ' + unicode(self.codhorcontrat) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.hrentr) + ' - ' + unicode(self.hrsaida) + ' - ' + unicode(self.durjornada) + ' - ' + unicode(self.perhorflexivel)
    #s1050_inclusao_custom#
    #s1050_inclusao_custom#
    class Meta:
        db_table = r's1050_inclusao'
        managed = True
        ordering = ['s1050_evttabhortur', 'codhorcontrat', 'inivalid', 'fimvalid', 'hrentr', 'hrsaida', 'durjornada', 'perhorflexivel']


class s1050inclusaohorarioIntervalo(models.Model):
    s1050_inclusao = models.ForeignKey('s1050inclusao',
        related_name='%(class)s_s1050_inclusao')
    tpinterv = models.IntegerField(choices=CHOICES_S1050_INCLUSAO_TPINTERV)
    durinterv = models.IntegerField()
    iniinterv = models.CharField(max_length=4, blank=True, null=True)
    terminterv = models.CharField(max_length=4, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1050_inclusao) + ' - ' + unicode(self.tpinterv) + ' - ' + unicode(self.durinterv) + ' - ' + unicode(self.iniinterv) + ' - ' + unicode(self.terminterv)
    #s1050_inclusao_horariointervalo_custom#
    #s1050_inclusao_horariointervalo_custom#
    class Meta:
        db_table = r's1050_inclusao_horariointervalo'
        managed = True
        ordering = ['s1050_inclusao', 'tpinterv', 'durinterv', 'iniinterv', 'terminterv']


#VIEWS_MODELS
