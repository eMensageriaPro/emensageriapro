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



CHOICES_R2010_TPPROCRETADIC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2010_TPPROCRETPRINC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2010infoProcRetAd(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    tpprocretadic = models.IntegerField(choices=CHOICES_R2010_TPPROCRETADIC)
    nrprocretadic = models.CharField(max_length=21)
    codsuspadic = models.IntegerField(blank=True, null=True)
    valoradic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.tpprocretadic) + ' - ' + unicode(self.nrprocretadic) + ' - ' + unicode(self.codsuspadic) + ' - ' + unicode(self.valoradic)
    #r2010_infoprocretad_custom#
    #r2010_infoprocretad_custom#
    class Meta:
        db_table = r'r2010_infoprocretad'
        managed = True
        ordering = ['r2010_evtservtom', 'tpprocretadic', 'nrprocretadic', 'codsuspadic', 'valoradic']


class r2010infoProcRetPr(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    tpprocretprinc = models.IntegerField(choices=CHOICES_R2010_TPPROCRETPRINC)
    nrprocretprinc = models.CharField(max_length=21)
    codsuspprinc = models.IntegerField(blank=True, null=True)
    valorprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.tpprocretprinc) + ' - ' + unicode(self.nrprocretprinc) + ' - ' + unicode(self.codsuspprinc) + ' - ' + unicode(self.valorprinc)
    #r2010_infoprocretpr_custom#
    #r2010_infoprocretpr_custom#
    class Meta:
        db_table = r'r2010_infoprocretpr'
        managed = True
        ordering = ['r2010_evtservtom', 'tpprocretprinc', 'nrprocretprinc', 'codsuspprinc', 'valorprinc']


class r2010infoTpServ(models.Model):
    r2010_nfs = models.ForeignKey('r2010nfs',
        related_name='%(class)s_r2010_nfs')
    def evento(self): return self.r2010_nfs.evento()
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
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_nfs) + ' - ' + unicode(self.tpservico) + ' - ' + unicode(self.vlrbaseret) + ' - ' + unicode(self.vlrretencao) + ' - ' + unicode(self.vlrretsub) + ' - ' + unicode(self.vlrnretprinc) + ' - ' + unicode(self.vlrservicos15) + ' - ' + unicode(self.vlrservicos20) + ' - ' + unicode(self.vlrservicos25) + ' - ' + unicode(self.vlradicional) + ' - ' + unicode(self.vlrnretadic)
    #r2010_infotpserv_custom#
    #r2010_infotpserv_custom#
    class Meta:
        db_table = r'r2010_infotpserv'
        managed = True
        ordering = ['r2010_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao', 'vlrretsub', 'vlrnretprinc', 'vlrservicos15', 'vlrservicos20', 'vlrservicos25', 'vlradicional', 'vlrnretadic']


class r2010nfs(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    serie = models.CharField(max_length=5)
    numdocto = models.CharField(max_length=15)
    dtemissaonf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    obs = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.numdocto) + ' - ' + unicode(self.dtemissaonf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.obs)
    #r2010_nfs_custom#
    #r2010_nfs_custom#
    class Meta:
        db_table = r'r2010_nfs'
        managed = True
        ordering = ['r2010_evtservtom', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto', 'obs']


#VIEWS_MODELS
