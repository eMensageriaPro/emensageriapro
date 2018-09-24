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

CHOICES_R3010_CATEGEVENTO = (
    (1, u'1 - Internacional'),
    (2, u'2 - Interestadual'),
    (3, u'3 - Estadual'),
    (4, u'4 - Local'),
)

CHOICES_R3010_TPCOMPETICAO = (
    (1, u'1 - Oficial'),
    (2, u'2 - Não Oficial'),
)

CHOICES_R3010_TPINGRESSO = (
    (1, u'1 - Arquibancada'),
    (2, u'2 - Geral'),
    (3, u'3 - Cadeiras'),
    (4, u'4 - Camarote'),
)

CHOICES_R3010_TPINSCESTAB = (
    (1, u'1 - CNPJ'),
)

CHOICES_R3010_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R3010_TPRECEITA = (
    (1, u'1 - Transmissão'),
    (2, u'2 - Propaganda'),
    (3, u'3 - Publicidade'),
    (4, u'4 - Sorteio'),
    (5, u'5 - Outros'),
)

class r3010boletim(models.Model):
    r3010_ideestab = models.ForeignKey('r3010ideEstab',
        related_name='%(class)s_r3010_ideestab')
    def evento(self): return self.r3010_ideestab.evento()
    nrboletim = models.CharField(max_length=4)
    tpcompeticao = models.IntegerField(choices=CHOICES_R3010_TPCOMPETICAO)
    categevento = models.IntegerField(choices=CHOICES_R3010_CATEGEVENTO)
    moddesportiva = models.CharField(max_length=100)
    nomecompeticao = models.CharField(max_length=100)
    cnpjmandante = models.CharField(max_length=14)
    cnpjvisitante = models.CharField(max_length=14, blank=True, null=True)
    nomevisitante = models.CharField(max_length=80, blank=True, null=True)
    pracadesportiva = models.CharField(max_length=100)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    qtdepagantes = models.IntegerField()
    qtdenaopagantes = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r3010_ideestab) + ' - ' + unicode(self.nrboletim) + ' - ' + unicode(self.tpcompeticao) + ' - ' + unicode(self.categevento) + ' - ' + unicode(self.moddesportiva) + ' - ' + unicode(self.nomecompeticao) + ' - ' + unicode(self.cnpjmandante) + ' - ' + unicode(self.cnpjvisitante) + ' - ' + unicode(self.nomevisitante) + ' - ' + unicode(self.pracadesportiva) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.qtdepagantes) + ' - ' + unicode(self.qtdenaopagantes)
    #r3010_boletim_custom#
    #r3010_boletim_custom#
    class Meta:
        db_table = r'r3010_boletim'
        managed = True
        ordering = ['r3010_ideestab', 'nrboletim', 'tpcompeticao', 'categevento', 'moddesportiva', 'nomecompeticao', 'cnpjmandante', 'cnpjvisitante', 'nomevisitante', 'pracadesportiva', 'codmunic', 'uf', 'qtdepagantes', 'qtdenaopagantes']



class r3010boletimSerializer(ModelSerializer):
    class Meta:
        model = r3010boletim
        fields = '__all__'
            

class r3010ideEstab(models.Model):
    r3010_evtespdesportivo = models.ForeignKey('efdreinf.r3010evtEspDesportivo',
        related_name='%(class)s_r3010_evtespdesportivo')
    def evento(self): return self.r3010_evtespdesportivo.evento()
    tpinscestab = models.IntegerField(choices=CHOICES_R3010_TPINSCESTAB)
    nrinscestab = models.CharField(max_length=14)
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcpsusptotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrreceitaclubes = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretparc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r3010_evtespdesportivo) + ' - ' + unicode(self.tpinscestab) + ' - ' + unicode(self.nrinscestab) + ' - ' + unicode(self.vlrreceitatotal) + ' - ' + unicode(self.vlrcp) + ' - ' + unicode(self.vlrcpsusptotal) + ' - ' + unicode(self.vlrreceitaclubes) + ' - ' + unicode(self.vlrretparc)
    #r3010_ideestab_custom#
    #r3010_ideestab_custom#
    class Meta:
        db_table = r'r3010_ideestab'
        managed = True
        ordering = ['r3010_evtespdesportivo', 'tpinscestab', 'nrinscestab', 'vlrreceitatotal', 'vlrcp', 'vlrcpsusptotal', 'vlrreceitaclubes', 'vlrretparc']



class r3010ideEstabSerializer(ModelSerializer):
    class Meta:
        model = r3010ideEstab
        fields = '__all__'
            

class r3010infoProc(models.Model):
    r3010_ideestab = models.ForeignKey('r3010ideEstab',
        related_name='%(class)s_r3010_ideestab')
    def evento(self): return self.r3010_ideestab.evento()
    tpproc = models.IntegerField(choices=CHOICES_R3010_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r3010_ideestab) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vlrcpsusp)
    #r3010_infoproc_custom#
    #r3010_infoproc_custom#
    class Meta:
        db_table = r'r3010_infoproc'
        managed = True
        ordering = ['r3010_ideestab', 'tpproc', 'nrproc', 'codsusp', 'vlrcpsusp']



class r3010infoProcSerializer(ModelSerializer):
    class Meta:
        model = r3010infoProc
        fields = '__all__'
            

class r3010outrasReceitas(models.Model):
    r3010_boletim = models.ForeignKey('r3010boletim',
        related_name='%(class)s_r3010_boletim')
    def evento(self): return self.r3010_boletim.evento()
    tpreceita = models.IntegerField(choices=CHOICES_R3010_TPRECEITA)
    vlrreceita = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    descreceita = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r3010_boletim) + ' - ' + unicode(self.tpreceita) + ' - ' + unicode(self.vlrreceita) + ' - ' + unicode(self.descreceita)
    #r3010_outrasreceitas_custom#
    #r3010_outrasreceitas_custom#
    class Meta:
        db_table = r'r3010_outrasreceitas'
        managed = True
        ordering = ['r3010_boletim', 'tpreceita', 'vlrreceita', 'descreceita']



class r3010outrasReceitasSerializer(ModelSerializer):
    class Meta:
        model = r3010outrasReceitas
        fields = '__all__'
            

class r3010receitaIngressos(models.Model):
    r3010_boletim = models.ForeignKey('r3010boletim',
        related_name='%(class)s_r3010_boletim')
    def evento(self): return self.r3010_boletim.evento()
    tpingresso = models.IntegerField(choices=CHOICES_R3010_TPINGRESSO)
    descingr = models.CharField(max_length=30)
    qtdeingrvenda = models.IntegerField()
    qtdeingrvendidos = models.IntegerField()
    qtdeingrdev = models.IntegerField()
    precoindiv = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r3010_boletim) + ' - ' + unicode(self.tpingresso) + ' - ' + unicode(self.descingr) + ' - ' + unicode(self.qtdeingrvenda) + ' - ' + unicode(self.qtdeingrvendidos) + ' - ' + unicode(self.qtdeingrdev) + ' - ' + unicode(self.precoindiv) + ' - ' + unicode(self.vlrtotal)
    #r3010_receitaingressos_custom#
    #r3010_receitaingressos_custom#
    class Meta:
        db_table = r'r3010_receitaingressos'
        managed = True
        ordering = ['r3010_boletim', 'tpingresso', 'descingr', 'qtdeingrvenda', 'qtdeingrvendidos', 'qtdeingrdev', 'precoindiv', 'vlrtotal']



class r3010receitaIngressosSerializer(ModelSerializer):
    class Meta:
        model = r3010receitaIngressos
        fields = '__all__'
            

#VIEWS_MODELS
