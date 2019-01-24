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



CHOICES_S2405_DEPFINSPREV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_INCFISMEN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_SEXODEP = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
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

class s2405brasil(models.Model):
    s2405_evtcdbenefalt = models.OneToOneField('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt')
    def evento(self): return self.s2405_evtcdbenefalt.evento()
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=80)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2405_brasil_custom#
    class Meta:
        db_table = r's2405_brasil'
        managed = True # s2405_brasil #
        ordering = ['s2405_evtcdbenefalt', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf']



class s2405brasilSerializer(ModelSerializer):
    class Meta:
        model = s2405brasil
        fields = '__all__'
            

class s2405dependente(models.Model):
    s2405_evtcdbenefalt = models.ForeignKey('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt')
    def evento(self): return self.s2405_evtcdbenefalt.evento()
    tpdep = models.CharField(max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2405_SEXODEP, max_length=1)
    depirrf = models.CharField(choices=CHOICES_S2405_DEPIRRF, max_length=1)
    incfismen = models.CharField(choices=CHOICES_S2405_INCFISMEN, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2405_DEPFINSPREV, max_length=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.sexodep) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.incfismen) + ' - ' + unicode(self.depfinsprev)
    #s2405_dependente_custom#
    class Meta:
        db_table = r's2405_dependente'
        managed = True # s2405_dependente #
        ordering = ['s2405_evtcdbenefalt', 'tpdep', 'nmdep', 'dtnascto', 'sexodep', 'depirrf', 'incfismen', 'depfinsprev']



class s2405dependenteSerializer(ModelSerializer):
    class Meta:
        model = s2405dependente
        fields = '__all__'
            

class s2405exterior(models.Model):
    s2405_evtcdbenefalt = models.OneToOneField('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt')
    def evento(self): return self.s2405_evtcdbenefalt.evento()
    paisresid = models.TextField(max_length=3)
    dsclograd = models.CharField(max_length=80)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.nmcid)
    #s2405_exterior_custom#
    class Meta:
        db_table = r's2405_exterior'
        managed = True # s2405_exterior #
        ordering = ['s2405_evtcdbenefalt', 'paisresid', 'dsclograd', 'nrlograd', 'nmcid']



class s2405exteriorSerializer(ModelSerializer):
    class Meta:
        model = s2405exterior
        fields = '__all__'
            

#VIEWS_MODELS
