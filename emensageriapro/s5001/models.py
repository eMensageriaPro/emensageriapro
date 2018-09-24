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



CHOICES_S5001_IND13 = (
    (0, u'0 - Mensal'),
    (1, u'1 - 13° salário - {codIncCP} = [12, 14, 16, 22, 26, 32, 92, 94]'),
)

CHOICES_S5001_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S5001_TPCR = (
    (108201, u'108201 - Contribuição previdenciária (CP) descontada do segurado empregado/avulso, alíquotas 8%, 9% ou 11%'),
    (108202, u'108202 - CP descontada do segurado empregado rural curto prazo, alíquota de 8%, lei 11718/2008'),
    (108203, u'108203 - CP descontada do segurado empregado doméstico ou segurado especial, alíquota de 8%, 9% ou 11%'),
    (108204, u'108204 - CP descontada do segurado especial curto prazo, alíquota de 8%, lei 11718/2008'),
    (108221, u'108221 - CP descontada do segurado empregado/avulso 13° salário, alíquotas 8%, 9% ou 11% (codIncCP = [12, 16])'),
    (108222, u'108222 - CP descontada do segurado empregado rural curto prazo 13° salário, alíquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'),
    (108223, u'108223 - CP descontada do segurado empregado doméstico ou segurado especial 13° salário, alíquota de 8%, 9% ou 11%(codIncCP = [12, 16])'),
    (108224, u'108224 - CP descontada do segurado especial curto prazo 13° salário, alíquota de 8%, lei 11718/2008 (codIncCP = [12, 16])'),
    (109901, u'109901 - CP descontada do contribuinte individual, alíquota de 11%'),
    (109902, u'109902 - CP descontada do contribuinte individual, alíquota de 20%'),
    (121802, u'121802 - Contribuição ao SEST, descontada do transportador autônomo, à alíquota de 1,5%'),
    (122102, u'122102 - Contribuição ao SENAT, descontada do transportador autônomo, à alíquota de 1,0%'),
)

CHOICES_S5001_TPINSC = (
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S5001_TPVALOR = (
    (11, u'11 - Base de cálculo da Contribuição Previdenciária normal'),
    (12, u'12 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição'),
    (13, u'13 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição'),
    (14, u'14 - Base de cálculo da Contribuição Previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição'),
    (15, u'15 - Base de cálculo da contribuição previdenciária adicional normal - exclusiva do empregador'),
    (16, u'16 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 15 anos de contribuição - exclusiva do empregador'),
    (17, u'17 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 20 anos de contribuição - exclusiva do empregador'),
    (18, u'18 - Base de cálculo da contribuição previdenciária adicional para o financiamento dos benefícios de aposentadoria especial após 25 anos de contribuição - exclusiva do empregador'),
    (19, u'19 - Base de cálculo da contribuição previdenciária exclusiva do empregado'),
    (21, u'21 - Valor total descontado do trabalhador para recolhimento à Previdência Social'),
    (22, u'22 - Valor descontado do trabalhador para recolhimento ao Sest'),
    (23, u'23 - Valor descontado do trabalhador para recolhimento ao Senat'),
    (31, u'31 - Valor pago ao trabalhador a título de salário-família'),
    (32, u'32 - Valor pago ao trabalhador a título de salário-maternidade'),
    (91, u'91 - Incidência suspensa em decorrência de decisão judicial - Base de cálculo (BC) da Contribuição Previdenciária (CP) Normal'),
    (92, u'92 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 15 anos de trabalho'),
    (93, u'93 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 20 anos de trabalho'),
    (94, u'94 - Incid. suspensa em decorrência de decisão judicial - BC CP Aposentadoria Especial aos 25 anos de trabalho'),
)

class s5001calcTerc(models.Model):
    s5001_infocategincid = models.ForeignKey('s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid')
    tpcr = models.IntegerField(choices=CHOICES_S5001_TPCR)
    vrcssegterc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescterc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_infocategincid) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcssegterc) + ' - ' + unicode(self.vrdescterc)
    #s5001_calcterc_custom#
    #s5001_calcterc_custom#
    class Meta:
        db_table = r's5001_calcterc'
        managed = True
        ordering = ['s5001_infocategincid', 'tpcr', 'vrcssegterc', 'vrdescterc']



class s5001calcTercSerializer(ModelSerializer):
    class Meta:
        model = s5001calcTerc
        fields = '__all__'
            

class s5001ideEstabLot(models.Model):
    s5001_infocp = models.ForeignKey('s5001infoCp',
        related_name='%(class)s_s5001_infocp')
    tpinsc = models.IntegerField(choices=CHOICES_S5001_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_infocp) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s5001_ideestablot_custom#
    #s5001_ideestablot_custom#
    class Meta:
        db_table = r's5001_ideestablot'
        managed = True
        ordering = ['s5001_infocp', 'tpinsc', 'nrinsc', 'codlotacao']



class s5001ideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s5001ideEstabLot
        fields = '__all__'
            

class s5001infoBaseCS(models.Model):
    s5001_infocategincid = models.ForeignKey('s5001infoCategIncid',
        related_name='%(class)s_s5001_infocategincid')
    ind13 = models.IntegerField(choices=CHOICES_S5001_IND13)
    tpvalor = models.IntegerField(choices=CHOICES_S5001_TPVALOR)
    valor = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_infocategincid) + ' - ' + unicode(self.ind13) + ' - ' + unicode(self.tpvalor) + ' - ' + unicode(self.valor)
    #s5001_infobasecs_custom#
    #s5001_infobasecs_custom#
    class Meta:
        db_table = r's5001_infobasecs'
        managed = True
        ordering = ['s5001_infocategincid', 'ind13', 'tpvalor', 'valor']



class s5001infoBaseCSSerializer(ModelSerializer):
    class Meta:
        model = s5001infoBaseCS
        fields = '__all__'
            

class s5001infoCategIncid(models.Model):
    s5001_ideestablot = models.ForeignKey('s5001ideEstabLot',
        related_name='%(class)s_s5001_ideestablot')
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    indsimples = models.IntegerField(choices=CHOICES_S5001_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_ideestablot) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.indsimples)
    #s5001_infocategincid_custom#
    #s5001_infocategincid_custom#
    class Meta:
        db_table = r's5001_infocategincid'
        managed = True
        ordering = ['s5001_ideestablot', 'matricula', 'codcateg', 'indsimples']



class s5001infoCategIncidSerializer(ModelSerializer):
    class Meta:
        model = s5001infoCategIncid
        fields = '__all__'
            

class s5001infoCp(models.Model):
    s5001_evtbasestrab = models.OneToOneField('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab)
    #s5001_infocp_custom#
    #s5001_infocp_custom#
    class Meta:
        db_table = r's5001_infocp'
        managed = True
        ordering = ['s5001_evtbasestrab']



class s5001infoCpSerializer(ModelSerializer):
    class Meta:
        model = s5001infoCp
        fields = '__all__'
            

class s5001infoCpCalc(models.Model):
    s5001_evtbasestrab = models.ForeignKey('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    tpcr = models.IntegerField(choices=CHOICES_S5001_TPCR)
    vrcpseg = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdescseg = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcpseg) + ' - ' + unicode(self.vrdescseg)
    #s5001_infocpcalc_custom#
    #s5001_infocpcalc_custom#
    class Meta:
        db_table = r's5001_infocpcalc'
        managed = True
        ordering = ['s5001_evtbasestrab', 'tpcr', 'vrcpseg', 'vrdescseg']



class s5001infoCpCalcSerializer(ModelSerializer):
    class Meta:
        model = s5001infoCpCalc
        fields = '__all__'
            

class s5001procJudTrab(models.Model):
    s5001_evtbasestrab = models.ForeignKey('esocial.s5001evtBasesTrab',
        related_name='%(class)s_s5001_evtbasestrab')
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5001_evtbasestrab) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s5001_procjudtrab_custom#
    #s5001_procjudtrab_custom#
    class Meta:
        db_table = r's5001_procjudtrab'
        managed = True
        ordering = ['s5001_evtbasestrab', 'nrprocjud', 'codsusp']



class s5001procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s5001procJudTrab
        fields = '__all__'
            

#VIEWS_MODELS
