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

class s2250cancAvPrevio(models.Model):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    dtcancavprv = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    mtvcancavprevio = models.IntegerField(choices=CHOICES_S2250_MTVCANCAVPREVIO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtcancavprv) + ' - ' + unicode(self.observacao) + ' - ' + unicode(self.mtvcancavprevio)
    #s2250_cancavprevio_custom#
    #s2250_cancavprevio_custom#
    class Meta:
        db_table = r's2250_cancavprevio'
        managed = True
        ordering = ['s2250_evtavprevio', 'dtcancavprv', 'observacao', 'mtvcancavprevio']



class s2250cancAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250cancAvPrevio
        fields = '__all__'
            

class s2250detAvPrevio(models.Model):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    dtavprv = models.DateField()
    dtprevdeslig = models.DateField()
    tpavprevio = models.IntegerField(choices=CHOICES_S2250_TPAVPREVIO)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtavprv) + ' - ' + unicode(self.dtprevdeslig) + ' - ' + unicode(self.tpavprevio) + ' - ' + unicode(self.observacao)
    #s2250_detavprevio_custom#
    #s2250_detavprevio_custom#
    class Meta:
        db_table = r's2250_detavprevio'
        managed = True
        ordering = ['s2250_evtavprevio', 'dtavprv', 'dtprevdeslig', 'tpavprevio', 'observacao']



class s2250detAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250detAvPrevio
        fields = '__all__'
            

#VIEWS_MODELS
