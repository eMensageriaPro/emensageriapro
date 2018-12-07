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



CHOICES_S2200_CASADOBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_CATEGORIACNH = (
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

CHOICES_S2200_CLASSTRABESTRANG = (
    (1, u'1 - Visto permanente'),
    (10, u'10 - Beneficiado pelo acordo entre países do Mercosul'),
    (11, u'11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil'),
    (12, u'12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa'),
    (2, u'2 - Visto temporário'),
    (3, u'3 - Asilado'),
    (4, u'4 - Refugiado'),
    (5, u'5 - Solicitante de Refúgio'),
    (6, u'6 - Residente em país fronteiriço ao Brasil'),
    (7, u'7 - Deficiente físico e com mais de 51 anos'),
    (8, u'8 - Com residência provisória e anistiado, em situação irregular'),
    (9, u'9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros'),
)

CHOICES_S2200_CODMOTAFAST = (
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

CHOICES_S2200_DEFAUDITIVA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFFISICA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFINTELECTUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFMENTAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFVISUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEPFINSPREV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEPSF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DIA = (
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável'),
)

CHOICES_S2200_FILHOSBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_HIPLEG = (
    (1, u'1 - Necessidade de substituição transitória de pessoal permanente'),
    (2, u'2 - Demanda complementar de serviços'),
)

CHOICES_S2200_INCTRAB = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INDABONOPERM = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INDADMISSAO = (
    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Ação Fiscal'),
    (3, u'3 - Decorrente de Decisão Judicial'),
)

CHOICES_S2200_INDPARCREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INDPROVIM = (
    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Decisão Judicial'),
)

CHOICES_S2200_INDTETORGPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INFOCOTA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2200_OPCFGTS = (
    (1, u'1 - Optante'),
    (2, u'2 - Não Optante'),
)

CHOICES_S2200_REABREADAP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_SEXODEP = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2200_TMPPARC = (
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais'),
)

CHOICES_S2200_TPADMISSAO = (
    (1, u'1 - Admissão'),
    (2, u'2 - Transferência de empresa do mesmo grupo econômico'),
    (3, u'3 - Transferência de empresa consorciada ou de consórcio'),
    (4, u'4 - Transferência por motivo de sucessão, incorporação, cisão ou fusão'),
    (5, u'5 - Transferência do empregado doméstico para outro representante da mesma unidade familiar'),
)

CHOICES_S2200_TPDEP = (
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

CHOICES_S2200_TPINCLCONTR = (
    (1, u'1 - Locais sem filiais'),
    (2, u'2 - Estudo de mercado'),
    (3, u'3 - Contratação superior a 3 meses'),
)

CHOICES_S2200_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_TPJORNADA = (
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada'),
)

CHOICES_S2200_TPPLANRP = (
    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro'),
)

CHOICES_S2200_TPPROV = (
    (1, u'1 - Nomeação em cargo efetivo'),
    (2, u'2 - Nomeação em cargo em comissão'),
    (3, u'3 - Incorporação (militar)'),
    (4, u'4 - Matrícula (militar)'),
    (5, u'5 - Reinclusão (militar)'),
    (6, u'6 - Diplomação'),
    (99, u'99 - Outros não relacionados acima'),
)

CHOICES_S2200_TPREGJOR = (
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT'),
)

CHOICES_S2200_TRABAPOSENT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

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

class s2200CNH(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    nrregcnh = models.CharField(max_length=12)
    dtexped = models.DateField(blank=True, null=True)
    ufcnh = models.CharField(choices=ESTADOS, max_length=2)
    dtvalid = models.DateField()
    dtprihab = models.DateField(blank=True, null=True)
    categoriacnh = models.CharField(choices=CHOICES_S2200_CATEGORIACNH, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.categoriacnh)
    #s2200_cnh_custom#
    #s2200_cnh_custom#
    class Meta:
        db_table = r's2200_cnh'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh']



class s2200CNHSerializer(ModelSerializer):
    class Meta:
        model = s2200CNH
        fields = '__all__'
            

class s2200CTPS(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)
    #s2200_ctps_custom#
    #s2200_ctps_custom#
    class Meta:
        db_table = r's2200_ctps'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrctps', 'seriectps', 'ufctps']



class s2200CTPSSerializer(ModelSerializer):
    class Meta:
        model = s2200CTPS
        fields = '__all__'
            

class s2200OC(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor)
    #s2200_oc_custom#
    #s2200_oc_custom#
    class Meta:
        db_table = r's2200_oc'
        managed = True
        ordering = ['s2200_evtadmissao', 'nroc', 'orgaoemissor']



class s2200OCSerializer(ModelSerializer):
    class Meta:
        model = s2200OC
        fields = '__all__'
            

class s2200RG(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor)
    #s2200_rg_custom#
    #s2200_rg_custom#
    class Meta:
        db_table = r's2200_rg'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrrg', 'orgaoemissor']



class s2200RGSerializer(ModelSerializer):
    class Meta:
        model = s2200RG
        fields = '__all__'
            

class s2200RIC(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor)
    #s2200_ric_custom#
    #s2200_ric_custom#
    class Meta:
        db_table = r's2200_ric'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrric', 'orgaoemissor']



class s2200RICSerializer(ModelSerializer):
    class Meta:
        model = s2200RIC
        fields = '__all__'
            

class s2200RNE(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor)
    #s2200_rne_custom#
    #s2200_rne_custom#
    class Meta:
        db_table = r's2200_rne'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrrne', 'orgaoemissor']



class s2200RNESerializer(ModelSerializer):
    class Meta:
        model = s2200RNE
        fields = '__all__'
            

class s2200afastamento(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtiniafast = models.DateField()
    codmotafast = models.CharField(choices=CHOICES_S2200_CODMOTAFAST, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtiniafast) + ' - ' + unicode(self.codmotafast)
    #s2200_afastamento_custom#
    #s2200_afastamento_custom#
    class Meta:
        db_table = r's2200_afastamento'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtiniafast', 'codmotafast']



class s2200afastamentoSerializer(ModelSerializer):
    class Meta:
        model = s2200afastamento
        fields = '__all__'
            

class s2200alvaraJudicial(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrprocjud)
    #s2200_alvarajudicial_custom#
    #s2200_alvarajudicial_custom#
    class Meta:
        db_table = r's2200_alvarajudicial'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrprocjud']



class s2200alvaraJudicialSerializer(ModelSerializer):
    class Meta:
        model = s2200alvaraJudicial
        fields = '__all__'
            

class s2200aposentadoria(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    trabaposent = models.CharField(choices=CHOICES_S2200_TRABAPOSENT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.trabaposent)
    #s2200_aposentadoria_custom#
    #s2200_aposentadoria_custom#
    class Meta:
        db_table = r's2200_aposentadoria'
        managed = True
        ordering = ['s2200_evtadmissao', 'trabaposent']



class s2200aposentadoriaSerializer(ModelSerializer):
    class Meta:
        model = s2200aposentadoria
        fields = '__all__'
            

class s2200aprend(models.Model):
    s2200_infoceletista = models.OneToOneField('s2200infoCeletista',
        related_name='%(class)s_s2200_infoceletista')
    def evento(self): return self.s2200_infoceletista.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoceletista) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_aprend_custom#
    #s2200_aprend_custom#
    class Meta:
        db_table = r's2200_aprend'
        managed = True
        ordering = ['s2200_infoceletista', 'tpinsc', 'nrinsc']



class s2200aprendSerializer(ModelSerializer):
    class Meta:
        model = s2200aprend
        fields = '__all__'
            

class s2200brasil(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2200_brasil_custom#
    #s2200_brasil_custom#
    class Meta:
        db_table = r's2200_brasil'
        managed = True
        ordering = ['s2200_evtadmissao', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2200brasilSerializer(ModelSerializer):
    class Meta:
        model = s2200brasil
        fields = '__all__'
            

class s2200cessao(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtinicessao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtinicessao)
    #s2200_cessao_custom#
    #s2200_cessao_custom#
    class Meta:
        db_table = r's2200_cessao'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtinicessao']



class s2200cessaoSerializer(ModelSerializer):
    class Meta:
        model = s2200cessao
        fields = '__all__'
            

class s2200contato(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao)
    #s2200_contato_custom#
    #s2200_contato_custom#
    class Meta:
        db_table = r's2200_contato'
        managed = True
        ordering = ['s2200_evtadmissao']



class s2200contatoSerializer(ModelSerializer):
    class Meta:
        model = s2200contato
        fields = '__all__'
            

class s2200dependente(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tpdep = models.CharField(choices=CHOICES_S2200_TPDEP, max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2200_SEXODEP, max_length=1, blank=True, null=True)
    depirrf = models.CharField(choices=CHOICES_S2200_DEPIRRF, max_length=1)
    depsf = models.CharField(choices=CHOICES_S2200_DEPSF, max_length=1)
    inctrab = models.CharField(choices=CHOICES_S2200_INCTRAB, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2200_DEPFINSPREV, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab)
    #s2200_dependente_custom#
    #s2200_dependente_custom#
    class Meta:
        db_table = r's2200_dependente'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab']



class s2200dependenteSerializer(ModelSerializer):
    class Meta:
        model = s2200dependente
        fields = '__all__'
            

class s2200desligamento(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtdeslig = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtdeslig)
    #s2200_desligamento_custom#
    #s2200_desligamento_custom#
    class Meta:
        db_table = r's2200_desligamento'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtdeslig']



class s2200desligamentoSerializer(ModelSerializer):
    class Meta:
        model = s2200desligamento
        fields = '__all__'
            

class s2200exterior(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)
    #s2200_exterior_custom#
    #s2200_exterior_custom#
    class Meta:
        db_table = r's2200_exterior'
        managed = True
        ordering = ['s2200_evtadmissao', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid']



class s2200exteriorSerializer(ModelSerializer):
    class Meta:
        model = s2200exterior
        fields = '__all__'
            

class s2200filiacaoSindical(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cnpjsindtrab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cnpjsindtrab)
    #s2200_filiacaosindical_custom#
    #s2200_filiacaosindical_custom#
    class Meta:
        db_table = r's2200_filiacaosindical'
        managed = True
        ordering = ['s2200_evtadmissao', 'cnpjsindtrab']



class s2200filiacaoSindicalSerializer(ModelSerializer):
    class Meta:
        model = s2200filiacaoSindical
        fields = '__all__'
            

class s2200horContratual(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, max_length=4, blank=True, null=True)
    tpjornada = models.IntegerField(choices=CHOICES_S2200_TPJORNADA)
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True)
    tmpparc = models.IntegerField(choices=CHOICES_S2200_TMPPARC)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpjornada) + ' - ' + unicode(self.tmpparc)
    #s2200_horcontratual_custom#
    #s2200_horcontratual_custom#
    class Meta:
        db_table = r's2200_horcontratual'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpjornada', 'tmpparc']



class s2200horContratualSerializer(ModelSerializer):
    class Meta:
        model = s2200horContratual
        fields = '__all__'
            

class s2200horario(models.Model):
    s2200_horcontratual = models.ForeignKey('s2200horContratual',
        related_name='%(class)s_s2200_horcontratual')
    def evento(self): return self.s2200_horcontratual.evento()
    dia = models.IntegerField(choices=CHOICES_S2200_DIA)
    codhorcontrat = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_horcontratual) + ' - ' + unicode(self.dia) + ' - ' + unicode(self.codhorcontrat)
    #s2200_horario_custom#
    #s2200_horario_custom#
    class Meta:
        db_table = r's2200_horario'
        managed = True
        ordering = ['s2200_horcontratual', 'dia', 'codhorcontrat']



class s2200horarioSerializer(ModelSerializer):
    class Meta:
        model = s2200horario
        fields = '__all__'
            

class s2200ideEstabVinc(models.Model):
    s2200_trabtemporario = models.OneToOneField('s2200trabTemporario',
        related_name='%(class)s_s2200_trabtemporario')
    def evento(self): return self.s2200_trabtemporario.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_trabtemporario) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_ideestabvinc_custom#
    #s2200_ideestabvinc_custom#
    class Meta:
        db_table = r's2200_ideestabvinc'
        managed = True
        ordering = ['s2200_trabtemporario', 'tpinsc', 'nrinsc']



class s2200ideEstabVincSerializer(ModelSerializer):
    class Meta:
        model = s2200ideEstabVinc
        fields = '__all__'
            

class s2200ideTrabSubstituido(models.Model):
    s2200_trabtemporario = models.ForeignKey('s2200trabTemporario',
        related_name='%(class)s_s2200_trabtemporario')
    def evento(self): return self.s2200_trabtemporario.evento()
    cpftrabsubst = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_trabtemporario) + ' - ' + unicode(self.cpftrabsubst)
    #s2200_idetrabsubstituido_custom#
    #s2200_idetrabsubstituido_custom#
    class Meta:
        db_table = r's2200_idetrabsubstituido'
        managed = True
        ordering = ['s2200_trabtemporario', 'cpftrabsubst']



class s2200ideTrabSubstituidoSerializer(ModelSerializer):
    class Meta:
        model = s2200ideTrabSubstituido
        fields = '__all__'
            

class s2200infoCeletista(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtadm = models.DateField()
    tpadmissao = models.IntegerField(choices=CHOICES_S2200_TPADMISSAO)
    indadmissao = models.IntegerField(choices=CHOICES_S2200_INDADMISSAO)
    tpregjor = models.IntegerField(choices=CHOICES_S2200_TPREGJOR)
    natatividade = models.IntegerField(choices=CHOICES_S2200_NATATIVIDADE)
    dtbase = models.IntegerField(blank=True, null=True)
    cnpjsindcategprof = models.CharField(max_length=14)
    opcfgts = models.IntegerField(choices=CHOICES_S2200_OPCFGTS)
    dtopcfgts = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtadm) + ' - ' + unicode(self.tpadmissao) + ' - ' + unicode(self.indadmissao) + ' - ' + unicode(self.tpregjor) + ' - ' + unicode(self.natatividade) + ' - ' + unicode(self.cnpjsindcategprof) + ' - ' + unicode(self.opcfgts)
    #s2200_infoceletista_custom#
    #s2200_infoceletista_custom#
    class Meta:
        db_table = r's2200_infoceletista'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtadm', 'tpadmissao', 'indadmissao', 'tpregjor', 'natatividade', 'cnpjsindcategprof', 'opcfgts']



class s2200infoCeletistaSerializer(ModelSerializer):
    class Meta:
        model = s2200infoCeletista
        fields = '__all__'
            

class s2200infoDecJud(models.Model):
    s2200_infoestatutario = models.OneToOneField('s2200infoEstatutario',
        related_name='%(class)s_s2200_infoestatutario')
    def evento(self): return self.s2200_infoestatutario.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoestatutario) + ' - ' + unicode(self.nrprocjud)
    #s2200_infodecjud_custom#
    #s2200_infodecjud_custom#
    class Meta:
        db_table = r's2200_infodecjud'
        managed = True
        ordering = ['s2200_infoestatutario', 'nrprocjud']



class s2200infoDecJudSerializer(ModelSerializer):
    class Meta:
        model = s2200infoDecJud
        fields = '__all__'
            

class s2200infoDeficiencia(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    deffisica = models.CharField(choices=CHOICES_S2200_DEFFISICA, max_length=1)
    defvisual = models.CharField(choices=CHOICES_S2200_DEFVISUAL, max_length=1)
    defauditiva = models.CharField(choices=CHOICES_S2200_DEFAUDITIVA, max_length=1)
    defmental = models.CharField(choices=CHOICES_S2200_DEFMENTAL, max_length=1)
    defintelectual = models.CharField(choices=CHOICES_S2200_DEFINTELECTUAL, max_length=1)
    reabreadap = models.CharField(choices=CHOICES_S2200_REABREADAP, max_length=1)
    infocota = models.CharField(choices=CHOICES_S2200_INFOCOTA, max_length=1)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap) + ' - ' + unicode(self.infocota)
    #s2200_infodeficiencia_custom#
    #s2200_infodeficiencia_custom#
    class Meta:
        db_table = r's2200_infodeficiencia'
        managed = True
        ordering = ['s2200_evtadmissao', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap', 'infocota']



class s2200infoDeficienciaSerializer(ModelSerializer):
    class Meta:
        model = s2200infoDeficiencia
        fields = '__all__'
            

class s2200infoEstatutario(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    indprovim = models.IntegerField(choices=CHOICES_S2200_INDPROVIM)
    tpprov = models.IntegerField(choices=CHOICES_S2200_TPPROV)
    dtnomeacao = models.DateField()
    dtposse = models.DateField()
    dtexercicio = models.DateField()
    dtingsvpub = models.DateField()
    tpplanrp = models.IntegerField(choices=CHOICES_S2200_TPPLANRP, blank=True, null=True)
    indtetorgps = models.CharField(choices=CHOICES_S2200_INDTETORGPS, max_length=1, blank=True, null=True)
    indabonoperm = models.CharField(choices=CHOICES_S2200_INDABONOPERM, max_length=1, blank=True, null=True)
    dtiniabono = models.DateField(blank=True, null=True)
    indparcremun = models.CharField(choices=CHOICES_S2200_INDPARCREMUN, max_length=1, blank=True, null=True)
    dtiniparc = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.indprovim) + ' - ' + unicode(self.tpprov) + ' - ' + unicode(self.dtnomeacao) + ' - ' + unicode(self.dtposse) + ' - ' + unicode(self.dtexercicio) + ' - ' + unicode(self.dtingsvpub)
    #s2200_infoestatutario_custom#
    #s2200_infoestatutario_custom#
    class Meta:
        db_table = r's2200_infoestatutario'
        managed = True
        ordering = ['s2200_evtadmissao', 'indprovim', 'tpprov', 'dtnomeacao', 'dtposse', 'dtexercicio', 'dtingsvpub']



class s2200infoEstatutarioSerializer(ModelSerializer):
    class Meta:
        model = s2200infoEstatutario
        fields = '__all__'
            

class s2200localTrabDom(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2200_localtrabdom_custom#
    #s2200_localtrabdom_custom#
    class Meta:
        db_table = r's2200_localtrabdom'
        managed = True
        ordering = ['s2200_evtadmissao', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2200localTrabDomSerializer(ModelSerializer):
    class Meta:
        model = s2200localTrabDom
        fields = '__all__'
            

class s2200localTrabGeral(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    desccomp = models.CharField(max_length=80, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_localtrabgeral_custom#
    #s2200_localtrabgeral_custom#
    class Meta:
        db_table = r's2200_localtrabgeral'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpinsc', 'nrinsc']



class s2200localTrabGeralSerializer(ModelSerializer):
    class Meta:
        model = s2200localTrabGeral
        fields = '__all__'
            

class s2200mudancaCPF(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cpfant = models.CharField(max_length=11)
    matricant = models.CharField(max_length=30)
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cpfant) + ' - ' + unicode(self.matricant) + ' - ' + unicode(self.dtaltcpf)
    #s2200_mudancacpf_custom#
    #s2200_mudancacpf_custom#
    class Meta:
        db_table = r's2200_mudancacpf'
        managed = True
        ordering = ['s2200_evtadmissao', 'cpfant', 'matricant', 'dtaltcpf']



class s2200mudancaCPFSerializer(ModelSerializer):
    class Meta:
        model = s2200mudancaCPF
        fields = '__all__'
            

class s2200observacoes(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.observacao)
    #s2200_observacoes_custom#
    #s2200_observacoes_custom#
    class Meta:
        db_table = r's2200_observacoes'
        managed = True
        ordering = ['s2200_evtadmissao', 'observacao']



class s2200observacoesSerializer(ModelSerializer):
    class Meta:
        model = s2200observacoes
        fields = '__all__'
            

class s2200sucessaoVinc(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tpinscant = models.IntegerField()
    cnpjempregant = models.CharField(max_length=14)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dttransf = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpinscant) + ' - ' + unicode(self.cnpjempregant) + ' - ' + unicode(self.dttransf)
    #s2200_sucessaovinc_custom#
    #s2200_sucessaovinc_custom#
    class Meta:
        db_table = r's2200_sucessaovinc'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpinscant', 'cnpjempregant', 'dttransf']



class s2200sucessaoVincSerializer(ModelSerializer):
    class Meta:
        model = s2200sucessaoVinc
        fields = '__all__'
            

class s2200trabEstrangeiro(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtchegada = models.DateField(blank=True, null=True)
    classtrabestrang = models.IntegerField(choices=CHOICES_S2200_CLASSTRABESTRANG)
    casadobr = models.CharField(choices=CHOICES_S2200_CASADOBR, max_length=1)
    filhosbr = models.CharField(choices=CHOICES_S2200_FILHOSBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)
    #s2200_trabestrangeiro_custom#
    #s2200_trabestrangeiro_custom#
    class Meta:
        db_table = r's2200_trabestrangeiro'
        managed = True
        ordering = ['s2200_evtadmissao', 'classtrabestrang', 'casadobr', 'filhosbr']



class s2200trabEstrangeiroSerializer(ModelSerializer):
    class Meta:
        model = s2200trabEstrangeiro
        fields = '__all__'
            

class s2200trabTemporario(models.Model):
    s2200_infoceletista = models.OneToOneField('s2200infoCeletista',
        related_name='%(class)s_s2200_infoceletista')
    def evento(self): return self.s2200_infoceletista.evento()
    hipleg = models.IntegerField(choices=CHOICES_S2200_HIPLEG)
    justcontr = models.CharField(max_length=999)
    tpinclcontr = models.IntegerField(choices=CHOICES_S2200_TPINCLCONTR)
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoceletista) + ' - ' + unicode(self.hipleg) + ' - ' + unicode(self.justcontr) + ' - ' + unicode(self.tpinclcontr) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_trabtemporario_custom#
    #s2200_trabtemporario_custom#
    class Meta:
        db_table = r's2200_trabtemporario'
        managed = True
        ordering = ['s2200_infoceletista', 'hipleg', 'justcontr', 'tpinclcontr', 'tpinsc', 'nrinsc']



class s2200trabTemporarioSerializer(ModelSerializer):
    class Meta:
        model = s2200trabTemporario
        fields = '__all__'
            

class s2200transfDom(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cpfsubstituido = models.CharField(max_length=11)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dttransf = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cpfsubstituido) + ' - ' + unicode(self.dttransf)
    #s2200_transfdom_custom#
    #s2200_transfdom_custom#
    class Meta:
        db_table = r's2200_transfdom'
        managed = True
        ordering = ['s2200_evtadmissao', 'cpfsubstituido', 'dttransf']



class s2200transfDomSerializer(ModelSerializer):
    class Meta:
        model = s2200transfDom
        fields = '__all__'
            

#VIEWS_MODELS
