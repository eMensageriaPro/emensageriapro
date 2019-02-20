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



class s2241altAposentEsp(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtaltcondicao)
    #s2241_altaposentesp_custom#

    class Meta:
        db_table = r's2241_altaposentesp'       
        managed = True # s2241_altaposentesp #
        permissions = (
            ("can_view_s2241_altaposentesp", "Can view s2241_altaposentesp"),
            #custom_permissions_s2241_altaposentesp
        )
        ordering = ['s2241_evtinsapo', 'dtaltcondicao']



class s2241altAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEsp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241altAposentEspfatRisco(SoftDeletionModel):
    s2241_altaposentesp_infoamb = models.ForeignKey('s2241altAposentEspinfoamb',
        related_name='%(class)s_s2241_altaposentesp_infoamb')
    def evento(self): return self.s2241_altaposentesp_infoamb.evento()
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_altaposentesp_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_altaposentesp_fatrisco_custom#

    class Meta:
        db_table = r's2241_altaposentesp_fatrisco'       
        managed = True # s2241_altaposentesp_fatrisco #
        permissions = (
            ("can_view_s2241_altaposentesp_fatrisco", "Can view s2241_altaposentesp_fatrisco"),
            #custom_permissions_s2241_altaposentesp_fatrisco
        )
        ordering = ['s2241_altaposentesp_infoamb', 'codfatris']



class s2241altAposentEspfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEspfatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241altAposentEspinfoamb(SoftDeletionModel):
    s2241_altaposentesp = models.ForeignKey('s2241altAposentEsp',
        related_name='%(class)s_s2241_altaposentesp')
    def evento(self): return self.s2241_altaposentesp.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_altaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_altaposentesp_infoamb_custom#

    class Meta:
        db_table = r's2241_altaposentesp_infoamb'       
        managed = True # s2241_altaposentesp_infoamb #
        permissions = (
            ("can_view_s2241_altaposentesp_infoamb", "Can view s2241_altaposentesp_infoamb"),
            #custom_permissions_s2241_altaposentesp_infoamb
        )
        ordering = ['s2241_altaposentesp', 'codamb']



class s2241altAposentEspinfoambSerializer(ModelSerializer):
    class Meta:
        model = s2241altAposentEspinfoamb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241altInsalPeric(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtaltcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtaltcondicao)
    #s2241_altinsalperic_custom#

    class Meta:
        db_table = r's2241_altinsalperic'       
        managed = True # s2241_altinsalperic #
        permissions = (
            ("can_view_s2241_altinsalperic", "Can view s2241_altinsalperic"),
            #custom_permissions_s2241_altinsalperic
        )
        ordering = ['s2241_evtinsapo', 'dtaltcondicao']



class s2241altInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPeric
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241altInsalPericfatRisco(SoftDeletionModel):
    s2241_altinsalperic_infoamb = models.ForeignKey('s2241altInsalPericinfoamb',
        related_name='%(class)s_s2241_altinsalperic_infoamb')
    def evento(self): return self.s2241_altinsalperic_infoamb.evento()
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_altinsalperic_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_altinsalperic_fatrisco_custom#

    class Meta:
        db_table = r's2241_altinsalperic_fatrisco'       
        managed = True # s2241_altinsalperic_fatrisco #
        permissions = (
            ("can_view_s2241_altinsalperic_fatrisco", "Can view s2241_altinsalperic_fatrisco"),
            #custom_permissions_s2241_altinsalperic_fatrisco
        )
        ordering = ['s2241_altinsalperic_infoamb', 'codfatris']



class s2241altInsalPericfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPericfatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241altInsalPericinfoamb(SoftDeletionModel):
    s2241_altinsalperic = models.ForeignKey('s2241altInsalPeric',
        related_name='%(class)s_s2241_altinsalperic')
    def evento(self): return self.s2241_altinsalperic.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_altinsalperic) + ' - ' + unicode(self.codamb)
    #s2241_altinsalperic_infoamb_custom#

    class Meta:
        db_table = r's2241_altinsalperic_infoamb'       
        managed = True # s2241_altinsalperic_infoamb #
        permissions = (
            ("can_view_s2241_altinsalperic_infoamb", "Can view s2241_altinsalperic_infoamb"),
            #custom_permissions_s2241_altinsalperic_infoamb
        )
        ordering = ['s2241_altinsalperic', 'codamb']



class s2241altInsalPericinfoambSerializer(ModelSerializer):
    class Meta:
        model = s2241altInsalPericinfoamb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241fimAposentEsp(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtfimcondicao)
    #s2241_fimaposentesp_custom#

    class Meta:
        db_table = r's2241_fimaposentesp'       
        managed = True # s2241_fimaposentesp #
        permissions = (
            ("can_view_s2241_fimaposentesp", "Can view s2241_fimaposentesp"),
            #custom_permissions_s2241_fimaposentesp
        )
        ordering = ['s2241_evtinsapo', 'dtfimcondicao']



class s2241fimAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241fimAposentEsp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241fimAposentEspinfoAmb(SoftDeletionModel):
    s2241_fimaposentesp = models.ForeignKey('s2241fimAposentEsp',
        related_name='%(class)s_s2241_fimaposentesp')
    def evento(self): return self.s2241_fimaposentesp.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_fimaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_fimaposentesp_infoamb_custom#

    class Meta:
        db_table = r's2241_fimaposentesp_infoamb'       
        managed = True # s2241_fimaposentesp_infoamb #
        permissions = (
            ("can_view_s2241_fimaposentesp_infoamb", "Can view s2241_fimaposentesp_infoamb"),
            #custom_permissions_s2241_fimaposentesp_infoamb
        )
        ordering = ['s2241_fimaposentesp', 'codamb']



class s2241fimAposentEspinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241fimAposentEspinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241fimInsalPeric(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtfimcondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtfimcondicao)
    #s2241_fiminsalperic_custom#

    class Meta:
        db_table = r's2241_fiminsalperic'       
        managed = True # s2241_fiminsalperic #
        permissions = (
            ("can_view_s2241_fiminsalperic", "Can view s2241_fiminsalperic"),
            #custom_permissions_s2241_fiminsalperic
        )
        ordering = ['s2241_evtinsapo', 'dtfimcondicao']



class s2241fimInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241fimInsalPeric
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241fimInsalPericinfoAmb(SoftDeletionModel):
    s2241_fiminsalperic = models.ForeignKey('s2241fimInsalPeric',
        related_name='%(class)s_s2241_fiminsalperic')
    def evento(self): return self.s2241_fiminsalperic.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_fiminsalperic) + ' - ' + unicode(self.codamb)
    #s2241_fiminsalperic_infoamb_custom#

    class Meta:
        db_table = r's2241_fiminsalperic_infoamb'       
        managed = True # s2241_fiminsalperic_infoamb #
        permissions = (
            ("can_view_s2241_fiminsalperic_infoamb", "Can view s2241_fiminsalperic_infoamb"),
            #custom_permissions_s2241_fiminsalperic_infoamb
        )
        ordering = ['s2241_fiminsalperic', 'codamb']



class s2241fimInsalPericinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241fimInsalPericinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniAposentEsp(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtinicondicao)
    #s2241_iniaposentesp_custom#

    class Meta:
        db_table = r's2241_iniaposentesp'       
        managed = True # s2241_iniaposentesp #
        permissions = (
            ("can_view_s2241_iniaposentesp", "Can view s2241_iniaposentesp"),
            #custom_permissions_s2241_iniaposentesp
        )
        ordering = ['s2241_evtinsapo', 'dtinicondicao']



class s2241iniAposentEspSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEsp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniAposentEspfatRisco(SoftDeletionModel):
    s2241_iniaposentesp_infoamb = models.ForeignKey('s2241iniAposentEspinfoAmb',
        related_name='%(class)s_s2241_iniaposentesp_infoamb')
    def evento(self): return self.s2241_iniaposentesp_infoamb.evento()
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_iniaposentesp_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_iniaposentesp_fatrisco_custom#

    class Meta:
        db_table = r's2241_iniaposentesp_fatrisco'       
        managed = True # s2241_iniaposentesp_fatrisco #
        permissions = (
            ("can_view_s2241_iniaposentesp_fatrisco", "Can view s2241_iniaposentesp_fatrisco"),
            #custom_permissions_s2241_iniaposentesp_fatrisco
        )
        ordering = ['s2241_iniaposentesp_infoamb', 'codfatris']



class s2241iniAposentEspfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEspfatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniAposentEspinfoAmb(SoftDeletionModel):
    s2241_iniaposentesp = models.ForeignKey('s2241iniAposentEsp',
        related_name='%(class)s_s2241_iniaposentesp')
    def evento(self): return self.s2241_iniaposentesp.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_iniaposentesp) + ' - ' + unicode(self.codamb)
    #s2241_iniaposentesp_infoamb_custom#

    class Meta:
        db_table = r's2241_iniaposentesp_infoamb'       
        managed = True # s2241_iniaposentesp_infoamb #
        permissions = (
            ("can_view_s2241_iniaposentesp_infoamb", "Can view s2241_iniaposentesp_infoamb"),
            #custom_permissions_s2241_iniaposentesp_infoamb
        )
        ordering = ['s2241_iniaposentesp', 'codamb']



class s2241iniAposentEspinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241iniAposentEspinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniInsalPeric(SoftDeletionModel):
    s2241_evtinsapo = models.OneToOneField('esocial.s2241evtInsApo',
        related_name='%(class)s_s2241_evtinsapo')
    def evento(self): return self.s2241_evtinsapo.evento()
    dtinicondicao = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_evtinsapo) + ' - ' + unicode(self.dtinicondicao)
    #s2241_iniinsalperic_custom#

    class Meta:
        db_table = r's2241_iniinsalperic'       
        managed = True # s2241_iniinsalperic #
        permissions = (
            ("can_view_s2241_iniinsalperic", "Can view s2241_iniinsalperic"),
            #custom_permissions_s2241_iniinsalperic
        )
        ordering = ['s2241_evtinsapo', 'dtinicondicao']



class s2241iniInsalPericSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPeric
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniInsalPericfatRisco(SoftDeletionModel):
    s2241_iniinsalperic_infoamb = models.ForeignKey('s2241iniInsalPericinfoAmb',
        related_name='%(class)s_s2241_iniinsalperic_infoamb')
    def evento(self): return self.s2241_iniinsalperic_infoamb.evento()
    codfatris = models.TextField(max_length=10)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_iniinsalperic_infoamb) + ' - ' + unicode(self.codfatris)
    #s2241_iniinsalperic_fatrisco_custom#

    class Meta:
        db_table = r's2241_iniinsalperic_fatrisco'       
        managed = True # s2241_iniinsalperic_fatrisco #
        permissions = (
            ("can_view_s2241_iniinsalperic_fatrisco", "Can view s2241_iniinsalperic_fatrisco"),
            #custom_permissions_s2241_iniinsalperic_fatrisco
        )
        ordering = ['s2241_iniinsalperic_infoamb', 'codfatris']



class s2241iniInsalPericfatRiscoSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPericfatRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2241iniInsalPericinfoAmb(SoftDeletionModel):
    s2241_iniinsalperic = models.ForeignKey('s2241iniInsalPeric',
        related_name='%(class)s_s2241_iniinsalperic')
    def evento(self): return self.s2241_iniinsalperic.evento()
    codamb = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2241_iniinsalperic) + ' - ' + unicode(self.codamb)
    #s2241_iniinsalperic_infoamb_custom#

    class Meta:
        db_table = r's2241_iniinsalperic_infoamb'       
        managed = True # s2241_iniinsalperic_infoamb #
        permissions = (
            ("can_view_s2241_iniinsalperic_infoamb", "Can view s2241_iniinsalperic_infoamb"),
            #custom_permissions_s2241_iniinsalperic_infoamb
        )
        ordering = ['s2241_iniinsalperic', 'codamb']



class s2241iniInsalPericinfoAmbSerializer(ModelSerializer):
    class Meta:
        model = s2241iniInsalPericinfoAmb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
