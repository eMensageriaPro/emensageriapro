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



CHOICES_R2020_TPPROCRETADIC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2020_TPPROCRETPRINC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2020infoProcRetAd(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    tpprocretadic = models.IntegerField(choices=CHOICES_R2020_TPPROCRETADIC)
    nrprocretadic = models.CharField(max_length=21)
    codsuspadic = models.IntegerField(blank=True, null=True)
    valoradic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.tpprocretadic) + ' - ' + unicode(self.nrprocretadic) + ' - ' + unicode(self.valoradic)
    #r2020_infoprocretad_custom#
    class Meta:
        db_table = r'r2020_infoprocretad'
        managed = True # r2020_infoprocretad #
        ordering = ['r2020_evtservprest', 'tpprocretadic', 'nrprocretadic', 'valoradic']



class r2020infoProcRetAdSerializer(ModelSerializer):
    class Meta:
        model = r2020infoProcRetAd
        fields = '__all__'
            

class r2020infoProcRetPr(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    tpprocretprinc = models.IntegerField(choices=CHOICES_R2020_TPPROCRETPRINC)
    nrprocretprinc = models.CharField(max_length=21)
    codsuspprinc = models.IntegerField(blank=True, null=True)
    valorprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.tpprocretprinc) + ' - ' + unicode(self.nrprocretprinc) + ' - ' + unicode(self.valorprinc)
    #r2020_infoprocretpr_custom#
    class Meta:
        db_table = r'r2020_infoprocretpr'
        managed = True # r2020_infoprocretpr #
        ordering = ['r2020_evtservprest', 'tpprocretprinc', 'nrprocretprinc', 'valorprinc']



class r2020infoProcRetPrSerializer(ModelSerializer):
    class Meta:
        model = r2020infoProcRetPr
        fields = '__all__'
            

class r2020infoTpServ(models.Model):
    r2020_nfs = models.ForeignKey('r2020nfs',
        related_name='%(class)s_r2020_nfs')
    def evento(self): return self.r2020_nfs.evento()
    tpservico = models.IntegerField()
    vlrbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretencao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretsub = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlradicional = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r2020_nfs) + ' - ' + unicode(self.tpservico) + ' - ' + unicode(self.vlrbaseret) + ' - ' + unicode(self.vlrretencao)
    #r2020_infotpserv_custom#
    class Meta:
        db_table = r'r2020_infotpserv'
        managed = True # r2020_infotpserv #
        ordering = ['r2020_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao']



class r2020infoTpServSerializer(ModelSerializer):
    class Meta:
        model = r2020infoTpServ
        fields = '__all__'
            

class r2020nfs(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    serie = models.CharField(max_length=5)
    numdocto = models.CharField(max_length=15)
    dtemissaonf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    obs = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True, default=False)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.numdocto) + ' - ' + unicode(self.dtemissaonf) + ' - ' + unicode(self.vlrbruto)
    #r2020_nfs_custom#
    class Meta:
        db_table = r'r2020_nfs'
        managed = True # r2020_nfs #
        ordering = ['r2020_evtservprest', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto']



class r2020nfsSerializer(ModelSerializer):
    class Meta:
        model = r2020nfs
        fields = '__all__'
            

#VIEWS_MODELS
