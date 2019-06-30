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
from emensageriapro.s5001.choices import *
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





class s5001calcTerc(SoftDeletionModel):

    s5001_infocategincid = models.ForeignKey('s5001.s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid', )

    def evento(self):
        return self.s5001_infocategincid.evento()
    tpcr = models.CharField(choices=CHOICES_S5001_TPCR, max_length=6, null=True, )
    vrcssegterc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdescterc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_infocategincid), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Cálculo das contribuições sociais devidas a Outras Entidades e Fundos.'
        db_table = r's5001_calcterc'
        managed = True # s5001_calcterc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001calcTerc", u"Pode ver listagem do modelo S5001CALCTERC"),
            ("can_see_data_s5001calcTerc", u"Pode visualizar o conteúdo do modelo S5001CALCTERC"),
            ("can_see_menu_s5001calcTerc", u"Pode visualizar no menu o modelo S5001CALCTERC"),
            ("can_print_list_s5001calcTerc", u"Pode imprimir listagem do modelo S5001CALCTERC"),
            ("can_print_data_s5001calcTerc", u"Pode imprimir o conteúdo do modelo S5001CALCTERC"), )

        ordering = [
            's5001_infocategincid',
            'tpcr',
            'vrcssegterc',
            'vrdescterc',]



class s5001calcTercSerializer(ModelSerializer):

    class Meta:

        model = s5001calcTerc
        fields = '__all__'


class s5001ideEstabLot(SoftDeletionModel):

    s5001_infocp = models.ForeignKey('s5001.s5001infoCp',
        related_name='%(class)s_s5001_infocp', )

    def evento(self):
        return self.s5001_infocp.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_infocp), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's5001_ideestablot'
        managed = True # s5001_ideestablot #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001ideEstabLot", u"Pode ver listagem do modelo S5001IDEESTABLOT"),
            ("can_see_data_s5001ideEstabLot", u"Pode visualizar o conteúdo do modelo S5001IDEESTABLOT"),
            ("can_see_menu_s5001ideEstabLot", u"Pode visualizar no menu o modelo S5001IDEESTABLOT"),
            ("can_print_list_s5001ideEstabLot", u"Pode imprimir listagem do modelo S5001IDEESTABLOT"),
            ("can_print_data_s5001ideEstabLot", u"Pode imprimir o conteúdo do modelo S5001IDEESTABLOT"), )

        ordering = [
            's5001_infocp',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s5001ideEstabLotSerializer(ModelSerializer):

    class Meta:

        model = s5001ideEstabLot
        fields = '__all__'


class s5001infoBaseCS(SoftDeletionModel):

    s5001_infocategincid = models.ForeignKey('s5001.s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid', )

    def evento(self):
        return self.s5001_infocategincid.evento()
    ind13 = models.IntegerField(choices=CHOICES_S5001_IND13, null=True, )
    tpvalor = models.IntegerField(null=True, )
    valor = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_infocategincid), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre bases de cálculo, descontos e deduções de contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos. Evento de origem (S-1200, S-2299 e S-2399).'
        db_table = r's5001_infobasecs'
        managed = True # s5001_infobasecs #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001infoBaseCS", u"Pode ver listagem do modelo S5001INFOBASECS"),
            ("can_see_data_s5001infoBaseCS", u"Pode visualizar o conteúdo do modelo S5001INFOBASECS"),
            ("can_see_menu_s5001infoBaseCS", u"Pode visualizar no menu o modelo S5001INFOBASECS"),
            ("can_print_list_s5001infoBaseCS", u"Pode imprimir listagem do modelo S5001INFOBASECS"),
            ("can_print_data_s5001infoBaseCS", u"Pode imprimir o conteúdo do modelo S5001INFOBASECS"), )

        ordering = [
            's5001_infocategincid',
            'ind13',
            'tpvalor',
            'valor',]



class s5001infoBaseCSSerializer(ModelSerializer):

    class Meta:

        model = s5001infoBaseCS
        fields = '__all__'


class s5001infoCategIncid(SoftDeletionModel):

    s5001_ideestablot = models.ForeignKey('s5001.s5001ideEstabLot',
        related_name='%(class)s_s5001_ideestablot', )

    def evento(self):
        return self.s5001_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    indsimples = models.IntegerField(choices=CHOICES_S5001_INDSIMPLES, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_ideestablot), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações relativas à matrícula e categoria do trabalhador e tipos de incidências.'
        db_table = r's5001_infocategincid'
        managed = True # s5001_infocategincid #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001infoCategIncid", u"Pode ver listagem do modelo S5001INFOCATEGINCID"),
            ("can_see_data_s5001infoCategIncid", u"Pode visualizar o conteúdo do modelo S5001INFOCATEGINCID"),
            ("can_see_menu_s5001infoCategIncid", u"Pode visualizar no menu o modelo S5001INFOCATEGINCID"),
            ("can_print_list_s5001infoCategIncid", u"Pode imprimir listagem do modelo S5001INFOCATEGINCID"),
            ("can_print_data_s5001infoCategIncid", u"Pode imprimir o conteúdo do modelo S5001INFOCATEGINCID"), )

        ordering = [
            's5001_ideestablot',
            'codcateg',]



class s5001infoCategIncidSerializer(ModelSerializer):

    class Meta:

        model = s5001infoCategIncid
        fields = '__all__'


class s5001infoCp(SoftDeletionModel):

    s5001_evtbasestrab = models.ForeignKey('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab', )

    def evento(self):
        return self.s5001_evtbasestrab.evento()

    def __unicode__(self):

        lista = [
            unicode(self.s5001_evtbasestrab), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre bases de cálculo, descontos e deduções de contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos, referentes à Remuneração do Período de Apuração e de Períodos Anteriores informados nos eventos S-1200, S-2299 e S-2399.'
        db_table = r's5001_infocp'
        managed = True # s5001_infocp #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001infoCp", u"Pode ver listagem do modelo S5001INFOCP"),
            ("can_see_data_s5001infoCp", u"Pode visualizar o conteúdo do modelo S5001INFOCP"),
            ("can_see_menu_s5001infoCp", u"Pode visualizar no menu o modelo S5001INFOCP"),
            ("can_print_list_s5001infoCp", u"Pode imprimir listagem do modelo S5001INFOCP"),
            ("can_print_data_s5001infoCp", u"Pode imprimir o conteúdo do modelo S5001INFOCP"), )

        ordering = [
            's5001_evtbasestrab',]



class s5001infoCpSerializer(ModelSerializer):

    class Meta:

        model = s5001infoCp
        fields = '__all__'


class s5001infoCpCalc(SoftDeletionModel):

    s5001_evtbasestrab = models.ForeignKey('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab', )

    def evento(self):
        return self.s5001_evtbasestrab.evento()
    tpcr = models.CharField(choices=CHOICES_S5001_TPCR, max_length=6, null=True, )
    vrcpseg = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vrdescseg = models.DecimalField(max_digits=15, decimal_places=2, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_evtbasestrab), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Cálculo da contribuição previdenciária do segurado, incidente sobre a Remuneração do Período de Apuração e de Períodos Anteriores informada nos eventos S-1200, S-2299 e S-2399.'
        db_table = r's5001_infocpcalc'
        managed = True # s5001_infocpcalc #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001infoCpCalc", u"Pode ver listagem do modelo S5001INFOCPCALC"),
            ("can_see_data_s5001infoCpCalc", u"Pode visualizar o conteúdo do modelo S5001INFOCPCALC"),
            ("can_see_menu_s5001infoCpCalc", u"Pode visualizar no menu o modelo S5001INFOCPCALC"),
            ("can_print_list_s5001infoCpCalc", u"Pode imprimir listagem do modelo S5001INFOCPCALC"),
            ("can_print_data_s5001infoCpCalc", u"Pode imprimir o conteúdo do modelo S5001INFOCPCALC"), )

        ordering = [
            's5001_evtbasestrab',
            'tpcr',
            'vrcpseg',
            'vrdescseg',]



class s5001infoCpCalcSerializer(ModelSerializer):

    class Meta:

        model = s5001infoCpCalc
        fields = '__all__'


class s5001procJudTrab(SoftDeletionModel):

    s5001_evtbasestrab = models.ForeignKey('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab', )

    def evento(self):
        return self.s5001_evtbasestrab.evento()
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.s5001_evtbasestrab), ]

        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return unicode(self.id)

    class Meta:

        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's5001_procjudtrab'
        managed = True # s5001_procjudtrab #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_s5001procJudTrab", u"Pode ver listagem do modelo S5001PROCJUDTRAB"),
            ("can_see_data_s5001procJudTrab", u"Pode visualizar o conteúdo do modelo S5001PROCJUDTRAB"),
            ("can_see_menu_s5001procJudTrab", u"Pode visualizar no menu o modelo S5001PROCJUDTRAB"),
            ("can_print_list_s5001procJudTrab", u"Pode imprimir listagem do modelo S5001PROCJUDTRAB"),
            ("can_print_data_s5001procJudTrab", u"Pode imprimir o conteúdo do modelo S5001PROCJUDTRAB"), )

        ordering = [
            's5001_evtbasestrab',
            'nrprocjud',
            'codsusp',]



class s5001procJudTrabSerializer(ModelSerializer):

    class Meta:

        model = s5001procJudTrab
        fields = '__all__'