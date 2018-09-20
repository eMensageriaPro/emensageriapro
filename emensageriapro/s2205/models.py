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

CHOICES_S2205_CASADOBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_CATEGORIACNH = (
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

CHOICES_S2205_CLASSTRABESTRANG = (
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

CHOICES_S2205_DEFAUDITIVA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEFFISICA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEFINTELECTUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEFMENTAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEFVISUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEPFINSPREV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_DEPSF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_FILHOSBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_INCTRAB = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_INFOCOTA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_REABREADAP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2205_SEXODEP = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

CHOICES_S2205_TPDEP = (
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

CHOICES_S2205_TRABAPOSENT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

class s2205CNH(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
    nrregcnh = models.CharField(max_length=12)
    dtexped = models.DateField(blank=True, null=True)
    ufcnh = models.CharField(choices=ESTADOS, max_length=2)
    dtvalid = models.DateField()
    dtprihab = models.DateField(blank=True, null=True)
    categoriacnh = models.CharField(choices=CHOICES_S2205_CATEGORIACNH, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.dtexped) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.dtprihab) + ' - ' + unicode(self.categoriacnh)
    #s2205_cnh_custom#
    #s2205_cnh_custom#
    class Meta:
        db_table = r's2205_cnh'
        managed = True
        ordering = ['s2205_documentos', 'nrregcnh', 'dtexped', 'ufcnh', 'dtvalid', 'dtprihab', 'categoriacnh']


class s2205CTPS(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
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
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)
    #s2205_ctps_custom#
    #s2205_ctps_custom#
    class Meta:
        db_table = r's2205_ctps'
        managed = True
        ordering = ['s2205_documentos', 'nrctps', 'seriectps', 'ufctps']


class s2205OC(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
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
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped) + ' - ' + unicode(self.dtvalid)
    #s2205_oc_custom#
    #s2205_oc_custom#
    class Meta:
        db_table = r's2205_oc'
        managed = True
        ordering = ['s2205_documentos', 'nroc', 'orgaoemissor', 'dtexped', 'dtvalid']


class s2205RG(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
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
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2205_rg_custom#
    #s2205_rg_custom#
    class Meta:
        db_table = r's2205_rg'
        managed = True
        ordering = ['s2205_documentos', 'nrrg', 'orgaoemissor', 'dtexped']


class s2205RIC(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
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
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2205_ric_custom#
    #s2205_ric_custom#
    class Meta:
        db_table = r's2205_ric'
        managed = True
        ordering = ['s2205_documentos', 'nrric', 'orgaoemissor', 'dtexped']


class s2205RNE(models.Model):
    s2205_documentos = models.OneToOneField('s2205documentos',
        related_name='%(class)s_s2205_documentos')
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
        return unicode(self.s2205_documentos) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2205_rne_custom#
    #s2205_rne_custom#
    class Meta:
        db_table = r's2205_rne'
        managed = True
        ordering = ['s2205_documentos', 'nrrne', 'orgaoemissor', 'dtexped']


class s2205aposentadoria(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    trabaposent = models.CharField(choices=CHOICES_S2205_TRABAPOSENT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.trabaposent)
    #s2205_aposentadoria_custom#
    #s2205_aposentadoria_custom#
    class Meta:
        db_table = r's2205_aposentadoria'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'trabaposent']


class s2205brasil(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
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
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2205_brasil_custom#
    #s2205_brasil_custom#
    class Meta:
        db_table = r's2205_brasil'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']


class s2205contato(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
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
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.foneprinc) + ' - ' + unicode(self.fonealternat) + ' - ' + unicode(self.emailprinc) + ' - ' + unicode(self.emailalternat)
    #s2205_contato_custom#
    #s2205_contato_custom#
    class Meta:
        db_table = r's2205_contato'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'foneprinc', 'fonealternat', 'emailprinc', 'emailalternat']


class s2205dependente(models.Model):
    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    tpdep = models.CharField(choices=CHOICES_S2205_TPDEP, max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2205_SEXODEP, max_length=1, blank=True, null=True)
    depirrf = models.CharField(choices=CHOICES_S2205_DEPIRRF, max_length=1)
    depsf = models.CharField(choices=CHOICES_S2205_DEPSF, max_length=1)
    inctrab = models.CharField(choices=CHOICES_S2205_INCTRAB, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2205_DEPFINSPREV, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.sexodep) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab) + ' - ' + unicode(self.depfinsprev)
    #s2205_dependente_custom#
    #s2205_dependente_custom#
    class Meta:
        db_table = r's2205_dependente'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'depsf', 'inctrab', 'depfinsprev']


class s2205documentos(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral)
    #s2205_documentos_custom#
    #s2205_documentos_custom#
    class Meta:
        db_table = r's2205_documentos'
        managed = True
        ordering = ['s2205_evtaltcadastral']


class s2205exterior(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
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
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s2205_exterior_custom#
    #s2205_exterior_custom#
    class Meta:
        db_table = r's2205_exterior'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal']


class s2205infoDeficiencia(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    deffisica = models.CharField(choices=CHOICES_S2205_DEFFISICA, max_length=1)
    defvisual = models.CharField(choices=CHOICES_S2205_DEFVISUAL, max_length=1)
    defauditiva = models.CharField(choices=CHOICES_S2205_DEFAUDITIVA, max_length=1)
    defmental = models.CharField(choices=CHOICES_S2205_DEFMENTAL, max_length=1)
    defintelectual = models.CharField(choices=CHOICES_S2205_DEFINTELECTUAL, max_length=1)
    reabreadap = models.CharField(choices=CHOICES_S2205_REABREADAP, max_length=1)
    infocota = models.CharField(choices=CHOICES_S2205_INFOCOTA, max_length=1, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap) + ' - ' + unicode(self.infocota) + ' - ' + unicode(self.observacao)
    #s2205_infodeficiencia_custom#
    #s2205_infodeficiencia_custom#
    class Meta:
        db_table = r's2205_infodeficiencia'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap', 'infocota', 'observacao']


class s2205trabEstrangeiro(models.Model):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    dtchegada = models.DateField(blank=True, null=True)
    classtrabestrang = models.IntegerField(choices=CHOICES_S2205_CLASSTRABESTRANG)
    casadobr = models.CharField(choices=CHOICES_S2205_CASADOBR, max_length=1)
    filhosbr = models.CharField(choices=CHOICES_S2205_FILHOSBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.dtchegada) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)
    #s2205_trabestrangeiro_custom#
    #s2205_trabestrangeiro_custom#
    class Meta:
        db_table = r's2205_trabestrangeiro'
        managed = True
        ordering = ['s2205_evtaltcadastral', 'dtchegada', 'classtrabestrang', 'casadobr', 'filhosbr']


#VIEWS_MODELS
