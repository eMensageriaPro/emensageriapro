#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s1020.choices import *
get_model = apps.get_model


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


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class s1020alteracao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao', 
        related_name='%(class)s_s1020_evttablotacao', )
    
    def evento(self): 
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    tplotacao = models.CharField(choices=CHOICES_S1020_TPLOTACAO_ALTERACAO, max_length=2, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_S1020_TPINSC_ALTERACAO, blank=True, null=True, )
    nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    fpas = models.IntegerField(choices=CHOICES_S1020_FPAS_ALTERACAO, null=True, )
    codtercs = models.CharField(choices=CHOICES_S1020_CODTERCS_ALTERACAO, max_length=4, null=True, )
    codtercssusp = models.CharField(choices=CHOICES_S1020_CODTERCSSUSP_ALTERACAO, max_length=4, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_evttablotacao),
            unicode(self.codlotacao),
            unicode(self.inivalid),
            unicode(self.tplotacao),
            unicode(self.fpas),
            unicode(self.codtercs),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1020_alteracao'       
        managed = True # s1020_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_alteracao", "Can view s1020_alteracao"), )
            
        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',
            'tplotacao',
            'fpas',
            'codtercs',]



class s1020alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1020alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020alteracaoinfoEmprParcial(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao', 
        related_name='%(class)s_s1020_alteracao', )
    
    def evento(self): 
        return self.s1020_alteracao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_TPINSCCONTRAT_ALTERACAO, null=True, )
    nrinsccontrat = models.CharField(max_length=14, null=True, )
    tpinscprop = models.IntegerField(null=True, )
    nrinscprop = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_alteracao),
            unicode(self.tpinsccontrat),
            unicode(self.nrinsccontrat),
            unicode(self.tpinscprop),
            unicode(self.nrinscprop),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação complementar que apresenta identificação do contratante e do proprietário de obra de construção civil contratada sob regime de empreitada parcial ou subempreitada'
        db_table = r's1020_alteracao_infoemprparcial'       
        managed = True # s1020_alteracao_infoemprparcial #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_alteracao_infoemprparcial", "Can view s1020_alteracao_infoemprparcial"), )
            
        ordering = [
            's1020_alteracao',
            'tpinsccontrat',
            'nrinsccontrat',
            'tpinscprop',
            'nrinscprop',]



class s1020alteracaoinfoEmprParcialSerializer(ModelSerializer):

    class Meta:
    
        model = s1020alteracaoinfoEmprParcial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020alteracaoinfoProcJudTerceiros(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao', 
        related_name='%(class)s_s1020_alteracao', )
    
    def evento(self): 
        return self.s1020_alteracao.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_alteracao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a existência de processos judiciais, com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos.'
        db_table = r's1020_alteracao_infoprocjudterceiros'       
        managed = True # s1020_alteracao_infoprocjudterceiros #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_alteracao_infoprocjudterceiros", "Can view s1020_alteracao_infoprocjudterceiros"), )
            
        ordering = [
            's1020_alteracao',]



class s1020alteracaoinfoProcJudTerceirosSerializer(ModelSerializer):

    class Meta:
    
        model = s1020alteracaoinfoProcJudTerceiros
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020alteracaonovaValidade(SoftDeletionModel):

    s1020_alteracao = models.ForeignKey('s1020.s1020alteracao', 
        related_name='%(class)s_s1020_alteracao', )
    
    def evento(self): 
        return self.s1020_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1020_alteracao_novavalidade'       
        managed = True # s1020_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_alteracao_novavalidade", "Can view s1020_alteracao_novavalidade"), )
            
        ordering = [
            's1020_alteracao',
            'inivalid',]



class s1020alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1020alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020alteracaoprocJudTerceiro(SoftDeletionModel):

    s1020_alteracao_infoprocjudterceiros = models.ForeignKey('s1020.s1020alteracaoinfoProcJudTerceiros', 
        related_name='%(class)s_s1020_alteracao_infoprocjudterceiros', )
    
    def evento(self): 
        return self.s1020_alteracao_infoprocjudterceiros.evento()
    codterc = models.CharField(choices=CHOICES_S1020_CODTERC_ALTERACAO, max_length=4, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_alteracao_infoprocjudterceiros),
            unicode(self.codterc),
            unicode(self.nrprocjud),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do Processo Judicial'
        db_table = r's1020_alteracao_procjudterceiro'       
        managed = True # s1020_alteracao_procjudterceiro #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_alteracao_procjudterceiro", "Can view s1020_alteracao_procjudterceiro"), )
            
        ordering = [
            's1020_alteracao_infoprocjudterceiros',
            'codterc',
            'nrprocjud',
            'codsusp',]



class s1020alteracaoprocJudTerceiroSerializer(ModelSerializer):

    class Meta:
    
        model = s1020alteracaoprocJudTerceiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020exclusao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao', 
        related_name='%(class)s_s1020_evttablotacao', )
    
    def evento(self): 
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_evttablotacao),
            unicode(self.codlotacao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1020_exclusao'       
        managed = True # s1020_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_exclusao", "Can view s1020_exclusao"), )
            
        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',]



class s1020exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1020exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020inclusao(SoftDeletionModel):

    s1020_evttablotacao = models.ForeignKey('esocial.s1020evtTabLotacao', 
        related_name='%(class)s_s1020_evttablotacao', )
    
    def evento(self): 
        return self.s1020_evttablotacao.evento()
    codlotacao = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    tplotacao = models.CharField(choices=CHOICES_S1020_TPLOTACAO_INCLUSAO, max_length=2, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_S1020_TPINSC_INCLUSAO, blank=True, null=True, )
    nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    fpas = models.IntegerField(choices=CHOICES_S1020_FPAS_INCLUSAO, null=True, )
    codtercs = models.CharField(choices=CHOICES_S1020_CODTERCS_INCLUSAO, max_length=4, null=True, )
    codtercssusp = models.CharField(choices=CHOICES_S1020_CODTERCSSUSP_INCLUSAO, max_length=4, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_evttablotacao),
            unicode(self.codlotacao),
            unicode(self.inivalid),
            unicode(self.tplotacao),
            unicode(self.fpas),
            unicode(self.codtercs),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1020_inclusao'       
        managed = True # s1020_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_inclusao", "Can view s1020_inclusao"), )
            
        ordering = [
            's1020_evttablotacao',
            'codlotacao',
            'inivalid',
            'tplotacao',
            'fpas',
            'codtercs',]



class s1020inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1020inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020inclusaoinfoEmprParcial(SoftDeletionModel):

    s1020_inclusao = models.ForeignKey('s1020.s1020inclusao', 
        related_name='%(class)s_s1020_inclusao', )
    
    def evento(self): 
        return self.s1020_inclusao.evento()
    tpinsccontrat = models.IntegerField(choices=CHOICES_S1020_TPINSCCONTRAT_INCLUSAO, null=True, )
    nrinsccontrat = models.CharField(max_length=14, null=True, )
    tpinscprop = models.IntegerField(null=True, )
    nrinscprop = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_inclusao),
            unicode(self.tpinsccontrat),
            unicode(self.nrinsccontrat),
            unicode(self.tpinscprop),
            unicode(self.nrinscprop),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação complementar que apresenta identificação do contratante e do proprietário de obra de construção civil contratada sob regime de empreitada parcial ou subempreitada'
        db_table = r's1020_inclusao_infoemprparcial'       
        managed = True # s1020_inclusao_infoemprparcial #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_inclusao_infoemprparcial", "Can view s1020_inclusao_infoemprparcial"), )
            
        ordering = [
            's1020_inclusao',
            'tpinsccontrat',
            'nrinsccontrat',
            'tpinscprop',
            'nrinscprop',]



class s1020inclusaoinfoEmprParcialSerializer(ModelSerializer):

    class Meta:
    
        model = s1020inclusaoinfoEmprParcial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020inclusaoinfoProcJudTerceiros(SoftDeletionModel):

    s1020_inclusao = models.ForeignKey('s1020.s1020inclusao', 
        related_name='%(class)s_s1020_inclusao', )
    
    def evento(self): 
        return self.s1020_inclusao.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_inclusao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a existência de processos judiciais, com sentença/decisão favorável ao contribuinte, relativos às contribuições destinadas a outras Entidades e Fundos.'
        db_table = r's1020_inclusao_infoprocjudterceiros'       
        managed = True # s1020_inclusao_infoprocjudterceiros #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_inclusao_infoprocjudterceiros", "Can view s1020_inclusao_infoprocjudterceiros"), )
            
        ordering = [
            's1020_inclusao',]



class s1020inclusaoinfoProcJudTerceirosSerializer(ModelSerializer):

    class Meta:
    
        model = s1020inclusaoinfoProcJudTerceiros
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1020inclusaoprocJudTerceiro(SoftDeletionModel):

    s1020_inclusao_infoprocjudterceiros = models.ForeignKey('s1020.s1020inclusaoinfoProcJudTerceiros', 
        related_name='%(class)s_s1020_inclusao_infoprocjudterceiros', )
    
    def evento(self): 
        return self.s1020_inclusao_infoprocjudterceiros.evento()
    codterc = models.CharField(choices=CHOICES_S1020_CODTERC_INCLUSAO, max_length=4, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1020_inclusao_infoprocjudterceiros),
            unicode(self.codterc),
            unicode(self.nrprocjud),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do Processo Judicial'
        db_table = r's1020_inclusao_procjudterceiro'       
        managed = True # s1020_inclusao_procjudterceiro #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1020_inclusao_procjudterceiro", "Can view s1020_inclusao_procjudterceiro"), )
            
        ordering = [
            's1020_inclusao_infoprocjudterceiros',
            'codterc',
            'nrprocjud',
            'codsusp',]



class s1020inclusaoprocJudTerceiroSerializer(ModelSerializer):

    class Meta:
    
        model = s1020inclusaoprocJudTerceiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()