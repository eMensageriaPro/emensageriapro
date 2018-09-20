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
from django.apps import apps
get_model = apps.get_model



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

CHOICES_S2240_INIEXPRISCO_HIERUSO = (
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

CHOICES_S2240_INIEXPRISCO_MANUTENCAO = (
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

class s2240altExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtaltcondicao)
    #s2240_altexprisco_custom#
    #s2240_altexprisco_custom#
    class Meta:
        db_table = r's2240_altexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtaltcondicao']


class s2240altExpRiscoepc(models.Model):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.dscepc) + ' - ' + unicode(self.eficepc)
    #s2240_altexprisco_epc_custom#
    #s2240_altexprisco_epc_custom#
    class Meta:
        db_table = r's2240_altexprisco_epc'
        managed = True
        ordering = ['s2240_altexprisco_fatrisco', 'dscepc', 'eficepc']


class s2240altExpRiscoepi(models.Model):
    s2240_altexprisco_fatrisco = models.ForeignKey('s2240altExpRiscofatRisco',
        related_name='%(class)s_s2240_altexprisco_fatrisco')
    caepi = models.CharField(max_length=20, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_CONDFUNCTO, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_ALTEXPRISCO_HIGIENIZACAO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_fatrisco) + ' - ' + unicode(self.caepi) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao)
    #s2240_altexprisco_epi_custom#
    #s2240_altexprisco_epi_custom#
    class Meta:
        db_table = r's2240_altexprisco_epi'
        managed = True
        ordering = ['s2240_altexprisco_fatrisco', 'caepi', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao']


class s2240altExpRiscofatRisco(models.Model):
    s2240_altexprisco_infoamb = models.ForeignKey('s2240altExpRiscoinfoAmb',
        related_name='%(class)s_s2240_altexprisco_infoamb')
    codfatris = models.TextField(max_length=10)
    intconc = models.CharField(max_length=15, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPC)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_ALTEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.intconc) + ' - ' + unicode(self.tecmedicao) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.utilizepi)
    #s2240_altexprisco_fatrisco_custom#
    #s2240_altexprisco_fatrisco_custom#
    class Meta:
        db_table = r's2240_altexprisco_fatrisco'
        managed = True
        ordering = ['s2240_altexprisco_infoamb', 'codfatris', 'intconc', 'tecmedicao', 'utilizepc', 'utilizepi']


class s2240altExpRiscoinfoAmb(models.Model):
    s2240_altexprisco = models.ForeignKey('s2240altExpRisco',
        related_name='%(class)s_s2240_altexprisco')
    codamb = models.CharField(max_length=30)
    dscativdes = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_altexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)
    #s2240_altexprisco_infoamb_custom#
    #s2240_altexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_altexprisco_infoamb'
        managed = True
        ordering = ['s2240_altexprisco', 'codamb', 'dscativdes']


class s2240fimExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtfimcondicao)
    #s2240_fimexprisco_custom#
    #s2240_fimexprisco_custom#
    class Meta:
        db_table = r's2240_fimexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtfimcondicao']


class s2240fimExpRiscoinfoAmb(models.Model):
    s2240_fimexprisco = models.ForeignKey('s2240fimExpRisco',
        related_name='%(class)s_s2240_fimexprisco')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_fimexprisco) + ' - ' + unicode(self.codamb)
    #s2240_fimexprisco_infoamb_custom#
    #s2240_fimexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_fimexprisco_infoamb'
        managed = True
        ordering = ['s2240_fimexprisco', 'codamb']


class s2240fimExpRiscorespReg(models.Model):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtini = models.DateField()
    dtfim = models.DateField(blank=True, null=True)
    nisresp = models.CharField(max_length=11)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtini) + ' - ' + unicode(self.dtfim) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)
    #s2240_fimexprisco_respreg_custom#
    #s2240_fimexprisco_respreg_custom#
    class Meta:
        db_table = r's2240_fimexprisco_respreg'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtini', 'dtfim', 'nisresp', 'nroc', 'ufoc']


class s2240iniExpRisco(models.Model):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.dtinicondicao)
    #s2240_iniexprisco_custom#
    #s2240_iniexprisco_custom#
    class Meta:
        db_table = r's2240_iniexprisco'
        managed = True
        ordering = ['s2240_evtexprisco', 'dtinicondicao']


class s2240iniExpRiscoativPericInsal(models.Model):
    s2240_iniexprisco_infoamb = models.ForeignKey('s2240iniExpRiscoinfoAmb',
        related_name='%(class)s_s2240_iniexprisco_infoamb')
    codativ = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_infoamb) + ' - ' + unicode(self.codativ)
    #s2240_iniexprisco_ativpericinsal_custom#
    #s2240_iniexprisco_ativpericinsal_custom#
    class Meta:
        db_table = r's2240_iniexprisco_ativpericinsal'
        managed = True
        ordering = ['s2240_iniexprisco_infoamb', 'codativ']


class s2240iniExpRiscoepc(models.Model):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    codep = models.CharField(max_length=30)
    dscepc = models.CharField(max_length=70)
    eficepc = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPC, max_length=1, blank=True, null=True)
    codep = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.codep) + ' - ' + unicode(self.dscepc) + ' - ' + unicode(self.eficepc) + ' - ' + unicode(self.codep)
    #s2240_iniexprisco_epc_custom#
    #s2240_iniexprisco_epc_custom#
    class Meta:
        db_table = r's2240_iniexprisco_epc'
        managed = True
        ordering = ['s2240_iniexprisco_fatrisco', 'codep', 'dscepc', 'eficepc', 'codep']


class s2240iniExpRiscoepi(models.Model):
    s2240_iniexprisco_fatrisco = models.ForeignKey('s2240iniExpRiscofatRisco',
        related_name='%(class)s_s2240_iniexprisco_fatrisco')
    caepi = models.CharField(max_length=20, blank=True, null=True)
    eficepi = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_EFICEPI, max_length=1)
    medprotecao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_MEDPROTECAO, max_length=1)
    condfuncto = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_CONDFUNCTO, max_length=1)
    przvalid = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PRZVALID, max_length=1)
    periodictroca = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PERIODICTROCA, max_length=1)
    higienizacao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_HIGIENIZACAO, max_length=1)
    manutencao = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_MANUTENCAO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_fatrisco) + ' - ' + unicode(self.caepi) + ' - ' + unicode(self.eficepi) + ' - ' + unicode(self.medprotecao) + ' - ' + unicode(self.condfuncto) + ' - ' + unicode(self.przvalid) + ' - ' + unicode(self.periodictroca) + ' - ' + unicode(self.higienizacao) + ' - ' + unicode(self.manutencao)
    #s2240_iniexprisco_epi_custom#
    #s2240_iniexprisco_epi_custom#
    class Meta:
        db_table = r's2240_iniexprisco_epi'
        managed = True
        ordering = ['s2240_iniexprisco_fatrisco', 'caepi', 'eficepi', 'medprotecao', 'condfuncto', 'przvalid', 'periodictroca', 'higienizacao', 'manutencao']


class s2240iniExpRiscofatRisco(models.Model):
    s2240_iniexprisco_infoamb = models.ForeignKey('s2240iniExpRiscoinfoAmb',
        related_name='%(class)s_s2240_iniexprisco_infoamb')
    codfatris = models.TextField(max_length=10)
    tpaval = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_TPAVAL)
    intconc = models.CharField(max_length=15, blank=True, null=True)
    unmed = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UNMED, blank=True, null=True)
    tecmedicao = models.CharField(max_length=40, blank=True, null=True)
    insalubridade = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_INSALUBRIDADE, max_length=1)
    periculosidade = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_PERICULOSIDADE, max_length=1)
    aposentesp = models.CharField(choices=CHOICES_S2240_INIEXPRISCO_APOSENTESP, max_length=1)
    utilizepc = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPC)
    hieruso = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_HIERUSO)
    utilizepi = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_UTILIZEPI)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco_infoamb) + ' - ' + unicode(self.codfatris) + ' - ' + unicode(self.tpaval) + ' - ' + unicode(self.intconc) + ' - ' + unicode(self.unmed) + ' - ' + unicode(self.tecmedicao) + ' - ' + unicode(self.insalubridade) + ' - ' + unicode(self.periculosidade) + ' - ' + unicode(self.aposentesp) + ' - ' + unicode(self.utilizepc) + ' - ' + unicode(self.hieruso) + ' - ' + unicode(self.utilizepi)
    #s2240_iniexprisco_fatrisco_custom#
    #s2240_iniexprisco_fatrisco_custom#
    class Meta:
        db_table = r's2240_iniexprisco_fatrisco'
        managed = True
        ordering = ['s2240_iniexprisco_infoamb', 'codfatris', 'tpaval', 'intconc', 'unmed', 'tecmedicao', 'insalubridade', 'periculosidade', 'aposentesp', 'utilizepc', 'hieruso', 'utilizepi']


class s2240iniExpRiscoinfoAmb(models.Model):
    s2240_iniexprisco = models.ForeignKey('s2240iniExpRisco',
        related_name='%(class)s_s2240_iniexprisco')
    codamb = models.CharField(max_length=30)
    dscativdes = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_iniexprisco) + ' - ' + unicode(self.codamb) + ' - ' + unicode(self.dscativdes)
    #s2240_iniexprisco_infoamb_custom#
    #s2240_iniexprisco_infoamb_custom#
    class Meta:
        db_table = r's2240_iniexprisco_infoamb'
        managed = True
        ordering = ['s2240_iniexprisco', 'codamb', 'dscativdes']


class s2240iniExpRiscoobs(models.Model):
    s2240_evtexprisco = models.OneToOneField('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    meterg = models.CharField(max_length=999)
    observacao = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.meterg) + ' - ' + unicode(self.observacao)
    #s2240_iniexprisco_obs_custom#
    #s2240_iniexprisco_obs_custom#
    class Meta:
        db_table = r's2240_iniexprisco_obs'
        managed = True
        ordering = ['s2240_evtexprisco', 'meterg', 'observacao']


class s2240iniExpRiscorespReg(models.Model):
    s2240_evtexprisco = models.ForeignKey('esocial.s2240evtExpRisco',
        related_name='%(class)s_s2240_evtexprisco')
    cpfresp = models.CharField(max_length=11)
    nisresp = models.CharField(max_length=11)
    nmresp = models.CharField(max_length=70)
    ideoc = models.IntegerField(choices=CHOICES_S2240_INIEXPRISCO_IDEOC)
    dscoc = models.CharField(max_length=20, blank=True, null=True)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2240_evtexprisco) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.nisresp) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.ideoc) + ' - ' + unicode(self.dscoc) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.ufoc)
    #s2240_iniexprisco_respreg_custom#
    #s2240_iniexprisco_respreg_custom#
    class Meta:
        db_table = r's2240_iniexprisco_respreg'
        managed = True
        ordering = ['s2240_evtexprisco', 'cpfresp', 'nisresp', 'nmresp', 'ideoc', 'dscoc', 'nroc', 'ufoc']


#VIEWS_MODELS
