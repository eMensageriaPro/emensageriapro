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

CHOICES_S2300_CASADOBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_CATEGORIACNH = (
    ('A', u'A - A'),
    ('AB', u'AB - AB'),
    ('AC', u'AC - AC'),
    ('AD', u'AD - AD'),
    ('AE', u'AE - AE'),
    ('B', u'B - B'),
    ('C', u'C - C'),
    ('D', u'D - D'),
    ('E', u'E - E'),
)

CHOICES_S2300_CLASSTRABESTRANG = (
    (1, u'1 - Visto permanente'),
    (10, u'10 - Beneficiado pelo acordo entre países do Mercosul'),
    (11, u'11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil'),
    (12, u'12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa'),
    (2, u'2 - Visto temporário'),
    (3, u'3 - Asilado'),
    (4, u'4 - Refugiado'),
    (5, u'5 - Solicitante de Refúgio'),
    (6, u'6 - Residente fora do Brasil'),
    (7, u'7 - Deficiente físico e com mais de 51 anos'),
    (8, u'8 - Com residência provisória e anistiado, em situação irregular'),
    (9, u'9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros'),
)

CHOICES_S2300_CODMOTAFAST = (
    ('01', u'01 - Acidente/Doença do trabalho'),
    ('03', u'03 - Acidente/Doença não relacionada ao trabalho'),
    ('05', u'05 - Afastamento/licença prevista em regime próprio (estatuto), sem remuneração'),
    ('06', u'06 - Aposentadoria por invalidez'),
    ('07', u'07 - Acompanhamento - Licença para acompanhamento de membro da família enfermo'),
    ('08', u'08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, §6º, Dec. 99.684/90 (Regulamento do FGTS)'),
    ('10', u'10 - Afastamento/licença prevista em regime próprio (estatuto), com remuneração'),
    ('11', u'11 - Cárcere'),
    ('12', u'12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25°, parágrafo único - Celetistas em geral'),
    ('13', u'13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1°, inciso II, alínea 1 - Servidor público, estatutário ou não, dos órgãos ou entidades da Administração Direta ou Indireta da União, dos Estados, do Distrito Federal, dos Muni (...)'),
    ('14', u'14 - Cessão / Requisição'),
    ('15', u'15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso'),
    ('16', u'16 - Licença remunerada - Lei, liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho'),
    ('17', u'17 - Licença Maternidade - 120 dias e suas prorrogações/antecipações, inclusive para o cônjuge sobrevivente'),
    ('18', u'18 - Licença Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente'),
    ('19', u'19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso'),
    ('20', u'20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança, inclusive para o cônjuge sobrevivente'),
    ('21', u'21 - Licença não remunerada ou Sem Vencimento'),
    ('22', u'22 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, sem remuneração'),
    ('23', u'23 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, com remuneração'),
    ('24', u'24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical'),
    ('25', u'25 - Mulher vítima de violência - Lei 11.340/2006 - art. 9º §2o, II - Lei Maria da Penha'),
    ('26', u'26 - Participação de empregado no Conselho Nacional de Previdência Social-CNPS (art. 3º, Lei 8.213/1991)'),
    ('27', u'27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT'),
    ('28', u'28 - Representante Sindical - Afastamento pelo tempo que se fizer necessário, quando, na qualidade de representante de entidade sindical, estiver participando de reunião oficial de organismo internacional do qual o Brasil seja membro'),
    ('29', u'29 - Serviço Militar - Afastamento temporário para prestar serviço militar obrigatório;'),
    ('30', u'30 - Suspensão disciplinar - CLT, art. 474'),
    ('31', u'31 - Servidor Público em Disponibilidade'),
    ('33', u'33 - Licença Maternidade - de 180 dias, Lei 13.301/2016.'),
    ('34', u'34 - Inatividade do trabalhador avulso (portuário ou não portuário) por período superior a 90 dias'),
)

CHOICES_S2300_DEFAUDITIVA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEFFISICA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEFINTELECTUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEFMENTAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEFVISUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEPFINSPREV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_DEPSF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_FILHOSBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_INCTRAB = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_INDREMUNCARGO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_INFONUS = (
    (1, u'1 - Ônus do Cedente'),
    (2, u'2 - Ônus do Cessionário'),
    (3, u'3 - Ônus do Cedente e Cessionário'),
)

CHOICES_S2300_NATESTAGIO = (
    ('N', u'N - Não Obrigatório'),
    ('O', u'O - Obrigatório'),
)

CHOICES_S2300_NIVESTAGIO = (
    (1, u'1 - Fundamental'),
    (2, u'2 - Médio'),
    (3, u'3 - Formação Profissional'),
    (4, u'4 - Superior'),
    (8, u'8 - Especial'),
    (9, u'9 - Mãe social (Lei 7644, de 1987)'),
)

CHOICES_S2300_OPCFGTS = (
    (1, u'1 - Optante'),
    (2, u'2 - Não Optante'),
)

CHOICES_S2300_REABREADAP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2300_SEXODEP = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2300_TPDEP = (
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

CHOICES_S2300_TPREGPREV = (
    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior'),
)

CHOICES_S2300_TPREGTRAB = (
    (1, u'1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas'),
    (2, u'2 - Estatutário'),
)

CHOICES_S2300_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

class s2300CNH(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nrregcnh = models.CharField(max_length=12)
    dtexped = models.DateField(blank=True, null=True)
    ufcnh = models.CharField(choices=ESTADOS, max_length=2)
    dtvalid = models.DateField()
    dtprihab = models.DateField(blank=True, null=True)
    categoriacnh = models.CharField(choices=CHOICES_S2300_CATEGORIACNH, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.categoriacnh)
    #s2300_cnh_custom#
    #s2300_cnh_custom#
    class Meta:
        db_table = r's2300_cnh'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh']



class s2300CNHSerializer(ModelSerializer):
    class Meta:
        model = s2300CNH
        fields = '__all__'
            

class s2300CTPS(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nrctps = models.CharField(max_length=11)
    seriectps = models.CharField(max_length=5)
    ufctps = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)
    #s2300_ctps_custom#
    #s2300_ctps_custom#
    class Meta:
        db_table = r's2300_ctps'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nrctps', 'seriectps', 'ufctps']



class s2300CTPSSerializer(ModelSerializer):
    class Meta:
        model = s2300CTPS
        fields = '__all__'
            

class s2300OC(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nroc = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    dtvalid = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor)
    #s2300_oc_custom#
    #s2300_oc_custom#
    class Meta:
        db_table = r's2300_oc'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nroc', 'orgaoemissor']



class s2300OCSerializer(ModelSerializer):
    class Meta:
        model = s2300OC
        fields = '__all__'
            

class s2300RG(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nrrg = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor)
    #s2300_rg_custom#
    #s2300_rg_custom#
    class Meta:
        db_table = r's2300_rg'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nrrg', 'orgaoemissor']



class s2300RGSerializer(ModelSerializer):
    class Meta:
        model = s2300RG
        fields = '__all__'
            

class s2300RIC(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nrric = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor)
    #s2300_ric_custom#
    #s2300_ric_custom#
    class Meta:
        db_table = r's2300_ric'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nrric', 'orgaoemissor']



class s2300RICSerializer(ModelSerializer):
    class Meta:
        model = s2300RIC
        fields = '__all__'
            

class s2300RNE(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    nrrne = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor)
    #s2300_rne_custom#
    #s2300_rne_custom#
    class Meta:
        db_table = r's2300_rne'
        managed = True
        ordering = ['s2300_evttsvinicio', 'nrrne', 'orgaoemissor']



class s2300RNESerializer(ModelSerializer):
    class Meta:
        model = s2300RNE
        fields = '__all__'
            

class s2300afastamento(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    dtiniafast = models.DateField()
    codmotafast = models.CharField(choices=CHOICES_S2300_CODMOTAFAST, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.dtiniafast) + ' - ' + unicode(self.codmotafast)
    #s2300_afastamento_custom#
    #s2300_afastamento_custom#
    class Meta:
        db_table = r's2300_afastamento'
        managed = True
        ordering = ['s2300_evttsvinicio', 'dtiniafast', 'codmotafast']



class s2300afastamentoSerializer(ModelSerializer):
    class Meta:
        model = s2300afastamento
        fields = '__all__'
            

class s2300ageIntegracao(models.Model):
    s2300_infoestagiario = models.OneToOneField('s2300infoEstagiario',
        related_name='%(class)s_s2300_infoestagiario')
    def evento(self): return self.s2300_infoestagiario.evento()
    cnpjagntinteg = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_infoestagiario) + ' - ' + unicode(self.cnpjagntinteg) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.uf)
    #s2300_ageintegracao_custom#
    #s2300_ageintegracao_custom#
    class Meta:
        db_table = r's2300_ageintegracao'
        managed = True
        ordering = ['s2300_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf']



class s2300ageIntegracaoSerializer(ModelSerializer):
    class Meta:
        model = s2300ageIntegracao
        fields = '__all__'
            

class s2300brasil(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2300_brasil_custom#
    #s2300_brasil_custom#
    class Meta:
        db_table = r's2300_brasil'
        managed = True
        ordering = ['s2300_evttsvinicio', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2300brasilSerializer(ModelSerializer):
    class Meta:
        model = s2300brasil
        fields = '__all__'
            

class s2300cargoFuncao(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    codcargo = models.CharField(max_length=30)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.codcargo)
    #s2300_cargofuncao_custom#
    #s2300_cargofuncao_custom#
    class Meta:
        db_table = r's2300_cargofuncao'
        managed = True
        ordering = ['s2300_evttsvinicio', 'codcargo']



class s2300cargoFuncaoSerializer(ModelSerializer):
    class Meta:
        model = s2300cargoFuncao
        fields = '__all__'
            

class s2300contato(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True)
    fonealternat = models.CharField(max_length=13, blank=True, null=True)
    emailprinc = models.CharField(max_length=60, blank=True, null=True)
    emailalternat = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio)
    #s2300_contato_custom#
    #s2300_contato_custom#
    class Meta:
        db_table = r's2300_contato'
        managed = True
        ordering = ['s2300_evttsvinicio']



class s2300contatoSerializer(ModelSerializer):
    class Meta:
        model = s2300contato
        fields = '__all__'
            

class s2300dependente(models.Model):
    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    tpdep = models.CharField(choices=CHOICES_S2300_TPDEP, max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2300_SEXODEP, max_length=1, blank=True, null=True)
    depirrf = models.CharField(choices=CHOICES_S2300_DEPIRRF, max_length=1)
    depsf = models.CharField(choices=CHOICES_S2300_DEPSF, max_length=1)
    inctrab = models.CharField(choices=CHOICES_S2300_INCTRAB, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2300_DEPFINSPREV, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab)
    #s2300_dependente_custom#
    #s2300_dependente_custom#
    class Meta:
        db_table = r's2300_dependente'
        managed = True
        ordering = ['s2300_evttsvinicio', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab']



class s2300dependenteSerializer(ModelSerializer):
    class Meta:
        model = s2300dependente
        fields = '__all__'
            

class s2300exterior(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    paisresid = models.TextField(max_length=3)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
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
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)
    #s2300_exterior_custom#
    #s2300_exterior_custom#
    class Meta:
        db_table = r's2300_exterior'
        managed = True
        ordering = ['s2300_evttsvinicio', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid']



class s2300exteriorSerializer(ModelSerializer):
    class Meta:
        model = s2300exterior
        fields = '__all__'
            

class s2300fgts(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    opcfgts = models.IntegerField(choices=CHOICES_S2300_OPCFGTS)
    dtopcfgts = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.opcfgts)
    #s2300_fgts_custom#
    #s2300_fgts_custom#
    class Meta:
        db_table = r's2300_fgts'
        managed = True
        ordering = ['s2300_evttsvinicio', 'opcfgts']



class s2300fgtsSerializer(ModelSerializer):
    class Meta:
        model = s2300fgts
        fields = '__all__'
            

class s2300infoDeficiencia(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    deffisica = models.CharField(choices=CHOICES_S2300_DEFFISICA, max_length=1)
    defvisual = models.CharField(choices=CHOICES_S2300_DEFVISUAL, max_length=1)
    defauditiva = models.CharField(choices=CHOICES_S2300_DEFAUDITIVA, max_length=1)
    defmental = models.CharField(choices=CHOICES_S2300_DEFMENTAL, max_length=1)
    defintelectual = models.CharField(choices=CHOICES_S2300_DEFINTELECTUAL, max_length=1)
    reabreadap = models.CharField(choices=CHOICES_S2300_REABREADAP, max_length=1)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap)
    #s2300_infodeficiencia_custom#
    #s2300_infodeficiencia_custom#
    class Meta:
        db_table = r's2300_infodeficiencia'
        managed = True
        ordering = ['s2300_evttsvinicio', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap']



class s2300infoDeficienciaSerializer(ModelSerializer):
    class Meta:
        model = s2300infoDeficiencia
        fields = '__all__'
            

class s2300infoDirigenteSindical(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    categorig = models.IntegerField()
    cnpjorigem = models.CharField(max_length=14, blank=True, null=True)
    dtadmorig = models.DateField(blank=True, null=True)
    matricorig = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.categorig)
    #s2300_infodirigentesindical_custom#
    #s2300_infodirigentesindical_custom#
    class Meta:
        db_table = r's2300_infodirigentesindical'
        managed = True
        ordering = ['s2300_evttsvinicio', 'categorig']



class s2300infoDirigenteSindicalSerializer(ModelSerializer):
    class Meta:
        model = s2300infoDirigenteSindical
        fields = '__all__'
            

class s2300infoEstagiario(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    natestagio = models.CharField(choices=CHOICES_S2300_NATESTAGIO, max_length=1)
    nivestagio = models.IntegerField(choices=CHOICES_S2300_NIVESTAGIO)
    areaatuacao = models.CharField(max_length=50, blank=True, null=True)
    nrapol = models.CharField(max_length=30, blank=True, null=True)
    vlrbolsa = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    dtprevterm = models.DateField()
    cnpjinstensino = models.CharField(max_length=14, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    dsclograd = models.CharField(max_length=100, blank=True, null=True)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.natestagio) + ' - ' + unicode(self.nivestagio) + ' - ' + unicode(self.dtprevterm) + ' - ' + unicode(self.nmrazao)
    #s2300_infoestagiario_custom#
    #s2300_infoestagiario_custom#
    class Meta:
        db_table = r's2300_infoestagiario'
        managed = True
        ordering = ['s2300_evttsvinicio', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao']



class s2300infoEstagiarioSerializer(ModelSerializer):
    class Meta:
        model = s2300infoEstagiario
        fields = '__all__'
            

class s2300infoTrabCedido(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    categorig = models.IntegerField()
    cnpjcednt = models.CharField(max_length=14)
    matricced = models.CharField(max_length=30)
    dtadmced = models.DateField()
    tpregtrab = models.IntegerField(choices=CHOICES_S2300_TPREGTRAB)
    tpregprev = models.IntegerField(choices=CHOICES_S2300_TPREGPREV)
    infonus = models.IntegerField(choices=CHOICES_S2300_INFONUS)
    indremuncargo = models.CharField(choices=CHOICES_S2300_INDREMUNCARGO, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.categorig) + ' - ' + unicode(self.cnpjcednt) + ' - ' + unicode(self.matricced) + ' - ' + unicode(self.dtadmced) + ' - ' + unicode(self.tpregtrab) + ' - ' + unicode(self.tpregprev) + ' - ' + unicode(self.infonus)
    #s2300_infotrabcedido_custom#
    #s2300_infotrabcedido_custom#
    class Meta:
        db_table = r's2300_infotrabcedido'
        managed = True
        ordering = ['s2300_evttsvinicio', 'categorig', 'cnpjcednt', 'matricced', 'dtadmced', 'tpregtrab', 'tpregprev', 'infonus']



class s2300infoTrabCedidoSerializer(ModelSerializer):
    class Meta:
        model = s2300infoTrabCedido
        fields = '__all__'
            

class s2300mudancaCPF(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    cpfant = models.CharField(max_length=11)
    dtaltcpf = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.cpfant) + ' - ' + unicode(self.dtaltcpf)
    #s2300_mudancacpf_custom#
    #s2300_mudancacpf_custom#
    class Meta:
        db_table = r's2300_mudancacpf'
        managed = True
        ordering = ['s2300_evttsvinicio', 'cpfant', 'dtaltcpf']



class s2300mudancaCPFSerializer(ModelSerializer):
    class Meta:
        model = s2300mudancaCPF
        fields = '__all__'
            

class s2300remuneracao(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2300_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo)
    #s2300_remuneracao_custom#
    #s2300_remuneracao_custom#
    class Meta:
        db_table = r's2300_remuneracao'
        managed = True
        ordering = ['s2300_evttsvinicio', 'vrsalfx', 'undsalfixo']



class s2300remuneracaoSerializer(ModelSerializer):
    class Meta:
        model = s2300remuneracao
        fields = '__all__'
            

class s2300supervisorEstagio(models.Model):
    s2300_infoestagiario = models.OneToOneField('s2300infoEstagiario',
        related_name='%(class)s_s2300_infoestagiario')
    def evento(self): return self.s2300_infoestagiario.evento()
    cpfsupervisor = models.CharField(max_length=11)
    nmsuperv = models.CharField(max_length=70)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_infoestagiario) + ' - ' + unicode(self.cpfsupervisor) + ' - ' + unicode(self.nmsuperv)
    #s2300_supervisorestagio_custom#
    #s2300_supervisorestagio_custom#
    class Meta:
        db_table = r's2300_supervisorestagio'
        managed = True
        ordering = ['s2300_infoestagiario', 'cpfsupervisor', 'nmsuperv']



class s2300supervisorEstagioSerializer(ModelSerializer):
    class Meta:
        model = s2300supervisorEstagio
        fields = '__all__'
            

class s2300termino(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    dtterm = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.dtterm)
    #s2300_termino_custom#
    #s2300_termino_custom#
    class Meta:
        db_table = r's2300_termino'
        managed = True
        ordering = ['s2300_evttsvinicio', 'dtterm']



class s2300terminoSerializer(ModelSerializer):
    class Meta:
        model = s2300termino
        fields = '__all__'
            

class s2300trabEstrangeiro(models.Model):
    s2300_evttsvinicio = models.OneToOneField('esocial.s2300evtTSVInicio',
        related_name='%(class)s_s2300_evttsvinicio')
    def evento(self): return self.s2300_evttsvinicio.evento()
    dtchegada = models.DateField(blank=True, null=True)
    classtrabestrang = models.IntegerField(choices=CHOICES_S2300_CLASSTRABESTRANG)
    casadobr = models.CharField(choices=CHOICES_S2300_CASADOBR, max_length=1)
    filhosbr = models.CharField(choices=CHOICES_S2300_FILHOSBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2300_evttsvinicio) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)
    #s2300_trabestrangeiro_custom#
    #s2300_trabestrangeiro_custom#
    class Meta:
        db_table = r's2300_trabestrangeiro'
        managed = True
        ordering = ['s2300_evttsvinicio', 'classtrabestrang', 'casadobr', 'filhosbr']



class s2300trabEstrangeiroSerializer(ModelSerializer):
    class Meta:
        model = s2300trabEstrangeiro
        fields = '__all__'
            

#VIEWS_MODELS
