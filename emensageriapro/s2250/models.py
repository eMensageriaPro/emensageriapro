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
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S2250_MTVCANCAVPREVIO = (
    (1, u'1 - Reconsideração prevista no artigo 489 da CLT'),
    (2, u'2 - Determinação Judicial'),
    (3, u'3 - Cumprimento de norma legal'),
    (9, u'9 - Outros'),
)

CHOICES_S2250_TPAVPREVIO = (
    (1, u'1 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de duas horas diárias [caput do art. 488 da CLT]'),
    (2, u'2 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de dias corridos [parágrafo único do art. 488 da CLT]'),
    (4, u'4 - Aviso prévio dado pelo empregado (pedido de demissão), não dispensado de seu cumprimento, sob pena de desconto, pelo empregador, dos salários correspondentes ao prazo respectivo (§2º do art. 487 da CLT)'),
    (5, u'5 - Aviso prévio trabalhado dado pelo empregador rural ao empregado, com redução de um dia por semana ( art. 15 da Lei nº 5889/73)'),
)

class s2250cancAvPrevio(SoftDeletionModel):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    def evento(self): return self.s2250_evtavprevio.evento()
    dtcancavprv = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    mtvcancavprevio = models.IntegerField(choices=CHOICES_S2250_MTVCANCAVPREVIO)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtcancavprv) + ' - ' + unicode(self.mtvcancavprevio)
    #s2250_cancavprevio_custom#

    class Meta:
        db_table = r's2250_cancavprevio'       
        managed = True # s2250_cancavprevio #
        permissions = (
            ("can_view_s2250_cancavprevio", "Can view s2250_cancavprevio"),
            #custom_permissions_s2250_cancavprevio
        )
        ordering = ['s2250_evtavprevio', 'dtcancavprv', 'mtvcancavprevio']



class s2250cancAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250cancAvPrevio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2250detAvPrevio(SoftDeletionModel):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    def evento(self): return self.s2250_evtavprevio.evento()
    dtavprv = models.DateField()
    dtprevdeslig = models.DateField()
    tpavprevio = models.IntegerField(choices=CHOICES_S2250_TPAVPREVIO)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtavprv) + ' - ' + unicode(self.dtprevdeslig) + ' - ' + unicode(self.tpavprevio)
    #s2250_detavprevio_custom#

    class Meta:
        db_table = r's2250_detavprevio'       
        managed = True # s2250_detavprevio #
        permissions = (
            ("can_view_s2250_detavprevio", "Can view s2250_detavprevio"),
            #custom_permissions_s2250_detavprevio
        )
        ordering = ['s2250_evtavprevio', 'dtavprv', 'dtprevdeslig', 'tpavprevio']



class s2250detAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250detAvPrevio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
