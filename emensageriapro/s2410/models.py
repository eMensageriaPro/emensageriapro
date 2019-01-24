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



CHOICES_S2410_INTAPOSENTADO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_TPPENMORTE = (
    (1, u'1 - Vitalícia'),
    (2, u'2 - Temporária'),
)

class s2410homologTC(models.Model):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    dthomol = models.DateField()
    nratolegal = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.dthomol) + ' - ' + unicode(self.nratolegal)
    #s2410_homologtc_custom#
    class Meta:
        db_table = r's2410_homologtc'
        managed = True # s2410_homologtc #
        ordering = ['s2410_evtcdbenin', 'dthomol', 'nratolegal']



class s2410homologTCSerializer(ModelSerializer):
    class Meta:
        model = s2410homologTC
        fields = '__all__'
            

class s2410infoPenMorte(models.Model):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2410_TPPENMORTE)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.tppenmorte)
    #s2410_infopenmorte_custom#
    class Meta:
        db_table = r's2410_infopenmorte'
        managed = True # s2410_infopenmorte #
        ordering = ['s2410_evtcdbenin', 'tppenmorte']



class s2410infoPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410infoPenMorte
        fields = '__all__'
            

class s2410instPenMorte(models.Model):
    s2410_infopenmorte = models.OneToOneField('s2410infoPenMorte',
        related_name='%(class)s_s2410_infopenmorte')
    def evento(self): return self.s2410_infopenmorte.evento()
    cpfinst = models.CharField(max_length=11)
    dtinst = models.DateField()
    intaposentado = models.CharField(choices=CHOICES_S2410_INTAPOSENTADO, max_length=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2410_infopenmorte) + ' - ' + unicode(self.cpfinst) + ' - ' + unicode(self.dtinst) + ' - ' + unicode(self.intaposentado)
    #s2410_instpenmorte_custom#
    class Meta:
        db_table = r's2410_instpenmorte'
        managed = True # s2410_instpenmorte #
        ordering = ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado']



class s2410instPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410instPenMorte
        fields = '__all__'
            

#VIEWS_MODELS
