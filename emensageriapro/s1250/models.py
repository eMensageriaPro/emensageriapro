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



class s1250ideProdutor(models.Model):
    s1250_tpaquis = models.ForeignKey('s1250tpAquis',
        related_name='%(class)s_s1250_tpaquis')
    def evento(self): return self.s1250_tpaquis.evento()
    tpinscprod = models.IntegerField()
    nrinscprod = models.CharField(max_length=14)
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    indopccp = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1250_tpaquis) + ' - ' + unicode(self.tpinscprod) + ' - ' + unicode(self.nrinscprod) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrsenardesc) + ' - ' + unicode(self.indopccp)
    #s1250_ideprodutor_custom#
    class Meta:
        db_table = r's1250_ideprodutor'
        managed = True # s1250_ideprodutor #
        ordering = ['s1250_tpaquis', 'tpinscprod', 'nrinscprod', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc', 'indopccp']



class s1250ideProdutorSerializer(ModelSerializer):
    class Meta:
        model = s1250ideProdutor
        fields = '__all__'
            

class s1250infoProcJ(models.Model):
    s1250_tpaquis = models.ForeignKey('s1250tpAquis',
        related_name='%(class)s_s1250_tpaquis')
    def evento(self): return self.s1250_tpaquis.evento()
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1250_tpaquis) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vrcpnret) + ' - ' + unicode(self.vrratnret) + ' - ' + unicode(self.vrsenarnret)
    #s1250_infoprocj_custom#
    class Meta:
        db_table = r's1250_infoprocj'
        managed = True # s1250_infoprocj #
        ordering = ['s1250_tpaquis', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret']



class s1250infoProcJSerializer(ModelSerializer):
    class Meta:
        model = s1250infoProcJ
        fields = '__all__'
            

class s1250infoProcJud(models.Model):
    s1250_ideprodutor = models.ForeignKey('s1250ideProdutor',
        related_name='%(class)s_s1250_ideprodutor')
    def evento(self): return self.s1250_ideprodutor.evento()
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1250_ideprodutor) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vrcpnret) + ' - ' + unicode(self.vrratnret) + ' - ' + unicode(self.vrsenarnret)
    #s1250_infoprocjud_custom#
    class Meta:
        db_table = r's1250_infoprocjud'
        managed = True # s1250_infoprocjud #
        ordering = ['s1250_ideprodutor', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret']



class s1250infoProcJudSerializer(ModelSerializer):
    class Meta:
        model = s1250infoProcJud
        fields = '__all__'
            

class s1250nfs(models.Model):
    s1250_ideprodutor = models.ForeignKey('s1250ideProdutor',
        related_name='%(class)s_s1250_ideprodutor')
    def evento(self): return self.s1250_ideprodutor.evento()
    serie = models.CharField(max_length=5, blank=True, null=True)
    nrdocto = models.CharField(max_length=20)
    dtemisnf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1250_ideprodutor) + ' - ' + unicode(self.nrdocto) + ' - ' + unicode(self.dtemisnf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrsenardesc)
    #s1250_nfs_custom#
    class Meta:
        db_table = r's1250_nfs'
        managed = True # s1250_nfs #
        ordering = ['s1250_ideprodutor', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc']



class s1250nfsSerializer(ModelSerializer):
    class Meta:
        model = s1250nfs
        fields = '__all__'
            

class s1250tpAquis(models.Model):
    s1250_evtaqprod = models.ForeignKey('esocial.s1250evtAqProd',
        related_name='%(class)s_s1250_evtaqprod')
    def evento(self): return self.s1250_evtaqprod.evento()
    indaquis = models.IntegerField()
    vlrtotaquis = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1250_evtaqprod) + ' - ' + unicode(self.indaquis) + ' - ' + unicode(self.vlrtotaquis)
    #s1250_tpaquis_custom#
    class Meta:
        db_table = r's1250_tpaquis'
        managed = True # s1250_tpaquis #
        ordering = ['s1250_evtaqprod', 'indaquis', 'vlrtotaquis']



class s1250tpAquisSerializer(ModelSerializer):
    class Meta:
        model = s1250tpAquis
        fields = '__all__'
            

#VIEWS_MODELS
