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

CHOICES_S2230_CODMOTAFAST = (
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

CHOICES_S2230_IDEOC = (
    (1, u'1 - Conselho Regional de Medicina (CRM)'),
    (2, u'2 - Conselho Regional de Odontologia (CRO)'),
    (3, u'3 - Registro do Ministério da Saúde (RMS)'),
)

CHOICES_S2230_INFOMESMOMTV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2230_INFONUS = (
    (1, u'1 - Ônus do Cedente'),
    (2, u'2 - Ônus do Cessionário'),
    (3, u'3 - Ônus do Cedente e Cessionário'),
)

CHOICES_S2230_INFONUSREMUN = (
    (1, u'1 - Apenas do Empregador'),
    (2, u'2 - Apenas do Sindicato'),
    (3, u'3 - Parte do Empregador, sendo a diferença e/ou complementação salarial paga pelo Sindicato'),
)

CHOICES_S2230_ORIGRETIF = (
    (1, u'1 - Por iniciativa do empregador'),
    (2, u'2 - Revisão Administrativa'),
    (3, u'3 - Determinação Judicial'),
)

CHOICES_S2230_TPACIDTRANSITO = (
    (1, u'1 - Atropelamento'),
    (2, u'2 - Colisão'),
    (3, u'3 - Outros'),
)

CHOICES_S2230_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (3, u'3 - Número de Benefício (NB) do INSS'),
)

class s2230emitente(models.Model):
    s2230_infoatestado = models.OneToOneField('s2230infoAtestado',
        related_name='%(class)s_s2230_infoatestado')
    def evento(self): return self.s2230_infoatestado.evento()
    nmemit = models.CharField(max_length=70)
    ideoc = models.IntegerField(choices=CHOICES_S2230_IDEOC)
    nroc = models.CharField(max_length=14)
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_infoatestado) + ' - ' + unicode(self.nmemit) + ' - ' + unicode(self.ideoc) + ' - ' + unicode(self.nroc)
    #s2230_emitente_custom#
    #s2230_emitente_custom#
    class Meta:
        db_table = r's2230_emitente'
        managed = True
        ordering = ['s2230_infoatestado', 'nmemit', 'ideoc', 'nroc']



class s2230emitenteSerializer(ModelSerializer):
    class Meta:
        model = s2230emitente
        fields = '__all__'
            

class s2230fimAfastamento(models.Model):
    s2230_evtafasttemp = models.OneToOneField('esocial.s2230evtAfastTemp',
        related_name='%(class)s_s2230_evtafasttemp')
    def evento(self): return self.s2230_evtafasttemp.evento()
    dttermafast = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_evtafasttemp) + ' - ' + unicode(self.dttermafast)
    #s2230_fimafastamento_custom#
    #s2230_fimafastamento_custom#
    class Meta:
        db_table = r's2230_fimafastamento'
        managed = True
        ordering = ['s2230_evtafasttemp', 'dttermafast']



class s2230fimAfastamentoSerializer(ModelSerializer):
    class Meta:
        model = s2230fimAfastamento
        fields = '__all__'
            

class s2230infoAtestado(models.Model):
    s2230_iniafastamento = models.ForeignKey('s2230iniAfastamento',
        related_name='%(class)s_s2230_iniafastamento')
    def evento(self): return self.s2230_iniafastamento.evento()
    codcid = models.CharField(max_length=4, blank=True, null=True)
    qtddiasafast = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_iniafastamento) + ' - ' + unicode(self.qtddiasafast)
    #s2230_infoatestado_custom#
    #s2230_infoatestado_custom#
    class Meta:
        db_table = r's2230_infoatestado'
        managed = True
        ordering = ['s2230_iniafastamento', 'qtddiasafast']



class s2230infoAtestadoSerializer(ModelSerializer):
    class Meta:
        model = s2230infoAtestado
        fields = '__all__'
            

class s2230infoCessao(models.Model):
    s2230_iniafastamento = models.OneToOneField('s2230iniAfastamento',
        related_name='%(class)s_s2230_iniafastamento')
    def evento(self): return self.s2230_iniafastamento.evento()
    cnpjcess = models.CharField(max_length=14)
    infonus = models.IntegerField(choices=CHOICES_S2230_INFONUS)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_iniafastamento) + ' - ' + unicode(self.cnpjcess) + ' - ' + unicode(self.infonus)
    #s2230_infocessao_custom#
    #s2230_infocessao_custom#
    class Meta:
        db_table = r's2230_infocessao'
        managed = True
        ordering = ['s2230_iniafastamento', 'cnpjcess', 'infonus']



class s2230infoCessaoSerializer(ModelSerializer):
    class Meta:
        model = s2230infoCessao
        fields = '__all__'
            

class s2230infoMandSind(models.Model):
    s2230_iniafastamento = models.OneToOneField('s2230iniAfastamento',
        related_name='%(class)s_s2230_iniafastamento')
    def evento(self): return self.s2230_iniafastamento.evento()
    cnpjsind = models.CharField(max_length=14)
    infonusremun = models.IntegerField(choices=CHOICES_S2230_INFONUSREMUN)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_iniafastamento) + ' - ' + unicode(self.cnpjsind) + ' - ' + unicode(self.infonusremun)
    #s2230_infomandsind_custom#
    #s2230_infomandsind_custom#
    class Meta:
        db_table = r's2230_infomandsind'
        managed = True
        ordering = ['s2230_iniafastamento', 'cnpjsind', 'infonusremun']



class s2230infoMandSindSerializer(ModelSerializer):
    class Meta:
        model = s2230infoMandSind
        fields = '__all__'
            

class s2230infoRetif(models.Model):
    s2230_evtafasttemp = models.OneToOneField('esocial.s2230evtAfastTemp',
        related_name='%(class)s_s2230_evtafasttemp')
    def evento(self): return self.s2230_evtafasttemp.evento()
    origretif = models.IntegerField(choices=CHOICES_S2230_ORIGRETIF)
    tpproc = models.IntegerField(choices=CHOICES_S2230_TPPROC, blank=True, null=True)
    nrproc = models.CharField(max_length=21, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_evtafasttemp) + ' - ' + unicode(self.origretif)
    #s2230_inforetif_custom#
    #s2230_inforetif_custom#
    class Meta:
        db_table = r's2230_inforetif'
        managed = True
        ordering = ['s2230_evtafasttemp', 'origretif']



class s2230infoRetifSerializer(ModelSerializer):
    class Meta:
        model = s2230infoRetif
        fields = '__all__'
            

class s2230iniAfastamento(models.Model):
    s2230_evtafasttemp = models.OneToOneField('esocial.s2230evtAfastTemp',
        related_name='%(class)s_s2230_evtafasttemp')
    def evento(self): return self.s2230_evtafasttemp.evento()
    dtiniafast = models.DateField()
    codmotafast = models.CharField(choices=CHOICES_S2230_CODMOTAFAST, max_length=2)
    infomesmomtv = models.CharField(choices=CHOICES_S2230_INFOMESMOMTV, max_length=1, blank=True, null=True)
    tpacidtransito = models.IntegerField(choices=CHOICES_S2230_TPACIDTRANSITO, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2230_evtafasttemp) + ' - ' + unicode(self.dtiniafast) + ' - ' + unicode(self.codmotafast)
    #s2230_iniafastamento_custom#
    #s2230_iniafastamento_custom#
    class Meta:
        db_table = r's2230_iniafastamento'
        managed = True
        ordering = ['s2230_evtafasttemp', 'dtiniafast', 'codmotafast']



class s2230iniAfastamentoSerializer(ModelSerializer):
    class Meta:
        model = s2230iniAfastamento
        fields = '__all__'
            

#VIEWS_MODELS
