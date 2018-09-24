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



CHOICES_S2231_INDCESSAO = (
    (1, u'1 - Cessão'),
    (2, u'2 - Agente público à disposição da Justiça Eleitoral'),
    (3, u'3 - Exercício em outro órgão, em caso diferente de cessão'),
)

CHOICES_S2231_INFONUS = (
    (1, u'1 - Pagamento exclusivamente pelo cedente/origem'),
    (2, u'2 - Pagamento exclusivamente pelo cessionário/destino'),
    (3, u'3 - Pagamento pelo cedente/origem e pelo cessionário/destino'),
    (4, u'4 - Pagamento pelo cedente/origem com ressarcimento pelo cessionário/destino'),
)

class s2231fimCessao(models.Model):
    s2231_evtcessao = models.OneToOneField('esocial.s2231evtCessao',
        related_name='%(class)s_s2231_evtcessao')
    dttermcessao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2231_evtcessao) + ' - ' + unicode(self.dttermcessao)
    #s2231_fimcessao_custom#
    #s2231_fimcessao_custom#
    class Meta:
        db_table = r's2231_fimcessao'
        managed = True
        ordering = ['s2231_evtcessao', 'dttermcessao']



class s2231fimCessaoSerializer(ModelSerializer):
    class Meta:
        model = s2231fimCessao
        fields = '__all__'
            

class s2231iniCessao(models.Model):
    s2231_evtcessao = models.OneToOneField('esocial.s2231evtCessao',
        related_name='%(class)s_s2231_evtcessao')
    dtinicessao = models.DateField()
    cnpjcess = models.CharField(max_length=14)
    infonus = models.IntegerField(choices=CHOICES_S2231_INFONUS)
    indcessao = models.IntegerField(choices=CHOICES_S2231_INDCESSAO)
    dscsituacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2231_evtcessao) + ' - ' + unicode(self.dtinicessao) + ' - ' + unicode(self.cnpjcess) + ' - ' + unicode(self.infonus) + ' - ' + unicode(self.indcessao) + ' - ' + unicode(self.dscsituacao)
    #s2231_inicessao_custom#
    #s2231_inicessao_custom#
    class Meta:
        db_table = r's2231_inicessao'
        managed = True
        ordering = ['s2231_evtcessao', 'dtinicessao', 'cnpjcess', 'infonus', 'indcessao', 'dscsituacao']



class s2231iniCessaoSerializer(ModelSerializer):
    class Meta:
        model = s2231iniCessao
        fields = '__all__'
            

#VIEWS_MODELS
