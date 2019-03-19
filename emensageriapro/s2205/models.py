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

class s2205CNH(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nrregcnh = models.CharField(max_length=12)
    dtexped = models.DateField(blank=True, null=True)
    ufcnh = models.CharField(choices=ESTADOS, max_length=2)
    dtvalid = models.DateField()
    dtprihab = models.DateField(blank=True, null=True)
    categoriacnh = models.CharField(choices=CHOICES_S2205_CATEGORIACNH, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.categoriacnh)
    #s2205_cnh_custom#

    class Meta:
        # verbose_name = u'Informações da Carteira Nacional de Habilitação (CNH)'
        db_table = r's2205_cnh'       
        managed = True # s2205_cnh #
        unique_together = (
            #custom_unique_together_s2205_cnh#
            
        )
        index_together = (
            #custom_index_together_s2205_cnh
            #index_together_s2205_cnh
        )
        permissions = (
            ("can_view_s2205_cnh", "Can view s2205_cnh"),
            #custom_permissions_s2205_cnh
        )
        ordering = ['s2205_evtaltcadastral', 'nrregcnh', 'ufcnh', 'dtvalid', 'categoriacnh']



class s2205CNHSerializer(ModelSerializer):
    class Meta:
        model = s2205CNH
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205CTPS(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nrctps = models.CharField(max_length=11)
    seriectps = models.CharField(max_length=5)
    ufctps = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)
    #s2205_ctps_custom#

    class Meta:
        # verbose_name = u'Informações da Carteira de Trabalho e Previdência Social'
        db_table = r's2205_ctps'       
        managed = True # s2205_ctps #
        unique_together = (
            #custom_unique_together_s2205_ctps#
            
        )
        index_together = (
            #custom_index_together_s2205_ctps
            #index_together_s2205_ctps
        )
        permissions = (
            ("can_view_s2205_ctps", "Can view s2205_ctps"),
            #custom_permissions_s2205_ctps
        )
        ordering = ['s2205_evtaltcadastral', 'nrctps', 'seriectps', 'ufctps']



class s2205CTPSSerializer(ModelSerializer):
    class Meta:
        model = s2205CTPS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205OC(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nroc = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    dtvalid = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor)
    #s2205_oc_custom#

    class Meta:
        # verbose_name = u'Informações do número de registro em Órgão de Classe (OC)'
        db_table = r's2205_oc'       
        managed = True # s2205_oc #
        unique_together = (
            #custom_unique_together_s2205_oc#
            
        )
        index_together = (
            #custom_index_together_s2205_oc
            #index_together_s2205_oc
        )
        permissions = (
            ("can_view_s2205_oc", "Can view s2205_oc"),
            #custom_permissions_s2205_oc
        )
        ordering = ['s2205_evtaltcadastral', 'nroc', 'orgaoemissor']



class s2205OCSerializer(ModelSerializer):
    class Meta:
        model = s2205OC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205RG(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nrrg = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor)
    #s2205_rg_custom#

    class Meta:
        # verbose_name = u'Informações do Registro Geral (RG)'
        db_table = r's2205_rg'       
        managed = True # s2205_rg #
        unique_together = (
            #custom_unique_together_s2205_rg#
            
        )
        index_together = (
            #custom_index_together_s2205_rg
            #index_together_s2205_rg
        )
        permissions = (
            ("can_view_s2205_rg", "Can view s2205_rg"),
            #custom_permissions_s2205_rg
        )
        ordering = ['s2205_evtaltcadastral', 'nrrg', 'orgaoemissor']



class s2205RGSerializer(ModelSerializer):
    class Meta:
        model = s2205RG
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205RIC(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nrric = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor)
    #s2205_ric_custom#

    class Meta:
        # verbose_name = u'Informações do Documento Nacional de Identidade - DNI (Registro de Identificação Civil - RIC)'
        db_table = r's2205_ric'       
        managed = True # s2205_ric #
        unique_together = (
            #custom_unique_together_s2205_ric#
            
        )
        index_together = (
            #custom_index_together_s2205_ric
            #index_together_s2205_ric
        )
        permissions = (
            ("can_view_s2205_ric", "Can view s2205_ric"),
            #custom_permissions_s2205_ric
        )
        ordering = ['s2205_evtaltcadastral', 'nrric', 'orgaoemissor']



class s2205RICSerializer(ModelSerializer):
    class Meta:
        model = s2205RIC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205RNE(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    nrrne = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor)
    #s2205_rne_custom#

    class Meta:
        # verbose_name = u'Informações do Registro Nacional de Estrangeiro'
        db_table = r's2205_rne'       
        managed = True # s2205_rne #
        unique_together = (
            #custom_unique_together_s2205_rne#
            
        )
        index_together = (
            #custom_index_together_s2205_rne
            #index_together_s2205_rne
        )
        permissions = (
            ("can_view_s2205_rne", "Can view s2205_rne"),
            #custom_permissions_s2205_rne
        )
        ordering = ['s2205_evtaltcadastral', 'nrrne', 'orgaoemissor']



class s2205RNESerializer(ModelSerializer):
    class Meta:
        model = s2205RNE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205aposentadoria(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    trabaposent = models.CharField(choices=CHOICES_S2205_TRABAPOSENT, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.trabaposent)
    #s2205_aposentadoria_custom#

    class Meta:
        # verbose_name = u'Informação de aposentadoria do trabalhador'
        db_table = r's2205_aposentadoria'       
        managed = True # s2205_aposentadoria #
        unique_together = (
            #custom_unique_together_s2205_aposentadoria#
            
        )
        index_together = (
            #custom_index_together_s2205_aposentadoria
            #index_together_s2205_aposentadoria
        )
        permissions = (
            ("can_view_s2205_aposentadoria", "Can view s2205_aposentadoria"),
            #custom_permissions_s2205_aposentadoria
        )
        ordering = ['s2205_evtaltcadastral', 'trabaposent']



class s2205aposentadoriaSerializer(ModelSerializer):
    class Meta:
        model = s2205aposentadoria
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205brasil(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2205_brasil_custom#

    class Meta:
        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2205_brasil'       
        managed = True # s2205_brasil #
        unique_together = (
            #custom_unique_together_s2205_brasil#
            
        )
        index_together = (
            #custom_index_together_s2205_brasil
            #index_together_s2205_brasil
        )
        permissions = (
            ("can_view_s2205_brasil", "Can view s2205_brasil"),
            #custom_permissions_s2205_brasil
        )
        ordering = ['s2205_evtaltcadastral', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2205brasilSerializer(ModelSerializer):
    class Meta:
        model = s2205brasil
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205contato(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True)
    fonealternat = models.CharField(max_length=13, blank=True, null=True)
    emailprinc = models.CharField(max_length=60, blank=True, null=True)
    emailalternat = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral)
    #s2205_contato_custom#

    class Meta:
        # verbose_name = u'Informações de contato'
        db_table = r's2205_contato'       
        managed = True # s2205_contato #
        unique_together = (
            #custom_unique_together_s2205_contato#
            
        )
        index_together = (
            #custom_index_together_s2205_contato
            #index_together_s2205_contato
        )
        permissions = (
            ("can_view_s2205_contato", "Can view s2205_contato"),
            #custom_permissions_s2205_contato
        )
        ordering = ['s2205_evtaltcadastral']



class s2205contatoSerializer(ModelSerializer):
    class Meta:
        model = s2205contato
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205dependente(SoftDeletionModel):
    s2205_evtaltcadastral = models.ForeignKey('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    tpdep = models.CharField(choices=CHOICES_S2205_TPDEP, max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2205_SEXODEP, max_length=1, blank=True, null=True)
    depirrf = models.CharField(choices=CHOICES_S2205_DEPIRRF, max_length=1)
    depsf = models.CharField(choices=CHOICES_S2205_DEPSF, max_length=1)
    inctrab = models.CharField(choices=CHOICES_S2205_INCTRAB, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2205_DEPFINSPREV, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab)
    #s2205_dependente_custom#

    class Meta:
        # verbose_name = u'Informações dos dependentes'
        db_table = r's2205_dependente'       
        managed = True # s2205_dependente #
        unique_together = (
            #custom_unique_together_s2205_dependente#
            
        )
        index_together = (
            #custom_index_together_s2205_dependente
            #index_together_s2205_dependente
        )
        permissions = (
            ("can_view_s2205_dependente", "Can view s2205_dependente"),
            #custom_permissions_s2205_dependente
        )
        ordering = ['s2205_evtaltcadastral', 'tpdep', 'nmdep', 'dtnascto', 'depirrf', 'depsf', 'inctrab']



class s2205dependenteSerializer(ModelSerializer):
    class Meta:
        model = s2205dependente
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205exterior(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    paisresid = models.TextField(max_length=3)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)
    #s2205_exterior_custom#

    class Meta:
        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2205_exterior'       
        managed = True # s2205_exterior #
        unique_together = (
            #custom_unique_together_s2205_exterior#
            
        )
        index_together = (
            #custom_index_together_s2205_exterior
            #index_together_s2205_exterior
        )
        permissions = (
            ("can_view_s2205_exterior", "Can view s2205_exterior"),
            #custom_permissions_s2205_exterior
        )
        ordering = ['s2205_evtaltcadastral', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid']



class s2205exteriorSerializer(ModelSerializer):
    class Meta:
        model = s2205exterior
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205infoDeficiencia(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    deffisica = models.CharField(choices=CHOICES_S2205_DEFFISICA, max_length=1)
    defvisual = models.CharField(choices=CHOICES_S2205_DEFVISUAL, max_length=1)
    defauditiva = models.CharField(choices=CHOICES_S2205_DEFAUDITIVA, max_length=1)
    defmental = models.CharField(choices=CHOICES_S2205_DEFMENTAL, max_length=1)
    defintelectual = models.CharField(choices=CHOICES_S2205_DEFINTELECTUAL, max_length=1)
    reabreadap = models.CharField(choices=CHOICES_S2205_REABREADAP, max_length=1)
    infocota = models.CharField(choices=CHOICES_S2205_INFOCOTA, max_length=1, blank=True, null=True)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap)
    #s2205_infodeficiencia_custom#

    class Meta:
        # verbose_name = u'Pessoa com Deficiência'
        db_table = r's2205_infodeficiencia'       
        managed = True # s2205_infodeficiencia #
        unique_together = (
            #custom_unique_together_s2205_infodeficiencia#
            
        )
        index_together = (
            #custom_index_together_s2205_infodeficiencia
            #index_together_s2205_infodeficiencia
        )
        permissions = (
            ("can_view_s2205_infodeficiencia", "Can view s2205_infodeficiencia"),
            #custom_permissions_s2205_infodeficiencia
        )
        ordering = ['s2205_evtaltcadastral', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap']



class s2205infoDeficienciaSerializer(ModelSerializer):
    class Meta:
        model = s2205infoDeficiencia
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2205trabEstrangeiro(SoftDeletionModel):
    s2205_evtaltcadastral = models.OneToOneField('esocial.s2205evtAltCadastral',
        related_name='%(class)s_s2205_evtaltcadastral')
    def evento(self): return self.s2205_evtaltcadastral.evento()
    dtchegada = models.DateField(blank=True, null=True)
    classtrabestrang = models.IntegerField(choices=CHOICES_S2205_CLASSTRABESTRANG)
    casadobr = models.CharField(choices=CHOICES_S2205_CASADOBR, max_length=1)
    filhosbr = models.CharField(choices=CHOICES_S2205_FILHOSBR, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2205_evtaltcadastral) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)
    #s2205_trabestrangeiro_custom#

    class Meta:
        # verbose_name = u'Grupo de informações do Trabalhador Estrangeiro'
        db_table = r's2205_trabestrangeiro'       
        managed = True # s2205_trabestrangeiro #
        unique_together = (
            #custom_unique_together_s2205_trabestrangeiro#
            
        )
        index_together = (
            #custom_index_together_s2205_trabestrangeiro
            #index_together_s2205_trabestrangeiro
        )
        permissions = (
            ("can_view_s2205_trabestrangeiro", "Can view s2205_trabestrangeiro"),
            #custom_permissions_s2205_trabestrangeiro
        )
        ordering = ['s2205_evtaltcadastral', 'classtrabestrang', 'casadobr', 'filhosbr']



class s2205trabEstrangeiroSerializer(ModelSerializer):
    class Meta:
        model = s2205trabEstrangeiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
