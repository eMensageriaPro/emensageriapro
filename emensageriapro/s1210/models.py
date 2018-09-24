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



CHOICES_S1210_DETPGTOANT_TPBCIRRF = (
    ('11', u'11 - Remuneração Mensal'),
    ('12', u'12 - 13o Salário'),
    ('13', u'13 - Férias'),
    ('14', u'14 - PLR'),
    ('15', u'15 - Rendimentos Recebidos Acumuladamente - RRA'),
    ('31', u'31 - Retenções do IRRF efetuadas sobre: Remuneração mensal'),
    ('32', u'32 - Retenções do IRRF efetuadas sobre: 13o Salário'),
    ('33', u'33 - Retenções do IRRF efetuadas sobre: Férias'),
    ('34', u'34 - Retenções do IRRF efetuadas sobre: PLR'),
    ('35', u'35 - Retenções do IRRF efetuadas sobre: RRA'),
    ('41', u'41 - Deduções da base de cálculo do IRRF: Previdência Social Oficial - PSO - Remuner. Mensal'),
    ('42', u'42 - Deduções da base de cálculo do IRRF: PSO - 13° salário'),
    ('43', u'43 - Deduções da base de cálculo do IRRF: PSO - Férias'),
    ('44', u'44 - Deduções da base de cálculo do IRRF: PSO - RRA'),
    ('46', u'46 - Deduções da base de cálculo do IRRF: Previdência Privada - salário mensal'),
    ('47', u'47 - Deduções da base de cálculo do IRRF: Previdência Privada - 13° salário'),
    ('51', u'51 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Remuneração Mensal'),
    ('52', u'52 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - 13° salário'),
    ('53', u'53 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Férias'),
    ('54', u'54 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - PLR'),
    ('55', u'55 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - RRA'),
    ('61', u'61 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração Mensal'),
    ('62', u'62 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13° salário'),
    ('63', u'63 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - Remuneração Mensal'),
    ('64', u'64 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - 13° salário'),
    ('70', u'70 - Isenções do IRRF: Parcela Isenta 65 anos - Remuneração Mensal'),
    ('71', u'71 - Isenções do IRRF: Parcela Isenta 65 anos - 13° salário'),
    ('72', u'72 - Isenções do IRRF: Diárias'),
    ('73', u'73 - Isenções do IRRF: Ajuda de Custo'),
    ('74', u'74 - Isenções do IRRF: Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho'),
    ('75', u'75 - Isenções do IRRF: Abono pecuniário'),
    ('76', u'76 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal'),
    ('77', u'77 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário'),
    ('78', u'78 - Isenções do IRRF: Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    ('79', u'79 - Isenções do IRRF: Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)'),
    ('81', u'81 - Demandas Judiciais: Depósito Judicial'),
    ('82', u'82 - Demandas Judiciais: Compensação Judicial do ano calendário'),
    ('83', u'83 - Demandas Judiciais: Compensação Judicial de anos anteriores'),
    ('91', u'91 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Remuneração Mensal'),
    ('92', u'92 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: 13o Salário'),
    ('93', u'93 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Férias'),
    ('94', u'94 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: PLR'),
    ('95', u'95 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: RRA'),
)

CHOICES_S1210_DETPGTOBENPR_INDPGTOTT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_DETPGTOFL_INDPGTOTT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_IDEPGTOEXT_INDNIF = (
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF'),
)

CHOICES_S1210_INDRESBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_TPPGTO = (
    (1, u'1 - Pagamento de remuneração, conforme apurado em {dmDev} do S-1200'),
    (2, u'2 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2299'),
    (3, u'3 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2399'),
    (5, u'5 - Pagamento de remuneração conforme apurado em {dmDev} do S-1202'),
    (6, u'6 - Pagamento de Benefícios Previdenciários, conforme apurado em {dmDev} do S-1207'),
    (7, u'7 - Recibo de férias'),
    (9, u'9 - Pagamento relativo a competências anteriores ao início de obrigatoriedade dos eventos periódicos para o contribuinte'),
)

class s1210deps(models.Model):
    s1210_evtpgtos = models.OneToOneField('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos')
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.vrdeddep)
    #s1210_deps_custom#
    #s1210_deps_custom#
    class Meta:
        db_table = r's1210_deps'
        managed = True
        ordering = ['s1210_evtpgtos', 'vrdeddep']



class s1210depsSerializer(ModelSerializer):
    class Meta:
        model = s1210deps
        fields = '__all__'
            

class s1210detPgtoAnt(models.Model):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg)
    #s1210_detpgtoant_custom#
    #s1210_detpgtoant_custom#
    class Meta:
        db_table = r's1210_detpgtoant'
        managed = True
        ordering = ['s1210_infopgto', 'codcateg']



class s1210detPgtoAntSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoAnt
        fields = '__all__'
            

class s1210detPgtoAntinfoPgtoAnt(models.Model):
    s1210_detpgtoant = models.ForeignKey('s1210detPgtoAnt',
        related_name='%(class)s_s1210_detpgtoant')
    tpbcirrf = models.CharField(choices=CHOICES_S1210_DETPGTOANT_TPBCIRRF, max_length=2)
    vrbcirrf = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtoant) + ' - ' + unicode(self.tpbcirrf) + ' - ' + unicode(self.vrbcirrf)
    #s1210_detpgtoant_infopgtoant_custom#
    #s1210_detpgtoant_infopgtoant_custom#
    class Meta:
        db_table = r's1210_detpgtoant_infopgtoant'
        managed = True
        ordering = ['s1210_detpgtoant', 'tpbcirrf', 'vrbcirrf']



class s1210detPgtoAntinfoPgtoAntSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoAntinfoPgtoAnt
        fields = '__all__'
            

class s1210detPgtoBenPr(models.Model):
    s1210_infopgto = models.OneToOneField('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    perref = models.CharField(max_length=7)
    idedmdev = models.CharField(max_length=30)
    indpgtott = models.CharField(choices=CHOICES_S1210_DETPGTOBENPR_INDPGTOTT, max_length=1)
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.perref) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq)
    #s1210_detpgtobenpr_custom#
    #s1210_detpgtobenpr_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr'
        managed = True
        ordering = ['s1210_infopgto', 'perref', 'idedmdev', 'indpgtott', 'vrliq']



class s1210detPgtoBenPrSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPr
        fields = '__all__'
            

class s1210detPgtoBenPrinfoPgtoParc(models.Model):
    s1210_detpgtobenpr = models.ForeignKey('s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr')
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtobenpr_infopgtoparc_custom#
    #s1210_detpgtobenpr_infopgtoparc_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr_infopgtoparc'
        managed = True
        ordering = ['s1210_detpgtobenpr', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1210detPgtoBenPrinfoPgtoParcSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPrinfoPgtoParc
        fields = '__all__'
            

class s1210detPgtoBenPrretPgtoTot(models.Model):
    s1210_detpgtobenpr = models.ForeignKey('s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr')
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtobenpr_retpgtotot_custom#
    #s1210_detpgtobenpr_retpgtotot_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr_retpgtotot'
        managed = True
        ordering = ['s1210_detpgtobenpr', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1210detPgtoBenPrretPgtoTotSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPrretPgtoTot
        fields = '__all__'
            

class s1210detPgtoFer(models.Model):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    codcateg = models.TextField(max_length=3)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    dtinigoz = models.DateField()
    qtdias = models.IntegerField()
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.dtinigoz) + ' - ' + unicode(self.qtdias) + ' - ' + unicode(self.vrliq)
    #s1210_detpgtofer_custom#
    #s1210_detpgtofer_custom#
    class Meta:
        db_table = r's1210_detpgtofer'
        managed = True
        ordering = ['s1210_infopgto', 'codcateg', 'matricula', 'dtinigoz', 'qtdias', 'vrliq']



class s1210detPgtoFerSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFer
        fields = '__all__'
            

class s1210detPgtoFerdetRubrFer(models.Model):
    s1210_detpgtofer = models.ForeignKey('s1210detPgtoFer',
        related_name='%(class)s_s1210_detpgtofer')
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofer) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofer_detrubrfer_custom#
    #s1210_detpgtofer_detrubrfer_custom#
    class Meta:
        db_table = r's1210_detpgtofer_detrubrfer'
        managed = True
        ordering = ['s1210_detpgtofer', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1210detPgtoFerdetRubrFerSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFerdetRubrFer
        fields = '__all__'
            

class s1210detPgtoFerpenAlim(models.Model):
    s1210_detpgtofer_detrubrfer = models.ForeignKey('s1210detPgtoFerdetRubrFer',
        related_name='%(class)s_s1210_detpgtofer_detrubrfer')
    cpfbenef = models.CharField(max_length=11)
    dtnasctobenef = models.DateField(blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofer_detrubrfer) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.dtnasctobenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)
    #s1210_detpgtofer_penalim_custom#
    #s1210_detpgtofer_penalim_custom#
    class Meta:
        db_table = r's1210_detpgtofer_penalim'
        managed = True
        ordering = ['s1210_detpgtofer_detrubrfer', 'cpfbenef', 'dtnasctobenef', 'nmbenefic', 'vlrpensao']



class s1210detPgtoFerpenAlimSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFerpenAlim
        fields = '__all__'
            

class s1210detPgtoFl(models.Model):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    perref = models.CharField(max_length=7, blank=True, null=True)
    idedmdev = models.CharField(max_length=30)
    indpgtott = models.CharField(choices=CHOICES_S1210_DETPGTOFL_INDPGTOTT, max_length=1)
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    nrrecarq = models.CharField(max_length=40, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.perref) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq) + ' - ' + unicode(self.nrrecarq)
    #s1210_detpgtofl_custom#
    #s1210_detpgtofl_custom#
    class Meta:
        db_table = r's1210_detpgtofl'
        managed = True
        ordering = ['s1210_infopgto', 'perref', 'idedmdev', 'indpgtott', 'vrliq', 'nrrecarq']



class s1210detPgtoFlSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFl
        fields = '__all__'
            

class s1210detPgtoFlinfoPgtoParc(models.Model):
    s1210_detpgtofl = models.ForeignKey('s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl')
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofl_infopgtoparc_custom#
    #s1210_detpgtofl_infopgtoparc_custom#
    class Meta:
        db_table = r's1210_detpgtofl_infopgtoparc'
        managed = True
        ordering = ['s1210_detpgtofl', 'matricula', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1210detPgtoFlinfoPgtoParcSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlinfoPgtoParc
        fields = '__all__'
            

class s1210detPgtoFlpenAlim(models.Model):
    s1210_detpgtofl_retpgtotot = models.ForeignKey('s1210detPgtoFlretPgtoTot',
        related_name='%(class)s_s1210_detpgtofl_retpgtotot')
    cpfbenef = models.CharField(max_length=11)
    dtnasctobenef = models.DateField(blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl_retpgtotot) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.dtnasctobenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)
    #s1210_detpgtofl_penalim_custom#
    #s1210_detpgtofl_penalim_custom#
    class Meta:
        db_table = r's1210_detpgtofl_penalim'
        managed = True
        ordering = ['s1210_detpgtofl_retpgtotot', 'cpfbenef', 'dtnasctobenef', 'nmbenefic', 'vlrpensao']



class s1210detPgtoFlpenAlimSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlpenAlim
        fields = '__all__'
            

class s1210detPgtoFlretPgtoTot(models.Model):
    s1210_detpgtofl = models.ForeignKey('s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl')
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofl_retpgtotot_custom#
    #s1210_detpgtofl_retpgtotot_custom#
    class Meta:
        db_table = r's1210_detpgtofl_retpgtotot'
        managed = True
        ordering = ['s1210_detpgtofl', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1210detPgtoFlretPgtoTotSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlretPgtoTot
        fields = '__all__'
            

class s1210idePgtoExt(models.Model):
    s1210_infopgto = models.OneToOneField('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    codpais = models.TextField(max_length=3)
    indnif = models.IntegerField(choices=CHOICES_S1210_IDEPGTOEXT_INDNIF)
    nifbenef = models.CharField(max_length=20, blank=True, null=True)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    complem = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codpais) + ' - ' + unicode(self.indnif) + ' - ' + unicode(self.nifbenef) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complem) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s1210_idepgtoext_custom#
    #s1210_idepgtoext_custom#
    class Meta:
        db_table = r's1210_idepgtoext'
        managed = True
        ordering = ['s1210_infopgto', 'codpais', 'indnif', 'nifbenef', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'nmcid', 'codpostal']



class s1210idePgtoExtSerializer(ModelSerializer):
    class Meta:
        model = s1210idePgtoExt
        fields = '__all__'
            

class s1210infoPgto(models.Model):
    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos')
    dtpgto = models.DateField()
    tppgto = models.IntegerField(choices=CHOICES_S1210_TPPGTO)
    indresbr = models.CharField(choices=CHOICES_S1210_INDRESBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.dtpgto) + ' - ' + unicode(self.tppgto) + ' - ' + unicode(self.indresbr)
    #s1210_infopgto_custom#
    #s1210_infopgto_custom#
    class Meta:
        db_table = r's1210_infopgto'
        managed = True
        ordering = ['s1210_evtpgtos', 'dtpgto', 'tppgto', 'indresbr']



class s1210infoPgtoSerializer(ModelSerializer):
    class Meta:
        model = s1210infoPgto
        fields = '__all__'
            

#VIEWS_MODELS
