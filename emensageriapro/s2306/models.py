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



CHOICES_S2306_INDREMUNCARGO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2306_NATESTAGIO = (
    ('N', u'N - Não Obrigatório'),
    ('O', u'O - Obrigatório'),
)

CHOICES_S2306_NIVESTAGIO = (
    (1, u'1 - Fundamental'),
    (2, u'2 - Médio'),
    (3, u'3 - Formação Profissional'),
    (4, u'4 - Superior'),
    (8, u'8 - Especial'),
    (9, u'9 - Mãe social (Lei 7644, de 1987)'),
)

CHOICES_S2306_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
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

class s2306ageIntegracao(SoftDeletionModel):
    s2306_infoestagiario = models.OneToOneField('s2306infoEstagiario',
        related_name='%(class)s_s2306_infoestagiario')
    def evento(self): return self.s2306_infoestagiario.evento()
    cnpjagntinteg = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_infoestagiario) + ' - ' + unicode(self.cnpjagntinteg) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.uf)
    #s2306_ageintegracao_custom#

    class Meta:
        db_table = r's2306_ageintegracao'       
        managed = True # s2306_ageintegracao #
        permissions = (
            ("can_view_s2306_ageintegracao", "Can view s2306_ageintegracao"),
            #custom_permissions_s2306_ageintegracao
        )
        ordering = ['s2306_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf']



class s2306ageIntegracaoSerializer(ModelSerializer):
    class Meta:
        model = s2306ageIntegracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306cargoFuncao(SoftDeletionModel):
    s2306_evttsvaltcontr = models.OneToOneField('esocial.s2306evtTSVAltContr',
        related_name='%(class)s_s2306_evttsvaltcontr')
    def evento(self): return self.s2306_evttsvaltcontr.evento()
    codcargo = models.CharField(max_length=30)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_evttsvaltcontr) + ' - ' + unicode(self.codcargo)
    #s2306_cargofuncao_custom#

    class Meta:
        db_table = r's2306_cargofuncao'       
        managed = True # s2306_cargofuncao #
        permissions = (
            ("can_view_s2306_cargofuncao", "Can view s2306_cargofuncao"),
            #custom_permissions_s2306_cargofuncao
        )
        ordering = ['s2306_evttsvaltcontr', 'codcargo']



class s2306cargoFuncaoSerializer(ModelSerializer):
    class Meta:
        model = s2306cargoFuncao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306infoEstagiario(SoftDeletionModel):
    s2306_evttsvaltcontr = models.OneToOneField('esocial.s2306evtTSVAltContr',
        related_name='%(class)s_s2306_evttsvaltcontr')
    def evento(self): return self.s2306_evttsvaltcontr.evento()
    natestagio = models.CharField(choices=CHOICES_S2306_NATESTAGIO, max_length=1)
    nivestagio = models.IntegerField(choices=CHOICES_S2306_NIVESTAGIO)
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
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_evttsvaltcontr) + ' - ' + unicode(self.natestagio) + ' - ' + unicode(self.nivestagio) + ' - ' + unicode(self.dtprevterm) + ' - ' + unicode(self.nmrazao)
    #s2306_infoestagiario_custom#

    class Meta:
        db_table = r's2306_infoestagiario'       
        managed = True # s2306_infoestagiario #
        permissions = (
            ("can_view_s2306_infoestagiario", "Can view s2306_infoestagiario"),
            #custom_permissions_s2306_infoestagiario
        )
        ordering = ['s2306_evttsvaltcontr', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao']



class s2306infoEstagiarioSerializer(ModelSerializer):
    class Meta:
        model = s2306infoEstagiario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306infoTrabCedido(SoftDeletionModel):
    s2306_evttsvaltcontr = models.OneToOneField('esocial.s2306evtTSVAltContr',
        related_name='%(class)s_s2306_evttsvaltcontr')
    def evento(self): return self.s2306_evttsvaltcontr.evento()
    indremuncargo = models.CharField(choices=CHOICES_S2306_INDREMUNCARGO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_evttsvaltcontr) + ' - ' + unicode(self.indremuncargo)
    #s2306_infotrabcedido_custom#

    class Meta:
        db_table = r's2306_infotrabcedido'       
        managed = True # s2306_infotrabcedido #
        permissions = (
            ("can_view_s2306_infotrabcedido", "Can view s2306_infotrabcedido"),
            #custom_permissions_s2306_infotrabcedido
        )
        ordering = ['s2306_evttsvaltcontr', 'indremuncargo']



class s2306infoTrabCedidoSerializer(ModelSerializer):
    class Meta:
        model = s2306infoTrabCedido
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306remuneracao(SoftDeletionModel):
    s2306_evttsvaltcontr = models.OneToOneField('esocial.s2306evtTSVAltContr',
        related_name='%(class)s_s2306_evttsvaltcontr')
    def evento(self): return self.s2306_evttsvaltcontr.evento()
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2306_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_evttsvaltcontr) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo)
    #s2306_remuneracao_custom#

    class Meta:
        db_table = r's2306_remuneracao'       
        managed = True # s2306_remuneracao #
        permissions = (
            ("can_view_s2306_remuneracao", "Can view s2306_remuneracao"),
            #custom_permissions_s2306_remuneracao
        )
        ordering = ['s2306_evttsvaltcontr', 'vrsalfx', 'undsalfixo']



class s2306remuneracaoSerializer(ModelSerializer):
    class Meta:
        model = s2306remuneracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2306supervisorEstagio(SoftDeletionModel):
    s2306_infoestagiario = models.OneToOneField('s2306infoEstagiario',
        related_name='%(class)s_s2306_infoestagiario')
    def evento(self): return self.s2306_infoestagiario.evento()
    cpfsupervisor = models.CharField(max_length=11)
    nmsuperv = models.CharField(max_length=70)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2306_infoestagiario) + ' - ' + unicode(self.cpfsupervisor) + ' - ' + unicode(self.nmsuperv)
    #s2306_supervisorestagio_custom#

    class Meta:
        db_table = r's2306_supervisorestagio'       
        managed = True # s2306_supervisorestagio #
        permissions = (
            ("can_view_s2306_supervisorestagio", "Can view s2306_supervisorestagio"),
            #custom_permissions_s2306_supervisorestagio
        )
        ordering = ['s2306_infoestagiario', 'cpfsupervisor', 'nmsuperv']



class s2306supervisorEstagioSerializer(ModelSerializer):
    class Meta:
        model = s2306supervisorEstagio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
