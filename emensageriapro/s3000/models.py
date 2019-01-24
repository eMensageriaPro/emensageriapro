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



CHOICES_S3000_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

class s3000ideFolhaPagto(models.Model):
    s3000_evtexclusao = models.OneToOneField('esocial.s3000evtExclusao',
        related_name='%(class)s_s3000_evtexclusao')
    def evento(self): return self.s3000_evtexclusao.evento()
    indapuracao = models.IntegerField(choices=CHOICES_S3000_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s3000_evtexclusao) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur)
    #s3000_idefolhapagto_custom#
    class Meta:
        db_table = r's3000_idefolhapagto'
        managed = True # s3000_idefolhapagto #
        ordering = ['s3000_evtexclusao', 'indapuracao', 'perapur']



class s3000ideFolhaPagtoSerializer(ModelSerializer):
    class Meta:
        model = s3000ideFolhaPagto
        fields = '__all__'
            

class s3000ideTrabalhador(models.Model):
    s3000_evtexclusao = models.OneToOneField('esocial.s3000evtExclusao',
        related_name='%(class)s_s3000_evtexclusao')
    def evento(self): return self.s3000_evtexclusao.evento()
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s3000_evtexclusao) + ' - ' + unicode(self.cpftrab)
    #s3000_idetrabalhador_custom#
    class Meta:
        db_table = r's3000_idetrabalhador'
        managed = True # s3000_idetrabalhador #
        ordering = ['s3000_evtexclusao', 'cpftrab']



class s3000ideTrabalhadorSerializer(ModelSerializer):
    class Meta:
        model = s3000ideTrabalhador
        fields = '__all__'
            

#VIEWS_MODELS
