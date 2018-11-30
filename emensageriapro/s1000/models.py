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
    ('2019-01', u'Janeiro/2019'),
    ('2019-02', u'Fevereiro/2019'),
    ('2019-03', u'Março/2019'),
    ('2019-04', u'Abril/2019'),
    ('2019-05', u'Maio/2019'),
    ('2019-06', u'Junho/2019'),
    ('2019-07', u'Julho/2019'),
    ('2019-08', u'Agosto/2019'),
    ('2019-09', u'Setembro/2019'),
    ('2019-10', u'Outubro/2019'),
    ('2019-11', u'Novembro/2019'),
    ('2019-12', u'Dezembro/2019'),
)

CHOICES_S1000_ALTERACAO_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S1000_ALTERACAO_ESFERAOP = (
    (1, u'1 - Federal'),
    (2, u'2 - Estadual ou distrital'),
    (3, u'3 - Municipal'),
)

CHOICES_S1000_ALTERACAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_S1000_ALTERACAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_S1000_ALTERACAO_INDCONSTR = (
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora'),
)

CHOICES_S1000_ALTERACAO_INDCOOP = (
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas'),
)

CHOICES_S1000_ALTERACAO_INDDESFOLHA = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011'),
)

CHOICES_S1000_ALTERACAO_INDENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_INDETT = (
    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário'),
)

CHOICES_S1000_ALTERACAO_INDOPCCP = (
    (1, u'1 - Sobre a comercialização da sua produção'),
    (2, u'2 - Sobre a folha de pagamento'),
)

CHOICES_S1000_ALTERACAO_INDOPTREGELETRON = (
    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados'),
)

CHOICES_S1000_ALTERACAO_INDRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_INDSITPF = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente'),
)

CHOICES_S1000_ALTERACAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
)

CHOICES_S1000_ALTERACAO_INDUGRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_PODEROP = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (4, u'4 - Ministério Público'),
    (5, u'5 - Tribunal de Contas'),
    (6, u'6 - Defensoria Pública'),
)

CHOICES_S1000_ALTERACAO_PREVCOMP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_SUBTETO = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes'),
)

CHOICES_S1000_INCLUSAO_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S1000_INCLUSAO_ESFERAOP = (
    (1, u'1 - Federal'),
    (2, u'2 - Estadual ou distrital'),
    (3, u'3 - Municipal'),
)

CHOICES_S1000_INCLUSAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_S1000_INCLUSAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_S1000_INCLUSAO_INDCONSTR = (
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora'),
)

CHOICES_S1000_INCLUSAO_INDCOOP = (
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas'),
)

CHOICES_S1000_INCLUSAO_INDDESFOLHA = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011'),
)

CHOICES_S1000_INCLUSAO_INDENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_INDETT = (
    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário'),
)

CHOICES_S1000_INCLUSAO_INDOPCCP = (
    (1, u'1 - Sobre a comercialização da sua produção'),
    (2, u'2 - Sobre a folha de pagamento'),
)

CHOICES_S1000_INCLUSAO_INDOPTREGELETRON = (
    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados'),
)

CHOICES_S1000_INCLUSAO_INDRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_INDSITPF = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente'),
)

CHOICES_S1000_INCLUSAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
)

CHOICES_S1000_INCLUSAO_INDUGRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_PODEROP = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (4, u'4 - Ministério Público'),
    (5, u'5 - Tribunal de Contas'),
    (6, u'6 - Defensoria Pública'),
)

CHOICES_S1000_INCLUSAO_PREVCOMP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_SUBTETO = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes'),
)

class s1000alteracao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    classtrib = models.CharField(choices=CHOICES_S1000_ALTERACAO_CLASSTRIB, max_length=2)
    natjurid = models.TextField(max_length=4, blank=True, null=True)
    indcoop = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDCOOP, blank=True, null=True)
    indconstr = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDCONSTR, blank=True, null=True)
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDDESFOLHA)
    indopccp = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDOPCCP, blank=True, null=True)
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDOPTREGELETRON)
    indented = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDENTED, max_length=1, blank=True, null=True)
    indett = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDETT, max_length=1)
    nrregett = models.CharField(max_length=30, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.indett) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)
    #s1000_alteracao_custom#
    #s1000_alteracao_custom#
    class Meta:
        db_table = r's1000_alteracao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid', 'nmrazao', 'classtrib', 'inddesfolha', 'indoptregeletron', 'indett', 'nmctt', 'cpfctt']



class s1000alteracaoSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracao
        fields = '__all__'
            

class s1000alteracaodadosIsencao(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    ideminlei = models.CharField(max_length=70)
    nrcertif = models.CharField(max_length=40)
    dtemiscertif = models.DateField()
    dtvenccertif = models.DateField()
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True)
    dtprotrenov = models.DateField(blank=True, null=True)
    dtdou = models.DateField(blank=True, null=True)
    pagdou = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif)
    #s1000_alteracao_dadosisencao_custom#
    #s1000_alteracao_dadosisencao_custom#
    class Meta:
        db_table = r's1000_alteracao_dadosisencao'
        managed = True
        ordering = ['s1000_alteracao', 'ideminlei', 'nrcertif', 'dtemiscertif', 'dtvenccertif']



class s1000alteracaodadosIsencaoSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaodadosIsencao
        fields = '__all__'
            

class s1000alteracaoinfoEFR(models.Model):
    s1000_alteracao_infoop = models.OneToOneField('s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop')
    def evento(self): return self.s1000_alteracao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_ALTERACAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDRPPS, max_length=1)
    prevcomp = models.CharField(choices=CHOICES_S1000_ALTERACAO_PREVCOMP, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.prevcomp)
    #s1000_alteracao_infoefr_custom#
    #s1000_alteracao_infoefr_custom#
    class Meta:
        db_table = r's1000_alteracao_infoefr'
        managed = True
        ordering = ['s1000_alteracao_infoop', 'ideefr', 'indrpps', 'prevcomp']



class s1000alteracaoinfoEFRSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaoinfoEFR
        fields = '__all__'
            

class s1000alteracaoinfoEnte(models.Model):
    s1000_alteracao_infoop = models.OneToOneField('s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop')
    def evento(self): return self.s1000_alteracao_infoop.evento()
    nmente = models.CharField(max_length=100)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDRPPS, max_length=1)
    subteto = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_SUBTETO)
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)
    #s1000_alteracao_infoente_custom#
    #s1000_alteracao_infoente_custom#
    class Meta:
        db_table = r's1000_alteracao_infoente'
        managed = True
        ordering = ['s1000_alteracao_infoop', 'nmente', 'uf', 'indrpps', 'subteto', 'vrsubteto']



class s1000alteracaoinfoEnteSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaoinfoEnte
        fields = '__all__'
            

class s1000alteracaoinfoOP(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    nrsiafi = models.CharField(max_length=6)
    indugrpps = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDUGRPPS, max_length=1)
    esferaop = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_ESFERAOP, blank=True, null=True)
    poderop = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_PODEROP)
    vrtetorem = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    ideefr = models.CharField(choices=CHOICES_S1000_ALTERACAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.nrsiafi) + ' - ' + unicode(self.indugrpps) + ' - ' + unicode(self.poderop) + ' - ' + unicode(self.vrtetorem) + ' - ' + unicode(self.ideefr)
    #s1000_alteracao_infoop_custom#
    #s1000_alteracao_infoop_custom#
    class Meta:
        db_table = r's1000_alteracao_infoop'
        managed = True
        ordering = ['s1000_alteracao', 'nrsiafi', 'indugrpps', 'poderop', 'vrtetorem', 'ideefr']



class s1000alteracaoinfoOPSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaoinfoOP
        fields = '__all__'
            

class s1000alteracaoinfoOrgInternacional(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDACORDOISENMULTA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indacordoisenmulta)
    #s1000_alteracao_infoorginternacional_custom#
    #s1000_alteracao_infoorginternacional_custom#
    class Meta:
        db_table = r's1000_alteracao_infoorginternacional'
        managed = True
        ordering = ['s1000_alteracao', 'indacordoisenmulta']



class s1000alteracaoinfoOrgInternacionalSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaoinfoOrgInternacional
        fields = '__all__'
            

class s1000alteracaonovaValidade(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
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
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.inivalid)
    #s1000_alteracao_novavalidade_custom#
    #s1000_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1000_alteracao_novavalidade'
        managed = True
        ordering = ['s1000_alteracao', 'inivalid']



class s1000alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaonovaValidade
        fields = '__all__'
            

class s1000alteracaosituacaoPF(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDSITPF)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpf)
    #s1000_alteracao_situacaopf_custom#
    #s1000_alteracao_situacaopf_custom#
    class Meta:
        db_table = r's1000_alteracao_situacaopf'
        managed = True
        ordering = ['s1000_alteracao', 'indsitpf']



class s1000alteracaosituacaoPFSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaosituacaoPF
        fields = '__all__'
            

class s1000alteracaosituacaoPJ(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDSITPJ)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpj)
    #s1000_alteracao_situacaopj_custom#
    #s1000_alteracao_situacaopj_custom#
    class Meta:
        db_table = r's1000_alteracao_situacaopj'
        managed = True
        ordering = ['s1000_alteracao', 'indsitpj']



class s1000alteracaosituacaoPJSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaosituacaoPJ
        fields = '__all__'
            

class s1000alteracaosoftwareHouse(models.Model):
    s1000_alteracao = models.ForeignKey('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone)
    #s1000_alteracao_softwarehouse_custom#
    #s1000_alteracao_softwarehouse_custom#
    class Meta:
        db_table = r's1000_alteracao_softwarehouse'
        managed = True
        ordering = ['s1000_alteracao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone']



class s1000alteracaosoftwareHouseSerializer(ModelSerializer):
    class Meta:
        model = s1000alteracaosoftwareHouse
        fields = '__all__'
            

class s1000exclusao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
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
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid)
    #s1000_exclusao_custom#
    #s1000_exclusao_custom#
    class Meta:
        db_table = r's1000_exclusao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid']



class s1000exclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1000exclusao
        fields = '__all__'
            

class s1000inclusao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    classtrib = models.CharField(choices=CHOICES_S1000_INCLUSAO_CLASSTRIB, max_length=2)
    natjurid = models.TextField(max_length=4, blank=True, null=True)
    indcoop = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDCOOP, blank=True, null=True)
    indconstr = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDCONSTR, blank=True, null=True)
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDDESFOLHA)
    indopccp = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDOPCCP, blank=True, null=True)
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDOPTREGELETRON)
    indented = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDENTED, max_length=1, blank=True, null=True)
    indett = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDETT, max_length=1)
    nrregett = models.CharField(max_length=30, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.indett) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)
    #s1000_inclusao_custom#
    #s1000_inclusao_custom#
    class Meta:
        db_table = r's1000_inclusao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid', 'nmrazao', 'classtrib', 'inddesfolha', 'indoptregeletron', 'indett', 'nmctt', 'cpfctt']



class s1000inclusaoSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusao
        fields = '__all__'
            

class s1000inclusaodadosIsencao(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    ideminlei = models.CharField(max_length=70)
    nrcertif = models.CharField(max_length=40)
    dtemiscertif = models.DateField()
    dtvenccertif = models.DateField()
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True)
    dtprotrenov = models.DateField(blank=True, null=True)
    dtdou = models.DateField(blank=True, null=True)
    pagdou = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif)
    #s1000_inclusao_dadosisencao_custom#
    #s1000_inclusao_dadosisencao_custom#
    class Meta:
        db_table = r's1000_inclusao_dadosisencao'
        managed = True
        ordering = ['s1000_inclusao', 'ideminlei', 'nrcertif', 'dtemiscertif', 'dtvenccertif']



class s1000inclusaodadosIsencaoSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaodadosIsencao
        fields = '__all__'
            

class s1000inclusaoinfoEFR(models.Model):
    s1000_inclusao_infoop = models.OneToOneField('s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop')
    def evento(self): return self.s1000_inclusao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_INCLUSAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDRPPS, max_length=1)
    prevcomp = models.CharField(choices=CHOICES_S1000_INCLUSAO_PREVCOMP, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.prevcomp)
    #s1000_inclusao_infoefr_custom#
    #s1000_inclusao_infoefr_custom#
    class Meta:
        db_table = r's1000_inclusao_infoefr'
        managed = True
        ordering = ['s1000_inclusao_infoop', 'ideefr', 'indrpps', 'prevcomp']



class s1000inclusaoinfoEFRSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaoinfoEFR
        fields = '__all__'
            

class s1000inclusaoinfoEnte(models.Model):
    s1000_inclusao_infoop = models.OneToOneField('s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop')
    def evento(self): return self.s1000_inclusao_infoop.evento()
    nmente = models.CharField(max_length=100)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDRPPS, max_length=1)
    subteto = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_SUBTETO)
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)
    #s1000_inclusao_infoente_custom#
    #s1000_inclusao_infoente_custom#
    class Meta:
        db_table = r's1000_inclusao_infoente'
        managed = True
        ordering = ['s1000_inclusao_infoop', 'nmente', 'uf', 'indrpps', 'subteto', 'vrsubteto']



class s1000inclusaoinfoEnteSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaoinfoEnte
        fields = '__all__'
            

class s1000inclusaoinfoOP(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    nrsiafi = models.CharField(max_length=6)
    indugrpps = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDUGRPPS, max_length=1)
    esferaop = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_ESFERAOP, blank=True, null=True)
    poderop = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_PODEROP)
    vrtetorem = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    ideefr = models.CharField(choices=CHOICES_S1000_INCLUSAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.nrsiafi) + ' - ' + unicode(self.indugrpps) + ' - ' + unicode(self.poderop) + ' - ' + unicode(self.vrtetorem) + ' - ' + unicode(self.ideefr)
    #s1000_inclusao_infoop_custom#
    #s1000_inclusao_infoop_custom#
    class Meta:
        db_table = r's1000_inclusao_infoop'
        managed = True
        ordering = ['s1000_inclusao', 'nrsiafi', 'indugrpps', 'poderop', 'vrtetorem', 'ideefr']



class s1000inclusaoinfoOPSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaoinfoOP
        fields = '__all__'
            

class s1000inclusaoinfoOrgInternacional(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDACORDOISENMULTA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indacordoisenmulta)
    #s1000_inclusao_infoorginternacional_custom#
    #s1000_inclusao_infoorginternacional_custom#
    class Meta:
        db_table = r's1000_inclusao_infoorginternacional'
        managed = True
        ordering = ['s1000_inclusao', 'indacordoisenmulta']



class s1000inclusaoinfoOrgInternacionalSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaoinfoOrgInternacional
        fields = '__all__'
            

class s1000inclusaosituacaoPF(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDSITPF)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpf)
    #s1000_inclusao_situacaopf_custom#
    #s1000_inclusao_situacaopf_custom#
    class Meta:
        db_table = r's1000_inclusao_situacaopf'
        managed = True
        ordering = ['s1000_inclusao', 'indsitpf']



class s1000inclusaosituacaoPFSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaosituacaoPF
        fields = '__all__'
            

class s1000inclusaosituacaoPJ(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDSITPJ)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpj)
    #s1000_inclusao_situacaopj_custom#
    #s1000_inclusao_situacaopj_custom#
    class Meta:
        db_table = r's1000_inclusao_situacaopj'
        managed = True
        ordering = ['s1000_inclusao', 'indsitpj']



class s1000inclusaosituacaoPJSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaosituacaoPJ
        fields = '__all__'
            

class s1000inclusaosoftwareHouse(models.Model):
    s1000_inclusao = models.ForeignKey('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone)
    #s1000_inclusao_softwarehouse_custom#
    #s1000_inclusao_softwarehouse_custom#
    class Meta:
        db_table = r's1000_inclusao_softwarehouse'
        managed = True
        ordering = ['s1000_inclusao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone']



class s1000inclusaosoftwareHouseSerializer(ModelSerializer):
    class Meta:
        model = s1000inclusaosoftwareHouse
        fields = '__all__'
            

#VIEWS_MODELS
