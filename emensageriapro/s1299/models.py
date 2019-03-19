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



class s1299ideRespInf(SoftDeletionModel):
    s1299_evtfechaevper = models.OneToOneField('esocial.s1299evtFechaEvPer',
        related_name='%(class)s_s1299_evtfechaevper')
    def evento(self): return self.s1299_evtfechaevper.evento()
    nmresp = models.CharField(max_length=70)
    cpfresp = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1299_evtfechaevper) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.telefone)
    #s1299_iderespinf_custom#

    class Meta:
        # verbose_name = u'Responsável pelas informações'
        db_table = r's1299_iderespinf'       
        managed = True # s1299_iderespinf #
        unique_together = (
            #custom_unique_together_s1299_iderespinf#
            
        )
        index_together = (
            #custom_index_together_s1299_iderespinf
            #index_together_s1299_iderespinf
        )
        permissions = (
            ("can_view_s1299_iderespinf", "Can view s1299_iderespinf"),
            #custom_permissions_s1299_iderespinf
        )
        ordering = ['s1299_evtfechaevper', 'nmresp', 'cpfresp', 'telefone']



class s1299ideRespInfSerializer(ModelSerializer):
    class Meta:
        model = s1299ideRespInf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
