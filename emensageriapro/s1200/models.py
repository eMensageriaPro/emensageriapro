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



CHOICES_S1200_INDMV = (
    (1, u'1 - O declarante aplica a alíquota de desconto do segurado sobre a remuneração por ele informada (o percentual da alíquota será obtido considerando a remuneração total do trabalhador)'),
    (2, u'2 - O declarante aplica a alíquota de desconto do segurado sobre a diferença entre o limite máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'),
    (3, u'3 - O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite máximo de salário de contribuição em outra(s) empresa(s)'),
)

CHOICES_S1200_INFOPERANT_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S1200_INFOPERANT_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S1200_INFOPERANT_REMUNSUC = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1200_INFOPERANT_TPACCONV = (
    ('A', u'A - Acordo Coletivo de Trabalho'),
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('C', u'C - Convenção Coletiva de Trabalho'),
    ('D', u'D - Sentença Normativa - Dissídio'),
    ('E', u'E - Conversão de Licença Saúde em Acidente de Trabalho'),
)

CHOICES_S1200_INFOPERANT_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_INFOPERAPUR_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S1200_INFOPERAPUR_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S1200_INFOPERAPUR_TPDEP = (
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

CHOICES_S1200_INFOPERAPUR_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1200_TPINSCANT = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_S1200_TPTRIB = (
    (1, u'1 - IRRF'),
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (4, u'4 - Contribuição sindical'),
)

class s1200dmDev(models.Model):
    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    def evento(self): return self.s1200_evtremun.evento()
    idedmdev = models.CharField(max_length=30)
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.codcateg)
    #s1200_dmdev_custom#
    class Meta:
        db_table = r's1200_dmdev'
        managed = True # s1200_dmdev #
        ordering = ['s1200_evtremun', 'idedmdev', 'codcateg']



class s1200dmDevSerializer(ModelSerializer):
    class Meta:
        model = s1200dmDev
        fields = '__all__'
            

class s1200infoComplem(models.Model):
    s1200_evtremun = models.OneToOneField('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    def evento(self): return self.s1200_evtremun.evento()
    nmtrab = models.CharField(max_length=70)
    dtnascto = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.nmtrab) + ' - ' + unicode(self.dtnascto)
    #s1200_infocomplem_custom#
    class Meta:
        db_table = r's1200_infocomplem'
        managed = True # s1200_infocomplem #
        ordering = ['s1200_evtremun', 'nmtrab', 'dtnascto']



class s1200infoComplemSerializer(ModelSerializer):
    class Meta:
        model = s1200infoComplem
        fields = '__all__'
            

class s1200infoInterm(models.Model):
    s1200_evtremun = models.OneToOneField('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    def evento(self): return self.s1200_evtremun.evento()
    qtddiasinterm = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.qtddiasinterm)
    #s1200_infointerm_custom#
    class Meta:
        db_table = r's1200_infointerm'
        managed = True # s1200_infointerm #
        ordering = ['s1200_evtremun', 'qtddiasinterm']



class s1200infoIntermSerializer(ModelSerializer):
    class Meta:
        model = s1200infoInterm
        fields = '__all__'
            

class s1200infoMV(models.Model):
    s1200_evtremun = models.OneToOneField('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    def evento(self): return self.s1200_evtremun.evento()
    indmv = models.IntegerField(choices=CHOICES_S1200_INDMV)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.indmv)
    #s1200_infomv_custom#
    class Meta:
        db_table = r's1200_infomv'
        managed = True # s1200_infomv #
        ordering = ['s1200_evtremun', 'indmv']



class s1200infoMVSerializer(ModelSerializer):
    class Meta:
        model = s1200infoMV
        fields = '__all__'
            

class s1200infoPerAntideADC(models.Model):
    s1200_dmdev = models.ForeignKey('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    def evento(self): return self.s1200_dmdev.evento()
    dtacconv = models.DateField(blank=True, null=True)
    tpacconv = models.CharField(choices=CHOICES_S1200_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField(blank=True, null=True)
    dsc = models.CharField(max_length=255)
    remunsuc = models.CharField(choices=CHOICES_S1200_INFOPERANT_REMUNSUC, max_length=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_dmdev) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dsc) + ' - ' + unicode(self.remunsuc)
    #s1200_infoperant_ideadc_custom#
    class Meta:
        db_table = r's1200_infoperant_ideadc'
        managed = True # s1200_infoperant_ideadc #
        ordering = ['s1200_dmdev', 'tpacconv', 'dsc', 'remunsuc']



class s1200infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntideADC
        fields = '__all__'
            

class s1200infoPerAntideEstabLot(models.Model):
    s1200_infoperant_ideperiodo = models.ForeignKey('s1200infoPerAntidePeriodo',
        related_name='%(class)s_s1200_infoperant_ideperiodo')
    def evento(self): return self.s1200_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s1200_infoperant_ideestablot_custom#
    class Meta:
        db_table = r's1200_infoperant_ideestablot'
        managed = True # s1200_infoperant_ideestablot #
        ordering = ['s1200_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao']



class s1200infoPerAntideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntideEstabLot
        fields = '__all__'
            

class s1200infoPerAntidePeriodo(models.Model):
    s1200_infoperant_ideadc = models.ForeignKey('s1200infoPerAntideADC',
        related_name='%(class)s_s1200_infoperant_ideadc')
    def evento(self): return self.s1200_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s1200_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's1200_infoperant_ideperiodo'
        managed = True # s1200_infoperant_ideperiodo #
        ordering = ['s1200_infoperant_ideadc', 'perref']



class s1200infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntidePeriodo
        fields = '__all__'
            

class s1200infoPerAntinfoAgNocivo(models.Model):
    s1200_infoperant_remunperant = models.OneToOneField('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
    def evento(self): return self.s1200_infoperant_remunperant.evento()
    grauexp = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_GRAUEXP)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.grauexp)
    #s1200_infoperant_infoagnocivo_custom#
    class Meta:
        db_table = r's1200_infoperant_infoagnocivo'
        managed = True # s1200_infoperant_infoagnocivo #
        ordering = ['s1200_infoperant_remunperant', 'grauexp']



class s1200infoPerAntinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntinfoAgNocivo
        fields = '__all__'
            

class s1200infoPerAntinfoComplCont(models.Model):
    s1200_dmdev = models.OneToOneField('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    def evento(self): return self.s1200_dmdev.evento()
    codcbo = models.CharField(max_length=6)
    natatividade = models.IntegerField(blank=True, null=True)
    qtddiastrab = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_dmdev) + ' - ' + unicode(self.codcbo)
    #s1200_infoperant_infocomplcont_custom#
    class Meta:
        db_table = r's1200_infoperant_infocomplcont'
        managed = True # s1200_infoperant_infocomplcont #
        ordering = ['s1200_dmdev', 'codcbo']



class s1200infoPerAntinfoComplContSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntinfoComplCont
        fields = '__all__'
            

class s1200infoPerAntinfoTrabInterm(models.Model):
    s1200_infoperant_remunperant = models.ForeignKey('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
    def evento(self): return self.s1200_infoperant_remunperant.evento()
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codconv)
    #s1200_infoperant_infotrabinterm_custom#
    class Meta:
        db_table = r's1200_infoperant_infotrabinterm'
        managed = True # s1200_infoperant_infotrabinterm #
        ordering = ['s1200_infoperant_remunperant', 'codconv']



class s1200infoPerAntinfoTrabIntermSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntinfoTrabInterm
        fields = '__all__'
            

class s1200infoPerAntitensRemun(models.Model):
    s1200_infoperant_remunperant = models.ForeignKey('s1200infoPerAntremunPerAnt',
        related_name='%(class)s_s1200_infoperant_remunperant')
    def evento(self): return self.s1200_infoperant_remunperant.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1200_infoperant_itensremun_custom#
    class Meta:
        db_table = r's1200_infoperant_itensremun'
        managed = True # s1200_infoperant_itensremun #
        ordering = ['s1200_infoperant_remunperant', 'codrubr', 'idetabrubr', 'vrrubr']



class s1200infoPerAntitensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntitensRemun
        fields = '__all__'
            

class s1200infoPerAntremunPerAnt(models.Model):
    s1200_infoperant_ideestablot = models.ForeignKey('s1200infoPerAntideEstabLot',
        related_name='%(class)s_s1200_infoperant_ideestablot')
    def evento(self): return self.s1200_infoperant_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    indsimples = models.IntegerField(choices=CHOICES_S1200_INFOPERANT_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperant_ideestablot)
    #s1200_infoperant_remunperant_custom#
    class Meta:
        db_table = r's1200_infoperant_remunperant'
        managed = True # s1200_infoperant_remunperant #
        ordering = ['s1200_infoperant_ideestablot']



class s1200infoPerAntremunPerAntSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerAntremunPerAnt
        fields = '__all__'
            

class s1200infoPerApurdetOper(models.Model):
    s1200_infoperapur_remunperapur = models.ForeignKey('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    def evento(self): return self.s1200_infoperapur_remunperapur.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s1200_infoperapur_detoper_custom#
    class Meta:
        db_table = r's1200_infoperapur_detoper'
        managed = True # s1200_infoperapur_detoper #
        ordering = ['s1200_infoperapur_remunperapur', 'cnpjoper', 'regans', 'vrpgtit']



class s1200infoPerApurdetOperSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurdetOper
        fields = '__all__'
            

class s1200infoPerApurdetPlano(models.Model):
    s1200_infoperapur_detoper = models.ForeignKey('s1200infoPerApurdetOper',
        related_name='%(class)s_s1200_infoperapur_detoper')
    def evento(self): return self.s1200_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S1200_INFOPERAPUR_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s1200_infoperapur_detplano_custom#
    class Meta:
        db_table = r's1200_infoperapur_detplano'
        managed = True # s1200_infoperapur_detplano #
        ordering = ['s1200_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep']



class s1200infoPerApurdetPlanoSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurdetPlano
        fields = '__all__'
            

class s1200infoPerApurideEstabLot(models.Model):
    s1200_dmdev = models.ForeignKey('s1200dmDev',
        related_name='%(class)s_s1200_dmdev')
    def evento(self): return self.s1200_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    qtddiasav = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s1200_infoperapur_ideestablot_custom#
    class Meta:
        db_table = r's1200_infoperapur_ideestablot'
        managed = True # s1200_infoperapur_ideestablot #
        ordering = ['s1200_dmdev', 'tpinsc', 'nrinsc', 'codlotacao']



class s1200infoPerApurideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurideEstabLot
        fields = '__all__'
            

class s1200infoPerApurinfoAgNocivo(models.Model):
    s1200_infoperapur_remunperapur = models.OneToOneField('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    def evento(self): return self.s1200_infoperapur_remunperapur.evento()
    grauexp = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_GRAUEXP)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.grauexp)
    #s1200_infoperapur_infoagnocivo_custom#
    class Meta:
        db_table = r's1200_infoperapur_infoagnocivo'
        managed = True # s1200_infoperapur_infoagnocivo #
        ordering = ['s1200_infoperapur_remunperapur', 'grauexp']



class s1200infoPerApurinfoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurinfoAgNocivo
        fields = '__all__'
            

class s1200infoPerApurinfoTrabInterm(models.Model):
    s1200_infoperapur_remunperapur = models.ForeignKey('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    def evento(self): return self.s1200_infoperapur_remunperapur.evento()
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codconv)
    #s1200_infoperapur_infotrabinterm_custom#
    class Meta:
        db_table = r's1200_infoperapur_infotrabinterm'
        managed = True # s1200_infoperapur_infotrabinterm #
        ordering = ['s1200_infoperapur_remunperapur', 'codconv']



class s1200infoPerApurinfoTrabIntermSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurinfoTrabInterm
        fields = '__all__'
            

class s1200infoPerApuritensRemun(models.Model):
    s1200_infoperapur_remunperapur = models.ForeignKey('s1200infoPerApurremunPerApur',
        related_name='%(class)s_s1200_infoperapur_remunperapur')
    def evento(self): return self.s1200_infoperapur_remunperapur.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1200_infoperapur_itensremun_custom#
    class Meta:
        db_table = r's1200_infoperapur_itensremun'
        managed = True # s1200_infoperapur_itensremun #
        ordering = ['s1200_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'vrrubr']



class s1200infoPerApuritensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApuritensRemun
        fields = '__all__'
            

class s1200infoPerApurremunPerApur(models.Model):
    s1200_infoperapur_ideestablot = models.ForeignKey('s1200infoPerApurideEstabLot',
        related_name='%(class)s_s1200_infoperapur_ideestablot')
    def evento(self): return self.s1200_infoperapur_ideestablot.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    indsimples = models.IntegerField(choices=CHOICES_S1200_INFOPERAPUR_INDSIMPLES, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infoperapur_ideestablot)
    #s1200_infoperapur_remunperapur_custom#
    class Meta:
        db_table = r's1200_infoperapur_remunperapur'
        managed = True # s1200_infoperapur_remunperapur #
        ordering = ['s1200_infoperapur_ideestablot']



class s1200infoPerApurremunPerApurSerializer(ModelSerializer):
    class Meta:
        model = s1200infoPerApurremunPerApur
        fields = '__all__'
            

class s1200procJudTrab(models.Model):
    s1200_evtremun = models.ForeignKey('esocial.s1200evtRemun',
        related_name='%(class)s_s1200_evtremun')
    def evento(self): return self.s1200_evtremun.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1200_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_evtremun) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s1200_procjudtrab_custom#
    class Meta:
        db_table = r's1200_procjudtrab'
        managed = True # s1200_procjudtrab #
        ordering = ['s1200_evtremun', 'tptrib', 'nrprocjud']



class s1200procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s1200procJudTrab
        fields = '__all__'
            

class s1200remunOutrEmpr(models.Model):
    s1200_infomv = models.ForeignKey('s1200infoMV',
        related_name='%(class)s_s1200_infomv')
    def evento(self): return self.s1200_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.TextField(max_length=3)
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s1200_remunoutrempr_custom#
    class Meta:
        db_table = r's1200_remunoutrempr'
        managed = True # s1200_remunoutrempr #
        ordering = ['s1200_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']



class s1200remunOutrEmprSerializer(ModelSerializer):
    class Meta:
        model = s1200remunOutrEmpr
        fields = '__all__'
            

class s1200sucessaoVinc(models.Model):
    s1200_infocomplem = models.OneToOneField('s1200infoComplem',
        related_name='%(class)s_s1200_infocomplem')
    def evento(self): return self.s1200_infocomplem.evento()
    tpinscant = models.IntegerField(choices=CHOICES_S1200_TPINSCANT)
    cnpjempregant = models.CharField(max_length=14)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dtadm = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s1200_infocomplem) + ' - ' + unicode(self.tpinscant) + ' - ' + unicode(self.cnpjempregant) + ' - ' + unicode(self.dtadm)
    #s1200_sucessaovinc_custom#
    class Meta:
        db_table = r's1200_sucessaovinc'
        managed = True # s1200_sucessaovinc #
        ordering = ['s1200_infocomplem', 'tpinscant', 'cnpjempregant', 'dtadm']



class s1200sucessaoVincSerializer(ModelSerializer):
    class Meta:
        model = s1200sucessaoVinc
        fields = '__all__'
            

#VIEWS_MODELS
