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



CHOICES_S1207_INFOPERANT_TPACCONV = (
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('G', u'G - Decisão administrativa'),
    ('H', u'H - Decisão judicial'),
)

CHOICES_S1207_TPBENEF = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b" CF, Redação EC 20/98'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b" CF, Redação EC 41/03'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S1207_TPTRIB = (
    (1, u'1 - IRRF'),
    (5, u'5 - Contribuição para o RPPS/regime militar'),
)

class s1207dmDev(SoftDeletionModel):
    s1207_evtbenprrp = models.ForeignKey('esocial.s1207evtBenPrRP',
        related_name='%(class)s_s1207_evtbenprrp')
    def evento(self): return self.s1207_evtbenprrp.evento()
    tpbenef = models.IntegerField(choices=CHOICES_S1207_TPBENEF)
    nrbenefic = models.CharField(max_length=20)
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_evtbenprrp) + ' - ' + unicode(self.tpbenef) + ' - ' + unicode(self.nrbenefic) + ' - ' + unicode(self.idedmdev)
    #s1207_dmdev_custom#

    class Meta:
        db_table = r's1207_dmdev'       
        managed = True # s1207_dmdev #
        unique_together = (
            #custom_unique_together_s1207_dmdev#
            
        )
        index_together = (
            #custom_index_together_s1207_dmdev
            #index_together_s1207_dmdev
        )
        permissions = (
            ("can_view_s1207_dmdev", "Can view s1207_dmdev"),
            #custom_permissions_s1207_dmdev
        )
        ordering = ['s1207_evtbenprrp', 'tpbenef', 'nrbenefic', 'idedmdev']



class s1207dmDevSerializer(ModelSerializer):
    class Meta:
        model = s1207dmDev
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerAntideADC(SoftDeletionModel):
    s1207_dmdev = models.ForeignKey('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    dtacconv = models.DateField(blank=True, null=True)
    tpacconv = models.CharField(choices=CHOICES_S1207_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField(blank=True, null=True)
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_dmdev) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dsc)
    #s1207_infoperant_ideadc_custom#

    class Meta:
        db_table = r's1207_infoperant_ideadc'       
        managed = True # s1207_infoperant_ideadc #
        unique_together = (
            #custom_unique_together_s1207_infoperant_ideadc#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperant_ideadc
            #index_together_s1207_infoperant_ideadc
        )
        permissions = (
            ("can_view_s1207_infoperant_ideadc", "Can view s1207_infoperant_ideadc"),
            #custom_permissions_s1207_infoperant_ideadc
        )
        ordering = ['s1207_dmdev', 'tpacconv', 'dsc']



class s1207infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntideADC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerAntideEstab(SoftDeletionModel):
    s1207_infoperant_ideperiodo = models.ForeignKey('s1207infoPerAntidePeriodo',
        related_name='%(class)s_s1207_infoperant_ideperiodo')
    def evento(self): return self.s1207_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1207_infoperant_ideestab_custom#

    class Meta:
        db_table = r's1207_infoperant_ideestab'       
        managed = True # s1207_infoperant_ideestab #
        unique_together = (
            #custom_unique_together_s1207_infoperant_ideestab#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperant_ideestab
            #index_together_s1207_infoperant_ideestab
        )
        permissions = (
            ("can_view_s1207_infoperant_ideestab", "Can view s1207_infoperant_ideestab"),
            #custom_permissions_s1207_infoperant_ideestab
        )
        ordering = ['s1207_infoperant_ideperiodo', 'tpinsc', 'nrinsc']



class s1207infoPerAntideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntideEstab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerAntidePeriodo(SoftDeletionModel):
    s1207_infoperant_ideadc = models.ForeignKey('s1207infoPerAntideADC',
        related_name='%(class)s_s1207_infoperant_ideadc')
    def evento(self): return self.s1207_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s1207_infoperant_ideperiodo_custom#

    class Meta:
        db_table = r's1207_infoperant_ideperiodo'       
        managed = True # s1207_infoperant_ideperiodo #
        unique_together = (
            #custom_unique_together_s1207_infoperant_ideperiodo#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperant_ideperiodo
            #index_together_s1207_infoperant_ideperiodo
        )
        permissions = (
            ("can_view_s1207_infoperant_ideperiodo", "Can view s1207_infoperant_ideperiodo"),
            #custom_permissions_s1207_infoperant_ideperiodo
        )
        ordering = ['s1207_infoperant_ideadc', 'perref']



class s1207infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntidePeriodo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerAntitensRemun(SoftDeletionModel):
    s1207_infoperant_ideestab = models.ForeignKey('s1207infoPerAntideEstab',
        related_name='%(class)s_s1207_infoperant_ideestab')
    def evento(self): return self.s1207_infoperant_ideestab.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideestab) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1207_infoperant_itensremun_custom#

    class Meta:
        db_table = r's1207_infoperant_itensremun'       
        managed = True # s1207_infoperant_itensremun #
        unique_together = (
            #custom_unique_together_s1207_infoperant_itensremun#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperant_itensremun
            #index_together_s1207_infoperant_itensremun
        )
        permissions = (
            ("can_view_s1207_infoperant_itensremun", "Can view s1207_infoperant_itensremun"),
            #custom_permissions_s1207_infoperant_itensremun
        )
        ordering = ['s1207_infoperant_ideestab', 'codrubr', 'idetabrubr', 'vrrubr']



class s1207infoPerAntitensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntitensRemun
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerApurideEstab(SoftDeletionModel):
    s1207_dmdev = models.ForeignKey('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1207_infoperapur_ideestab_custom#

    class Meta:
        db_table = r's1207_infoperapur_ideestab'       
        managed = True # s1207_infoperapur_ideestab #
        unique_together = (
            #custom_unique_together_s1207_infoperapur_ideestab#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperapur_ideestab
            #index_together_s1207_infoperapur_ideestab
        )
        permissions = (
            ("can_view_s1207_infoperapur_ideestab", "Can view s1207_infoperapur_ideestab"),
            #custom_permissions_s1207_infoperapur_ideestab
        )
        ordering = ['s1207_dmdev', 'tpinsc', 'nrinsc']



class s1207infoPerApurideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApurideEstab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207infoPerApuritensRemun(SoftDeletionModel):
    s1207_infoperapur_ideestab = models.ForeignKey('s1207infoPerApurideEstab',
        related_name='%(class)s_s1207_infoperapur_ideestab')
    def evento(self): return self.s1207_infoperapur_ideestab.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_infoperapur_ideestab) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1207_infoperapur_itensremun_custom#

    class Meta:
        db_table = r's1207_infoperapur_itensremun'       
        managed = True # s1207_infoperapur_itensremun #
        unique_together = (
            #custom_unique_together_s1207_infoperapur_itensremun#
            
        )
        index_together = (
            #custom_index_together_s1207_infoperapur_itensremun
            #index_together_s1207_infoperapur_itensremun
        )
        permissions = (
            ("can_view_s1207_infoperapur_itensremun", "Can view s1207_infoperapur_itensremun"),
            #custom_permissions_s1207_infoperapur_itensremun
        )
        ordering = ['s1207_infoperapur_ideestab', 'codrubr', 'idetabrubr', 'vrrubr']



class s1207infoPerApuritensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApuritensRemun
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207itens(SoftDeletionModel):
    s1207_dmdev = models.ForeignKey('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_dmdev) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1207_itens_custom#

    class Meta:
        db_table = r's1207_itens'       
        managed = True # s1207_itens #
        unique_together = (
            #custom_unique_together_s1207_itens#
            
        )
        index_together = (
            #custom_index_together_s1207_itens
            #index_together_s1207_itens
        )
        permissions = (
            ("can_view_s1207_itens", "Can view s1207_itens"),
            #custom_permissions_s1207_itens
        )
        ordering = ['s1207_dmdev', 'codrubr', 'idetabrubr', 'vrrubr']



class s1207itensSerializer(ModelSerializer):
    class Meta:
        model = s1207itens
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s1207procJudTrab(SoftDeletionModel):
    s1207_evtbenprrp = models.ForeignKey('esocial.s1207evtBenPrRP',
        related_name='%(class)s_s1207_evtbenprrp')
    def evento(self): return self.s1207_evtbenprrp.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1207_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1207_evtbenprrp) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s1207_procjudtrab_custom#

    class Meta:
        db_table = r's1207_procjudtrab'       
        managed = True # s1207_procjudtrab #
        unique_together = (
            #custom_unique_together_s1207_procjudtrab#
            
        )
        index_together = (
            #custom_index_together_s1207_procjudtrab
            #index_together_s1207_procjudtrab
        )
        permissions = (
            ("can_view_s1207_procjudtrab", "Can view s1207_procjudtrab"),
            #custom_permissions_s1207_procjudtrab
        )
        ordering = ['s1207_evtbenprrp', 'tptrib', 'nrprocjud']



class s1207procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s1207procJudTrab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
