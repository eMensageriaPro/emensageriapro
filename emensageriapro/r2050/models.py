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
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from django.apps import apps
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_R2050_INDCOM = (
    (1, u'1 - Comercialização da Produção por Prod. Rural PJ/Agroindústria, exceto para entidades executoras do PAA'),
    (8, u'8 - Comercialização da Produção para Entidade do Programa de Aquisição de Alimentos - PAA'),
    (9, u'9 - Comercialização direta da Produção no Mercado Externo'),
)

CHOICES_R2050_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2050infoProc(SoftDeletionModel):
    r2050_tipocom = models.ForeignKey('r2050tipoCom',
        related_name='%(class)s_r2050_tipocom')
    def evento(self): return self.r2050_tipocom.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2050_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrratsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r2050_tipocom) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc)
    #r2050_infoproc_custom#
    class Meta:
        db_table = r'r2050_infoproc'
        managed = True # r2050_infoproc #
        ordering = ['r2050_tipocom', 'tpproc', 'nrproc']



class r2050infoProcSerializer(ModelSerializer):
    class Meta:
        model = r2050infoProc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class r2050tipoCom(SoftDeletionModel):
    r2050_evtcomprod = models.ForeignKey('efdreinf.r2050evtComProd',
        related_name='%(class)s_r2050_evtcomprod')
    def evento(self): return self.r2050_evtcomprod.evento()
    indcom = models.IntegerField(choices=CHOICES_R2050_INDCOM)
    vlrrecbruta = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r2050_evtcomprod) + ' - ' + unicode(self.indcom) + ' - ' + unicode(self.vlrrecbruta)
    #r2050_tipocom_custom#
    class Meta:
        db_table = r'r2050_tipocom'
        managed = True # r2050_tipocom #
        ordering = ['r2050_evtcomprod', 'indcom', 'vlrrecbruta']



class r2050tipoComSerializer(ModelSerializer):
    class Meta:
        model = r2050tipoCom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

#VIEWS_MODELS
