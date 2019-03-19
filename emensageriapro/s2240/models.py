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



CHOICES_S2240_ALTEXPRISCO_CONDFUNCTO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_EFICEPC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_EFICEPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_HIGIENIZACAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_MEDPROTECAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_PERIODICTROCA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_PRZVALID = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_ALTEXPRISCO_UTILIZEPC = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_ALTEXPRISCO_UTILIZEPI = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_INIEXPRISCO_APOSENTESP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_CONDFUNCTO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_EFICEPC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_EFICEPI = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_HIGIENIZACAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_IDEOC = (
    (1, u'1 - Conselho Regional de Medicina (CRM)'),
    (2, u'2 - Conselho Regional de Engenharia e Agronomia (CREA)'),
    (9, u'9 - Outros'),
)

CHOICES_S2240_INIEXPRISCO_INSALUBRIDADE = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_MEDPROTECAO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_PERICULOSIDADE = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_PERIODICTROCA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_PRZVALID = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_TPAVAL = (
    (1, u'1 - Critério quantitativo'),
    (2, u'2 - Critério qualitativo'),
)

CHOICES_S2240_INIEXPRISCO_UNMED = (
    (1, u'01 - Dose diária de ruído (número adimensional)'),
    (2, u'02 - Decibel linear (dB (linear))'),
    (3, u'03 - Decibel (C) (dB(C))'),
    (4, u'04 - Decibel (A) (dB(A))'),
    (5, u'05 - Quilocaloria por hora (kcal/h)'),
    (6, u'06 - Gray (Gy)'),
    (7, u'07 - Sievert (Sv)'),
    (8, u'08 - Quilograma-força por centímetro quadrado (kgf/cm2)'),
    (9, u'09 - Metro por segundo ao quadrado (m/s2)'),
    (10, u'10 - Metro por segundo elevado a 1,75 (m/s1,75)'),
    (11, u'11 - Parte de vapor ou gás por milhão de partes de ar contaminado (ppm)'),
    (12, u'12 - Miligrama por metro cúbico de ar (mg/m3)'),
    (13, u'13 - Fibra por centímetro cúbico (f/cm3)'),
    (14, u'14 - Grau centígrados (ºC)'),
    (15, u'15 - Metro por segundo (m/s)'),
    (16, u'16 - Percentual (%)'),
    (17, u'17 - Lux (lx)'),
    (18, u'18 - Unidade formadora de colônias por metro cúbico (ufc/m3)'),
)

CHOICES_S2240_INIEXPRISCO_USOININT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2240_INIEXPRISCO_UTILIZEPC = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

CHOICES_S2240_INIEXPRISCO_UTILIZEPI = (
    (0, u'0 - Não se aplica'),
    (1, u'1 - Não utilizado'),
    (2, u'2 - Utilizado'),
)

ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

class s2240altExpRisco(SoftDeletionModel):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtaltcondicao)
    #s2240_altexprisco_custom#

    class Meta:
        # verbose_name = u'Condições ambientais do trabalho - Alteração'
        db_table = r's2240_altexprisco'       
        managed = True # s2240_altexprisco #
        unique_together = (
            #custom_unique_together_s2240_altexprisco#
            
        )
        index_together = (
            #custom_index_together_s2240_altexprisco
            #index_together_s2240_altexprisco
        )
        permissions = (
            ("can_view_s2240_altexprisco", "Can view s2240_altexprisco"),
            #custom_permissions_s2240_altexprisco
        )
        ordering = ['s2240_evtexprisco', 'dtaltcondicao']



class s2240altExpRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2240altExpRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240altExpRiscoepc(SoftDeletionModel):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    def evento(self): return self.s2240_altexprisco_fatrisco.evento()
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.dscepc)
    #s2240_altexprisco_epc_custom#

    class Meta:
        # verbose_name = u'Equipamentos de Proteção Coletiva - EPC'
        db_table = r's2240_altexprisco_epc'       
        managed = True # s2240_altexprisco_epc #
        unique_together = (
            #custom_unique_together_s2240_altexprisco_epc#
            
        )
        index_together = (
            #custom_index_together_s2240_altexprisco_epc
            #index_together_s2240_altexprisco_epc
        )
        permissions = (
            ("can_view_s2240_altexprisco_epc", "Can view s2240_altexprisco_epc"),
            #custom_permissions_s2240_altexprisco_epc
        )
        ordering = ['s2240_altexprisco_fatrisco', 'dscepc']



class s2240altExpRiscoepcSerializer(ModelSerializer):
    class Meta:
        model = s2240altExpRiscoepc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240altExpRiscoepi(SoftDeletionModel):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    def evento(self): return self.s2240_altexprisco_fatrisco.evento()
    caepi = models.CharField(max_length=20, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_CONDFUNCTO, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_HIGIENIZACAO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)
    #s2240_altexprisco_epi_custom#

    class Meta:
        # verbose_name = u'Equipamentos de Proteção Individual - EPI'
        db_table = r's2240_altexprisco_epi'       
        managed = True # s2240_altexprisco_epi #
        unique_together = (
            #custom_unique_together_s2240_altexprisco_epi#
            
        )
        index_together = (
            #custom_index_together_s2240_altexprisco_epi
            #index_together_s2240_altexprisco_epi
        )
        permissions = (
            ("can_view_s2240_altexprisco_epi", "Can view s2240_altexprisco_epi"),
            #custom_permissions_s2240_altexprisco_epi
        )
        ordering = ['s2240_altexprisco_fatrisco', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao']



class s2240altExpRiscoepiSerializer(ModelSerializer):
    class Meta:
        model = s2240altExpRiscoepi
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240altExpRiscofatRisco(SoftDeletionModel):
    s2240_altexprisco_infoamb = models.ForeignKey('s2240altExpRiscoinfoAmb',
        related_name='%(class)s_s2240_altexprisco_infoamb')
    def evento(self): return self.s2240_altexprisco_infoamb.evento()
    codfatris = models.TextField(max_length=10)
    intconc = models.CharField(max_length=15, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPC)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)
    #s2240_altexprisco_fatrisco_custom#

    class Meta:
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2240_altexprisco_fatrisco'       
        managed = True # s2240_altexprisco_fatrisco #
        unique_together = (
            #custom_unique_together_s2240_altexprisco_fatrisco#
            
        )
        index_together = (
            #custom_index_together_s2240_altexprisco_fatrisco
            #index_together_s2240_altexprisco_fatrisco
        )
        permissions = (
            ("can_view_s2240_altexprisco_fatrisco", "Can view s2240_altexprisco_fatrisco"),
            #custom_permissions_s2240_altexprisco_fatrisco
        )
        ordering = ['s2240_altexprisco_infoamb', 'codfatris', 'utilizepc', 'utilizepi']



class s2240altExpRiscofatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2240altExpRiscofatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240altExpRiscoinfoAmb(SoftDeletionModel):
    s2240_altexprisco = models.ForeignKey('s2240altExpRisco',
        related_name='%(class)s_s2240_altexprisco')
    def evento(self): return self.s2240_altexprisco.evento()
    codamb = models.CharField(max_length=30)
    dscativdes = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)
    #s2240_altexprisco_infoamb_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_altexprisco_infoamb'       
        managed = True # s2240_altexprisco_infoamb #
        unique_together = (
            #custom_unique_together_s2240_altexprisco_infoamb#
            
        )
        index_together = (
            #custom_index_together_s2240_altexprisco_infoamb
            #index_together_s2240_altexprisco_infoamb
        )
        permissions = (
            ("can_view_s2240_altexprisco_infoamb", "Can view s2240_altexprisco_infoamb"),
            #custom_permissions_s2240_altexprisco_infoamb
        )
        ordering = ['s2240_altexprisco', 'codamb', 'dscativdes']



class s2240altExpRiscoinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2240altExpRiscoinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240fimExpRisco(SoftDeletionModel):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtfimcondicao)
    #s2240_fimexprisco_custom#

    class Meta:
        # verbose_name = u'Condições ambientais do trabalho - Fim'
        db_table = r's2240_fimexprisco'       
        managed = True # s2240_fimexprisco #
        unique_together = (
            #custom_unique_together_s2240_fimexprisco#
            
        )
        index_together = (
            #custom_index_together_s2240_fimexprisco
            #index_together_s2240_fimexprisco
        )
        permissions = (
            ("can_view_s2240_fimexprisco", "Can view s2240_fimexprisco"),
            #custom_permissions_s2240_fimexprisco
        )
        ordering = ['s2240_evtexprisco', 'dtfimcondicao']



class s2240fimExpRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2240fimExpRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240fimExpRiscoinfoAmb(SoftDeletionModel):
    s2240_fimexprisco = models.ForeignKey('s2240fimExpRisco',
        related_name='%(class)s_s2240_fimexprisco')
    def evento(self): return self.s2240_fimexprisco.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_fimexprisco) + ' - ' + unicode(self.codamb)
    #s2240_fimexprisco_infoamb_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_fimexprisco_infoamb'       
        managed = True # s2240_fimexprisco_infoamb #
        unique_together = (
            #custom_unique_together_s2240_fimexprisco_infoamb#
            
        )
        index_together = (
            #custom_index_together_s2240_fimexprisco_infoamb
            #index_together_s2240_fimexprisco_infoamb
        )
        permissions = (
            ("can_view_s2240_fimexprisco_infoamb", "Can view s2240_fimexprisco_infoamb"),
            #custom_permissions_s2240_fimexprisco_infoamb
        )
        ordering = ['s2240_fimexprisco', 'codamb']



class s2240fimExpRiscoinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2240fimExpRiscoinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240fimExpRiscorespReg(SoftDeletionModel):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    dtini = models.DateField()
    dtfim = models.DateField(blank=True, null=True)
    nisresp = models.CharField(max_length=11)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtini) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nroc)
    #s2240_fimexprisco_respreg_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao responsável pelos registros ambientais'
        db_table = r's2240_fimexprisco_respreg'       
        managed = True # s2240_fimexprisco_respreg #
        unique_together = (
            #custom_unique_together_s2240_fimexprisco_respreg#
            
        )
        index_together = (
            #custom_index_together_s2240_fimexprisco_respreg
            #index_together_s2240_fimexprisco_respreg
        )
        permissions = (
            ("can_view_s2240_fimexprisco_respreg", "Can view s2240_fimexprisco_respreg"),
            #custom_permissions_s2240_fimexprisco_respreg
        )
        ordering = ['s2240_evtexprisco', 'dtini', 'nisresp', 'nroc']



class s2240fimExpRiscorespRegSerializer(ModelSerializer):
    class Meta:
        model = s2240fimExpRiscorespReg
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscoativPericInsal(SoftDeletionModel):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    codativ = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codativ)
    #s2240_iniexprisco_ativpericinsal_custom#

    class Meta:
        # verbose_name = u'Informação da(s) atividade(s) periculosa(s), insalubre(s) ou especial(is) desempenhada(s)'
        db_table = r's2240_iniexprisco_ativpericinsal'       
        managed = True # s2240_iniexprisco_ativpericinsal #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_ativpericinsal#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_ativpericinsal
            #index_together_s2240_iniexprisco_ativpericinsal
        )
        permissions = (
            ("can_view_s2240_iniexprisco_ativpericinsal", "Can view s2240_iniexprisco_ativpericinsal"),
            #custom_permissions_s2240_iniexprisco_ativpericinsal
        )
        ordering = ['s2240_evtexprisco', 'codativ']



class s2240iniExpRiscoativPericInsalSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscoativPericInsal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscoepc(SoftDeletionModel):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    def evento(self): return self.s2240_iniexprisco_fatrisco.evento()
    codep = models.CharField(max_length=30)
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.dscepc)
    #s2240_iniexprisco_epc_custom#

    class Meta:
        # verbose_name = u'Equipamentos de Proteção Coletiva - EPC'
        db_table = r's2240_iniexprisco_epc'       
        managed = True # s2240_iniexprisco_epc #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_epc#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_epc
            #index_together_s2240_iniexprisco_epc
        )
        permissions = (
            ("can_view_s2240_iniexprisco_epc", "Can view s2240_iniexprisco_epc"),
            #custom_permissions_s2240_iniexprisco_epc
        )
        ordering = ['s2240_iniexprisco_fatrisco', 'codep', 'dscepc']



class s2240iniExpRiscoepcSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscoepc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscoepi(SoftDeletionModel):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    def evento(self): return self.s2240_iniexprisco_fatrisco.evento()
    caepi = models.CharField(max_length=20, blank=True, null=True)
    dscepi = models.CharField(max_length=999, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_CONDFUNCTO, max_length=1)
    usoinint = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_USOININT, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_HIGIENIZACAO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.usoinint) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)
    #s2240_iniexprisco_epi_custom#

    class Meta:
        # verbose_name = u'Equipamentos de Proteção Individual - EPI'
        db_table = r's2240_iniexprisco_epi'       
        managed = True # s2240_iniexprisco_epi #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_epi#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_epi
            #index_together_s2240_iniexprisco_epi
        )
        permissions = (
            ("can_view_s2240_iniexprisco_epi", "Can view s2240_iniexprisco_epi"),
            #custom_permissions_s2240_iniexprisco_epi
        )
        ordering = ['s2240_iniexprisco_fatrisco', 'eficepi', 'medprotecao', 'condfuncto', 'usoinint', 'przvalid', 'periodictroca', 'higienizacao']



class s2240iniExpRiscoepiSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscoepi
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscofatRisco(SoftDeletionModel):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    codfatris = models.TextField(max_length=9)
    tpaval = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_TPAVAL)
    intconc = models.DecimalField(max_digits=15, decimal_places=2, max_length=10, blank=True, null=True)
    limtol = models.DecimalField(max_digits=15, decimal_places=2, max_length=10, blank=True, null=True)
    unmed = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UNMED, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    insalubridade = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_INSALUBRIDADE, max_length=1, blank=True, null=True)
    periculosidade = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PERICULOSIDADE, max_length=1, blank=True, null=True)
    aposentesp = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_APOSENTESP, max_length=1, blank=True, null=True)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPC)
    eficepc = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.tpaval) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)
    #s2240_iniexprisco_fatrisco_custom#

    class Meta:
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2240_iniexprisco_fatrisco'       
        managed = True # s2240_iniexprisco_fatrisco #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_fatrisco#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_fatrisco
            #index_together_s2240_iniexprisco_fatrisco
        )
        permissions = (
            ("can_view_s2240_iniexprisco_fatrisco", "Can view s2240_iniexprisco_fatrisco"),
            #custom_permissions_s2240_iniexprisco_fatrisco
        )
        ordering = ['s2240_evtexprisco', 'codfatris', 'tpaval', 'utilizepc', 'utilizepi']



class s2240iniExpRiscofatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscofatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscoinfoAmb(SoftDeletionModel):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.codamb)
    #s2240_iniexprisco_infoamb_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2240_iniexprisco_infoamb'       
        managed = True # s2240_iniexprisco_infoamb #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_infoamb#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_infoamb
            #index_together_s2240_iniexprisco_infoamb
        )
        permissions = (
            ("can_view_s2240_iniexprisco_infoamb", "Can view s2240_iniexprisco_infoamb"),
            #custom_permissions_s2240_iniexprisco_infoamb
        )
        ordering = ['s2240_evtexprisco', 'codamb']



class s2240iniExpRiscoinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscoinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscoobs(SoftDeletionModel):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    meterg = models.CharField(max_length=999, blank=True, null=True)
    obscompl = models.CharField(max_length=999, blank=True, null=True)
    observacao = models.CharField(max_length=999, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco)
    #s2240_iniexprisco_obs_custom#

    class Meta:
        # verbose_name = u'Observações relativas a registros ambientais'
        db_table = r's2240_iniexprisco_obs'       
        managed = True # s2240_iniexprisco_obs #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_obs#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_obs
            #index_together_s2240_iniexprisco_obs
        )
        permissions = (
            ("can_view_s2240_iniexprisco_obs", "Can view s2240_iniexprisco_obs"),
            #custom_permissions_s2240_iniexprisco_obs
        )
        ordering = ['s2240_evtexprisco']



class s2240iniExpRiscoobsSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscoobs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2240iniExpRiscorespReg(SoftDeletionModel):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    def evento(self): return self.s2240_evtexprisco.evento()
    cpfresp = models.CharField(max_length=11)
    nisresp = models.CharField(max_length=11)
    nmresp = models.CharField(max_length=70)
    ideoc = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_IDEOC)
    dscoc = models.CharField(max_length=20, blank=True, null=True)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.ideoc) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)
    #s2240_iniexprisco_respreg_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao responsável pelos registros ambientais'
        db_table = r's2240_iniexprisco_respreg'       
        managed = True # s2240_iniexprisco_respreg #
        unique_together = (
            #custom_unique_together_s2240_iniexprisco_respreg#
            
        )
        index_together = (
            #custom_index_together_s2240_iniexprisco_respreg
            #index_together_s2240_iniexprisco_respreg
        )
        permissions = (
            ("can_view_s2240_iniexprisco_respreg", "Can view s2240_iniexprisco_respreg"),
            #custom_permissions_s2240_iniexprisco_respreg
        )
        ordering = ['s2240_evtexprisco', 'cpfresp', 'nisresp', 'nmresp', 'ideoc', 'nroc', 'ufoc']



class s2240iniExpRiscorespRegSerializer(ModelSerializer):
    class Meta:
        model = s2240iniExpRiscorespReg
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
