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



CHOICES_R2040_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2040_TPREPASSE = (
    (1, u'1 - Patrocínio'),
    (2, u'2 - Licenciamento de marcas e símbolos'),
    (3, u'3 - Publicidade'),
    (4, u'4 - Propaganda'),
    (5, u'5 - Transmissão de espetáculos'),
)

class r2040infoProc(models.Model):
    r2040_recursosrep = models.ForeignKey('r2040recursosRep',
        related_name='%(class)s_r2040_recursosrep')
    def evento(self): return self.r2040_recursosrep.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2040_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_recursosrep) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.vlrnret)
    #r2040_infoproc_custom#
    #r2040_infoproc_custom#
    class Meta:
        db_table = r'r2040_infoproc'
        managed = True
        ordering = ['r2040_recursosrep', 'tpproc', 'nrproc', 'vlrnret']



class r2040infoProcSerializer(ModelSerializer):
    class Meta:
        model = r2040infoProc
        fields = '__all__'
            

class r2040infoRecurso(models.Model):
    r2040_recursosrep = models.ForeignKey('r2040recursosRep',
        related_name='%(class)s_r2040_recursosrep')
    def evento(self): return self.r2040_recursosrep.evento()
    tprepasse = models.IntegerField(choices=CHOICES_R2040_TPREPASSE)
    descrecurso = models.CharField(max_length=20)
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_recursosrep) + ' - ' + unicode(self.tprepasse) + ' - ' + unicode(self.descrecurso) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vlrretapur)
    #r2040_inforecurso_custom#
    #r2040_inforecurso_custom#
    class Meta:
        db_table = r'r2040_inforecurso'
        managed = True
        ordering = ['r2040_recursosrep', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur']



class r2040infoRecursoSerializer(ModelSerializer):
    class Meta:
        model = r2040infoRecurso
        fields = '__all__'
            

class r2040recursosRep(models.Model):
    r2040_evtassocdesprep = models.ForeignKey('efdreinf.r2040evtAssocDespRep',
        related_name='%(class)s_r2040_evtassocdesprep')
    def evento(self): return self.r2040_evtassocdesprep.evento()
    cnpjassocdesp = models.CharField(max_length=14)
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_evtassocdesprep) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.vlrtotalret)
    #r2040_recursosrep_custom#
    #r2040_recursosrep_custom#
    class Meta:
        db_table = r'r2040_recursosrep'
        managed = True
        ordering = ['r2040_evtassocdesprep', 'cnpjassocdesp', 'vlrtotalrep', 'vlrtotalret']



class r2040recursosRepSerializer(ModelSerializer):
    class Meta:
        model = r2040recursosRep
        fields = '__all__'
            

#VIEWS_MODELS
