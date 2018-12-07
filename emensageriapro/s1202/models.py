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



CHOICES_S1202_INFOPERANT_TPACCONV = (
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('F', u'F - Outras verbas de natureza salarial ou não salarial devidas após o desligamento'),
    ('G', u'G - Decisão administrativa'),
    ('H', u'H - Decisão judicial'),
)

CHOICES_S1202_INFOPERANT_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1202_INFOPERAPUR_TPDEP = (
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

CHOICES_S1202_INFOPERAPUR_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1202_TPTRIB = (
    (2, u'2 - IRRF'),
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (4, u'4 - Contribuição sindical'),
)

class s1202dmDev(models.Model):
    s1202_evtrmnrpps = models.ForeignKey('esocial.s1202evtRmnRPPS',
        related_name='%(class)s_s1202_evtrmnrpps')
    def evento(self): return self.s1202_evtrmnrpps.evento()
    idedmdev = models.CharField(max_length=30)
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_evtrmnrpps) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.codcateg)
    #s1202_dmdev_custom#
    #s1202_dmdev_custom#
    class Meta:
        db_table = r's1202_dmdev'
        managed = True
        ordering = ['s1202_evtrmnrpps', 'idedmdev', 'codcateg']



class s1202dmDevSerializer(ModelSerializer):
    class Meta:
        model = s1202dmDev
        fields = '__all__'
            

class s1202infoPerAntideADC(models.Model):
    s1202_dmdev = models.ForeignKey('s1202dmDev',
        related_name='%(class)s_s1202_dmdev')
    def evento(self): return self.s1202_dmdev.evento()
    dtlei = models.DateField()
    nrlei = models.CharField(max_length=12)
    dtef = models.DateField(blank=True, null=True)
    dtacconv = models.DateField(blank=True, null=True)
    tpacconv = models.CharField(choices=CHOICES_S1202_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField(blank=True, null=True)
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_dmdev) + ' - ' + unicode(self.dtlei) + ' - ' + unicode(self.nrlei) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.dsc)
    #s1202_infoperant_ideadc_custom#
    #s1202_infoperant_ideadc_custom#
    class Meta:
        db_table = r's1202_infoperant_ideadc'
        managed = True
        ordering = ['s1202_dmdev', 'dtlei', 'nrlei', 'tpacconv', 'dsc']



class s1202infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerAntideADC
        fields = '__all__'
            

class s1202infoPerAntideEstab(models.Model):
    s1202_infoperant_ideperiodo = models.ForeignKey('s1202infoPerAntidePeriodo',
        related_name='%(class)s_s1202_infoperant_ideperiodo')
    def evento(self): return self.s1202_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1202_INFOPERANT_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1202_infoperant_ideestab_custom#
    #s1202_infoperant_ideestab_custom#
    class Meta:
        db_table = r's1202_infoperant_ideestab'
        managed = True
        ordering = ['s1202_infoperant_ideperiodo', 'tpinsc', 'nrinsc']



class s1202infoPerAntideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerAntideEstab
        fields = '__all__'
            

class s1202infoPerAntidePeriodo(models.Model):
    s1202_infoperant_ideadc = models.ForeignKey('s1202infoPerAntideADC',
        related_name='%(class)s_s1202_infoperant_ideadc')
    def evento(self): return self.s1202_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s1202_infoperant_ideperiodo_custom#
    #s1202_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's1202_infoperant_ideperiodo'
        managed = True
        ordering = ['s1202_infoperant_ideadc', 'perref']



class s1202infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerAntidePeriodo
        fields = '__all__'
            

class s1202infoPerAntitensRemun(models.Model):
    s1202_infoperant_remunperant = models.ForeignKey('s1202infoPerAntremunPerAnt',
        related_name='%(class)s_s1202_infoperant_remunperant')
    def evento(self): return self.s1202_infoperant_remunperant.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1202_infoperant_itensremun_custom#
    #s1202_infoperant_itensremun_custom#
    class Meta:
        db_table = r's1202_infoperant_itensremun'
        managed = True
        ordering = ['s1202_infoperant_remunperant', 'codrubr', 'idetabrubr', 'vrrubr']



class s1202infoPerAntitensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerAntitensRemun
        fields = '__all__'
            

class s1202infoPerAntremunPerAnt(models.Model):
    s1202_infoperant_ideestab = models.ForeignKey('s1202infoPerAntideEstab',
        related_name='%(class)s_s1202_infoperant_ideestab')
    def evento(self): return self.s1202_infoperant_ideestab.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperant_ideestab) + ' - ' + unicode(self.codcateg)
    #s1202_infoperant_remunperant_custom#
    #s1202_infoperant_remunperant_custom#
    class Meta:
        db_table = r's1202_infoperant_remunperant'
        managed = True
        ordering = ['s1202_infoperant_ideestab', 'codcateg']



class s1202infoPerAntremunPerAntSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerAntremunPerAnt
        fields = '__all__'
            

class s1202infoPerApurdetOper(models.Model):
    s1202_infoperapur_remunperapur = models.ForeignKey('s1202infoPerApurremunPerApur',
        related_name='%(class)s_s1202_infoperapur_remunperapur')
    def evento(self): return self.s1202_infoperapur_remunperapur.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperapur_remunperapur) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s1202_infoperapur_detoper_custom#
    #s1202_infoperapur_detoper_custom#
    class Meta:
        db_table = r's1202_infoperapur_detoper'
        managed = True
        ordering = ['s1202_infoperapur_remunperapur', 'cnpjoper', 'regans', 'vrpgtit']



class s1202infoPerApurdetOperSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerApurdetOper
        fields = '__all__'
            

class s1202infoPerApurdetPlano(models.Model):
    s1202_infoperapur_detoper = models.ForeignKey('s1202infoPerApurdetOper',
        related_name='%(class)s_s1202_infoperapur_detoper')
    def evento(self): return self.s1202_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S1202_INFOPERAPUR_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s1202_infoperapur_detplano_custom#
    #s1202_infoperapur_detplano_custom#
    class Meta:
        db_table = r's1202_infoperapur_detplano'
        managed = True
        ordering = ['s1202_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep']



class s1202infoPerApurdetPlanoSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerApurdetPlano
        fields = '__all__'
            

class s1202infoPerApurideEstab(models.Model):
    s1202_dmdev = models.ForeignKey('s1202dmDev',
        related_name='%(class)s_s1202_dmdev')
    def evento(self): return self.s1202_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1202_INFOPERAPUR_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1202_infoperapur_ideestab_custom#
    #s1202_infoperapur_ideestab_custom#
    class Meta:
        db_table = r's1202_infoperapur_ideestab'
        managed = True
        ordering = ['s1202_dmdev', 'tpinsc', 'nrinsc']



class s1202infoPerApurideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerApurideEstab
        fields = '__all__'
            

class s1202infoPerApuritensRemun(models.Model):
    s1202_infoperapur_remunperapur = models.ForeignKey('s1202infoPerApurremunPerApur',
        related_name='%(class)s_s1202_infoperapur_remunperapur')
    def evento(self): return self.s1202_infoperapur_remunperapur.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1202_infoperapur_itensremun_custom#
    #s1202_infoperapur_itensremun_custom#
    class Meta:
        db_table = r's1202_infoperapur_itensremun'
        managed = True
        ordering = ['s1202_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'vrrubr']



class s1202infoPerApuritensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerApuritensRemun
        fields = '__all__'
            

class s1202infoPerApurremunPerApur(models.Model):
    s1202_infoperapur_ideestab = models.ForeignKey('s1202infoPerApurideEstab',
        related_name='%(class)s_s1202_infoperapur_ideestab')
    def evento(self): return self.s1202_infoperapur_ideestab.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_infoperapur_ideestab) + ' - ' + unicode(self.codcateg)
    #s1202_infoperapur_remunperapur_custom#
    #s1202_infoperapur_remunperapur_custom#
    class Meta:
        db_table = r's1202_infoperapur_remunperapur'
        managed = True
        ordering = ['s1202_infoperapur_ideestab', 'codcateg']



class s1202infoPerApurremunPerApurSerializer(ModelSerializer):
    class Meta:
        model = s1202infoPerApurremunPerApur
        fields = '__all__'
            

class s1202procJudTrab(models.Model):
    s1202_evtrmnrpps = models.ForeignKey('esocial.s1202evtRmnRPPS',
        related_name='%(class)s_s1202_evtrmnrpps')
    def evento(self): return self.s1202_evtrmnrpps.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1202_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1202_evtrmnrpps) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s1202_procjudtrab_custom#
    #s1202_procjudtrab_custom#
    class Meta:
        db_table = r's1202_procjudtrab'
        managed = True
        ordering = ['s1202_evtrmnrpps', 'tptrib', 'nrprocjud']



class s1202procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s1202procJudTrab
        fields = '__all__'
            

#VIEWS_MODELS
