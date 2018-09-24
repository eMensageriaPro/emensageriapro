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



CHOICES_S5002_INDNIF = (
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF'),
)

CHOICES_S5002_INDRESBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S5002_TPCR = (
    (3533, u'3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pensão Pagos por Previdência Pública'),
    (47301, u'047301 - Renda e Proventos de Qualquer Natureza'),
    (56107, u'056107 - IRRF - Rendimento do Trabalho Assalariado no País/Ausente no Exterior a Serviço do País'),
    (56108, u'056108 - IRRF - Empregado Doméstico'),
    (56109, u'056109 - IRRF - Empregado Doméstico - 13º Sal Rescisão'),
    (56110, u'056110 - IRRF - Empregado doméstico - 13º salário'),
    (56111, u'056111 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'),
    (56112, u'056112 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário'),
    (56113, u'056113 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário rescisório'),
    (58806, u'058806 - IRRF - Rendimento do trabalho sem vínculo empregatício'),
    (61001, u'061001 - IRRF - Rendimentos relativos a prestação de serviços de transporte rodoviário internacional de carga, pagos a transportador autônomo PF residente no Paraguai'),
    (328006, u'328006 - IRRF - Serviços Prestados por associados de cooperativas de trabalho'),
    (356201, u'356201 - IRRF - Participação dos trabalhadores em Lucros ou Resultados (PLR)'),
)

class s5002basesIrrf(models.Model):
    s5002_infoirrf = models.ForeignKey('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    tpvalor = models.IntegerField()
    valor = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.tpvalor) + ' - ' + unicode(self.valor)
    #s5002_basesirrf_custom#
    #s5002_basesirrf_custom#
    class Meta:
        db_table = r's5002_basesirrf'
        managed = True
        ordering = ['s5002_infoirrf', 'tpvalor', 'valor']



class s5002basesIrrfSerializer(ModelSerializer):
    class Meta:
        model = s5002basesIrrf
        fields = '__all__'
            

class s5002idePgtoExt(models.Model):
    s5002_infoirrf = models.OneToOneField('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    codpais = models.TextField(max_length=3)
    indnif = models.IntegerField(choices=CHOICES_S5002_INDNIF)
    nifbenef = models.CharField(max_length=20, blank=True, null=True)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    complem = models.CharField(max_length=30, blank=True, null=True)
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
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.codpais) + ' - ' + unicode(self.indnif) + ' - ' + unicode(self.nifbenef) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complem) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s5002_idepgtoext_custom#
    #s5002_idepgtoext_custom#
    class Meta:
        db_table = r's5002_idepgtoext'
        managed = True
        ordering = ['s5002_infoirrf', 'codpais', 'indnif', 'nifbenef', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'nmcid', 'codpostal']



class s5002idePgtoExtSerializer(ModelSerializer):
    class Meta:
        model = s5002idePgtoExt
        fields = '__all__'
            

class s5002infoDep(models.Model):
    s5002_evtirrfbenef = models.OneToOneField('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef')
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_evtirrfbenef) + ' - ' + unicode(self.vrdeddep)
    #s5002_infodep_custom#
    #s5002_infodep_custom#
    class Meta:
        db_table = r's5002_infodep'
        managed = True
        ordering = ['s5002_evtirrfbenef', 'vrdeddep']



class s5002infoDepSerializer(ModelSerializer):
    class Meta:
        model = s5002infoDep
        fields = '__all__'
            

class s5002infoIrrf(models.Model):
    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef')
    codcateg = models.TextField(max_length=3, blank=True, null=True)
    indresbr = models.CharField(choices=CHOICES_S5002_INDRESBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_evtirrfbenef) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.indresbr)
    #s5002_infoirrf_custom#
    #s5002_infoirrf_custom#
    class Meta:
        db_table = r's5002_infoirrf'
        managed = True
        ordering = ['s5002_evtirrfbenef', 'codcateg', 'indresbr']



class s5002infoIrrfSerializer(ModelSerializer):
    class Meta:
        model = s5002infoIrrf
        fields = '__all__'
            

class s5002irrf(models.Model):
    s5002_infoirrf = models.ForeignKey('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    tpcr = models.IntegerField(choices=CHOICES_S5002_TPCR)
    vrirrfdesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrirrfdesc)
    #s5002_irrf_custom#
    #s5002_irrf_custom#
    class Meta:
        db_table = r's5002_irrf'
        managed = True
        ordering = ['s5002_infoirrf', 'tpcr', 'vrirrfdesc']



class s5002irrfSerializer(ModelSerializer):
    class Meta:
        model = s5002irrf
        fields = '__all__'
            

#VIEWS_MODELS
