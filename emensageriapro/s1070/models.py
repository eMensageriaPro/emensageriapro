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
from emensageriapro.s1070.choices import *
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





class s1070alteracao(SoftDeletionModel):

    s1070_evttabprocesso = models.ForeignKey('esocial.s1070evtTabProcesso', 
        related_name='%(class)s_s1070_evttabprocesso', )
    
    def evento(self): 
        return self.s1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1070_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    indautoria = models.IntegerField(choices=CHOICES_S1070_INDAUTORIA_ALTERACAO, blank=True, null=True, )
    indmatproc = models.IntegerField(choices=CHOICES_S1070_INDMATPROC_ALTERACAO, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),
            unicode(self.indmatproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1070_alteracao'       
        managed = True # s1070_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070alteracao", u"Pode ver listagem do modelo S1070ALTERACAO"),
            ("can_see_data_s1070alteracao", u"Pode visualizar o conteúdo do modelo S1070ALTERACAO"),
            ("can_see_menu_s1070alteracao", u"Pode visualizar no menu o modelo S1070ALTERACAO"),
            ("can_print_list_s1070alteracao", u"Pode imprimir listagem do modelo S1070ALTERACAO"),
            ("can_print_data_s1070alteracao", u"Pode imprimir o conteúdo do modelo S1070ALTERACAO"), )
            
        ordering = [
            's1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',
            'indmatproc',]



class s1070alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1070alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070alteracaodadosProcJud(SoftDeletionModel):

    s1070_alteracao = models.ForeignKey('s1070.s1070alteracao', 
        related_name='%(class)s_s1070_alteracao', )
    
    def evento(self): 
        return self.s1070_alteracao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.TextField(null=True, )
    idvara = models.IntegerField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_alteracao),
            unicode(self.ufvara),
            unicode(self.codmunic),
            unicode(self.idvara),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares do Processo Judicial'
        db_table = r's1070_alteracao_dadosprocjud'       
        managed = True # s1070_alteracao_dadosprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070alteracaodadosProcJud", u"Pode ver listagem do modelo S1070ALTERACAODADOSPROCJUD"),
            ("can_see_data_s1070alteracaodadosProcJud", u"Pode visualizar o conteúdo do modelo S1070ALTERACAODADOSPROCJUD"),
            ("can_see_menu_s1070alteracaodadosProcJud", u"Pode visualizar no menu o modelo S1070ALTERACAODADOSPROCJUD"),
            ("can_print_list_s1070alteracaodadosProcJud", u"Pode imprimir listagem do modelo S1070ALTERACAODADOSPROCJUD"),
            ("can_print_data_s1070alteracaodadosProcJud", u"Pode imprimir o conteúdo do modelo S1070ALTERACAODADOSPROCJUD"), )
            
        ordering = [
            's1070_alteracao',
            'ufvara',
            'codmunic',
            'idvara',]



class s1070alteracaodadosProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = s1070alteracaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070alteracaoinfoSusp(SoftDeletionModel):

    s1070_alteracao = models.ForeignKey('s1070.s1070alteracao', 
        related_name='%(class)s_s1070_alteracao', )
    
    def evento(self): 
        return self.s1070_alteracao.evento()
    codsusp = models.IntegerField(null=True, )
    indsusp = models.CharField(choices=CHOICES_S1070_INDSUSP_ALTERACAO, max_length=2, null=True, )
    dtdecisao = models.DateField(null=True, )
    inddeposito = models.CharField(choices=CHOICES_S1070_INDDEPOSITO_ALTERACAO, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_alteracao),
            unicode(self.codsusp),
            unicode(self.indsusp),
            unicode(self.dtdecisao),
            unicode(self.inddeposito),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de suspensão de exigibilidade de tributos e FGTS em virtude de processo administrativo ou judicial.'
        db_table = r's1070_alteracao_infosusp'       
        managed = True # s1070_alteracao_infosusp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070alteracaoinfoSusp", u"Pode ver listagem do modelo S1070ALTERACAOINFOSUSP"),
            ("can_see_data_s1070alteracaoinfoSusp", u"Pode visualizar o conteúdo do modelo S1070ALTERACAOINFOSUSP"),
            ("can_see_menu_s1070alteracaoinfoSusp", u"Pode visualizar no menu o modelo S1070ALTERACAOINFOSUSP"),
            ("can_print_list_s1070alteracaoinfoSusp", u"Pode imprimir listagem do modelo S1070ALTERACAOINFOSUSP"),
            ("can_print_data_s1070alteracaoinfoSusp", u"Pode imprimir o conteúdo do modelo S1070ALTERACAOINFOSUSP"), )
            
        ordering = [
            's1070_alteracao',
            'codsusp',
            'indsusp',
            'dtdecisao',
            'inddeposito',]



class s1070alteracaoinfoSuspSerializer(ModelSerializer):

    class Meta:
    
        model = s1070alteracaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070alteracaonovaValidade(SoftDeletionModel):

    s1070_alteracao = models.ForeignKey('s1070.s1070alteracao', 
        related_name='%(class)s_s1070_alteracao', )
    
    def evento(self): 
        return self.s1070_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1070_alteracao_novavalidade'       
        managed = True # s1070_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070alteracaonovaValidade", u"Pode ver listagem do modelo S1070ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1070alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1070ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1070alteracaonovaValidade", u"Pode visualizar no menu o modelo S1070ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1070alteracaonovaValidade", u"Pode imprimir listagem do modelo S1070ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1070alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1070ALTERACAONOVAVALIDADE"), )
            
        ordering = [
            's1070_alteracao',
            'inivalid',]



class s1070alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1070alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070exclusao(SoftDeletionModel):

    s1070_evttabprocesso = models.ForeignKey('esocial.s1070evtTabProcesso', 
        related_name='%(class)s_s1070_evttabprocesso', )
    
    def evento(self): 
        return self.s1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1070_TPPROC_EXCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1070_exclusao'       
        managed = True # s1070_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070exclusao", u"Pode ver listagem do modelo S1070EXCLUSAO"),
            ("can_see_data_s1070exclusao", u"Pode visualizar o conteúdo do modelo S1070EXCLUSAO"),
            ("can_see_menu_s1070exclusao", u"Pode visualizar no menu o modelo S1070EXCLUSAO"),
            ("can_print_list_s1070exclusao", u"Pode imprimir listagem do modelo S1070EXCLUSAO"),
            ("can_print_data_s1070exclusao", u"Pode imprimir o conteúdo do modelo S1070EXCLUSAO"), )
            
        ordering = [
            's1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',]



class s1070exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1070exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070inclusao(SoftDeletionModel):

    s1070_evttabprocesso = models.ForeignKey('esocial.s1070evtTabProcesso', 
        related_name='%(class)s_s1070_evttabprocesso', )
    
    def evento(self): 
        return self.s1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1070_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    indautoria = models.IntegerField(choices=CHOICES_S1070_INDAUTORIA_INCLUSAO, blank=True, null=True, )
    indmatproc = models.IntegerField(choices=CHOICES_S1070_INDMATPROC_INCLUSAO, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),
            unicode(self.indmatproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1070_inclusao'       
        managed = True # s1070_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070inclusao", u"Pode ver listagem do modelo S1070INCLUSAO"),
            ("can_see_data_s1070inclusao", u"Pode visualizar o conteúdo do modelo S1070INCLUSAO"),
            ("can_see_menu_s1070inclusao", u"Pode visualizar no menu o modelo S1070INCLUSAO"),
            ("can_print_list_s1070inclusao", u"Pode imprimir listagem do modelo S1070INCLUSAO"),
            ("can_print_data_s1070inclusao", u"Pode imprimir o conteúdo do modelo S1070INCLUSAO"), )
            
        ordering = [
            's1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',
            'indmatproc',]



class s1070inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1070inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070inclusaodadosProcJud(SoftDeletionModel):

    s1070_inclusao = models.ForeignKey('s1070.s1070inclusao', 
        related_name='%(class)s_s1070_inclusao', )
    
    def evento(self): 
        return self.s1070_inclusao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.TextField(null=True, )
    idvara = models.IntegerField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_inclusao),
            unicode(self.ufvara),
            unicode(self.codmunic),
            unicode(self.idvara),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares do Processo Judicial'
        db_table = r's1070_inclusao_dadosprocjud'       
        managed = True # s1070_inclusao_dadosprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070inclusaodadosProcJud", u"Pode ver listagem do modelo S1070INCLUSAODADOSPROCJUD"),
            ("can_see_data_s1070inclusaodadosProcJud", u"Pode visualizar o conteúdo do modelo S1070INCLUSAODADOSPROCJUD"),
            ("can_see_menu_s1070inclusaodadosProcJud", u"Pode visualizar no menu o modelo S1070INCLUSAODADOSPROCJUD"),
            ("can_print_list_s1070inclusaodadosProcJud", u"Pode imprimir listagem do modelo S1070INCLUSAODADOSPROCJUD"),
            ("can_print_data_s1070inclusaodadosProcJud", u"Pode imprimir o conteúdo do modelo S1070INCLUSAODADOSPROCJUD"), )
            
        ordering = [
            's1070_inclusao',
            'ufvara',
            'codmunic',
            'idvara',]



class s1070inclusaodadosProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = s1070inclusaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1070inclusaoinfoSusp(SoftDeletionModel):

    s1070_inclusao = models.ForeignKey('s1070.s1070inclusao', 
        related_name='%(class)s_s1070_inclusao', )
    
    def evento(self): 
        return self.s1070_inclusao.evento()
    codsusp = models.IntegerField(null=True, )
    indsusp = models.CharField(choices=CHOICES_S1070_INDSUSP_INCLUSAO, max_length=2, null=True, )
    dtdecisao = models.DateField(null=True, )
    inddeposito = models.CharField(choices=CHOICES_S1070_INDDEPOSITO_INCLUSAO, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1070_inclusao),
            unicode(self.codsusp),
            unicode(self.indsusp),
            unicode(self.dtdecisao),
            unicode(self.inddeposito),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de suspensão de exigibilidade de tributos e FGTS em virtude de processo administrativo ou judicial.'
        db_table = r's1070_inclusao_infosusp'       
        managed = True # s1070_inclusao_infosusp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070inclusaoinfoSusp", u"Pode ver listagem do modelo S1070INCLUSAOINFOSUSP"),
            ("can_see_data_s1070inclusaoinfoSusp", u"Pode visualizar o conteúdo do modelo S1070INCLUSAOINFOSUSP"),
            ("can_see_menu_s1070inclusaoinfoSusp", u"Pode visualizar no menu o modelo S1070INCLUSAOINFOSUSP"),
            ("can_print_list_s1070inclusaoinfoSusp", u"Pode imprimir listagem do modelo S1070INCLUSAOINFOSUSP"),
            ("can_print_data_s1070inclusaoinfoSusp", u"Pode imprimir o conteúdo do modelo S1070INCLUSAOINFOSUSP"), )
            
        ordering = [
            's1070_inclusao',
            'codsusp',
            'indsusp',
            'dtdecisao',
            'inddeposito',]



class s1070inclusaoinfoSuspSerializer(ModelSerializer):

    class Meta:
    
        model = s1070inclusaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()