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

PERIODOS = (
    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
)

CHOICES_S1070_ALTERACAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade, empresa ou empregado'),
)

CHOICES_S1070_ALTERACAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1070_ALTERACAO_INDMATPROC = (
    (1, u'1 - Tributária'),
    (2, u'2 - Autorização de trabalho de menor'),
    (3, u'3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD)'),
    (4, u'4 - Dispensa, ainda que parcial, de contratação de aprendiz'),
    (5, u'5 - Segurança e Saúde do Trabalho'),
    (6, u'6 - Conversão de Licença Saúde em Acidente de Trabalho'),
    (7, u'7 - FGTS'),
    (8, u'8 - Contribuição sindical'),
    (99, u'99 - Outros assuntos'),
)

CHOICES_S1070_ALTERACAO_INDSUSP = (
    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('14', u'14 - Contestação Administrativa FAP'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_S1070_ALTERACAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
)

CHOICES_S1070_EXCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
)

CHOICES_S1070_INCLUSAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade, empresa ou empregado'),
)

CHOICES_S1070_INCLUSAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1070_INCLUSAO_INDMATPROC = (
    (1, u'1 - Tributária'),
    (2, u'2 - Autorização de trabalho de menor'),
    (3, u'3 - Dispensa, ainda que parcial, de contratação de pessoa com deficiência (PCD)'),
    (4, u'4 - Dispensa, ainda que parcial, de contratação de aprendiz'),
    (5, u'5 - Segurança e Saúde do Trabalho'),
    (6, u'6 - Conversão de Licença Saúde em Acidente de Trabalho'),
    (7, u'7 - FGTS'),
    (8, u'8 - Contribuição sindical'),
    (99, u'99 - Outros assuntos'),
)

CHOICES_S1070_INCLUSAO_INDSUSP = (
    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('14', u'14 - Contestação Administrativa FAP'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_S1070_INCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
)

class s1070alteracao(models.Model):
    s1070_evttabprocesso = models.OneToOneField('esocial.s1070evtTabProcesso',
        related_name='%(class)s_s1070_evttabprocesso')
    tpproc = models.IntegerField(choices=CHOICES_S1070_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_S1070_ALTERACAO_INDAUTORIA, blank=True, null=True)
    indmatproc = models.IntegerField(choices=CHOICES_S1070_ALTERACAO_INDMATPROC)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.indautoria) + ' - ' + unicode(self.indmatproc) + ' - ' + unicode(self.observacao)
    #s1070_alteracao_custom#
    #s1070_alteracao_custom#
    class Meta:
        db_table = r's1070_alteracao'
        managed = True
        ordering = ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria', 'indmatproc', 'observacao']



class s1070alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1070alteracao
        fields = '__all__'
            

class s1070alteracaodadosProcJud(models.Model):
    s1070_alteracao = models.OneToOneField('s1070alteracao',
        related_name='%(class)s_s1070_alteracao')
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_alteracao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #s1070_alteracao_dadosprocjud_custom#
    #s1070_alteracao_dadosprocjud_custom#
    class Meta:
        db_table = r's1070_alteracao_dadosprocjud'
        managed = True
        ordering = ['s1070_alteracao', 'ufvara', 'codmunic', 'idvara']



class s1070alteracaodadosProcJudSerializer(ModelSerializer):
    class Meta:
        model = s1070alteracaodadosProcJud
        fields = '__all__'
            

class s1070alteracaoinfoSusp(models.Model):
    s1070_alteracao = models.ForeignKey('s1070alteracao',
        related_name='%(class)s_s1070_alteracao')
    codsusp = models.IntegerField()
    indsusp = models.CharField(choices=CHOICES_S1070_ALTERACAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_S1070_ALTERACAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_alteracao) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #s1070_alteracao_infosusp_custom#
    #s1070_alteracao_infosusp_custom#
    class Meta:
        db_table = r's1070_alteracao_infosusp'
        managed = True
        ordering = ['s1070_alteracao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito']



class s1070alteracaoinfoSuspSerializer(ModelSerializer):
    class Meta:
        model = s1070alteracaoinfoSusp
        fields = '__all__'
            

class s1070alteracaonovaValidade(models.Model):
    s1070_alteracao = models.OneToOneField('s1070alteracao',
        related_name='%(class)s_s1070_alteracao')
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1070_alteracao_novavalidade_custom#
    #s1070_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1070_alteracao_novavalidade'
        managed = True
        ordering = ['s1070_alteracao', 'inivalid', 'fimvalid']



class s1070alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1070alteracaonovaValidade
        fields = '__all__'
            

class s1070exclusao(models.Model):
    s1070_evttabprocesso = models.OneToOneField('esocial.s1070evtTabProcesso',
        related_name='%(class)s_s1070_evttabprocesso')
    tpproc = models.IntegerField(choices=CHOICES_S1070_EXCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1070_exclusao_custom#
    #s1070_exclusao_custom#
    class Meta:
        db_table = r's1070_exclusao'
        managed = True
        ordering = ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid']



class s1070exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1070exclusao
        fields = '__all__'
            

class s1070inclusao(models.Model):
    s1070_evttabprocesso = models.OneToOneField('esocial.s1070evtTabProcesso',
        related_name='%(class)s_s1070_evttabprocesso')
    tpproc = models.IntegerField(choices=CHOICES_S1070_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_S1070_INCLUSAO_INDAUTORIA, blank=True, null=True)
    indmatproc = models.IntegerField(choices=CHOICES_S1070_INCLUSAO_INDMATPROC)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.indautoria) + ' - ' + unicode(self.indmatproc) + ' - ' + unicode(self.observacao)
    #s1070_inclusao_custom#
    #s1070_inclusao_custom#
    class Meta:
        db_table = r's1070_inclusao'
        managed = True
        ordering = ['s1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria', 'indmatproc', 'observacao']



class s1070inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1070inclusao
        fields = '__all__'
            

class s1070inclusaodadosProcJud(models.Model):
    s1070_inclusao = models.OneToOneField('s1070inclusao',
        related_name='%(class)s_s1070_inclusao')
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_inclusao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #s1070_inclusao_dadosprocjud_custom#
    #s1070_inclusao_dadosprocjud_custom#
    class Meta:
        db_table = r's1070_inclusao_dadosprocjud'
        managed = True
        ordering = ['s1070_inclusao', 'ufvara', 'codmunic', 'idvara']



class s1070inclusaodadosProcJudSerializer(ModelSerializer):
    class Meta:
        model = s1070inclusaodadosProcJud
        fields = '__all__'
            

class s1070inclusaoinfoSusp(models.Model):
    s1070_inclusao = models.ForeignKey('s1070inclusao',
        related_name='%(class)s_s1070_inclusao')
    codsusp = models.IntegerField()
    indsusp = models.CharField(choices=CHOICES_S1070_INCLUSAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_S1070_INCLUSAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1070_inclusao) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #s1070_inclusao_infosusp_custom#
    #s1070_inclusao_infosusp_custom#
    class Meta:
        db_table = r's1070_inclusao_infosusp'
        managed = True
        ordering = ['s1070_inclusao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito']



class s1070inclusaoinfoSuspSerializer(ModelSerializer):
    class Meta:
        model = s1070inclusaoinfoSusp
        fields = '__all__'
            

#VIEWS_MODELS
