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
from emensageriapro.r9012.choices import *
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





class r9012infoTotalContrib(SoftDeletionModel):

    r9012_evtretcons = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_r9012_evtretcons', )

    def evento(self):
        return self.r9012_evtretcons.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_R9012_INDEXISTINFO, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_evtretcons), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações consolidadas por contribuinte relativas a totalizadores de bases e tributos'
        db_table = r'r9012_infototalcontrib'
        managed = True # r9012_infototalcontrib #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012infoTotalContrib", u"Pode ver listagem do modelo R9012INFOTOTALCONTRIB"),
            ("can_see_data_r9012infoTotalContrib", u"Pode visualizar o conteúdo do modelo R9012INFOTOTALCONTRIB"),
            ("can_see_menu_r9012infoTotalContrib", u"Pode visualizar no menu o modelo R9012INFOTOTALCONTRIB"),
            ("can_print_list_r9012infoTotalContrib", u"Pode imprimir listagem do modelo R9012INFOTOTALCONTRIB"),
            ("can_print_data_r9012infoTotalContrib", u"Pode imprimir o conteúdo do modelo R9012INFOTOTALCONTRIB"), )

        ordering = [
            'r9012_evtretcons',
            'indexistinfo',]



class r9012infoTotalContribSerializer(ModelSerializer):

    class Meta:

        model = r9012infoTotalContrib
        fields = '__all__'


class r9012regOcorrs(SoftDeletionModel):

    r9012_evtretcons = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_r9012_evtretcons', )

    def evento(self):
        return self.r9012_evtretcons.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R9012_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_evtretcons), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r9012_regocorrs'
        managed = True # r9012_regocorrs #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012regOcorrs", u"Pode ver listagem do modelo R9012REGOCORRS"),
            ("can_see_data_r9012regOcorrs", u"Pode visualizar o conteúdo do modelo R9012REGOCORRS"),
            ("can_see_menu_r9012regOcorrs", u"Pode visualizar no menu o modelo R9012REGOCORRS"),
            ("can_print_list_r9012regOcorrs", u"Pode imprimir listagem do modelo R9012REGOCORRS"),
            ("can_print_data_r9012regOcorrs", u"Pode imprimir o conteúdo do modelo R9012REGOCORRS"), )

        ordering = [
            'r9012_evtretcons',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r9012regOcorrsSerializer(ModelSerializer):

    class Meta:

        model = r9012regOcorrs
        fields = '__all__'


class r9012totApurDec(SoftDeletionModel):

    r9012_infototalcontrib = models.ForeignKey('r9012.r9012infoTotalContrib',
        related_name='%(class)s_r9012_infototalcontrib', )

    def evento(self):
        return self.r9012_infototalcontrib.evento()
    perapurdec = models.IntegerField(choices=CHOICES_R9012_PERAPURDEC, null=True, )
    crdec = models.CharField(max_length=6, null=True, )
    vlrbasecrdec = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrdec = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrdecsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrdecsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_infototalcontrib), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração decendial'
        db_table = r'r9012_totapurdec'
        managed = True # r9012_totapurdec #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012totApurDec", u"Pode ver listagem do modelo R9012TOTAPURDEC"),
            ("can_see_data_r9012totApurDec", u"Pode visualizar o conteúdo do modelo R9012TOTAPURDEC"),
            ("can_see_menu_r9012totApurDec", u"Pode visualizar no menu o modelo R9012TOTAPURDEC"),
            ("can_print_list_r9012totApurDec", u"Pode imprimir listagem do modelo R9012TOTAPURDEC"),
            ("can_print_data_r9012totApurDec", u"Pode imprimir o conteúdo do modelo R9012TOTAPURDEC"), )

        ordering = [
            'r9012_infototalcontrib',
            'perapurdec',
            'crdec',
            'vlrbasecrdec',
            'vlrcrdec',]



class r9012totApurDecSerializer(ModelSerializer):

    class Meta:

        model = r9012totApurDec
        fields = '__all__'


class r9012totApurDia(SoftDeletionModel):

    r9012_infototalcontrib = models.ForeignKey('r9012.r9012infoTotalContrib',
        related_name='%(class)s_r9012_infototalcontrib', )

    def evento(self):
        return self.r9012_infototalcontrib.evento()
    perapurdia = models.IntegerField(null=True, )
    crdia = models.CharField(max_length=6, null=True, )
    vlrbasecrdia = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrdia = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrdiasusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrdiasusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_infototalcontrib), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração diário'
        db_table = r'r9012_totapurdia'
        managed = True # r9012_totapurdia #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012totApurDia", u"Pode ver listagem do modelo R9012TOTAPURDIA"),
            ("can_see_data_r9012totApurDia", u"Pode visualizar o conteúdo do modelo R9012TOTAPURDIA"),
            ("can_see_menu_r9012totApurDia", u"Pode visualizar no menu o modelo R9012TOTAPURDIA"),
            ("can_print_list_r9012totApurDia", u"Pode imprimir listagem do modelo R9012TOTAPURDIA"),
            ("can_print_data_r9012totApurDia", u"Pode imprimir o conteúdo do modelo R9012TOTAPURDIA"), )

        ordering = [
            'r9012_infototalcontrib',
            'perapurdia',
            'crdia',
            'vlrbasecrdia',
            'vlrcrdia',]



class r9012totApurDiaSerializer(ModelSerializer):

    class Meta:

        model = r9012totApurDia
        fields = '__all__'


class r9012totApurMen(SoftDeletionModel):

    r9012_infototalcontrib = models.ForeignKey('r9012.r9012infoTotalContrib',
        related_name='%(class)s_r9012_infototalcontrib', )

    def evento(self):
        return self.r9012_infototalcontrib.evento()
    crmen = models.CharField(max_length=6, null=True, )
    vlrbasecrmen = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrmen = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrmensusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrmensusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_infototalcontrib), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração mensal'
        db_table = r'r9012_totapurmen'
        managed = True # r9012_totapurmen #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012totApurMen", u"Pode ver listagem do modelo R9012TOTAPURMEN"),
            ("can_see_data_r9012totApurMen", u"Pode visualizar o conteúdo do modelo R9012TOTAPURMEN"),
            ("can_see_menu_r9012totApurMen", u"Pode visualizar no menu o modelo R9012TOTAPURMEN"),
            ("can_print_list_r9012totApurMen", u"Pode imprimir listagem do modelo R9012TOTAPURMEN"),
            ("can_print_data_r9012totApurMen", u"Pode imprimir o conteúdo do modelo R9012TOTAPURMEN"), )

        ordering = [
            'r9012_infototalcontrib',
            'crmen',
            'vlrbasecrmen',
            'vlrcrmen',]



class r9012totApurMenSerializer(ModelSerializer):

    class Meta:

        model = r9012totApurMen
        fields = '__all__'


class r9012totApurQui(SoftDeletionModel):

    r9012_infototalcontrib = models.ForeignKey('r9012.r9012infoTotalContrib',
        related_name='%(class)s_r9012_infototalcontrib', )

    def evento(self):
        return self.r9012_infototalcontrib.evento()
    perapurqui = models.IntegerField(choices=CHOICES_R9012_PERAPURQUI, null=True, )
    crqui = models.CharField(max_length=6, null=True, )
    vlrbasecrqui = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrqui = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrquisusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrquisusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_infototalcontrib), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com período de apuração quinzenal'
        db_table = r'r9012_totapurqui'
        managed = True # r9012_totapurqui #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012totApurQui", u"Pode ver listagem do modelo R9012TOTAPURQUI"),
            ("can_see_data_r9012totApurQui", u"Pode visualizar o conteúdo do modelo R9012TOTAPURQUI"),
            ("can_see_menu_r9012totApurQui", u"Pode visualizar no menu o modelo R9012TOTAPURQUI"),
            ("can_print_list_r9012totApurQui", u"Pode imprimir listagem do modelo R9012TOTAPURQUI"),
            ("can_print_data_r9012totApurQui", u"Pode imprimir o conteúdo do modelo R9012TOTAPURQUI"), )

        ordering = [
            'r9012_infototalcontrib',
            'perapurqui',
            'crqui',
            'vlrbasecrqui',
            'vlrcrqui',]



class r9012totApurQuiSerializer(ModelSerializer):

    class Meta:

        model = r9012totApurQui
        fields = '__all__'


class r9012totApurSem(SoftDeletionModel):

    r9012_infototalcontrib = models.ForeignKey('r9012.r9012infoTotalContrib',
        related_name='%(class)s_r9012_infototalcontrib', )

    def evento(self):
        return self.r9012_infototalcontrib.evento()
    perapursem = models.IntegerField(null=True, )
    crsem = models.CharField(max_length=6, null=True, )
    vlrbasecrsem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrsem = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasecrsemsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrsemsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.r9012_infototalcontrib), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Totalizador das bases de cálculo e das retenções dos tributos com apuração semanal'
        db_table = r'r9012_totapursem'
        managed = True # r9012_totapursem #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_r9012totApurSem", u"Pode ver listagem do modelo R9012TOTAPURSEM"),
            ("can_see_data_r9012totApurSem", u"Pode visualizar o conteúdo do modelo R9012TOTAPURSEM"),
            ("can_see_menu_r9012totApurSem", u"Pode visualizar no menu o modelo R9012TOTAPURSEM"),
            ("can_print_list_r9012totApurSem", u"Pode imprimir listagem do modelo R9012TOTAPURSEM"),
            ("can_print_data_r9012totApurSem", u"Pode imprimir o conteúdo do modelo R9012TOTAPURSEM"), )

        ordering = [
            'r9012_infototalcontrib',
            'perapursem',
            'crsem',
            'vlrbasecrsem',
            'vlrcrsem',]



class r9012totApurSemSerializer(ModelSerializer):

    class Meta:

        model = r9012totApurSem
        fields = '__all__'