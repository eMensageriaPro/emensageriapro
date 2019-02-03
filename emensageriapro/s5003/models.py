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
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from django.apps import apps
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S5003_TPDPS = (
    (51, u'51 - Depósito do FGTS'),
    (52, u'52 - Depósito do FGTS 13° Salário'),
    (53, u'53 - Depósito do FGTS Dissídio'),
    (54, u'54 - Depósito do FGTS Dissídio 13º Salário'),
    (55, u'55 - Depósito do FGTS - Aprendiz'),
    (56, u'56 - Depósito do FGTS 13° Salário - Aprendiz'),
    (57, u'57 - Depósito do FGTS Dissídio - Aprendiz'),
    (58, u'58 - Depósito do FGTS Dissídio 13º Salário - Aprendiz'),
    (61, u'61 - Depósito do FGTS Rescisório'),
    (62, u'62 - Depósito do FGTS Rescisório - 13° Salário'),
    (63, u'63 - Depósito do FGTS Rescisório - Aviso Prévio'),
    (64, u'64 - Depósito do FGTS Rescisório - Dissídio'),
    (65, u'65 - Depósito do FGTS Rescisório - Dissídio 13º Salário'),
    (66, u'66 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio'),
    (67, u'67 - Depósito do FGTS Rescisório - Aprendiz'),
    (68, u'68 - Depósito do FGTS Rescisório - 13° Salário Aprendiz'),
    (69, u'69 - Depósito do FGTS Rescisório - Aviso Prévio Aprendiz'),
    (70, u'70 - Depósito do FGTS Rescisório - Dissídio Aprendiz'),
    (71, u'71 - Depósito do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (72, u'72 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
)

CHOICES_S5003_TPDPSE = (
    (53, u'53 - Depósito do FGTS Dissídio'),
    (54, u'54 - Depósito do FGTS Dissídio 13º Salário'),
    (57, u'57 - Depósito do FGTS Dissídio - Aprendiz'),
    (58, u'58 - Depósito do FGTS Dissídio 13º Salário - Aprendiz'),
    (64, u'64 - Depósito do FGTS Rescisório - Dissídio'),
    (65, u'65 - Depósito do FGTS Rescisório - Dissídio 13º Salário'),
    (66, u'66 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio'),
    (70, u'70 - Depósito do FGTS Rescisório - Dissídio Aprendiz'),
    (71, u'71 - Depósito do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (72, u'72 - Depósito do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
)

CHOICES_S5003_TPVALOR = (
    (11, u'11 - Base de Cálculo do FGTS'),
    (12, u'12 - Base de Cálculo do FGTS 13° Salário'),
    (13, u'13 - Base de Cálculo do FGTS Dissídio'),
    (14, u'14 - Base de Cálculo do FGTS Dissídio 13º Salário'),
    (15, u'15 - Base de Cálculo do FGTS - Aprendiz'),
    (16, u'16 - Base de Cálculo do FGTS 13° Salário - Aprendiz'),
    (17, u'17 - Base de Cálculo do FGTS Dissídio - Aprendiz'),
    (18, u'18 - Base de Cálculo do FGTS Dissídio 13º Salário - Aprendiz'),
    (21, u'21 - Base de Cálculo do FGTS Rescisório'),
    (22, u'22 - Base de Cálculo do FGTS Rescisório - 13° Salário'),
    (23, u'23 - Base de Cálculo do FGTS Rescisório - Aviso Prévio'),
    (24, u'24 - Base de Cálculo do FGTS Rescisório - Dissídio'),
    (25, u'25 - Base de Cálculo do FGTS Rescisório - Dissídio 13º Salário'),
    (26, u'26 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio'),
    (27, u'27 - Base de Cálculo do FGTS Rescisório - Aprendiz'),
    (28, u'28 - Base de Cálculo do FGTS Rescisório - 13° Salário Aprendiz'),
    (29, u'29 - Base de Cálculo do FGTS Rescisório - Aviso Prévio Aprendiz'),
    (30, u'30 - Base de Cálculo do FGTS Rescisório - Dissídio Aprendiz'),
    (31, u'31 - Base de Cálculo do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (32, u'32 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

CHOICES_S5003_TPVALORE = (
    (13, u'13 - Base de Cálculo do FGTS Dissídio'),
    (14, u'14 - Base de Cálculo do FGTS Dissídio 13º Salário'),
    (17, u'17 - Base de Cálculo do FGTS Dissídio - Aprendiz'),
    (18, u'18 - Base de Cálculo do FGTS Dissídio 13º Salário - Aprendiz'),
    (24, u'24 - Base de Cálculo do FGTS Rescisório - Dissídio'),
    (25, u'25 - Base de Cálculo do FGTS Rescisório - Dissídio 13º Salário'),
    (26, u'26 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio'),
    (30, u'30 - Base de Cálculo do FGTS Rescisório - Dissídio Aprendiz'),
    (31, u'31 - Base de Cálculo do FGTS Rescisório - Dissídio 13° Salário Aprendiz'),
    (32, u'32 - Base de Cálculo do FGTS Rescisório - Dissídio Aviso Prévio Aprendiz'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial'),
)

class s5003basePerAntE(SoftDeletionModel):
    s5003_infobaseperante = models.ForeignKey('s5003infoBasePerAntE',
        related_name='%(class)s_s5003_infobaseperante')
    def evento(self): return self.s5003_infobaseperante.evento()
    tpvalore = models.IntegerField(choices=CHOICES_S5003_TPVALORE)
    remfgtse = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infobaseperante) + ' - ' + unicode(self.tpvalore) + ' - ' + unicode(self.remfgtse)
    #s5003_baseperante_custom#
    class Meta:
        db_table = r's5003_baseperante'
        managed = True # s5003_baseperante #
        ordering = ['s5003_infobaseperante', 'tpvalore', 'remfgtse']



class s5003basePerAntESerializer(ModelSerializer):
    class Meta:
        model = s5003basePerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003basePerApur(SoftDeletionModel):
    s5003_infotrabfgts = models.ForeignKey('s5003infoTrabFGTS',
        related_name='%(class)s_s5003_infotrabfgts')
    def evento(self): return self.s5003_infotrabfgts.evento()
    tpvalor = models.IntegerField(choices=CHOICES_S5003_TPVALOR)
    remfgts = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infotrabfgts) + ' - ' + unicode(self.tpvalor) + ' - ' + unicode(self.remfgts)
    #s5003_baseperapur_custom#
    class Meta:
        db_table = r's5003_baseperapur'
        managed = True # s5003_baseperapur #
        ordering = ['s5003_infotrabfgts', 'tpvalor', 'remfgts']



class s5003basePerApurSerializer(ModelSerializer):
    class Meta:
        model = s5003basePerApur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003dpsPerAntE(SoftDeletionModel):
    s5003_infodpsperante = models.ForeignKey('s5003infoDpsPerAntE',
        related_name='%(class)s_s5003_infodpsperante')
    def evento(self): return self.s5003_infodpsperante.evento()
    tpdpse = models.IntegerField(choices=CHOICES_S5003_TPDPSE)
    dpsfgtse = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infodpsperante) + ' - ' + unicode(self.tpdpse) + ' - ' + unicode(self.dpsfgtse)
    #s5003_dpsperante_custom#
    class Meta:
        db_table = r's5003_dpsperante'
        managed = True # s5003_dpsperante #
        ordering = ['s5003_infodpsperante', 'tpdpse', 'dpsfgtse']



class s5003dpsPerAntESerializer(ModelSerializer):
    class Meta:
        model = s5003dpsPerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003dpsPerApur(SoftDeletionModel):
    s5003_infotrabdps = models.ForeignKey('s5003infoTrabDps',
        related_name='%(class)s_s5003_infotrabdps')
    def evento(self): return self.s5003_infotrabdps.evento()
    tpdps = models.IntegerField(choices=CHOICES_S5003_TPDPS)
    dpsfgts = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infotrabdps) + ' - ' + unicode(self.tpdps) + ' - ' + unicode(self.dpsfgts)
    #s5003_dpsperapur_custom#
    class Meta:
        db_table = r's5003_dpsperapur'
        managed = True # s5003_dpsperapur #
        ordering = ['s5003_infotrabdps', 'tpdps', 'dpsfgts']



class s5003dpsPerApurSerializer(ModelSerializer):
    class Meta:
        model = s5003dpsPerApur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003ideEstabLot(SoftDeletionModel):
    s5003_infofgts = models.ForeignKey('s5003infoFGTS',
        related_name='%(class)s_s5003_infofgts')
    def evento(self): return self.s5003_infofgts.evento()
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infofgts) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s5003_ideestablot_custom#
    class Meta:
        db_table = r's5003_ideestablot'
        managed = True # s5003_ideestablot #
        ordering = ['s5003_infofgts', 'tpinsc', 'nrinsc', 'codlotacao']



class s5003ideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s5003ideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003infoBasePerAntE(SoftDeletionModel):
    s5003_infotrabfgts = models.ForeignKey('s5003infoTrabFGTS',
        related_name='%(class)s_s5003_infotrabfgts')
    def evento(self): return self.s5003_infotrabfgts.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infotrabfgts) + ' - ' + unicode(self.perref)
    #s5003_infobaseperante_custom#
    class Meta:
        db_table = r's5003_infobaseperante'
        managed = True # s5003_infobaseperante #
        ordering = ['s5003_infotrabfgts', 'perref']



class s5003infoBasePerAntESerializer(ModelSerializer):
    class Meta:
        model = s5003infoBasePerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003infoDpsPerAntE(SoftDeletionModel):
    s5003_infotrabdps = models.ForeignKey('s5003infoTrabDps',
        related_name='%(class)s_s5003_infotrabdps')
    def evento(self): return self.s5003_infotrabdps.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infotrabdps) + ' - ' + unicode(self.perref)
    #s5003_infodpsperante_custom#
    class Meta:
        db_table = r's5003_infodpsperante'
        managed = True # s5003_infodpsperante #
        ordering = ['s5003_infotrabdps', 'perref']



class s5003infoDpsPerAntESerializer(ModelSerializer):
    class Meta:
        model = s5003infoDpsPerAntE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003infoFGTS(SoftDeletionModel):
    s5003_evtbasesfgts = models.OneToOneField('esocial.s5003evtBasesFGTS',
        related_name='%(class)s_s5003_evtbasesfgts')
    def evento(self): return self.s5003_evtbasesfgts.evento()
    dtvenc = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_evtbasesfgts)
    #s5003_infofgts_custom#
    class Meta:
        db_table = r's5003_infofgts'
        managed = True # s5003_infofgts #
        ordering = ['s5003_evtbasesfgts']



class s5003infoFGTSSerializer(ModelSerializer):
    class Meta:
        model = s5003infoFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003infoTrabDps(SoftDeletionModel):
    s5003_infofgts = models.ForeignKey('s5003infoFGTS',
        related_name='%(class)s_s5003_infofgts')
    def evento(self): return self.s5003_infofgts.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_infofgts) + ' - ' + unicode(self.codcateg)
    #s5003_infotrabdps_custom#
    class Meta:
        db_table = r's5003_infotrabdps'
        managed = True # s5003_infotrabdps #
        ordering = ['s5003_infofgts', 'codcateg']



class s5003infoTrabDpsSerializer(ModelSerializer):
    class Meta:
        model = s5003infoTrabDps
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s5003infoTrabFGTS(SoftDeletionModel):
    s5003_ideestablot = models.ForeignKey('s5003ideEstabLot',
        related_name='%(class)s_s5003_ideestablot')
    def evento(self): return self.s5003_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    dtadm = models.DateField(blank=True, null=True)
    dtdeslig = models.DateField(blank=True, null=True)
    dtinicio = models.DateField(blank=True, null=True)
    mtvdeslig = models.CharField(max_length=2, blank=True, null=True)
    dtterm = models.DateField(blank=True, null=True)
    mtvdesligtsv = models.CharField(max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s5003_ideestablot) + ' - ' + unicode(self.codcateg)
    #s5003_infotrabfgts_custom#
    class Meta:
        db_table = r's5003_infotrabfgts'
        managed = True # s5003_infotrabfgts #
        ordering = ['s5003_ideestablot', 'codcateg']



class s5003infoTrabFGTSSerializer(ModelSerializer):
    class Meta:
        model = s5003infoTrabFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

#VIEWS_MODELS
