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



CHOICES_S2299_INFOPERANT_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2299_INFOPERANT_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2299_INFOPERANT_TPACCONV = (
    ('A', u'A - Acordo Coletivo de Trabalho'),
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('C', u'C - Convenção Coletiva de Trabalho'),
    ('D', u'D - Sentença Normativa - Dissídio'),
    ('E', u'E - Conversão de Licença Saúde em Acidente de Trabalho'),
)

CHOICES_S2299_INFOPERANT_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOPERAPUR_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2299_INFOPERAPUR_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2299_INFOPERAPUR_TPDEP = (
    ('01', u'01 - Cônjuge'),
    ('02', u'02 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável'),
    ('03', u'03 - Filho(a) ou enteado(a)'),
    ('04', u'04 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau'),
    ('06', u'06 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'),
    ('07', u'07 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2° grau, do(a) qual detenha a guarda judicial'),
    ('09', u'09 - Pais, avós e bisavós'),
    ('10', u'10 - Menor pobre do qual detenha a guarda judicial'),
    ('11', u'11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'),
    ('12', u'12 - Ex-cônjuge'),
    ('99', u'99 - Agregado/Outros'),
)

CHOICES_S2299_INFOPERAPUR_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOTRABINTERM_INDMV = (
    (1, u'1 - O declarante aplica a alíquota de desconto do segurado sobre a remuneração por ele informada (o percentual da alíquota será obtido considerando a remuneração total do trabalhador)'),
    (2, u'2 - O declarante aplica a alíquota de desconto do segurado sobre a diferença entre o limite máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'),
    (3, u'3 - O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite máximo de salário de contribuição em outra(s) empresa(s)'),
)

CHOICES_S2299_INFOTRABINTERM_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOTRABINTERM_TPTRIB = (
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - IRRF'),
    (3, u'3 - FGTS'),
    (4, u'4 - Contribuição sindical'),
)

CHOICES_S2299_TPINSCSUC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

class s2299dmDev(SoftDeletionModel):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.idedmdev)
    #s2299_dmdev_custom#

    class Meta:
        # verbose_name = u'Identificação de cada um dos demonstrativos de valores devidos ao trabalhador antes das retenções de pensão alimentícia e IRRF'
        db_table = r's2299_dmdev'       
        managed = True # s2299_dmdev #
        unique_together = (
            #custom_unique_together_s2299_dmdev#
            
        )
        index_together = (
            #custom_index_together_s2299_dmdev
            #index_together_s2299_dmdev
        )
        permissions = (
            ("can_view_s2299_dmdev", "Can view s2299_dmdev"),
            #custom_permissions_s2299_dmdev
        )
        ordering = ['s2299_evtdeslig', 'idedmdev']



class s2299dmDevSerializer(ModelSerializer):
    class Meta:
        model = s2299dmDev
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntdetVerbas(SoftDeletionModel):
    s2299_infoperant_ideestablot = models.ForeignKey('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
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
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperant_detverbas_custom#

    class Meta:
        # verbose_name = u'Detalhamento das verbas rescisórias devidas ao trabalhador. Deve haver, pelo menos uma rubrica de folha, mesmo que o valor líquido a ser pago ao trabalhador seja 0 (zero) em função de descontos.'
        db_table = r's2299_infoperant_detverbas'       
        managed = True # s2299_infoperant_detverbas #
        unique_together = (
            #custom_unique_together_s2299_infoperant_detverbas#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_detverbas
            #index_together_s2299_infoperant_detverbas
        )
        permissions = (
            ("can_view_s2299_infoperant_detverbas", "Can view s2299_infoperant_detverbas"),
            #custom_permissions_s2299_infoperant_detverbas
        )
        ordering = ['s2299_infoperant_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr']



class s2299infoPerAntdetVerbasSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntdetVerbas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntideADC(SoftDeletionModel):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    dtacconv = models.DateField()
    tpacconv = models.CharField(choices=CHOICES_S2299_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField()
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.dtacconv) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dtefacconv) + ' - ' + unicode(self.dsc)
    #s2299_infoperant_ideadc_custom#

    class Meta:
        # verbose_name = u'Identificação do Instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores.'
        db_table = r's2299_infoperant_ideadc'       
        managed = True # s2299_infoperant_ideadc #
        unique_together = (
            #custom_unique_together_s2299_infoperant_ideadc#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_ideadc
            #index_together_s2299_infoperant_ideadc
        )
        permissions = (
            ("can_view_s2299_infoperant_ideadc", "Can view s2299_infoperant_ideadc"),
            #custom_permissions_s2299_infoperant_ideadc
        )
        ordering = ['s2299_dmdev', 'dtacconv', 'tpacconv', 'dtefacconv', 'dsc']



class s2299infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntideADC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntideEstabLot(SoftDeletionModel):
    s2299_infoperant_ideperiodo = models.ForeignKey('s2299infoPerAntidePeriodo',
        related_name='%(class)s_s2299_infoperant_ideperiodo')
    def evento(self): return self.s2299_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperant_ideestablot_custom#

    class Meta:
        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração. O estabelecimento identificado no registro pode ser: o número do CNPJ do estabelecimento da própria empresa (matriz/filial), o número da obra (...)'
        db_table = r's2299_infoperant_ideestablot'       
        managed = True # s2299_infoperant_ideestablot #
        unique_together = (
            #custom_unique_together_s2299_infoperant_ideestablot#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_ideestablot
            #index_together_s2299_infoperant_ideestablot
        )
        permissions = (
            ("can_view_s2299_infoperant_ideestablot", "Can view s2299_infoperant_ideestablot"),
            #custom_permissions_s2299_infoperant_ideestablot
        )
        ordering = ['s2299_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao']



class s2299infoPerAntideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntidePeriodo(SoftDeletionModel):
    s2299_infoperant_ideadc = models.ForeignKey('s2299infoPerAntideADC',
        related_name='%(class)s_s2299_infoperant_ideadc')
    def evento(self): return self.s2299_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s2299_infoperant_ideperiodo_custom#

    class Meta:
        # verbose_name = u'Período de validade das informações incluídas'
        db_table = r's2299_infoperant_ideperiodo'       
        managed = True # s2299_infoperant_ideperiodo #
        unique_together = (
            #custom_unique_together_s2299_infoperant_ideperiodo#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_ideperiodo
            #index_together_s2299_infoperant_ideperiodo
        )
        permissions = (
            ("can_view_s2299_infoperant_ideperiodo", "Can view s2299_infoperant_ideperiodo"),
            #custom_permissions_s2299_infoperant_ideperiodo
        )
        ordering = ['s2299_infoperant_ideadc', 'perref']



class s2299infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntidePeriodo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntinfoAgNocivo(SoftDeletionModel):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_GRAUEXP)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperant_infoagnocivo_custom#

    class Meta:
        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a coopera (...)'
        db_table = r's2299_infoperant_infoagnocivo'       
        managed = True # s2299_infoperant_infoagnocivo #
        unique_together = (
            #custom_unique_together_s2299_infoperant_infoagnocivo#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_infoagnocivo
            #index_together_s2299_infoperant_infoagnocivo
        )
        permissions = (
            ("can_view_s2299_infoperant_infoagnocivo", "Can view s2299_infoperant_infoagnocivo"),
            #custom_permissions_s2299_infoperant_infoagnocivo
        )
        ordering = ['s2299_infoperant_ideestablot', 'grauexp']



class s2299infoPerAntinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntinfoAgNocivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerAntinfoSimples(SoftDeletionModel):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperant_infosimples_custom#

    class Meta:
        # verbose_name = u'Informação relativa a empresas enquadradas no Regime de Tributação Simples'
        db_table = r's2299_infoperant_infosimples'       
        managed = True # s2299_infoperant_infosimples #
        unique_together = (
            #custom_unique_together_s2299_infoperant_infosimples#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperant_infosimples
            #index_together_s2299_infoperant_infosimples
        )
        permissions = (
            ("can_view_s2299_infoperant_infosimples", "Can view s2299_infoperant_infosimples"),
            #custom_permissions_s2299_infoperant_infosimples
        )
        ordering = ['s2299_infoperant_ideestablot', 'indsimples']



class s2299infoPerAntinfoSimplesSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntinfoSimples
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurdetOper(SoftDeletionModel):
    s2299_infoperapur_ideestablot = models.ForeignKey('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s2299_infoperapur_detoper_custom#

    class Meta:
        # verbose_name = u'Detalhamento dos valores pagos a Operadoras de Planos de Saúde.'
        db_table = r's2299_infoperapur_detoper'       
        managed = True # s2299_infoperapur_detoper #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_detoper#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_detoper
            #index_together_s2299_infoperapur_detoper
        )
        permissions = (
            ("can_view_s2299_infoperapur_detoper", "Can view s2299_infoperapur_detoper"),
            #custom_permissions_s2299_infoperapur_detoper
        )
        ordering = ['s2299_infoperapur_ideestablot', 'cnpjoper', 'regans', 'vrpgtit']



class s2299infoPerApurdetOperSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetOper
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurdetPlano(SoftDeletionModel):
    s2299_infoperapur_detoper = models.ForeignKey('s2299infoPerApurdetOper',
        related_name='%(class)s_s2299_infoperapur_detoper')
    def evento(self): return self.s2299_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S2299_INFOPERAPUR_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s2299_infoperapur_detplano_custom#

    class Meta:
        # verbose_name = u'Informações do dependente do plano privado de saúde.'
        db_table = r's2299_infoperapur_detplano'       
        managed = True # s2299_infoperapur_detplano #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_detplano#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_detplano
            #index_together_s2299_infoperapur_detplano
        )
        permissions = (
            ("can_view_s2299_infoperapur_detplano", "Can view s2299_infoperapur_detplano"),
            #custom_permissions_s2299_infoperapur_detplano
        )
        ordering = ['s2299_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep']



class s2299infoPerApurdetPlanoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetPlano
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurdetVerbas(SoftDeletionModel):
    s2299_infoperapur_ideestablot = models.ForeignKey('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
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
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperapur_detverbas_custom#

    class Meta:
        # verbose_name = u'Detalhamento das verbas rescisórias devidas ao trabalhador. Deve haver, pelo menos uma rubrica de folha, mesmo que o valor líquido a ser pago ao trabalhador seja 0 (zero) em função de descontos.'
        db_table = r's2299_infoperapur_detverbas'       
        managed = True # s2299_infoperapur_detverbas #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_detverbas#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_detverbas
            #index_together_s2299_infoperapur_detverbas
        )
        permissions = (
            ("can_view_s2299_infoperapur_detverbas", "Can view s2299_infoperapur_detverbas"),
            #custom_permissions_s2299_infoperapur_detverbas
        )
        ordering = ['s2299_infoperapur_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr']



class s2299infoPerApurdetVerbasSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetVerbas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurideEstabLot(SoftDeletionModel):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperapur_ideestablot_custom#

    class Meta:
        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração. O estabelecimento identificado no registro pode ser: o número do CNPJ do estabelecimento da própria empresa (matriz/filial), o número da obra (...)'
        db_table = r's2299_infoperapur_ideestablot'       
        managed = True # s2299_infoperapur_ideestablot #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_ideestablot#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_ideestablot
            #index_together_s2299_infoperapur_ideestablot
        )
        permissions = (
            ("can_view_s2299_infoperapur_ideestablot", "Can view s2299_infoperapur_ideestablot"),
            #custom_permissions_s2299_infoperapur_ideestablot
        )
        ordering = ['s2299_dmdev', 'tpinsc', 'nrinsc', 'codlotacao']



class s2299infoPerApurideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurinfoAgNocivo(SoftDeletionModel):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_GRAUEXP)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperapur_infoagnocivo_custom#

    class Meta:
        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a coopera (...)'
        db_table = r's2299_infoperapur_infoagnocivo'       
        managed = True # s2299_infoperapur_infoagnocivo #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_infoagnocivo#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_infoagnocivo
            #index_together_s2299_infoperapur_infoagnocivo
        )
        permissions = (
            ("can_view_s2299_infoperapur_infoagnocivo", "Can view s2299_infoperapur_infoagnocivo"),
            #custom_permissions_s2299_infoperapur_infoagnocivo
        )
        ordering = ['s2299_infoperapur_ideestablot', 'grauexp']



class s2299infoPerApurinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurinfoAgNocivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoPerApurinfoSimples(SoftDeletionModel):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperapur_infosimples_custom#

    class Meta:
        # verbose_name = u'Informação relativa a empresas enquadradas no Regime de Tributação Simples'
        db_table = r's2299_infoperapur_infosimples'       
        managed = True # s2299_infoperapur_infosimples #
        unique_together = (
            #custom_unique_together_s2299_infoperapur_infosimples#
            
        )
        index_together = (
            #custom_index_together_s2299_infoperapur_infosimples
            #index_together_s2299_infoperapur_infosimples
        )
        permissions = (
            ("can_view_s2299_infoperapur_infosimples", "Can view s2299_infoperapur_infosimples"),
            #custom_permissions_s2299_infoperapur_infosimples
        )
        ordering = ['s2299_infoperapur_ideestablot', 'indsimples']



class s2299infoPerApurinfoSimplesSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurinfoSimples
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabInterm(SoftDeletionModel):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.codconv)
    #s2299_infotrabinterm_custom#

    class Meta:
        # verbose_name = u'Informações da(s) convocação(ões) de trabalho intermitente'
        db_table = r's2299_infotrabinterm'       
        managed = True # s2299_infotrabinterm #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm
            #index_together_s2299_infotrabinterm
        )
        permissions = (
            ("can_view_s2299_infotrabinterm", "Can view s2299_infotrabinterm"),
            #custom_permissions_s2299_infotrabinterm
        )
        ordering = ['s2299_dmdev', 'codconv']



class s2299infoTrabIntermSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabInterm
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabIntermconsigFGTS(SoftDeletionModel):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    insconsig = models.CharField(max_length=5)
    nrcontr = models.CharField(max_length=40)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.insconsig) + ' - ' + unicode(self.nrcontr)
    #s2299_infotrabinterm_consigfgts_custom#

    class Meta:
        # verbose_name = u'Informações sobre operação de crédito consignado com garantia de FGTS'
        db_table = r's2299_infotrabinterm_consigfgts'       
        managed = True # s2299_infotrabinterm_consigfgts #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_consigfgts#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_consigfgts
            #index_together_s2299_infotrabinterm_consigfgts
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_consigfgts", "Can view s2299_infotrabinterm_consigfgts"),
            #custom_permissions_s2299_infotrabinterm_consigfgts
        )
        ordering = ['s2299_evtdeslig', 'insconsig', 'nrcontr']



class s2299infoTrabIntermconsigFGTSSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermconsigFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabInterminfoMV(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    indmv = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_INDMV)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.indmv)
    #s2299_infotrabinterm_infomv_custom#

    class Meta:
        # verbose_name = u'Registro preenchido exclusivamente em caso de trabalhador que possua outros vínculos/atividades para definição do limite do salário-de-contribuição e da alíquota a ser aplicada no desconto da contribuição previdenciária.'
        db_table = r's2299_infotrabinterm_infomv'       
        managed = True # s2299_infotrabinterm_infomv #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_infomv#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_infomv
            #index_together_s2299_infotrabinterm_infomv
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_infomv", "Can view s2299_infotrabinterm_infomv"),
            #custom_permissions_s2299_infotrabinterm_infomv
        )
        ordering = ['s2299_evtdeslig', 'indmv']



class s2299infoTrabInterminfoMVSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabInterminfoMV
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabIntermprocCS(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.nrprocjud)
    #s2299_infotrabinterm_proccs_custom#

    class Meta:
        # verbose_name = u'Informação sobre processo judicial que suspende a exigibilidade da Contribuição Social Rescisória'
        db_table = r's2299_infotrabinterm_proccs'       
        managed = True # s2299_infotrabinterm_proccs #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_proccs#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_proccs
            #index_together_s2299_infotrabinterm_proccs
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_proccs", "Can view s2299_infotrabinterm_proccs"),
            #custom_permissions_s2299_infotrabinterm_proccs
        )
        ordering = ['s2299_evtdeslig', 'nrprocjud']



class s2299infoTrabIntermprocCSSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermprocCS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabIntermprocJudTrab(SoftDeletionModel):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPTRIB)
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
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s2299_infotrabinterm_procjudtrab_custom#

    class Meta:
        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's2299_infotrabinterm_procjudtrab'       
        managed = True # s2299_infotrabinterm_procjudtrab #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_procjudtrab#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_procjudtrab
            #index_together_s2299_infotrabinterm_procjudtrab
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_procjudtrab", "Can view s2299_infotrabinterm_procjudtrab"),
            #custom_permissions_s2299_infotrabinterm_procjudtrab
        )
        ordering = ['s2299_evtdeslig', 'tptrib', 'nrprocjud']



class s2299infoTrabIntermprocJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermprocJudTrab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabIntermquarentena(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    dtfimquar = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.dtfimquar)
    #s2299_infotrabinterm_quarentena_custom#

    class Meta:
        # verbose_name = u'Informações sobre a "quarentena" remunerada de trabalhador desligado. O registro deve ser preenchido apenas no caso do trabalhador que recebe remuneração após o desligamento por estar impossibilitado de exercer atividade remunerada.'
        db_table = r's2299_infotrabinterm_quarentena'       
        managed = True # s2299_infotrabinterm_quarentena #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_quarentena#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_quarentena
            #index_together_s2299_infotrabinterm_quarentena
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_quarentena", "Can view s2299_infotrabinterm_quarentena"),
            #custom_permissions_s2299_infotrabinterm_quarentena
        )
        ordering = ['s2299_evtdeslig', 'dtfimquar']



class s2299infoTrabIntermquarentenaSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermquarentena
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299infoTrabIntermremunOutrEmpr(SoftDeletionModel):
    s2299_infotrabinterm_infomv = models.ForeignKey('s2299infoTrabInterminfoMV',
        related_name='%(class)s_s2299_infotrabinterm_infomv')
    def evento(self): return self.s2299_infotrabinterm_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.TextField(max_length=3)
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_infotrabinterm_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s2299_infotrabinterm_remunoutrempr_custom#

    class Meta:
        # verbose_name = u'Informações relativas ao trabalhador que possui vínculo empregatício com outra(s) empresa(s) e/ou que exerce outras atividades como contribuinte individual, detalhando as empresas que efetuaram (ou efetuarão) desconto da contribuição, ou ainda valores reco (...)'
        db_table = r's2299_infotrabinterm_remunoutrempr'       
        managed = True # s2299_infotrabinterm_remunoutrempr #
        unique_together = (
            #custom_unique_together_s2299_infotrabinterm_remunoutrempr#
            
        )
        index_together = (
            #custom_index_together_s2299_infotrabinterm_remunoutrempr
            #index_together_s2299_infotrabinterm_remunoutrempr
        )
        permissions = (
            ("can_view_s2299_infotrabinterm_remunoutrempr", "Can view s2299_infotrabinterm_remunoutrempr"),
            #custom_permissions_s2299_infotrabinterm_remunoutrempr
        )
        ordering = ['s2299_infotrabinterm_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']



class s2299infoTrabIntermremunOutrEmprSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermremunOutrEmpr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299mudancaCPF(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    novocpf = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.novocpf)
    #s2299_mudancacpf_custom#

    class Meta:
        # verbose_name = u'Informações de mudança de CPF do trabalhador.'
        db_table = r's2299_mudancacpf'       
        managed = True # s2299_mudancacpf #
        unique_together = (
            #custom_unique_together_s2299_mudancacpf#
            
        )
        index_together = (
            #custom_index_together_s2299_mudancacpf
            #index_together_s2299_mudancacpf
        )
        permissions = (
            ("can_view_s2299_mudancacpf", "Can view s2299_mudancacpf"),
            #custom_permissions_s2299_mudancacpf
        )
        ordering = ['s2299_evtdeslig', 'novocpf']



class s2299mudancaCPFSerializer(ModelSerializer):
    class Meta:
        model = s2299mudancaCPF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299observacoes(SoftDeletionModel):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.observacao)
    #s2299_observacoes_custom#

    class Meta:
        # verbose_name = u'Observações do contrato de trabalho'
        db_table = r's2299_observacoes'       
        managed = True # s2299_observacoes #
        unique_together = (
            #custom_unique_together_s2299_observacoes#
            
        )
        index_together = (
            #custom_index_together_s2299_observacoes
            #index_together_s2299_observacoes
        )
        permissions = (
            ("can_view_s2299_observacoes", "Can view s2299_observacoes"),
            #custom_permissions_s2299_observacoes
        )
        ordering = ['s2299_evtdeslig', 'observacao']



class s2299observacoesSerializer(ModelSerializer):
    class Meta:
        model = s2299observacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299sucessaoVinc(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    tpinscsuc = models.IntegerField(choices=CHOICES_S2299_TPINSCSUC)
    cnpjsucessora = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.tpinscsuc) + ' - ' + unicode(self.cnpjsucessora)
    #s2299_sucessaovinc_custom#

    class Meta:
        # verbose_name = u'Grupo de informações da sucessão de vínculo trabalhista/estatutário'
        db_table = r's2299_sucessaovinc'       
        managed = True # s2299_sucessaovinc #
        unique_together = (
            #custom_unique_together_s2299_sucessaovinc#
            
        )
        index_together = (
            #custom_index_together_s2299_sucessaovinc
            #index_together_s2299_sucessaovinc
        )
        permissions = (
            ("can_view_s2299_sucessaovinc", "Can view s2299_sucessaovinc"),
            #custom_permissions_s2299_sucessaovinc
        )
        ordering = ['s2299_evtdeslig', 'tpinscsuc', 'cnpjsucessora']



class s2299sucessaoVincSerializer(ModelSerializer):
    class Meta:
        model = s2299sucessaoVinc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2299transfTit(SoftDeletionModel):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    cpfsubstituto = models.CharField(max_length=11)
    dtnascto = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.cpfsubstituto) + ' - ' + unicode(self.dtnascto)
    #s2299_transftit_custom#

    class Meta:
        # verbose_name = u'Transferência de titularidade do empregado doméstico para outro representante da mesma unidade familiar'
        db_table = r's2299_transftit'       
        managed = True # s2299_transftit #
        unique_together = (
            #custom_unique_together_s2299_transftit#
            
        )
        index_together = (
            #custom_index_together_s2299_transftit
            #index_together_s2299_transftit
        )
        permissions = (
            ("can_view_s2299_transftit", "Can view s2299_transftit"),
            #custom_permissions_s2299_transftit
        )
        ordering = ['s2299_evtdeslig', 'cpfsubstituto', 'dtnascto']



class s2299transfTitSerializer(ModelSerializer):
    class Meta:
        model = s2299transfTit
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
