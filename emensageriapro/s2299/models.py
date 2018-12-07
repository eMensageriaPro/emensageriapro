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

class s2299dmDev(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.idedmdev)
    #s2299_dmdev_custom#
    #s2299_dmdev_custom#
    class Meta:
        db_table = r's2299_dmdev'
        managed = True
        ordering = ['s2299_evtdeslig', 'idedmdev']



class s2299dmDevSerializer(ModelSerializer):
    class Meta:
        model = s2299dmDev
        fields = '__all__'
            

class s2299infoPerAntdetVerbas(models.Model):
    s2299_infoperant_ideestablot = models.ForeignKey('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
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
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperant_detverbas_custom#
    #s2299_infoperant_detverbas_custom#
    class Meta:
        db_table = r's2299_infoperant_detverbas'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr']



class s2299infoPerAntdetVerbasSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntdetVerbas
        fields = '__all__'
            

class s2299infoPerAntideADC(models.Model):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    dtacconv = models.DateField()
    tpacconv = models.CharField(choices=CHOICES_S2299_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField()
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.dtacconv) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dtefacconv) + ' - ' + unicode(self.dsc)
    #s2299_infoperant_ideadc_custom#
    #s2299_infoperant_ideadc_custom#
    class Meta:
        db_table = r's2299_infoperant_ideadc'
        managed = True
        ordering = ['s2299_dmdev', 'dtacconv', 'tpacconv', 'dtefacconv', 'dsc']



class s2299infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntideADC
        fields = '__all__'
            

class s2299infoPerAntideEstabLot(models.Model):
    s2299_infoperant_ideperiodo = models.ForeignKey('s2299infoPerAntidePeriodo',
        related_name='%(class)s_s2299_infoperant_ideperiodo')
    def evento(self): return self.s2299_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_TPINSC)
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
        return unicode(self.s2299_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperant_ideestablot_custom#
    #s2299_infoperant_ideestablot_custom#
    class Meta:
        db_table = r's2299_infoperant_ideestablot'
        managed = True
        ordering = ['s2299_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao']



class s2299infoPerAntideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntideEstabLot
        fields = '__all__'
            

class s2299infoPerAntidePeriodo(models.Model):
    s2299_infoperant_ideadc = models.ForeignKey('s2299infoPerAntideADC',
        related_name='%(class)s_s2299_infoperant_ideadc')
    def evento(self): return self.s2299_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s2299_infoperant_ideperiodo_custom#
    #s2299_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's2299_infoperant_ideperiodo'
        managed = True
        ordering = ['s2299_infoperant_ideadc', 'perref']



class s2299infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntidePeriodo
        fields = '__all__'
            

class s2299infoPerAntinfoAgNocivo(models.Model):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperant_infoagnocivo_custom#
    #s2299_infoperant_infoagnocivo_custom#
    class Meta:
        db_table = r's2299_infoperant_infoagnocivo'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'grauexp']



class s2299infoPerAntinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntinfoAgNocivo
        fields = '__all__'
            

class s2299infoPerAntinfoSimples(models.Model):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperant_infosimples_custom#
    #s2299_infoperant_infosimples_custom#
    class Meta:
        db_table = r's2299_infoperant_infosimples'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'indsimples']



class s2299infoPerAntinfoSimplesSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerAntinfoSimples
        fields = '__all__'
            

class s2299infoPerApurdetOper(models.Model):
    s2299_infoperapur_ideestablot = models.ForeignKey('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s2299_infoperapur_detoper_custom#
    #s2299_infoperapur_detoper_custom#
    class Meta:
        db_table = r's2299_infoperapur_detoper'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'cnpjoper', 'regans', 'vrpgtit']



class s2299infoPerApurdetOperSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetOper
        fields = '__all__'
            

class s2299infoPerApurdetPlano(models.Model):
    s2299_infoperapur_detoper = models.ForeignKey('s2299infoPerApurdetOper',
        related_name='%(class)s_s2299_infoperapur_detoper')
    def evento(self): return self.s2299_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S2299_INFOPERAPUR_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s2299_infoperapur_detplano_custom#
    #s2299_infoperapur_detplano_custom#
    class Meta:
        db_table = r's2299_infoperapur_detplano'
        managed = True
        ordering = ['s2299_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep']



class s2299infoPerApurdetPlanoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetPlano
        fields = '__all__'
            

class s2299infoPerApurdetVerbas(models.Model):
    s2299_infoperapur_ideestablot = models.ForeignKey('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
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
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperapur_detverbas_custom#
    #s2299_infoperapur_detverbas_custom#
    class Meta:
        db_table = r's2299_infoperapur_detverbas'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr']



class s2299infoPerApurdetVerbasSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurdetVerbas
        fields = '__all__'
            

class s2299infoPerApurideEstabLot(models.Model):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_TPINSC)
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
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperapur_ideestablot_custom#
    #s2299_infoperapur_ideestablot_custom#
    class Meta:
        db_table = r's2299_infoperapur_ideestablot'
        managed = True
        ordering = ['s2299_dmdev', 'tpinsc', 'nrinsc', 'codlotacao']



class s2299infoPerApurideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurideEstabLot
        fields = '__all__'
            

class s2299infoPerApurinfoAgNocivo(models.Model):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperapur_infoagnocivo_custom#
    #s2299_infoperapur_infoagnocivo_custom#
    class Meta:
        db_table = r's2299_infoperapur_infoagnocivo'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'grauexp']



class s2299infoPerApurinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurinfoAgNocivo
        fields = '__all__'
            

class s2299infoPerApurinfoSimples(models.Model):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperapur_infosimples_custom#
    #s2299_infoperapur_infosimples_custom#
    class Meta:
        db_table = r's2299_infoperapur_infosimples'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'indsimples']



class s2299infoPerApurinfoSimplesSerializer(ModelSerializer):
    class Meta:
        model = s2299infoPerApurinfoSimples
        fields = '__all__'
            

class s2299infoTrabInterm(models.Model):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.codconv)
    #s2299_infotrabinterm_custom#
    #s2299_infotrabinterm_custom#
    class Meta:
        db_table = r's2299_infotrabinterm'
        managed = True
        ordering = ['s2299_dmdev', 'codconv']



class s2299infoTrabIntermSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabInterm
        fields = '__all__'
            

class s2299infoTrabIntermconsigFGTS(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    insconsig = models.CharField(max_length=5)
    nrcontr = models.CharField(max_length=40)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.insconsig) + ' - ' + unicode(self.nrcontr)
    #s2299_infotrabinterm_consigfgts_custom#
    #s2299_infotrabinterm_consigfgts_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_consigfgts'
        managed = True
        ordering = ['s2299_evtdeslig', 'insconsig', 'nrcontr']



class s2299infoTrabIntermconsigFGTSSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermconsigFGTS
        fields = '__all__'
            

class s2299infoTrabInterminfoMV(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    indmv = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_INDMV)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.indmv)
    #s2299_infotrabinterm_infomv_custom#
    #s2299_infotrabinterm_infomv_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_infomv'
        managed = True
        ordering = ['s2299_evtdeslig', 'indmv']



class s2299infoTrabInterminfoMVSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabInterminfoMV
        fields = '__all__'
            

class s2299infoTrabIntermprocCS(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.nrprocjud)
    #s2299_infotrabinterm_proccs_custom#
    #s2299_infotrabinterm_proccs_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_proccs'
        managed = True
        ordering = ['s2299_evtdeslig', 'nrprocjud']



class s2299infoTrabIntermprocCSSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermprocCS
        fields = '__all__'
            

class s2299infoTrabIntermprocJudTrab(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s2299_infotrabinterm_procjudtrab_custom#
    #s2299_infotrabinterm_procjudtrab_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_procjudtrab'
        managed = True
        ordering = ['s2299_evtdeslig', 'tptrib', 'nrprocjud']



class s2299infoTrabIntermprocJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermprocJudTrab
        fields = '__all__'
            

class s2299infoTrabIntermquarentena(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    dtfimquar = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.dtfimquar)
    #s2299_infotrabinterm_quarentena_custom#
    #s2299_infotrabinterm_quarentena_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_quarentena'
        managed = True
        ordering = ['s2299_evtdeslig', 'dtfimquar']



class s2299infoTrabIntermquarentenaSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermquarentena
        fields = '__all__'
            

class s2299infoTrabIntermremunOutrEmpr(models.Model):
    s2299_infotrabinterm_infomv = models.ForeignKey('s2299infoTrabInterminfoMV',
        related_name='%(class)s_s2299_infotrabinterm_infomv')
    def evento(self): return self.s2299_infotrabinterm_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.TextField(max_length=3)
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infotrabinterm_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s2299_infotrabinterm_remunoutrempr_custom#
    #s2299_infotrabinterm_remunoutrempr_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_remunoutrempr'
        managed = True
        ordering = ['s2299_infotrabinterm_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']



class s2299infoTrabIntermremunOutrEmprSerializer(ModelSerializer):
    class Meta:
        model = s2299infoTrabIntermremunOutrEmpr
        fields = '__all__'
            

class s2299mudancaCPF(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    novocpf = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.novocpf)
    #s2299_mudancacpf_custom#
    #s2299_mudancacpf_custom#
    class Meta:
        db_table = r's2299_mudancacpf'
        managed = True
        ordering = ['s2299_evtdeslig', 'novocpf']



class s2299mudancaCPFSerializer(ModelSerializer):
    class Meta:
        model = s2299mudancaCPF
        fields = '__all__'
            

class s2299observacoes(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.observacao)
    #s2299_observacoes_custom#
    #s2299_observacoes_custom#
    class Meta:
        db_table = r's2299_observacoes'
        managed = True
        ordering = ['s2299_evtdeslig', 'observacao']



class s2299observacoesSerializer(ModelSerializer):
    class Meta:
        model = s2299observacoes
        fields = '__all__'
            

class s2299sucessaoVinc(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    tpinscsuc = models.IntegerField(choices=CHOICES_S2299_TPINSCSUC)
    cnpjsucessora = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.tpinscsuc) + ' - ' + unicode(self.cnpjsucessora)
    #s2299_sucessaovinc_custom#
    #s2299_sucessaovinc_custom#
    class Meta:
        db_table = r's2299_sucessaovinc'
        managed = True
        ordering = ['s2299_evtdeslig', 'tpinscsuc', 'cnpjsucessora']



class s2299sucessaoVincSerializer(ModelSerializer):
    class Meta:
        model = s2299sucessaoVinc
        fields = '__all__'
            

class s2299transfTit(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    cpfsubstituto = models.CharField(max_length=11)
    dtnascto = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.cpfsubstituto) + ' - ' + unicode(self.dtnascto)
    #s2299_transftit_custom#
    #s2299_transftit_custom#
    class Meta:
        db_table = r's2299_transftit'
        managed = True
        ordering = ['s2299_evtdeslig', 'cpfsubstituto', 'dtnascto']



class s2299transfTitSerializer(ModelSerializer):
    class Meta:
        model = s2299transfTit
        fields = '__all__'
            

#VIEWS_MODELS
