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



CHOICES_R2070_INDDECTERCEIRO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2070_INDNIF = (
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF'),
)

CHOICES_R2070_INDPERREFERENCIA = (
    (1, u'1 - Folha de Pagamento Mensal'),
    (2, u'2 - Folha do Décimo Terceiro Salário'),
)

CHOICES_R2070_INDSUSPEXIG = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R2070_INDTPDEDUCAO = (
    (1, u'1 - Previdência Oficial'),
    (2, u'2 - Previdência Privada'),
    (3, u'3 - Fapi'),
    (4, u'4 - Funpresp'),
    (5, u'5 - Pensão Alimentícia'),
    (6, u'6 - Dependentes'),
)

CHOICES_R2070_INFOPROCJUD_INDORIGEMRECURSOS = (
    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros -Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores'),
)

CHOICES_R2070_INFOPROCJUD_TPINSCADVOGADO = (
    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física'),
)

CHOICES_R2070_INFORRA_TPINSCADVOGADO = (
    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física'),
)

CHOICES_R2070_INFORRA_TPPROCRRA = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2070_PGTOPJ_INDORIGEMRECURSOS = (
    (1, u'1 - Recursos do próprio declarante'),
    (2, u'2 - Recursos de terceiros - Declarante é a Instituição Financeira responsável apenas pelo repasse dos valores'),
)

CHOICES_R2070_PGTOPJ_TPINSCADVOGADO = (
    (1, u'1 - Pessoa Jurídica'),
    (2, u'2 - Pessoa Física'),
)

CHOICES_R2070_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
)

CHOICES_R2070_TPISENCAO = (
    (1, u'1 - Parcela Isenta 65 anos'),
    (10, u'10 - Bolsa de estudo recebida por médico-residente'),
    (11, u'11 - Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995'),
    (2, u'2 - Diária e Ajuda de Custo'),
    (3, u'3 - Indenização e rescisão de contrato, inclusive a título de PDV'),
    (4, u'4 - Abono pecuniário'),
    (5, u'5 - Outros (especificar)'),
    (6, u'6 - Lucros e dividendos pagos a partir de 1996'),
    (7, u'7 - Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    (8, u'8 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço'),
    (9, u'9 - Benefícios indiretos e/ou reembolso de despesas recebidas por voluntário da copa do mundo ou da copa das confederações'),
)

class r2070compJud(models.Model):
    r2070_pgtopf = models.OneToOneField('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    vlrcompanocalend = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrcompanoant = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf)
    #r2070_compjud_custom#
    #r2070_compjud_custom#
    class Meta:
        db_table = r'r2070_compjud'
        managed = True
        ordering = ['r2070_pgtopf']



class r2070compJudSerializer(ModelSerializer):
    class Meta:
        model = r2070compJud
        fields = '__all__'
            

class r2070depJudicial(models.Model):
    r2070_pgtopf = models.OneToOneField('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    vlrdepjudicial = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf)
    #r2070_depjudicial_custom#
    #r2070_depjudicial_custom#
    class Meta:
        db_table = r'r2070_depjudicial'
        managed = True
        ordering = ['r2070_pgtopf']



class r2070depJudicialSerializer(ModelSerializer):
    class Meta:
        model = r2070depJudicial
        fields = '__all__'
            

class r2070detCompet(models.Model):
    r2070_pgtopf = models.ForeignKey('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    indperreferencia = models.IntegerField(choices=CHOICES_R2070_INDPERREFERENCIA)
    perrefpagto = models.CharField(max_length=7)
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.indperreferencia) + ' - ' + unicode(self.perrefpagto) + ' - ' + unicode(self.vlrrendtributavel)
    #r2070_detcompet_custom#
    #r2070_detcompet_custom#
    class Meta:
        db_table = r'r2070_detcompet'
        managed = True
        ordering = ['r2070_pgtopf', 'indperreferencia', 'perrefpagto', 'vlrrendtributavel']



class r2070detCompetSerializer(ModelSerializer):
    class Meta:
        model = r2070detCompet
        fields = '__all__'
            

class r2070detDeducao(models.Model):
    r2070_pgtopf = models.ForeignKey('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    indtpdeducao = models.IntegerField(choices=CHOICES_R2070_INDTPDEDUCAO)
    vlrdeducao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.indtpdeducao) + ' - ' + unicode(self.vlrdeducao)
    #r2070_detdeducao_custom#
    #r2070_detdeducao_custom#
    class Meta:
        db_table = r'r2070_detdeducao'
        managed = True
        ordering = ['r2070_pgtopf', 'indtpdeducao', 'vlrdeducao']



class r2070detDeducaoSerializer(ModelSerializer):
    class Meta:
        model = r2070detDeducao
        fields = '__all__'
            

class r2070ideEstab(models.Model):
    r2070_evtpgtosdivs = models.ForeignKey('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs')
    def evento(self): return self.r2070_evtpgtosdivs.evento()
    tpinsc = models.IntegerField(choices=CHOICES_R2070_TPINSC)
    nrinsc = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #r2070_ideestab_custom#
    #r2070_ideestab_custom#
    class Meta:
        db_table = r'r2070_ideestab'
        managed = True
        ordering = ['r2070_evtpgtosdivs', 'tpinsc', 'nrinsc']



class r2070ideEstabSerializer(ModelSerializer):
    class Meta:
        model = r2070ideEstab
        fields = '__all__'
            

class r2070infoMolestia(models.Model):
    r2070_evtpgtosdivs = models.OneToOneField('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs')
    def evento(self): return self.r2070_evtpgtosdivs.evento()
    dtlaudo = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.dtlaudo)
    #r2070_infomolestia_custom#
    #r2070_infomolestia_custom#
    class Meta:
        db_table = r'r2070_infomolestia'
        managed = True
        ordering = ['r2070_evtpgtosdivs', 'dtlaudo']



class r2070infoMolestiaSerializer(ModelSerializer):
    class Meta:
        model = r2070infoMolestia
        fields = '__all__'
            

class r2070infoProcJud(models.Model):
    r2070_pgtopf = models.ForeignKey('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    nrprocjud = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    indorigemrecursos = models.IntegerField(choices=CHOICES_R2070_INFOPROCJUD_INDORIGEMRECURSOS)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.indorigemrecursos)
    #r2070_infoprocjud_custom#
    #r2070_infoprocjud_custom#
    class Meta:
        db_table = r'r2070_infoprocjud'
        managed = True
        ordering = ['r2070_pgtopf', 'nrprocjud', 'indorigemrecursos']



class r2070infoProcJudSerializer(ModelSerializer):
    class Meta:
        model = r2070infoProcJud
        fields = '__all__'
            

class r2070infoProcJuddespProcJud(models.Model):
    r2070_infoprocjud = models.OneToOneField('r2070infoProcJud',
        related_name='%(class)s_r2070_infoprocjud')
    def evento(self): return self.r2070_infoprocjud.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_infoprocjud) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)
    #r2070_infoprocjud_despprocjud_custom#
    #r2070_infoprocjud_despprocjud_custom#
    class Meta:
        db_table = r'r2070_infoprocjud_despprocjud'
        managed = True
        ordering = ['r2070_infoprocjud', 'vlrdespcustas', 'vlrdespadvogados']



class r2070infoProcJuddespProcJudSerializer(ModelSerializer):
    class Meta:
        model = r2070infoProcJuddespProcJud
        fields = '__all__'
            

class r2070infoProcJudideAdvogado(models.Model):
    r2070_infoprocjud_despprocjud = models.ForeignKey('r2070infoProcJuddespProcJud',
        related_name='%(class)s_r2070_infoprocjud_despprocjud')
    def evento(self): return self.r2070_infoprocjud_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_INFOPROCJUD_TPINSCADVOGADO)
    nrinscadvogado = models.CharField(max_length=14)
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_infoprocjud_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)
    #r2070_infoprocjud_ideadvogado_custom#
    #r2070_infoprocjud_ideadvogado_custom#
    class Meta:
        db_table = r'r2070_infoprocjud_ideadvogado'
        managed = True
        ordering = ['r2070_infoprocjud_despprocjud', 'tpinscadvogado', 'nrinscadvogado', 'vlradvogado']



class r2070infoProcJudideAdvogadoSerializer(ModelSerializer):
    class Meta:
        model = r2070infoProcJudideAdvogado
        fields = '__all__'
            

class r2070infoProcJudorigemRecursos(models.Model):
    r2070_infoprocjud = models.OneToOneField('r2070infoProcJud',
        related_name='%(class)s_r2070_infoprocjud')
    def evento(self): return self.r2070_infoprocjud.evento()
    cnpjorigemrecursos = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_infoprocjud) + ' - ' + unicode(self.cnpjorigemrecursos)
    #r2070_infoprocjud_origemrecursos_custom#
    #r2070_infoprocjud_origemrecursos_custom#
    class Meta:
        db_table = r'r2070_infoprocjud_origemrecursos'
        managed = True
        ordering = ['r2070_infoprocjud', 'cnpjorigemrecursos']



class r2070infoProcJudorigemRecursosSerializer(ModelSerializer):
    class Meta:
        model = r2070infoProcJudorigemRecursos
        fields = '__all__'
            

class r2070infoRRA(models.Model):
    r2070_pgtopf = models.ForeignKey('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    tpprocrra = models.IntegerField(choices=CHOICES_R2070_INFORRA_TPPROCRRA, blank=True, null=True)
    nrprocrra = models.CharField(max_length=21, blank=True, null=True)
    codsusp = models.IntegerField(blank=True, null=True)
    natrra = models.CharField(max_length=50, blank=True, null=True)
    qtdmesesrra = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf)
    #r2070_inforra_custom#
    #r2070_inforra_custom#
    class Meta:
        db_table = r'r2070_inforra'
        managed = True
        ordering = ['r2070_pgtopf']



class r2070infoRRASerializer(ModelSerializer):
    class Meta:
        model = r2070infoRRA
        fields = '__all__'
            

class r2070infoRRAdespProcJud(models.Model):
    r2070_inforra = models.OneToOneField('r2070infoRRA',
        related_name='%(class)s_r2070_inforra')
    def evento(self): return self.r2070_inforra.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_inforra) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)
    #r2070_inforra_despprocjud_custom#
    #r2070_inforra_despprocjud_custom#
    class Meta:
        db_table = r'r2070_inforra_despprocjud'
        managed = True
        ordering = ['r2070_inforra', 'vlrdespcustas', 'vlrdespadvogados']



class r2070infoRRAdespProcJudSerializer(ModelSerializer):
    class Meta:
        model = r2070infoRRAdespProcJud
        fields = '__all__'
            

class r2070infoRRAideAdvogado(models.Model):
    r2070_inforra_despprocjud = models.ForeignKey('r2070infoRRAdespProcJud',
        related_name='%(class)s_r2070_inforra_despprocjud')
    def evento(self): return self.r2070_inforra_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_INFORRA_TPINSCADVOGADO)
    nrinscadvogado = models.CharField(max_length=14)
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_inforra_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)
    #r2070_inforra_ideadvogado_custom#
    #r2070_inforra_ideadvogado_custom#
    class Meta:
        db_table = r'r2070_inforra_ideadvogado'
        managed = True
        ordering = ['r2070_inforra_despprocjud', 'tpinscadvogado', 'nrinscadvogado', 'vlradvogado']



class r2070infoRRAideAdvogadoSerializer(ModelSerializer):
    class Meta:
        model = r2070infoRRAideAdvogado
        fields = '__all__'
            

class r2070infoResidExt(models.Model):
    r2070_evtpgtosdivs = models.OneToOneField('efdreinf.r2070evtPgtosDivs',
        related_name='%(class)s_r2070_evtpgtosdivs')
    def evento(self): return self.r2070_evtpgtosdivs.evento()
    paisresid = models.TextField(max_length=3)
    dsclograd = models.CharField(max_length=80)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    complem = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    indnif = models.IntegerField(choices=CHOICES_R2070_INDNIF)
    nifbenef = models.CharField(max_length=20, blank=True, null=True)
    relfontepagad = models.CharField(max_length=3, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_evtpgtosdivs) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.indnif)
    #r2070_inforesidext_custom#
    #r2070_inforesidext_custom#
    class Meta:
        db_table = r'r2070_inforesidext'
        managed = True
        ordering = ['r2070_evtpgtosdivs', 'paisresid', 'dsclograd', 'indnif']



class r2070infoResidExtSerializer(ModelSerializer):
    class Meta:
        model = r2070infoResidExt
        fields = '__all__'
            

class r2070pgtoPF(models.Model):
    r2070_ideestab = models.ForeignKey('r2070ideEstab',
        related_name='%(class)s_r2070_ideestab')
    def evento(self): return self.r2070_ideestab.evento()
    dtpgto = models.DateField()
    indsuspexig = models.CharField(choices=CHOICES_R2070_INDSUSPEXIG, max_length=1)
    inddecterceiro = models.CharField(choices=CHOICES_R2070_INDDECTERCEIRO, max_length=1)
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrirrf = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_ideestab) + ' - ' + unicode(self.dtpgto) + ' - ' + unicode(self.indsuspexig) + ' - ' + unicode(self.inddecterceiro) + ' - ' + unicode(self.vlrrendtributavel) + ' - ' + unicode(self.vlrirrf)
    #r2070_pgtopf_custom#
    #r2070_pgtopf_custom#
    class Meta:
        db_table = r'r2070_pgtopf'
        managed = True
        ordering = ['r2070_ideestab', 'dtpgto', 'indsuspexig', 'inddecterceiro', 'vlrrendtributavel', 'vlrirrf']



class r2070pgtoPFSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPF
        fields = '__all__'
            

class r2070pgtoPJ(models.Model):
    r2070_ideestab = models.ForeignKey('r2070ideEstab',
        related_name='%(class)s_r2070_ideestab')
    def evento(self): return self.r2070_ideestab.evento()
    dtpagto = models.DateField()
    vlrrendtributavel = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_ideestab) + ' - ' + unicode(self.dtpagto) + ' - ' + unicode(self.vlrrendtributavel) + ' - ' + unicode(self.vlrret)
    #r2070_pgtopj_custom#
    #r2070_pgtopj_custom#
    class Meta:
        db_table = r'r2070_pgtopj'
        managed = True
        ordering = ['r2070_ideestab', 'dtpagto', 'vlrrendtributavel', 'vlrret']



class r2070pgtoPJSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPJ
        fields = '__all__'
            

class r2070pgtoPJdespProcJud(models.Model):
    r2070_pgtopj_infoprocjud = models.OneToOneField('r2070pgtoPJinfoProcJud',
        related_name='%(class)s_r2070_pgtopj_infoprocjud')
    def evento(self): return self.r2070_pgtopj_infoprocjud.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopj_infoprocjud) + ' - ' + unicode(self.vlrdespcustas) + ' - ' + unicode(self.vlrdespadvogados)
    #r2070_pgtopj_despprocjud_custom#
    #r2070_pgtopj_despprocjud_custom#
    class Meta:
        db_table = r'r2070_pgtopj_despprocjud'
        managed = True
        ordering = ['r2070_pgtopj_infoprocjud', 'vlrdespcustas', 'vlrdespadvogados']



class r2070pgtoPJdespProcJudSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPJdespProcJud
        fields = '__all__'
            

class r2070pgtoPJideAdvogado(models.Model):
    r2070_pgtopj_despprocjud = models.ForeignKey('r2070pgtoPJdespProcJud',
        related_name='%(class)s_r2070_pgtopj_despprocjud')
    def evento(self): return self.r2070_pgtopj_despprocjud.evento()
    tpinscadvogado = models.IntegerField(choices=CHOICES_R2070_PGTOPJ_TPINSCADVOGADO)
    nrinscadvogado = models.CharField(max_length=14)
    vlradvogado = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopj_despprocjud) + ' - ' + unicode(self.tpinscadvogado) + ' - ' + unicode(self.nrinscadvogado) + ' - ' + unicode(self.vlradvogado)
    #r2070_pgtopj_ideadvogado_custom#
    #r2070_pgtopj_ideadvogado_custom#
    class Meta:
        db_table = r'r2070_pgtopj_ideadvogado'
        managed = True
        ordering = ['r2070_pgtopj_despprocjud', 'tpinscadvogado', 'nrinscadvogado', 'vlradvogado']



class r2070pgtoPJideAdvogadoSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPJideAdvogado
        fields = '__all__'
            

class r2070pgtoPJinfoProcJud(models.Model):
    r2070_pgtopj = models.ForeignKey('r2070pgtoPJ',
        related_name='%(class)s_r2070_pgtopj')
    def evento(self): return self.r2070_pgtopj.evento()
    nrprocjud = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    indorigemrecursos = models.IntegerField(choices=CHOICES_R2070_PGTOPJ_INDORIGEMRECURSOS)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopj) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.indorigemrecursos)
    #r2070_pgtopj_infoprocjud_custom#
    #r2070_pgtopj_infoprocjud_custom#
    class Meta:
        db_table = r'r2070_pgtopj_infoprocjud'
        managed = True
        ordering = ['r2070_pgtopj', 'nrprocjud', 'indorigemrecursos']



class r2070pgtoPJinfoProcJudSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPJinfoProcJud
        fields = '__all__'
            

class r2070pgtoPJorigemRecursos(models.Model):
    r2070_pgtopj_infoprocjud = models.OneToOneField('r2070pgtoPJinfoProcJud',
        related_name='%(class)s_r2070_pgtopj_infoprocjud')
    def evento(self): return self.r2070_pgtopj_infoprocjud.evento()
    cnpjorigemrecursos = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopj_infoprocjud) + ' - ' + unicode(self.cnpjorigemrecursos)
    #r2070_pgtopj_origemrecursos_custom#
    #r2070_pgtopj_origemrecursos_custom#
    class Meta:
        db_table = r'r2070_pgtopj_origemrecursos'
        managed = True
        ordering = ['r2070_pgtopj_infoprocjud', 'cnpjorigemrecursos']



class r2070pgtoPJorigemRecursosSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoPJorigemRecursos
        fields = '__all__'
            

class r2070pgtoResidExt(models.Model):
    r2070_ideestab = models.OneToOneField('r2070ideEstab',
        related_name='%(class)s_r2070_ideestab')
    def evento(self): return self.r2070_ideestab.evento()
    dtpagto = models.DateField()
    tprendimento = models.IntegerField()
    formatributacao = models.CharField(max_length=2)
    vlrpgto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_ideestab) + ' - ' + unicode(self.dtpagto) + ' - ' + unicode(self.tprendimento) + ' - ' + unicode(self.formatributacao) + ' - ' + unicode(self.vlrpgto) + ' - ' + unicode(self.vlrret)
    #r2070_pgtoresidext_custom#
    #r2070_pgtoresidext_custom#
    class Meta:
        db_table = r'r2070_pgtoresidext'
        managed = True
        ordering = ['r2070_ideestab', 'dtpagto', 'tprendimento', 'formatributacao', 'vlrpgto', 'vlrret']



class r2070pgtoResidExtSerializer(ModelSerializer):
    class Meta:
        model = r2070pgtoResidExt
        fields = '__all__'
            

class r2070rendIsento(models.Model):
    r2070_pgtopf = models.ForeignKey('r2070pgtoPF',
        related_name='%(class)s_r2070_pgtopf')
    def evento(self): return self.r2070_pgtopf.evento()
    tpisencao = models.IntegerField(choices=CHOICES_R2070_TPISENCAO)
    vlrisento = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    descrendimento = models.CharField(max_length=100, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2070_pgtopf) + ' - ' + unicode(self.tpisencao) + ' - ' + unicode(self.vlrisento)
    #r2070_rendisento_custom#
    #r2070_rendisento_custom#
    class Meta:
        db_table = r'r2070_rendisento'
        managed = True
        ordering = ['r2070_pgtopf', 'tpisencao', 'vlrisento']



class r2070rendIsentoSerializer(ModelSerializer):
    class Meta:
        model = r2070rendIsento
        fields = '__all__'
            

#VIEWS_MODELS
