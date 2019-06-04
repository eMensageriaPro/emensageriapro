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
from emensageriapro.s2306.choices import *
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





class s2306ageIntegracao(SoftDeletionModel):

    s2306_infoestagiario = models.ForeignKey('s2306.s2306infoEstagiario', 
        related_name='%(class)s_s2306_infoestagiario', )
    
    def evento(self): 
        return self.s2306_infoestagiario.evento()
    cnpjagntinteg = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=100, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infoestagiario),
            unicode(self.cnpjagntinteg),
            unicode(self.nmrazao),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.cep),
            unicode(self.uf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Agente de Integração'
        db_table = r's2306_ageintegracao'       
        managed = True # s2306_ageintegracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306ageIntegracao", u"Pode ver listagem do modelo S2306AGEINTEGRACAO"),
            ("can_see_data_s2306ageIntegracao", u"Pode visualizar o conteúdo do modelo S2306AGEINTEGRACAO"),
            ("can_see_menu_s2306ageIntegracao", u"Pode visualizar no menu o modelo S2306AGEINTEGRACAO"),
            ("can_print_list_s2306ageIntegracao", u"Pode imprimir listagem do modelo S2306AGEINTEGRACAO"),
            ("can_print_data_s2306ageIntegracao", u"Pode imprimir o conteúdo do modelo S2306AGEINTEGRACAO"), )
            
        ordering = [
            's2306_infoestagiario',
            'cnpjagntinteg',
            'nmrazao',
            'dsclograd',
            'nrlograd',
            'cep',
            'uf',]



class s2306ageIntegracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2306ageIntegracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306cargoFuncao(SoftDeletionModel):

    s2306_infocomplementares = models.ForeignKey('s2306.s2306infoComplementares', 
        related_name='%(class)s_s2306_infocomplementares', )
    
    def evento(self): 
        return self.s2306_infocomplementares.evento()
    codcargo = models.CharField(max_length=30, null=True, )
    codfuncao = models.CharField(max_length=30, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infocomplementares),
            unicode(self.codcargo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta o cargo e/ou função ocupada pelo trabalhador sem vínculo'
        db_table = r's2306_cargofuncao'       
        managed = True # s2306_cargofuncao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306cargoFuncao", u"Pode ver listagem do modelo S2306CARGOFUNCAO"),
            ("can_see_data_s2306cargoFuncao", u"Pode visualizar o conteúdo do modelo S2306CARGOFUNCAO"),
            ("can_see_menu_s2306cargoFuncao", u"Pode visualizar no menu o modelo S2306CARGOFUNCAO"),
            ("can_print_list_s2306cargoFuncao", u"Pode imprimir listagem do modelo S2306CARGOFUNCAO"),
            ("can_print_data_s2306cargoFuncao", u"Pode imprimir o conteúdo do modelo S2306CARGOFUNCAO"), )
            
        ordering = [
            's2306_infocomplementares',
            'codcargo',]



class s2306cargoFuncaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2306cargoFuncao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306infoComplementares(SoftDeletionModel):

    s2306_evttsvaltcontr = models.ForeignKey('esocial.s2306evtTSVAltContr', 
        related_name='%(class)s_s2306_evttsvaltcontr', )
    
    def evento(self): 
        return self.s2306_evttsvaltcontr.evento()
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_evttsvaltcontr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares sobre o declarante'
        db_table = r's2306_infocomplementares'       
        managed = True # s2306_infocomplementares #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306infoComplementares", u"Pode ver listagem do modelo S2306INFOCOMPLEMENTARES"),
            ("can_see_data_s2306infoComplementares", u"Pode visualizar o conteúdo do modelo S2306INFOCOMPLEMENTARES"),
            ("can_see_menu_s2306infoComplementares", u"Pode visualizar no menu o modelo S2306INFOCOMPLEMENTARES"),
            ("can_print_list_s2306infoComplementares", u"Pode imprimir listagem do modelo S2306INFOCOMPLEMENTARES"),
            ("can_print_data_s2306infoComplementares", u"Pode imprimir o conteúdo do modelo S2306INFOCOMPLEMENTARES"), )
            
        ordering = [
            's2306_evttsvaltcontr',]



class s2306infoComplementaresSerializer(ModelSerializer):

    class Meta:
    
        model = s2306infoComplementares
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306infoEstagiario(SoftDeletionModel):

    s2306_infocomplementares = models.ForeignKey('s2306.s2306infoComplementares', 
        related_name='%(class)s_s2306_infocomplementares', )
    
    def evento(self): 
        return self.s2306_infocomplementares.evento()
    natestagio = models.CharField(choices=CHOICES_S2306_NATESTAGIO, max_length=1, null=True, )
    nivestagio = models.IntegerField(choices=CHOICES_S2306_NIVESTAGIO, null=True, )
    areaatuacao = models.CharField(max_length=50, blank=True, null=True, )
    nrapol = models.CharField(max_length=30, blank=True, null=True, )
    vlrbolsa = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    dtprevterm = models.DateField(null=True, )
    cnpjinstensino = models.CharField(max_length=14, blank=True, null=True, )
    nmrazao = models.CharField(max_length=100, null=True, )
    dsclograd = models.CharField(max_length=100, blank=True, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, blank=True, null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infocomplementares),
            unicode(self.natestagio),
            unicode(self.nivestagio),
            unicode(self.dtprevterm),
            unicode(self.nmrazao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao estagiário'
        db_table = r's2306_infoestagiario'       
        managed = True # s2306_infoestagiario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306infoEstagiario", u"Pode ver listagem do modelo S2306INFOESTAGIARIO"),
            ("can_see_data_s2306infoEstagiario", u"Pode visualizar o conteúdo do modelo S2306INFOESTAGIARIO"),
            ("can_see_menu_s2306infoEstagiario", u"Pode visualizar no menu o modelo S2306INFOESTAGIARIO"),
            ("can_print_list_s2306infoEstagiario", u"Pode imprimir listagem do modelo S2306INFOESTAGIARIO"),
            ("can_print_data_s2306infoEstagiario", u"Pode imprimir o conteúdo do modelo S2306INFOESTAGIARIO"), )
            
        ordering = [
            's2306_infocomplementares',
            'natestagio',
            'nivestagio',
            'dtprevterm',
            'nmrazao',]



class s2306infoEstagiarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2306infoEstagiario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306infoTrabCedido(SoftDeletionModel):

    s2306_infocomplementares = models.ForeignKey('s2306.s2306infoComplementares', 
        related_name='%(class)s_s2306_infocomplementares', )
    
    def evento(self): 
        return self.s2306_infocomplementares.evento()
    indremuncargo = models.CharField(choices=CHOICES_S2306_INDREMUNCARGO, max_length=1, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infocomplementares),
            unicode(self.indremuncargo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao trabalhador cedido, preenchidas exclusivamente pelo cessionário.'
        db_table = r's2306_infotrabcedido'       
        managed = True # s2306_infotrabcedido #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306infoTrabCedido", u"Pode ver listagem do modelo S2306INFOTRABCEDIDO"),
            ("can_see_data_s2306infoTrabCedido", u"Pode visualizar o conteúdo do modelo S2306INFOTRABCEDIDO"),
            ("can_see_menu_s2306infoTrabCedido", u"Pode visualizar no menu o modelo S2306INFOTRABCEDIDO"),
            ("can_print_list_s2306infoTrabCedido", u"Pode imprimir listagem do modelo S2306INFOTRABCEDIDO"),
            ("can_print_data_s2306infoTrabCedido", u"Pode imprimir o conteúdo do modelo S2306INFOTRABCEDIDO"), )
            
        ordering = [
            's2306_infocomplementares',
            'indremuncargo',]



class s2306infoTrabCedidoSerializer(ModelSerializer):

    class Meta:
    
        model = s2306infoTrabCedido
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306remuneracao(SoftDeletionModel):

    s2306_infocomplementares = models.ForeignKey('s2306.s2306infoComplementares', 
        related_name='%(class)s_s2306_infocomplementares', )
    
    def evento(self): 
        return self.s2306_infocomplementares.evento()
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    undsalfixo = models.IntegerField(choices=CHOICES_S2306_UNDSALFIXO, null=True, )
    dscsalvar = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infocomplementares),
            unicode(self.vrsalfx),
            unicode(self.undsalfixo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da remuneração e periodicidade de pagamento'
        db_table = r's2306_remuneracao'       
        managed = True # s2306_remuneracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306remuneracao", u"Pode ver listagem do modelo S2306REMUNERACAO"),
            ("can_see_data_s2306remuneracao", u"Pode visualizar o conteúdo do modelo S2306REMUNERACAO"),
            ("can_see_menu_s2306remuneracao", u"Pode visualizar no menu o modelo S2306REMUNERACAO"),
            ("can_print_list_s2306remuneracao", u"Pode imprimir listagem do modelo S2306REMUNERACAO"),
            ("can_print_data_s2306remuneracao", u"Pode imprimir o conteúdo do modelo S2306REMUNERACAO"), )
            
        ordering = [
            's2306_infocomplementares',
            'vrsalfx',
            'undsalfixo',]



class s2306remuneracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2306remuneracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2306supervisorEstagio(SoftDeletionModel):

    s2306_infoestagiario = models.ForeignKey('s2306.s2306infoEstagiario', 
        related_name='%(class)s_s2306_infoestagiario', )
    
    def evento(self): 
        return self.s2306_infoestagiario.evento()
    cpfsupervisor = models.CharField(max_length=11, null=True, )
    nmsuperv = models.CharField(max_length=70, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2306_infoestagiario),
            unicode(self.cpfsupervisor),
            unicode(self.nmsuperv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Supervisor do Estágio'
        db_table = r's2306_supervisorestagio'       
        managed = True # s2306_supervisorestagio #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306supervisorEstagio", u"Pode ver listagem do modelo S2306SUPERVISORESTAGIO"),
            ("can_see_data_s2306supervisorEstagio", u"Pode visualizar o conteúdo do modelo S2306SUPERVISORESTAGIO"),
            ("can_see_menu_s2306supervisorEstagio", u"Pode visualizar no menu o modelo S2306SUPERVISORESTAGIO"),
            ("can_print_list_s2306supervisorEstagio", u"Pode imprimir listagem do modelo S2306SUPERVISORESTAGIO"),
            ("can_print_data_s2306supervisorEstagio", u"Pode imprimir o conteúdo do modelo S2306SUPERVISORESTAGIO"), )
            
        ordering = [
            's2306_infoestagiario',
            'cpfsupervisor',
            'nmsuperv',]



class s2306supervisorEstagioSerializer(ModelSerializer):

    class Meta:
    
        model = s2306supervisorEstagio
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()