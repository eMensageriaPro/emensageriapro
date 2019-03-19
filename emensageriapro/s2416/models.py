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



CHOICES_S2416_MTVSUSPENSAO = (
    ('01', u'01 - Suspensão por não recadastramento'),
    ('99', u'99 - Outros motivos de suspensão'),
)

CHOICES_S2416_TPPENMORTE = (
    (1, u'1 - Vitalícia'),
    (2, u'2 - Temporária'),
)

class s2416homologTC(SoftDeletionModel):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    nratolegal = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.nratolegal)
    #s2416_homologtc_custom#

    class Meta:
        # verbose_name = u'Registro que apresenta as informações de homologação do benefício pelo Tribunal de Contas'
        db_table = r's2416_homologtc'       
        managed = True # s2416_homologtc #
        unique_together = (
            #custom_unique_together_s2416_homologtc#
            
        )
        index_together = (
            #custom_index_together_s2416_homologtc
            #index_together_s2416_homologtc
        )
        permissions = (
            ("can_view_s2416_homologtc", "Can view s2416_homologtc"),
            #custom_permissions_s2416_homologtc
        )
        ordering = ['s2416_evtcdbenalt', 'nratolegal']



class s2416homologTCSerializer(ModelSerializer):
    class Meta:
        model = s2416homologTC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2416infoPenMorte(SoftDeletionModel):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2416_TPPENMORTE)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.tppenmorte)
    #s2416_infopenmorte_custom#

    class Meta:
        # verbose_name = u'Informações relativas a pensão por morte'
        db_table = r's2416_infopenmorte'       
        managed = True # s2416_infopenmorte #
        unique_together = (
            #custom_unique_together_s2416_infopenmorte#
            
        )
        index_together = (
            #custom_index_together_s2416_infopenmorte
            #index_together_s2416_infopenmorte
        )
        permissions = (
            ("can_view_s2416_infopenmorte", "Can view s2416_infopenmorte"),
            #custom_permissions_s2416_infopenmorte
        )
        ordering = ['s2416_evtcdbenalt', 'tppenmorte']



class s2416infoPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2416infoPenMorte
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2416suspensao(SoftDeletionModel):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    mtvsuspensao = models.CharField(choices=CHOICES_S2416_MTVSUSPENSAO, max_length=2)
    dscsuspensao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.mtvsuspensao)
    #s2416_suspensao_custom#

    class Meta:
        # verbose_name = u'Informações referentes à suspensão do benefício'
        db_table = r's2416_suspensao'       
        managed = True # s2416_suspensao #
        unique_together = (
            #custom_unique_together_s2416_suspensao#
            
        )
        index_together = (
            #custom_index_together_s2416_suspensao
            #index_together_s2416_suspensao
        )
        permissions = (
            ("can_view_s2416_suspensao", "Can view s2416_suspensao"),
            #custom_permissions_s2416_suspensao
        )
        ordering = ['s2416_evtcdbenalt', 'mtvsuspensao']



class s2416suspensaoSerializer(ModelSerializer):
    class Meta:
        model = s2416suspensao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
