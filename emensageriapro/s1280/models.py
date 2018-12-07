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



CHOICES_S1280_INDSUBSTPATR = (
    (1, u'1 - Integralmente substituída'),
    (2, u'2 - Parcialmente substituída'),
)

class s1280infoAtivConcom(models.Model):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)
    #s1280_infoativconcom_custom#
    #s1280_infoativconcom_custom#
    class Meta:
        db_table = r's1280_infoativconcom'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'fatormes', 'fator13']



class s1280infoAtivConcomSerializer(ModelSerializer):
    class Meta:
        model = s1280infoAtivConcom
        fields = '__all__'
            

class s1280infoSubstPatr(models.Model):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    indsubstpatr = models.IntegerField(choices=CHOICES_S1280_INDSUBSTPATR)
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.indsubstpatr) + ' - ' + unicode(self.percredcontrib)
    #s1280_infosubstpatr_custom#
    #s1280_infosubstpatr_custom#
    class Meta:
        db_table = r's1280_infosubstpatr'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'indsubstpatr', 'percredcontrib']



class s1280infoSubstPatrSerializer(ModelSerializer):
    class Meta:
        model = s1280infoSubstPatr
        fields = '__all__'
            

class s1280infoSubstPatrOpPort(models.Model):
    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    cnpjopportuario = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.cnpjopportuario)
    #s1280_infosubstpatropport_custom#
    #s1280_infosubstpatropport_custom#
    class Meta:
        db_table = r's1280_infosubstpatropport'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'cnpjopportuario']



class s1280infoSubstPatrOpPortSerializer(ModelSerializer):
    class Meta:
        model = s1280infoSubstPatrOpPort
        fields = '__all__'
            

#VIEWS_MODELS
