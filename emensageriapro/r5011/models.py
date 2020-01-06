# eMensageriaAI #
#coding:utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.r5011.choices import *
get_model = apps.get_model


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


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class r5011RCPRB(SoftDeletionModel):

    r5011_infototalcontrib = models.ForeignKey('r5011.r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib', )

    def evento(self):
        return self.r5011_infototalcontrib.evento()
    crcprb = models.IntegerField(null=True, )
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcprb) + ' - ' + unicode(self.vlrcrcprb)

    class Meta:

        # verbose_name = u'Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB, apuradas no evento R-2060'
        db_table = r'r5011_rcprb'
        managed = True # r5011_rcprb #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011RCPRB", u"Pode ver listagem do modelo R5011RCPRB"),
            ("can_see_data_r5011RCPRB", u"Pode visualizar o conteúdo do modelo R5011RCPRB"),
            ("can_see_menu_r5011RCPRB", u"Pode visualizar no menu o modelo R5011RCPRB"),
            ("can_print_list_r5011RCPRB", u"Pode imprimir listagem do modelo R5011RCPRB"),
            ("can_print_data_r5011RCPRB", u"Pode imprimir o conteúdo do modelo R5011RCPRB"), )

        ordering = [
            'r5011_infototalcontrib',
            'crcprb',
            'vlrcrcprb',]



class r5011RCPRBSerializer(ModelSerializer):

    class Meta:

        model = r5011RCPRB
        fields = '__all__'


class r5011RComl(SoftDeletionModel):

    r5011_infototalcontrib = models.ForeignKey('r5011.r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib', )

    def evento(self):
        return self.r5011_infototalcontrib.evento()
    crcoml = models.IntegerField(null=True, )
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcoml) + ' - ' + unicode(self.vlrcrcoml)

    class Meta:

        # verbose_name = u'Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria, apuradas no evento R-2050'
        db_table = r'r5011_rcoml'
        managed = True # r5011_rcoml #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011RComl", u"Pode ver listagem do modelo R5011RCOML"),
            ("can_see_data_r5011RComl", u"Pode visualizar o conteúdo do modelo R5011RCOML"),
            ("can_see_menu_r5011RComl", u"Pode visualizar no menu o modelo R5011RCOML"),
            ("can_print_list_r5011RComl", u"Pode imprimir listagem do modelo R5011RCOML"),
            ("can_print_data_r5011RComl", u"Pode imprimir o conteúdo do modelo R5011RCOML"), )

        ordering = [
            'r5011_infototalcontrib',
            'crcoml',
            'vlrcrcoml',]



class r5011RComlSerializer(ModelSerializer):

    class Meta:

        model = r5011RComl
        fields = '__all__'


class r5011RPrest(SoftDeletionModel):

    r5011_infototalcontrib = models.ForeignKey('r5011.r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib', )

    def evento(self):
        return self.r5011_infototalcontrib.evento()
    tpinsctomador = models.IntegerField(choices=CHOICES_R5011_TPINSCTOMADOR, null=True, )
    nrinsctomador = models.CharField(max_length=14, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados, apuradas no evento R-2020'
        db_table = r'r5011_rprest'
        managed = True # r5011_rprest #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011RPrest", u"Pode ver listagem do modelo R5011RPREST"),
            ("can_see_data_r5011RPrest", u"Pode visualizar o conteúdo do modelo R5011RPREST"),
            ("can_see_menu_r5011RPrest", u"Pode visualizar no menu o modelo R5011RPREST"),
            ("can_print_list_r5011RPrest", u"Pode imprimir listagem do modelo R5011RPREST"),
            ("can_print_data_r5011RPrest", u"Pode imprimir o conteúdo do modelo R5011RPREST"), )

        ordering = [
            'r5011_infototalcontrib',
            'tpinsctomador',
            'nrinsctomador',
            'vlrtotalbaseret',
            'vlrtotalretprinc',]



class r5011RPrestSerializer(ModelSerializer):

    class Meta:

        model = r5011RPrest
        fields = '__all__'


class r5011RRecRepAD(SoftDeletionModel):

    r5011_infototalcontrib = models.ForeignKey('r5011.r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib', )

    def evento(self):
        return self.r5011_infototalcontrib.evento()
    cnpjassocdesp = models.CharField(max_length=14, null=True, )
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    crrecrepad = models.IntegerField(null=True, )
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.crrecrepad) + ' - ' + unicode(self.vlrcrrecrepad)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associações Desportivas que mantenham equipe de futebol profissional, apuradas no evento R-2040'
        db_table = r'r5011_rrecrepad'
        managed = True # r5011_rrecrepad #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011RRecRepAD", u"Pode ver listagem do modelo R5011RRECREPAD"),
            ("can_see_data_r5011RRecRepAD", u"Pode visualizar o conteúdo do modelo R5011RRECREPAD"),
            ("can_see_menu_r5011RRecRepAD", u"Pode visualizar no menu o modelo R5011RRECREPAD"),
            ("can_print_list_r5011RRecRepAD", u"Pode imprimir listagem do modelo R5011RRECREPAD"),
            ("can_print_data_r5011RRecRepAD", u"Pode imprimir o conteúdo do modelo R5011RRECREPAD"), )

        ordering = [
            'r5011_infototalcontrib',
            'cnpjassocdesp',
            'vlrtotalrep',
            'crrecrepad',
            'vlrcrrecrepad',]



class r5011RRecRepADSerializer(ModelSerializer):

    class Meta:

        model = r5011RRecRepAD
        fields = '__all__'


class r5011RTom(SoftDeletionModel):

    r5011_infototalcontrib = models.ForeignKey('r5011.r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib', )

    def evento(self):
        return self.r5011_infototalcontrib.evento()
    cnpjprestador = models.CharField(max_length=14, null=True, )
    cno = models.CharField(max_length=12, blank=True, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbaseret)

    class Meta:

        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados, apuradas no evento R-2010'
        db_table = r'r5011_rtom'
        managed = True # r5011_rtom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011RTom", u"Pode ver listagem do modelo R5011RTOM"),
            ("can_see_data_r5011RTom", u"Pode visualizar o conteúdo do modelo R5011RTOM"),
            ("can_see_menu_r5011RTom", u"Pode visualizar no menu o modelo R5011RTOM"),
            ("can_print_list_r5011RTom", u"Pode imprimir listagem do modelo R5011RTOM"),
            ("can_print_data_r5011RTom", u"Pode imprimir o conteúdo do modelo R5011RTOM"), )

        ordering = [
            'r5011_infototalcontrib',
            'cnpjprestador',
            'vlrtotalbaseret',]



class r5011RTomSerializer(ModelSerializer):

    class Meta:

        model = r5011RTom
        fields = '__all__'


class r5011infoCRTom(SoftDeletionModel):

    r5011_rtom = models.ForeignKey('r5011.r5011RTom',
        related_name='%(class)s_r5011_rtom', )

    def evento(self):
        return self.r5011_rtom.evento()
    crtom = models.IntegerField(null=True, )
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_rtom) + ' - ' + unicode(self.crtom)

    class Meta:

        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados'
        db_table = r'r5011_infocrtom'
        managed = True # r5011_infocrtom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011infoCRTom", u"Pode ver listagem do modelo R5011INFOCRTOM"),
            ("can_see_data_r5011infoCRTom", u"Pode visualizar o conteúdo do modelo R5011INFOCRTOM"),
            ("can_see_menu_r5011infoCRTom", u"Pode visualizar no menu o modelo R5011INFOCRTOM"),
            ("can_print_list_r5011infoCRTom", u"Pode imprimir listagem do modelo R5011INFOCRTOM"),
            ("can_print_data_r5011infoCRTom", u"Pode imprimir o conteúdo do modelo R5011INFOCRTOM"), )

        ordering = [
            'r5011_rtom',
            'crtom',]



class r5011infoCRTomSerializer(ModelSerializer):

    class Meta:

        model = r5011infoCRTom
        fields = '__all__'


class r5011infoTotalContrib(SoftDeletionModel):

    r5011_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib', )

    def evento(self):
        return self.r5011_evttotalcontrib.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_R5011_INDEXISTINFO, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.indexistinfo)

    class Meta:

        # verbose_name = u'Informações consolidadas por contribuinte relativas a totalizadores de bases e tributos'
        db_table = r'r5011_infototalcontrib'
        managed = True # r5011_infototalcontrib #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011infoTotalContrib", u"Pode ver listagem do modelo R5011INFOTOTALCONTRIB"),
            ("can_see_data_r5011infoTotalContrib", u"Pode visualizar o conteúdo do modelo R5011INFOTOTALCONTRIB"),
            ("can_see_menu_r5011infoTotalContrib", u"Pode visualizar no menu o modelo R5011INFOTOTALCONTRIB"),
            ("can_print_list_r5011infoTotalContrib", u"Pode imprimir listagem do modelo R5011INFOTOTALCONTRIB"),
            ("can_print_data_r5011infoTotalContrib", u"Pode imprimir o conteúdo do modelo R5011INFOTOTALCONTRIB"), )

        ordering = [
            'r5011_evttotalcontrib',
            'indexistinfo',]



class r5011infoTotalContribSerializer(ModelSerializer):

    class Meta:

        model = r5011infoTotalContrib
        fields = '__all__'


class r5011regOcorrs(SoftDeletionModel):

    r5011_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib', )

    def evento(self):
        return self.r5011_evttotalcontrib.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5011_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )

    def __unicode__(self):
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.tpocorr) + ' - ' + unicode(self.localerroaviso) + ' - ' + unicode(self.codresp) + ' - ' + unicode(self.dscresp)

    class Meta:

        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r5011_regocorrs'
        managed = True # r5011_regocorrs #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5011regOcorrs", u"Pode ver listagem do modelo R5011REGOCORRS"),
            ("can_see_data_r5011regOcorrs", u"Pode visualizar o conteúdo do modelo R5011REGOCORRS"),
            ("can_see_menu_r5011regOcorrs", u"Pode visualizar no menu o modelo R5011REGOCORRS"),
            ("can_print_list_r5011regOcorrs", u"Pode imprimir listagem do modelo R5011REGOCORRS"),
            ("can_print_data_r5011regOcorrs", u"Pode imprimir o conteúdo do modelo R5011REGOCORRS"), )

        ordering = [
            'r5011_evttotalcontrib',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r5011regOcorrsSerializer(ModelSerializer):

    class Meta:

        model = r5011regOcorrs
        fields = '__all__'