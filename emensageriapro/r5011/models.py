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



CHOICES_R5011_INDEXISTINFO = (
    (1, u'1 - Há informações de bases e/ou de tributos'),
    (2, u'2 - Há movimento, porém não há informações de bases ou de tributos'),
    (3, u'3 - Não há movimento na competência'),
)

CHOICES_R5011_TPINSCTOMADOR = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R5011_TPOCORR = (
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
)

class r5011RCPRB(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    crcprb = models.IntegerField()
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcprb) + ' - ' + unicode(self.vlrcrcprb)
    #r5011_rcprb_custom#
    class Meta:
        db_table = r'r5011_rcprb'
        managed = True # r5011_rcprb #
        ordering = ['r5011_infototalcontrib', 'crcprb', 'vlrcrcprb']



class r5011RCPRBSerializer(ModelSerializer):
    class Meta:
        model = r5011RCPRB
        fields = '__all__'
            

class r5011RComl(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    crcoml = models.IntegerField()
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcoml) + ' - ' + unicode(self.vlrcrcoml)
    #r5011_rcoml_custom#
    class Meta:
        db_table = r'r5011_rcoml'
        managed = True # r5011_rcoml #
        ordering = ['r5011_infototalcontrib', 'crcoml', 'vlrcrcoml']



class r5011RComlSerializer(ModelSerializer):
    class Meta:
        model = r5011RComl
        fields = '__all__'
            

class r5011RPrest(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    tpinsctomador = models.IntegerField(choices=CHOICES_R5011_TPINSCTOMADOR)
    nrinsctomador = models.CharField(max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc)
    #r5011_rprest_custom#
    class Meta:
        db_table = r'r5011_rprest'
        managed = True # r5011_rprest #
        ordering = ['r5011_infototalcontrib', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc']



class r5011RPrestSerializer(ModelSerializer):
    class Meta:
        model = r5011RPrest
        fields = '__all__'
            

class r5011RRecRepAD(models.Model):
    r5011_infototalcontrib = models.OneToOneField('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    cnpjassocdesp = models.CharField(max_length=14)
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    crrecrepad = models.IntegerField()
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.crrecrepad) + ' - ' + unicode(self.vlrcrrecrepad)
    #r5011_rrecrepad_custom#
    class Meta:
        db_table = r'r5011_rrecrepad'
        managed = True # r5011_rrecrepad #
        ordering = ['r5011_infototalcontrib', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad']



class r5011RRecRepADSerializer(ModelSerializer):
    class Meta:
        model = r5011RRecRepAD
        fields = '__all__'
            

class r5011RTom(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    cnpjprestador = models.CharField(max_length=14)
    cno = models.CharField(max_length=12, blank=True, null=True)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbaseret)
    #r5011_rtom_custom#
    class Meta:
        db_table = r'r5011_rtom'
        managed = True # r5011_rtom #
        ordering = ['r5011_infototalcontrib', 'cnpjprestador', 'vlrtotalbaseret']



class r5011RTomSerializer(ModelSerializer):
    class Meta:
        model = r5011RTom
        fields = '__all__'
            

class r5011infoCRTom(models.Model):
    r5011_rtom = models.ForeignKey('r5011RTom',
        related_name='%(class)s_r5011_rtom')
    def evento(self): return self.r5011_rtom.evento()
    crtom = models.IntegerField()
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_rtom) + ' - ' + unicode(self.crtom)
    #r5011_infocrtom_custom#
    class Meta:
        db_table = r'r5011_infocrtom'
        managed = True # r5011_infocrtom #
        ordering = ['r5011_rtom', 'crtom']



class r5011infoCRTomSerializer(ModelSerializer):
    class Meta:
        model = r5011infoCRTom
        fields = '__all__'
            

class r5011infoTotalContrib(models.Model):
    r5011_evttotalcontrib = models.OneToOneField('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib')
    def evento(self): return self.r5011_evttotalcontrib.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True)
    indexistinfo = models.IntegerField(choices=CHOICES_R5011_INDEXISTINFO)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.indexistinfo)
    #r5011_infototalcontrib_custom#
    class Meta:
        db_table = r'r5011_infototalcontrib'
        managed = True # r5011_infototalcontrib #
        ordering = ['r5011_evttotalcontrib', 'indexistinfo']



class r5011infoTotalContribSerializer(ModelSerializer):
    class Meta:
        model = r5011infoTotalContrib
        fields = '__all__'
            

class r5011regOcorrs(models.Model):
    r5011_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib')
    def evento(self): return self.r5011_evttotalcontrib.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5011_TPOCORR)
    localerroaviso = models.CharField(max_length=200)
    codresp = models.CharField(max_length=6)
    dscresp = models.CharField(max_length=999)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.tpocorr) + ' - ' + unicode(self.localerroaviso) + ' - ' + unicode(self.codresp) + ' - ' + unicode(self.dscresp)
    #r5011_regocorrs_custom#
    class Meta:
        db_table = r'r5011_regocorrs'
        managed = True # r5011_regocorrs #
        ordering = ['r5011_evttotalcontrib', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp']



class r5011regOcorrsSerializer(ModelSerializer):
    class Meta:
        model = r5011regOcorrs
        fields = '__all__'
            

#VIEWS_MODELS
