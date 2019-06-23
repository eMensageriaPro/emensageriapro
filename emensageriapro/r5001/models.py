#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.r5001.choices import *
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





class r5001RCPRB(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    crcprb = models.IntegerField(null=True, )
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB, apuradas no evento R-2060'
        db_table = r'r5001_rcprb'
        managed = True # r5001_rcprb #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RCPRB", u"Pode ver listagem do modelo R5001RCPRB"),
            ("can_see_data_r5001RCPRB", u"Pode visualizar o conteúdo do modelo R5001RCPRB"),
            ("can_see_menu_r5001RCPRB", u"Pode visualizar no menu o modelo R5001RCPRB"),
            ("can_print_list_r5001RCPRB", u"Pode imprimir listagem do modelo R5001RCPRB"),
            ("can_print_data_r5001RCPRB", u"Pode imprimir o conteúdo do modelo R5001RCPRB"), )

        ordering = [
            'r5001_infototal',
            'crcprb',
            'vlrcrcprb',]



class r5001RCPRBSerializer(ModelSerializer):

    class Meta:

        model = r5001RCPRB
        fields = '__all__'


class r5001RComl(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    crcoml = models.IntegerField(null=True, )
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria, apuradas no evento R-2050'
        db_table = r'r5001_rcoml'
        managed = True # r5001_rcoml #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RComl", u"Pode ver listagem do modelo R5001RCOML"),
            ("can_see_data_r5001RComl", u"Pode visualizar o conteúdo do modelo R5001RCOML"),
            ("can_see_menu_r5001RComl", u"Pode visualizar no menu o modelo R5001RCOML"),
            ("can_print_list_r5001RComl", u"Pode imprimir listagem do modelo R5001RCOML"),
            ("can_print_data_r5001RComl", u"Pode imprimir o conteúdo do modelo R5001RCOML"), )

        ordering = [
            'r5001_infototal',
            'crcoml',
            'vlrcrcoml',]



class r5001RComlSerializer(ModelSerializer):

    class Meta:

        model = r5001RComl
        fields = '__all__'


class r5001RPrest(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    tpinsctomador = models.IntegerField(null=True, )
    nrinsctomador = models.CharField(max_length=14, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados, apuradas no evento R-2020'
        db_table = r'r5001_rprest'
        managed = True # r5001_rprest #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RPrest", u"Pode ver listagem do modelo R5001RPREST"),
            ("can_see_data_r5001RPrest", u"Pode visualizar o conteúdo do modelo R5001RPREST"),
            ("can_see_menu_r5001RPrest", u"Pode visualizar no menu o modelo R5001RPREST"),
            ("can_print_list_r5001RPrest", u"Pode imprimir listagem do modelo R5001RPREST"),
            ("can_print_data_r5001RPrest", u"Pode imprimir o conteúdo do modelo R5001RPREST"), )

        ordering = [
            'r5001_infototal',
            'tpinsctomador',
            'nrinsctomador',
            'vlrtotalbaseret',
            'vlrtotalretprinc',]



class r5001RPrestSerializer(ModelSerializer):

    class Meta:

        model = r5001RPrest
        fields = '__all__'


class r5001RRecEspetDesp(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    crrecespetdesp = models.IntegerField(null=True, )
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecespetdesp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecespetdespsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador da contribuição previdenciária incidente sobre Receitas de Espetáculos Desportivos, apuradas no evento R-3010.'
        db_table = r'r5001_rrecespetdesp'
        managed = True # r5001_rrecespetdesp #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RRecEspetDesp", u"Pode ver listagem do modelo R5001RRECESPETDESP"),
            ("can_see_data_r5001RRecEspetDesp", u"Pode visualizar o conteúdo do modelo R5001RRECESPETDESP"),
            ("can_see_menu_r5001RRecEspetDesp", u"Pode visualizar no menu o modelo R5001RRECESPETDESP"),
            ("can_print_list_r5001RRecEspetDesp", u"Pode imprimir listagem do modelo R5001RRECESPETDESP"),
            ("can_print_data_r5001RRecEspetDesp", u"Pode imprimir o conteúdo do modelo R5001RRECESPETDESP"), )

        ordering = [
            'r5001_infototal',
            'crrecespetdesp',
            'vlrreceitatotal',
            'vlrcrrecespetdesp',]



class r5001RRecEspetDespSerializer(ModelSerializer):

    class Meta:

        model = r5001RRecEspetDesp
        fields = '__all__'


class r5001RRecRepAD(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    cnpjassocdesp = models.CharField(max_length=14, null=True, )
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    crrecrepad = models.IntegerField(null=True, )
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associações Desportivas que mantenham equipe de futebol profissional, apuradas no evento R-2040'
        db_table = r'r5001_rrecrepad'
        managed = True # r5001_rrecrepad #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RRecRepAD", u"Pode ver listagem do modelo R5001RRECREPAD"),
            ("can_see_data_r5001RRecRepAD", u"Pode visualizar o conteúdo do modelo R5001RRECREPAD"),
            ("can_see_menu_r5001RRecRepAD", u"Pode visualizar no menu o modelo R5001RRECREPAD"),
            ("can_print_list_r5001RRecRepAD", u"Pode imprimir listagem do modelo R5001RRECREPAD"),
            ("can_print_data_r5001RRecRepAD", u"Pode imprimir o conteúdo do modelo R5001RRECREPAD"), )

        ordering = [
            'r5001_infototal',
            'cnpjassocdesp',
            'vlrtotalrep',
            'crrecrepad',
            'vlrcrrecrepad',]



class r5001RRecRepADSerializer(ModelSerializer):

    class Meta:

        model = r5001RRecRepAD
        fields = '__all__'


class r5001RTom(SoftDeletionModel):

    r5001_infototal = models.ForeignKey('r5001.r5001infoTotal',
        related_name='%(class)s_r5001_infototal', )

    def evento(self):
        return self.r5001_infototal.evento()
    cnpjprestador = models.CharField(max_length=14, null=True, )
    cno = models.CharField(max_length=12, blank=True, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_infototal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados, apuradas no evento R-2010'
        db_table = r'r5001_rtom'
        managed = True # r5001_rtom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001RTom", u"Pode ver listagem do modelo R5001RTOM"),
            ("can_see_data_r5001RTom", u"Pode visualizar o conteúdo do modelo R5001RTOM"),
            ("can_see_menu_r5001RTom", u"Pode visualizar no menu o modelo R5001RTOM"),
            ("can_print_list_r5001RTom", u"Pode imprimir listagem do modelo R5001RTOM"),
            ("can_print_data_r5001RTom", u"Pode imprimir o conteúdo do modelo R5001RTOM"), )

        ordering = [
            'r5001_infototal',
            'cnpjprestador',
            'vlrtotalbaseret',]



class r5001RTomSerializer(ModelSerializer):

    class Meta:

        model = r5001RTom
        fields = '__all__'


class r5001infoCRTom(SoftDeletionModel):

    r5001_rtom = models.ForeignKey('r5001.r5001RTom',
        related_name='%(class)s_r5001_rtom', )

    def evento(self):
        return self.r5001_rtom.evento()
    crtom = models.IntegerField(null=True, )
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_rtom), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados'
        db_table = r'r5001_infocrtom'
        managed = True # r5001_infocrtom #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001infoCRTom", u"Pode ver listagem do modelo R5001INFOCRTOM"),
            ("can_see_data_r5001infoCRTom", u"Pode visualizar o conteúdo do modelo R5001INFOCRTOM"),
            ("can_see_menu_r5001infoCRTom", u"Pode visualizar no menu o modelo R5001INFOCRTOM"),
            ("can_print_list_r5001infoCRTom", u"Pode imprimir listagem do modelo R5001INFOCRTOM"),
            ("can_print_data_r5001infoCRTom", u"Pode imprimir o conteúdo do modelo R5001INFOCRTOM"), )

        ordering = [
            'r5001_rtom',
            'crtom',]



class r5001infoCRTomSerializer(ModelSerializer):

    class Meta:

        model = r5001infoCRTom
        fields = '__all__'


class r5001infoTotal(SoftDeletionModel):

    r5001_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal', )

    def evento(self):
        return self.r5001_evttotal.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_evttotal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Informações relativas a totalizadores de bases e tributos'
        db_table = r'r5001_infototal'
        managed = True # r5001_infototal #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001infoTotal", u"Pode ver listagem do modelo R5001INFOTOTAL"),
            ("can_see_data_r5001infoTotal", u"Pode visualizar o conteúdo do modelo R5001INFOTOTAL"),
            ("can_see_menu_r5001infoTotal", u"Pode visualizar no menu o modelo R5001INFOTOTAL"),
            ("can_print_list_r5001infoTotal", u"Pode imprimir listagem do modelo R5001INFOTOTAL"),
            ("can_print_data_r5001infoTotal", u"Pode imprimir o conteúdo do modelo R5001INFOTOTAL"), )

        ordering = [
            'r5001_evttotal',
            'tpinsc',
            'nrinsc',]



class r5001infoTotalSerializer(ModelSerializer):

    class Meta:

        model = r5001infoTotal
        fields = '__all__'


class r5001regOcorrs(SoftDeletionModel):

    r5001_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal', )

    def evento(self):
        return self.r5001_evttotal.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5001_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r5001_evttotal), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id

    class Meta:

        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r5001_regocorrs'
        managed = True # r5001_regocorrs #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r5001regOcorrs", u"Pode ver listagem do modelo R5001REGOCORRS"),
            ("can_see_data_r5001regOcorrs", u"Pode visualizar o conteúdo do modelo R5001REGOCORRS"),
            ("can_see_menu_r5001regOcorrs", u"Pode visualizar no menu o modelo R5001REGOCORRS"),
            ("can_print_list_r5001regOcorrs", u"Pode imprimir listagem do modelo R5001REGOCORRS"),
            ("can_print_data_r5001regOcorrs", u"Pode imprimir o conteúdo do modelo R5001REGOCORRS"), )

        ordering = [
            'r5001_evttotal',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r5001regOcorrsSerializer(ModelSerializer):

    class Meta:

        model = r5001regOcorrs
        fields = '__all__'