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



CHOICES_S2410_INTAPOSENTADO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_TPPENMORTE = (
    (1, u'1 - Vitalícia'),
    (2, u'2 - Temporária'),
)

class s2410homologTC(SoftDeletionModel):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    dthomol = models.DateField()
    nratolegal = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.dthomol) + ' - ' + unicode(self.nratolegal)
    #s2410_homologtc_custom#

    class Meta:
        # verbose_name = u'Registro que apresenta as informações de homologação do benefício pelo Tribunal de Contas'
        db_table = r's2410_homologtc'       
        managed = True # s2410_homologtc #
        unique_together = (
            #custom_unique_together_s2410_homologtc#
            
        )
        index_together = (
            #custom_index_together_s2410_homologtc
            #index_together_s2410_homologtc
        )
        permissions = (
            ("can_view_s2410_homologtc", "Can view s2410_homologtc"),
            #custom_permissions_s2410_homologtc
        )
        ordering = ['s2410_evtcdbenin', 'dthomol', 'nratolegal']



class s2410homologTCSerializer(ModelSerializer):
    class Meta:
        model = s2410homologTC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2410infoPenMorte(SoftDeletionModel):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2410_TPPENMORTE)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.tppenmorte)
    #s2410_infopenmorte_custom#

    class Meta:
        # verbose_name = u'Informações relativas a pensão por morte'
        db_table = r's2410_infopenmorte'       
        managed = True # s2410_infopenmorte #
        unique_together = (
            #custom_unique_together_s2410_infopenmorte#
            
        )
        index_together = (
            #custom_index_together_s2410_infopenmorte
            #index_together_s2410_infopenmorte
        )
        permissions = (
            ("can_view_s2410_infopenmorte", "Can view s2410_infopenmorte"),
            #custom_permissions_s2410_infopenmorte
        )
        ordering = ['s2410_evtcdbenin', 'tppenmorte']



class s2410infoPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410infoPenMorte
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2410instPenMorte(SoftDeletionModel):
    s2410_infopenmorte = models.OneToOneField('s2410infoPenMorte',
        related_name='%(class)s_s2410_infopenmorte')
    def evento(self): return self.s2410_infopenmorte.evento()
    cpfinst = models.CharField(max_length=11)
    dtinst = models.DateField()
    intaposentado = models.CharField(choices=CHOICES_S2410_INTAPOSENTADO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_infopenmorte) + ' - ' + unicode(self.cpfinst) + ' - ' + unicode(self.dtinst) + ' - ' + unicode(self.intaposentado)
    #s2410_instpenmorte_custom#

    class Meta:
        # verbose_name = u'Informações do instituidor da pensão por morte'
        db_table = r's2410_instpenmorte'       
        managed = True # s2410_instpenmorte #
        unique_together = (
            #custom_unique_together_s2410_instpenmorte#
            
        )
        index_together = (
            #custom_index_together_s2410_instpenmorte
            #index_together_s2410_instpenmorte
        )
        permissions = (
            ("can_view_s2410_instpenmorte", "Can view s2410_instpenmorte"),
            #custom_permissions_s2410_instpenmorte
        )
        ordering = ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado']



class s2410instPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410instPenMorte
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
