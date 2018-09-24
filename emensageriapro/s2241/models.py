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



class s2241altAposentEsp(models.Model):
    s2241_aposentesp = models.OneToOneField('s2241aposentEsp',
        related_name='%(class)s_s2241_aposentesp')
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_aposentesp) + ' - ' + unicode(self.dtaltcondicao)
    #s2241_altaposentesp_custom#
    #s2241_altaposentesp_custom#
    class Meta:
        db_table = r's2241_altaposentesp'
        managed = True
        ordering = ['s2241_aposentesp', 'dtaltcondicao']



class s2241altAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEsp
        fields = '__all__'
            

class s2241altAposentEspfatRisco(models.Model):
    s2241_altaposentesp_infoamb = models.ForeignKey('s2241altAposentEspinfoamb',
        related_name='%(class)s_s2241_altaposentesp_infoamb')
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_altaposentesp_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_altaposentesp_fatrisco_custom#
    #s2241_altaposentesp_fatrisco_custom#
    class Meta:
        db_table = r's2241_altaposentesp_fatrisco'
        managed = True
        ordering = ['s2241_altaposentesp_infoamb', 'codfatris']



class s2241altAposentEspfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEspfatRisco
        fields = '__all__'
            

class s2241altAposentEspinfoamb(models.Model):
    s2241_altaposentesp = models.ForeignKey('s2241altAposentEsp',
        related_name='%(class)s_s2241_altaposentesp')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_altaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_altaposentesp_infoamb_custom#
    #s2241_altaposentesp_infoamb_custom#
    class Meta:
        db_table = r's2241_altaposentesp_infoamb'
        managed = True
        ordering = ['s2241_altaposentesp', 'codamb']



class s2241altAposentEspinfoambSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEspinfoamb
        fields = '__all__'
            

class s2241altInsalPeric(models.Model):
    s2241_insalperic = models.OneToOneField('s2241insalPeric',
        related_name='%(class)s_s2241_insalperic')
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_insalperic) + ' - ' + unicode(self.dtaltcondicao)
    #s2241_altinsalperic_custom#
    #s2241_altinsalperic_custom#
    class Meta:
        db_table = r's2241_altinsalperic'
        managed = True
        ordering = ['s2241_insalperic', 'dtaltcondicao']



class s2241altInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPeric
        fields = '__all__'
            

class s2241altInsalPericfatRisco(models.Model):
    s2241_altinsalperic_infoamb = models.ForeignKey('s2241altInsalPericinfoamb',
        related_name='%(class)s_s2241_altinsalperic_infoamb')
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_altinsalperic_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_altinsalperic_fatrisco_custom#
    #s2241_altinsalperic_fatrisco_custom#
    class Meta:
        db_table = r's2241_altinsalperic_fatrisco'
        managed = True
        ordering = ['s2241_altinsalperic_infoamb', 'codfatris']



class s2241altInsalPericfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPericfatRisco
        fields = '__all__'
            

class s2241altInsalPericinfoamb(models.Model):
    s2241_altinsalperic = models.ForeignKey('s2241altInsalPeric',
        related_name='%(class)s_s2241_altinsalperic')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_altinsalperic) + ' - ' + unicode(self.codamb)
    #s2241_altinsalperic_infoamb_custom#
    #s2241_altinsalperic_infoamb_custom#
    class Meta:
        db_table = r's2241_altinsalperic_infoamb'
        managed = True
        ordering = ['s2241_altinsalperic', 'codamb']



class s2241altInsalPericinfoambSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPericinfoamb
        fields = '__all__'
            

class s2241aposentEsp(models.Model):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo)
    #s2241_aposentesp_custom#
    #s2241_aposentesp_custom#
    class Meta:
        db_table = r's2241_aposentesp'
        managed = True
        ordering = ['s2241_evtinsapo']



class s2241aposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241aposentEsp
        fields = '__all__'
            

class s2241fimAposentEsp(models.Model):
    s2241_aposentesp = models.OneToOneField('s2241aposentEsp',
        related_name='%(class)s_s2241_aposentesp')
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_aposentesp) + ' - ' + unicode(self.dtfimcondicao)
    #s2241_fimaposentesp_custom#
    #s2241_fimaposentesp_custom#
    class Meta:
        db_table = r's2241_fimaposentesp'
        managed = True
        ordering = ['s2241_aposentesp', 'dtfimcondicao']



class s2241fimAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241fimAposentEsp
        fields = '__all__'
            

class s2241fimAposentEspinfoAmb(models.Model):
    s2241_fimaposentesp = models.ForeignKey('s2241fimAposentEsp',
        related_name='%(class)s_s2241_fimaposentesp')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_fimaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_fimaposentesp_infoamb_custom#
    #s2241_fimaposentesp_infoamb_custom#
    class Meta:
        db_table = r's2241_fimaposentesp_infoamb'
        managed = True
        ordering = ['s2241_fimaposentesp', 'codamb']



class s2241fimAposentEspinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241fimAposentEspinfoAmb
        fields = '__all__'
            

class s2241fimInsalPeric(models.Model):
    s2241_insalperic = models.OneToOneField('s2241insalPeric',
        related_name='%(class)s_s2241_insalperic')
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_insalperic) + ' - ' + unicode(self.dtfimcondicao)
    #s2241_fiminsalperic_custom#
    #s2241_fiminsalperic_custom#
    class Meta:
        db_table = r's2241_fiminsalperic'
        managed = True
        ordering = ['s2241_insalperic', 'dtfimcondicao']



class s2241fimInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241fimInsalPeric
        fields = '__all__'
            

class s2241fimInsalPericinfoAmb(models.Model):
    s2241_fiminsalperic = models.ForeignKey('s2241fimInsalPeric',
        related_name='%(class)s_s2241_fiminsalperic')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_fiminsalperic) + ' - ' + unicode(self.codamb)
    #s2241_fiminsalperic_infoamb_custom#
    #s2241_fiminsalperic_infoamb_custom#
    class Meta:
        db_table = r's2241_fiminsalperic_infoamb'
        managed = True
        ordering = ['s2241_fiminsalperic', 'codamb']



class s2241fimInsalPericinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241fimInsalPericinfoAmb
        fields = '__all__'
            

class s2241iniAposentEsp(models.Model):
    s2241_aposentesp = models.OneToOneField('s2241aposentEsp',
        related_name='%(class)s_s2241_aposentesp')
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_aposentesp) + ' - ' + unicode(self.dtinicondicao)
    #s2241_iniaposentesp_custom#
    #s2241_iniaposentesp_custom#
    class Meta:
        db_table = r's2241_iniaposentesp'
        managed = True
        ordering = ['s2241_aposentesp', 'dtinicondicao']



class s2241iniAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEsp
        fields = '__all__'
            

class s2241iniAposentEspfatRisco(models.Model):
    s2241_iniaposentesp_infoamb = models.ForeignKey('s2241iniAposentEspinfoAmb',
        related_name='%(class)s_s2241_iniaposentesp_infoamb')
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_iniaposentesp_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_iniaposentesp_fatrisco_custom#
    #s2241_iniaposentesp_fatrisco_custom#
    class Meta:
        db_table = r's2241_iniaposentesp_fatrisco'
        managed = True
        ordering = ['s2241_iniaposentesp_infoamb', 'codfatris']



class s2241iniAposentEspfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEspfatRisco
        fields = '__all__'
            

class s2241iniAposentEspinfoAmb(models.Model):
    s2241_iniaposentesp = models.ForeignKey('s2241iniAposentEsp',
        related_name='%(class)s_s2241_iniaposentesp')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_iniaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_iniaposentesp_infoamb_custom#
    #s2241_iniaposentesp_infoamb_custom#
    class Meta:
        db_table = r's2241_iniaposentesp_infoamb'
        managed = True
        ordering = ['s2241_iniaposentesp', 'codamb']



class s2241iniAposentEspinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEspinfoAmb
        fields = '__all__'
            

class s2241iniInsalPeric(models.Model):
    s2241_insalperic = models.OneToOneField('s2241insalPeric',
        related_name='%(class)s_s2241_insalperic')
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_insalperic) + ' - ' + unicode(self.dtinicondicao)
    #s2241_iniinsalperic_custom#
    #s2241_iniinsalperic_custom#
    class Meta:
        db_table = r's2241_iniinsalperic'
        managed = True
        ordering = ['s2241_insalperic', 'dtinicondicao']



class s2241iniInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPeric
        fields = '__all__'
            

class s2241iniInsalPericfatRisco(models.Model):
    s2241_iniinsalperic_infoamb = models.ForeignKey('s2241iniInsalPericinfoAmb',
        related_name='%(class)s_s2241_iniinsalperic_infoamb')
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_iniinsalperic_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_iniinsalperic_fatrisco_custom#
    #s2241_iniinsalperic_fatrisco_custom#
    class Meta:
        db_table = r's2241_iniinsalperic_fatrisco'
        managed = True
        ordering = ['s2241_iniinsalperic_infoamb', 'codfatris']



class s2241iniInsalPericfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPericfatRisco
        fields = '__all__'
            

class s2241iniInsalPericinfoAmb(models.Model):
    s2241_iniinsalperic = models.ForeignKey('s2241iniInsalPeric',
        related_name='%(class)s_s2241_iniinsalperic')
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_iniinsalperic) + ' - ' + unicode(self.codamb)
    #s2241_iniinsalperic_infoamb_custom#
    #s2241_iniinsalperic_infoamb_custom#
    class Meta:
        db_table = r's2241_iniinsalperic_infoamb'
        managed = True
        ordering = ['s2241_iniinsalperic', 'codamb']



class s2241iniInsalPericinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPericinfoAmb
        fields = '__all__'
            

class s2241insalPeric(models.Model):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo)
    #s2241_insalperic_custom#
    #s2241_insalperic_custom#
    class Meta:
        db_table = r's2241_insalperic'
        managed = True
        ordering = ['s2241_evtinsapo']



class s2241insalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241insalPeric
        fields = '__all__'
            

#VIEWS_MODELS
