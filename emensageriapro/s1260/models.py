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



CHOICES_S1260_INDCOMERC = (
    (2, u'2 - Comercialização da Produção efetuada diretamente no varejo a consumidor final ou a outro produtor rural pessoa física por Produtor Rural Pessoa Física, inclusive por Segurado Especial ou por Pessoa Física não produtor rural'),
    (3, u'3 - Comercialização da Produção por Prod. Rural PF/Seg. Especia - Vendas a PJ (exceto Entidade inscrita no Programa de Aquisição de Alimentos - PAA) ou a Intermediário PF'),
    (7, u'7 - Comercialização da Produção Isenta de acordo com a Lei no 13.606/2018'),
    (8, u'8 - Comercialização da Produção da Pessoa Física/Segurado Especial para Entidade inscrita no Programa de Aquisição de Alimentos - PAA'),
    (9, u'9 - Comercialização da Produção no Mercado Externo'),
)

CHOICES_S1260_TPINSC = (
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1260_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class s1260ideAdquir(models.Model):
    s1260_tpcomerc = models.ForeignKey('s1260tpComerc',
        related_name='%(class)s_s1260_tpcomerc')
    tpinsc = models.IntegerField(choices=CHOICES_S1260_TPINSC)
    nrinsc = models.CharField(max_length=15)
    vrcomerc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1260_tpcomerc) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.vrcomerc)
    #s1260_ideadquir_custom#
    #s1260_ideadquir_custom#
    class Meta:
        db_table = r's1260_ideadquir'
        managed = True
        ordering = ['s1260_tpcomerc', 'tpinsc', 'nrinsc', 'vrcomerc']



class s1260ideAdquirSerializer(ModelSerializer):
    class Meta:
        model = s1260ideAdquir
        fields = '__all__'
            

class s1260infoProcJud(models.Model):
    s1260_tpcomerc = models.ForeignKey('s1260tpComerc',
        related_name='%(class)s_s1260_tpcomerc')
    tpproc = models.IntegerField(choices=CHOICES_S1260_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    vrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrratsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1260_tpcomerc) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vrcpsusp) + ' - ' + unicode(self.vrratsusp) + ' - ' + unicode(self.vrsenarsusp)
    #s1260_infoprocjud_custom#
    #s1260_infoprocjud_custom#
    class Meta:
        db_table = r's1260_infoprocjud'
        managed = True
        ordering = ['s1260_tpcomerc', 'tpproc', 'nrproc', 'codsusp', 'vrcpsusp', 'vrratsusp', 'vrsenarsusp']



class s1260infoProcJudSerializer(ModelSerializer):
    class Meta:
        model = s1260infoProcJud
        fields = '__all__'
            

class s1260nfs(models.Model):
    s1260_ideadquir = models.ForeignKey('s1260ideAdquir',
        related_name='%(class)s_s1260_ideadquir')
    serie = models.CharField(max_length=5, blank=True, null=True)
    nrdocto = models.CharField(max_length=20)
    dtemisnf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1260_ideadquir) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.nrdocto) + ' - ' + unicode(self.dtemisnf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrsenardesc)
    #s1260_nfs_custom#
    #s1260_nfs_custom#
    class Meta:
        db_table = r's1260_nfs'
        managed = True
        ordering = ['s1260_ideadquir', 'serie', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc']



class s1260nfsSerializer(ModelSerializer):
    class Meta:
        model = s1260nfs
        fields = '__all__'
            

class s1260tpComerc(models.Model):
    s1260_evtcomprod = models.ForeignKey('esocial.s1260evtComProd',
        related_name='%(class)s_s1260_evtcomprod')
    indcomerc = models.IntegerField(choices=CHOICES_S1260_INDCOMERC)
    vrtotcom = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1260_evtcomprod) + ' - ' + unicode(self.indcomerc) + ' - ' + unicode(self.vrtotcom)
    #s1260_tpcomerc_custom#
    #s1260_tpcomerc_custom#
    class Meta:
        db_table = r's1260_tpcomerc'
        managed = True
        ordering = ['s1260_evtcomprod', 'indcomerc', 'vrtotcom']



class s1260tpComercSerializer(ModelSerializer):
    class Meta:
        model = s1260tpComerc
        fields = '__all__'
            

#VIEWS_MODELS
