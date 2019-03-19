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



CHOICES_R5001_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (4, u'4 - CNO'),
)

CHOICES_R5001_TPINSCTOMADOR = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R5001_TPOCORR = (
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
)

class r5001RCPRB(SoftDeletionModel):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crcprb = models.IntegerField()
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crcprb) + ' - ' + unicode(self.vlrcrcprb)
    #r5001_rcprb_custom#

    class Meta:
        # verbose_name = u'Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB, apuradas no evento R-2060'
        db_table = r'r5001_rcprb'       
        managed = True # r5001_rcprb #
        unique_together = (
            #custom_unique_together_r5001_rcprb#
            
        )
        index_together = (
            #custom_index_together_r5001_rcprb
            #index_together_r5001_rcprb
        )
        permissions = (
            ("can_view_r5001_rcprb", "Can view r5001_rcprb"),
            #custom_permissions_r5001_rcprb
        )
        ordering = ['r5001_infototal', 'crcprb', 'vlrcrcprb']



class r5001RCPRBSerializer(ModelSerializer):
    class Meta:
        model = r5001RCPRB
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001RComl(SoftDeletionModel):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crcoml = models.IntegerField()
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crcoml) + ' - ' + unicode(self.vlrcrcoml)
    #r5001_rcoml_custom#

    class Meta:
        # verbose_name = u'Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria, apuradas no evento R-2050'
        db_table = r'r5001_rcoml'       
        managed = True # r5001_rcoml #
        unique_together = (
            #custom_unique_together_r5001_rcoml#
            
        )
        index_together = (
            #custom_index_together_r5001_rcoml
            #index_together_r5001_rcoml
        )
        permissions = (
            ("can_view_r5001_rcoml", "Can view r5001_rcoml"),
            #custom_permissions_r5001_rcoml
        )
        ordering = ['r5001_infototal', 'crcoml', 'vlrcrcoml']



class r5001RComlSerializer(ModelSerializer):
    class Meta:
        model = r5001RComl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001RPrest(SoftDeletionModel):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    tpinsctomador = models.IntegerField(choices=CHOICES_R5001_TPINSCTOMADOR)
    nrinsctomador = models.CharField(max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc)
    #r5001_rprest_custom#

    class Meta:
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados, apuradas no evento R-2020'
        db_table = r'r5001_rprest'       
        managed = True # r5001_rprest #
        unique_together = (
            #custom_unique_together_r5001_rprest#
            
        )
        index_together = (
            #custom_index_together_r5001_rprest
            #index_together_r5001_rprest
        )
        permissions = (
            ("can_view_r5001_rprest", "Can view r5001_rprest"),
            #custom_permissions_r5001_rprest
        )
        ordering = ['r5001_infototal', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc']



class r5001RPrestSerializer(ModelSerializer):
    class Meta:
        model = r5001RPrest
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001RRecEspetDesp(SoftDeletionModel):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crrecespetdesp = models.IntegerField()
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecespetdesp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecespetdespsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crrecespetdesp) + ' - ' + unicode(self.vlrreceitatotal) + ' - ' + unicode(self.vlrcrrecespetdesp)
    #r5001_rrecespetdesp_custom#

    class Meta:
        # verbose_name = u'Totalizador da contribuição previdenciária incidente sobre Receitas de Espetáculos Desportivos, apuradas no evento R-3010.'
        db_table = r'r5001_rrecespetdesp'       
        managed = True # r5001_rrecespetdesp #
        unique_together = (
            #custom_unique_together_r5001_rrecespetdesp#
            
        )
        index_together = (
            #custom_index_together_r5001_rrecespetdesp
            #index_together_r5001_rrecespetdesp
        )
        permissions = (
            ("can_view_r5001_rrecespetdesp", "Can view r5001_rrecespetdesp"),
            #custom_permissions_r5001_rrecespetdesp
        )
        ordering = ['r5001_infototal', 'crrecespetdesp', 'vlrreceitatotal', 'vlrcrrecespetdesp']



class r5001RRecEspetDespSerializer(ModelSerializer):
    class Meta:
        model = r5001RRecEspetDesp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001RRecRepAD(SoftDeletionModel):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    cnpjassocdesp = models.CharField(max_length=14)
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    crrecrepad = models.IntegerField()
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.crrecrepad) + ' - ' + unicode(self.vlrcrrecrepad)
    #r5001_rrecrepad_custom#

    class Meta:
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associações Desportivas que mantenham equipe de futebol profissional, apuradas no evento R-2040'
        db_table = r'r5001_rrecrepad'       
        managed = True # r5001_rrecrepad #
        unique_together = (
            #custom_unique_together_r5001_rrecrepad#
            
        )
        index_together = (
            #custom_index_together_r5001_rrecrepad
            #index_together_r5001_rrecrepad
        )
        permissions = (
            ("can_view_r5001_rrecrepad", "Can view r5001_rrecrepad"),
            #custom_permissions_r5001_rrecrepad
        )
        ordering = ['r5001_infototal', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad']



class r5001RRecRepADSerializer(ModelSerializer):
    class Meta:
        model = r5001RRecRepAD
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001RTom(SoftDeletionModel):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    cnpjprestador = models.CharField(max_length=14)
    cno = models.CharField(max_length=12, blank=True, null=True)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbaseret)
    #r5001_rtom_custom#

    class Meta:
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados, apuradas no evento R-2010'
        db_table = r'r5001_rtom'       
        managed = True # r5001_rtom #
        unique_together = (
            #custom_unique_together_r5001_rtom#
            
        )
        index_together = (
            #custom_index_together_r5001_rtom
            #index_together_r5001_rtom
        )
        permissions = (
            ("can_view_r5001_rtom", "Can view r5001_rtom"),
            #custom_permissions_r5001_rtom
        )
        ordering = ['r5001_infototal', 'cnpjprestador', 'vlrtotalbaseret']



class r5001RTomSerializer(ModelSerializer):
    class Meta:
        model = r5001RTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001infoCRTom(SoftDeletionModel):
    r5001_rtom = models.ForeignKey('r5001RTom',
        related_name='%(class)s_r5001_rtom')
    def evento(self): return self.r5001_rtom.evento()
    crtom = models.IntegerField()
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_rtom) + ' - ' + unicode(self.crtom)
    #r5001_infocrtom_custom#

    class Meta:
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados'
        db_table = r'r5001_infocrtom'       
        managed = True # r5001_infocrtom #
        unique_together = (
            #custom_unique_together_r5001_infocrtom#
            
        )
        index_together = (
            #custom_index_together_r5001_infocrtom
            #index_together_r5001_infocrtom
        )
        permissions = (
            ("can_view_r5001_infocrtom", "Can view r5001_infocrtom"),
            #custom_permissions_r5001_infocrtom
        )
        ordering = ['r5001_rtom', 'crtom']



class r5001infoCRTomSerializer(ModelSerializer):
    class Meta:
        model = r5001infoCRTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001infoTotal(SoftDeletionModel):
    r5001_evttotal = models.OneToOneField('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal')
    def evento(self): return self.r5001_evttotal.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True)
    tpinsc = models.IntegerField(choices=CHOICES_R5001_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_evttotal) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r5001_infototal_custom#

    class Meta:
        # verbose_name = u'Informações relativas a totalizadores de bases e tributos'
        db_table = r'r5001_infototal'       
        managed = True # r5001_infototal #
        unique_together = (
            #custom_unique_together_r5001_infototal#
            
        )
        index_together = (
            #custom_index_together_r5001_infototal
            #index_together_r5001_infototal
        )
        permissions = (
            ("can_view_r5001_infototal", "Can view r5001_infototal"),
            #custom_permissions_r5001_infototal
        )
        ordering = ['r5001_evttotal', 'tpinsc', 'nrinsc']



class r5001infoTotalSerializer(ModelSerializer):
    class Meta:
        model = r5001infoTotal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r5001regOcorrs(SoftDeletionModel):
    r5001_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal')
    def evento(self): return self.r5001_evttotal.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5001_TPOCORR)
    localerroaviso = models.CharField(max_length=200)
    codresp = models.CharField(max_length=6)
    dscresp = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r5001_evttotal) + ' - ' + unicode(self.tpocorr) + ' - ' + unicode(self.localerroaviso) + ' - ' + unicode(self.codresp) + ' - ' + unicode(self.dscresp)
    #r5001_regocorrs_custom#

    class Meta:
        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r5001_regocorrs'       
        managed = True # r5001_regocorrs #
        unique_together = (
            #custom_unique_together_r5001_regocorrs#
            
        )
        index_together = (
            #custom_index_together_r5001_regocorrs
            #index_together_r5001_regocorrs
        )
        permissions = (
            ("can_view_r5001_regocorrs", "Can view r5001_regocorrs"),
            #custom_permissions_r5001_regocorrs
        )
        ordering = ['r5001_evttotal', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp']



class r5001regOcorrsSerializer(ModelSerializer):
    class Meta:
        model = r5001regOcorrs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
