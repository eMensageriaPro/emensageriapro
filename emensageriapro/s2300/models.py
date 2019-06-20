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
from emensageriapro.s2300.choices import *
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





class s2300CNH(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nrregcnh = models.CharField(max_length=12, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    ufcnh = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    dtvalid = models.DateField(null=True, )
    dtprihab = models.DateField(blank=True, null=True, )
    categoriacnh = models.CharField(choices=CHOICES_S2300_CATEGORIACNH, max_length=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações da Carteira Nacional de Habilitação (CNH)'
        db_table = r's2300_cnh'       
        managed = True # s2300_cnh #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300CNH", u"Pode ver listagem do modelo S2300CNH"),
            ("can_see_data_s2300CNH", u"Pode visualizar o conteúdo do modelo S2300CNH"),
            ("can_see_menu_s2300CNH", u"Pode visualizar no menu o modelo S2300CNH"),
            ("can_print_list_s2300CNH", u"Pode imprimir listagem do modelo S2300CNH"),
            ("can_print_data_s2300CNH", u"Pode imprimir o conteúdo do modelo S2300CNH"), )
            
        ordering = [
            's2300_documentos',
            'nrregcnh',
            'ufcnh',
            'dtvalid',
            'categoriacnh',]



class s2300CNHSerializer(ModelSerializer):

    class Meta:
    
        model = s2300CNH
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300CTPS(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nrctps = models.CharField(max_length=11, null=True, )
    seriectps = models.CharField(max_length=5, null=True, )
    ufctps = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações da Carteira de Trabalho e Previdência Social'
        db_table = r's2300_ctps'       
        managed = True # s2300_ctps #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300CTPS", u"Pode ver listagem do modelo S2300CTPS"),
            ("can_see_data_s2300CTPS", u"Pode visualizar o conteúdo do modelo S2300CTPS"),
            ("can_see_menu_s2300CTPS", u"Pode visualizar no menu o modelo S2300CTPS"),
            ("can_print_list_s2300CTPS", u"Pode imprimir listagem do modelo S2300CTPS"),
            ("can_print_data_s2300CTPS", u"Pode imprimir o conteúdo do modelo S2300CTPS"), )
            
        ordering = [
            's2300_documentos',
            'nrctps',
            'seriectps',
            'ufctps',]



class s2300CTPSSerializer(ModelSerializer):

    class Meta:
    
        model = s2300CTPS
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300OC(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nroc = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    dtvalid = models.DateField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações do número de registro em Órgão de Classe (OC)'
        db_table = r's2300_oc'       
        managed = True # s2300_oc #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300OC", u"Pode ver listagem do modelo S2300OC"),
            ("can_see_data_s2300OC", u"Pode visualizar o conteúdo do modelo S2300OC"),
            ("can_see_menu_s2300OC", u"Pode visualizar no menu o modelo S2300OC"),
            ("can_print_list_s2300OC", u"Pode imprimir listagem do modelo S2300OC"),
            ("can_print_data_s2300OC", u"Pode imprimir o conteúdo do modelo S2300OC"), )
            
        ordering = [
            's2300_documentos',
            'nroc',
            'orgaoemissor',]



class s2300OCSerializer(ModelSerializer):

    class Meta:
    
        model = s2300OC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300RG(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nrrg = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações do Registro Geral (RG)'
        db_table = r's2300_rg'       
        managed = True # s2300_rg #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300RG", u"Pode ver listagem do modelo S2300RG"),
            ("can_see_data_s2300RG", u"Pode visualizar o conteúdo do modelo S2300RG"),
            ("can_see_menu_s2300RG", u"Pode visualizar no menu o modelo S2300RG"),
            ("can_print_list_s2300RG", u"Pode imprimir listagem do modelo S2300RG"),
            ("can_print_data_s2300RG", u"Pode imprimir o conteúdo do modelo S2300RG"), )
            
        ordering = [
            's2300_documentos',
            'nrrg',
            'orgaoemissor',]



class s2300RGSerializer(ModelSerializer):

    class Meta:
    
        model = s2300RG
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300RIC(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nrric = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações do Documento Nacional de Identidade - DNI (Registro de Identificação Civil - RIC)'
        db_table = r's2300_ric'       
        managed = True # s2300_ric #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300RIC", u"Pode ver listagem do modelo S2300RIC"),
            ("can_see_data_s2300RIC", u"Pode visualizar o conteúdo do modelo S2300RIC"),
            ("can_see_menu_s2300RIC", u"Pode visualizar no menu o modelo S2300RIC"),
            ("can_print_list_s2300RIC", u"Pode imprimir listagem do modelo S2300RIC"),
            ("can_print_data_s2300RIC", u"Pode imprimir o conteúdo do modelo S2300RIC"), )
            
        ordering = [
            's2300_documentos',
            'nrric',
            'orgaoemissor',]



class s2300RICSerializer(ModelSerializer):

    class Meta:
    
        model = s2300RIC
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300RNE(SoftDeletionModel):

    s2300_documentos = models.ForeignKey('s2300.s2300documentos', 
        related_name='%(class)s_s2300_documentos', )
    
    def evento(self): 
        return self.s2300_documentos.evento()
    nrrne = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações do Registro Nacional de Estrangeiro'
        db_table = r's2300_rne'       
        managed = True # s2300_rne #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300RNE", u"Pode ver listagem do modelo S2300RNE"),
            ("can_see_data_s2300RNE", u"Pode visualizar o conteúdo do modelo S2300RNE"),
            ("can_see_menu_s2300RNE", u"Pode visualizar no menu o modelo S2300RNE"),
            ("can_print_list_s2300RNE", u"Pode imprimir listagem do modelo S2300RNE"),
            ("can_print_data_s2300RNE", u"Pode imprimir o conteúdo do modelo S2300RNE"), )
            
        ordering = [
            's2300_documentos',
            'nrrne',
            'orgaoemissor',]



class s2300RNESerializer(ModelSerializer):

    class Meta:
    
        model = s2300RNE
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300afastamento(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    dtiniafast = models.DateField(null=True, )
    codmotafast = models.TextField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de afastamento do trabalhador'
        db_table = r's2300_afastamento'       
        managed = True # s2300_afastamento #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300afastamento", u"Pode ver listagem do modelo S2300AFASTAMENTO"),
            ("can_see_data_s2300afastamento", u"Pode visualizar o conteúdo do modelo S2300AFASTAMENTO"),
            ("can_see_menu_s2300afastamento", u"Pode visualizar no menu o modelo S2300AFASTAMENTO"),
            ("can_print_list_s2300afastamento", u"Pode imprimir listagem do modelo S2300AFASTAMENTO"),
            ("can_print_data_s2300afastamento", u"Pode imprimir o conteúdo do modelo S2300AFASTAMENTO"), )
            
        ordering = [
            's2300_evttsvinicio',
            'dtiniafast',
            'codmotafast',]



class s2300afastamentoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300afastamento
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300ageIntegracao(SoftDeletionModel):

    s2300_infoestagiario = models.ForeignKey('s2300.s2300infoEstagiario', 
        related_name='%(class)s_s2300_infoestagiario', )
    
    def evento(self): 
        return self.s2300_infoestagiario.evento()
    cnpjagntinteg = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=100, null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Agente de Integração'
        db_table = r's2300_ageintegracao'       
        managed = True # s2300_ageintegracao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300ageIntegracao", u"Pode ver listagem do modelo S2300AGEINTEGRACAO"),
            ("can_see_data_s2300ageIntegracao", u"Pode visualizar o conteúdo do modelo S2300AGEINTEGRACAO"),
            ("can_see_menu_s2300ageIntegracao", u"Pode visualizar no menu o modelo S2300AGEINTEGRACAO"),
            ("can_print_list_s2300ageIntegracao", u"Pode imprimir listagem do modelo S2300AGEINTEGRACAO"),
            ("can_print_data_s2300ageIntegracao", u"Pode imprimir o conteúdo do modelo S2300AGEINTEGRACAO"), )
            
        ordering = [
            's2300_infoestagiario',
            'cnpjagntinteg',
            'nmrazao',
            'dsclograd',
            'nrlograd',
            'cep',
            'uf',]



class s2300ageIntegracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300ageIntegracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300brasil(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2300_brasil'       
        managed = True # s2300_brasil #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300brasil", u"Pode ver listagem do modelo S2300BRASIL"),
            ("can_see_data_s2300brasil", u"Pode visualizar o conteúdo do modelo S2300BRASIL"),
            ("can_see_menu_s2300brasil", u"Pode visualizar no menu o modelo S2300BRASIL"),
            ("can_print_list_s2300brasil", u"Pode imprimir listagem do modelo S2300BRASIL"),
            ("can_print_data_s2300brasil", u"Pode imprimir o conteúdo do modelo S2300BRASIL"), )
            
        ordering = [
            's2300_evttsvinicio',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2300brasilSerializer(ModelSerializer):

    class Meta:
    
        model = s2300brasil
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300cargoFuncao(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    codcargo = models.CharField(max_length=30, null=True, )
    codfuncao = models.CharField(max_length=30, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Registro que apresenta o cargo e/ou função ocupada pelo trabalhador sem vínculo'
        db_table = r's2300_cargofuncao'       
        managed = True # s2300_cargofuncao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300cargoFuncao", u"Pode ver listagem do modelo S2300CARGOFUNCAO"),
            ("can_see_data_s2300cargoFuncao", u"Pode visualizar o conteúdo do modelo S2300CARGOFUNCAO"),
            ("can_see_menu_s2300cargoFuncao", u"Pode visualizar no menu o modelo S2300CARGOFUNCAO"),
            ("can_print_list_s2300cargoFuncao", u"Pode imprimir listagem do modelo S2300CARGOFUNCAO"),
            ("can_print_data_s2300cargoFuncao", u"Pode imprimir o conteúdo do modelo S2300CARGOFUNCAO"), )
            
        ordering = [
            's2300_infocomplementares',
            'codcargo',]



class s2300cargoFuncaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300cargoFuncao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300contato(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True, )
    fonealternat = models.CharField(max_length=13, blank=True, null=True, )
    emailprinc = models.CharField(max_length=60, blank=True, null=True, )
    emailalternat = models.CharField(max_length=60, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de contato'
        db_table = r's2300_contato'       
        managed = True # s2300_contato #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300contato", u"Pode ver listagem do modelo S2300CONTATO"),
            ("can_see_data_s2300contato", u"Pode visualizar o conteúdo do modelo S2300CONTATO"),
            ("can_see_menu_s2300contato", u"Pode visualizar no menu o modelo S2300CONTATO"),
            ("can_print_list_s2300contato", u"Pode imprimir listagem do modelo S2300CONTATO"),
            ("can_print_data_s2300contato", u"Pode imprimir o conteúdo do modelo S2300CONTATO"), )
            
        ordering = [
            's2300_evttsvinicio',]



class s2300contatoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300contato
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300dependente(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    sexodep = models.CharField(choices=CHOICES_S2300_SEXODEP, max_length=1, blank=True, null=True, )
    depirrf = models.CharField(choices=CHOICES_S2300_DEPIRRF, max_length=1, null=True, )
    depsf = models.CharField(choices=CHOICES_S2300_DEPSF, max_length=1, null=True, )
    inctrab = models.CharField(choices=CHOICES_S2300_INCTRAB, max_length=1, null=True, )
    depfinsprev = models.CharField(choices=CHOICES_S2300_DEPFINSPREV, max_length=1, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações dos dependentes'
        db_table = r's2300_dependente'       
        managed = True # s2300_dependente #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300dependente", u"Pode ver listagem do modelo S2300DEPENDENTE"),
            ("can_see_data_s2300dependente", u"Pode visualizar o conteúdo do modelo S2300DEPENDENTE"),
            ("can_see_menu_s2300dependente", u"Pode visualizar no menu o modelo S2300DEPENDENTE"),
            ("can_print_list_s2300dependente", u"Pode imprimir listagem do modelo S2300DEPENDENTE"),
            ("can_print_data_s2300dependente", u"Pode imprimir o conteúdo do modelo S2300DEPENDENTE"), )
            
        ordering = [
            's2300_evttsvinicio',
            'tpdep',
            'nmdep',
            'dtnascto',
            'depirrf',
            'depsf',
            'inctrab',]



class s2300dependenteSerializer(ModelSerializer):

    class Meta:
    
        model = s2300dependente
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300documentos(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações dos documentos pessoais do trabalhador'
        db_table = r's2300_documentos'       
        managed = True # s2300_documentos #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300documentos", u"Pode ver listagem do modelo S2300DOCUMENTOS"),
            ("can_see_data_s2300documentos", u"Pode visualizar o conteúdo do modelo S2300DOCUMENTOS"),
            ("can_see_menu_s2300documentos", u"Pode visualizar no menu o modelo S2300DOCUMENTOS"),
            ("can_print_list_s2300documentos", u"Pode imprimir listagem do modelo S2300DOCUMENTOS"),
            ("can_print_data_s2300documentos", u"Pode imprimir o conteúdo do modelo S2300DOCUMENTOS"), )
            
        ordering = [
            's2300_evttsvinicio',]



class s2300documentosSerializer(ModelSerializer):

    class Meta:
    
        model = s2300documentos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300exterior(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2300_exterior'       
        managed = True # s2300_exterior #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300exterior", u"Pode ver listagem do modelo S2300EXTERIOR"),
            ("can_see_data_s2300exterior", u"Pode visualizar o conteúdo do modelo S2300EXTERIOR"),
            ("can_see_menu_s2300exterior", u"Pode visualizar no menu o modelo S2300EXTERIOR"),
            ("can_print_list_s2300exterior", u"Pode imprimir listagem do modelo S2300EXTERIOR"),
            ("can_print_data_s2300exterior", u"Pode imprimir o conteúdo do modelo S2300EXTERIOR"), )
            
        ordering = [
            's2300_evttsvinicio',
            'paisresid',
            'dsclograd',
            'nrlograd',
            'nmcid',]



class s2300exteriorSerializer(ModelSerializer):

    class Meta:
    
        model = s2300exterior
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300fgts(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    opcfgts = models.IntegerField(choices=CHOICES_S2300_OPCFGTS, null=True, )
    dtopcfgts = models.DateField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao FGTS.'
        db_table = r's2300_fgts'       
        managed = True # s2300_fgts #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300fgts", u"Pode ver listagem do modelo S2300FGTS"),
            ("can_see_data_s2300fgts", u"Pode visualizar o conteúdo do modelo S2300FGTS"),
            ("can_see_menu_s2300fgts", u"Pode visualizar no menu o modelo S2300FGTS"),
            ("can_print_list_s2300fgts", u"Pode imprimir listagem do modelo S2300FGTS"),
            ("can_print_data_s2300fgts", u"Pode imprimir o conteúdo do modelo S2300FGTS"), )
            
        ordering = [
            's2300_infocomplementares',
            'opcfgts',]



class s2300fgtsSerializer(ModelSerializer):

    class Meta:
    
        model = s2300fgts
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300infoComplementares(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações complementares sobre o declarante'
        db_table = r's2300_infocomplementares'       
        managed = True # s2300_infocomplementares #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300infoComplementares", u"Pode ver listagem do modelo S2300INFOCOMPLEMENTARES"),
            ("can_see_data_s2300infoComplementares", u"Pode visualizar o conteúdo do modelo S2300INFOCOMPLEMENTARES"),
            ("can_see_menu_s2300infoComplementares", u"Pode visualizar no menu o modelo S2300INFOCOMPLEMENTARES"),
            ("can_print_list_s2300infoComplementares", u"Pode imprimir listagem do modelo S2300INFOCOMPLEMENTARES"),
            ("can_print_data_s2300infoComplementares", u"Pode imprimir o conteúdo do modelo S2300INFOCOMPLEMENTARES"), )
            
        ordering = [
            's2300_evttsvinicio',]



class s2300infoComplementaresSerializer(ModelSerializer):

    class Meta:
    
        model = s2300infoComplementares
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300infoDeficiencia(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    deffisica = models.CharField(choices=CHOICES_S2300_DEFFISICA, max_length=1, null=True, )
    defvisual = models.CharField(choices=CHOICES_S2300_DEFVISUAL, max_length=1, null=True, )
    defauditiva = models.CharField(choices=CHOICES_S2300_DEFAUDITIVA, max_length=1, null=True, )
    defmental = models.CharField(choices=CHOICES_S2300_DEFMENTAL, max_length=1, null=True, )
    defintelectual = models.CharField(choices=CHOICES_S2300_DEFINTELECTUAL, max_length=1, null=True, )
    reabreadap = models.CharField(choices=CHOICES_S2300_REABREADAP, max_length=1, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Pessoa com Deficiência'
        db_table = r's2300_infodeficiencia'       
        managed = True # s2300_infodeficiencia #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300infoDeficiencia", u"Pode ver listagem do modelo S2300INFODEFICIENCIA"),
            ("can_see_data_s2300infoDeficiencia", u"Pode visualizar o conteúdo do modelo S2300INFODEFICIENCIA"),
            ("can_see_menu_s2300infoDeficiencia", u"Pode visualizar no menu o modelo S2300INFODEFICIENCIA"),
            ("can_print_list_s2300infoDeficiencia", u"Pode imprimir listagem do modelo S2300INFODEFICIENCIA"),
            ("can_print_data_s2300infoDeficiencia", u"Pode imprimir o conteúdo do modelo S2300INFODEFICIENCIA"), )
            
        ordering = [
            's2300_evttsvinicio',
            'deffisica',
            'defvisual',
            'defauditiva',
            'defmental',
            'defintelectual',
            'reabreadap',]



class s2300infoDeficienciaSerializer(ModelSerializer):

    class Meta:
    
        model = s2300infoDeficiencia
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300infoDirigenteSindical(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    categorig = models.IntegerField(null=True, )
    cnpjorigem = models.CharField(max_length=14, blank=True, null=True, )
    dtadmorig = models.DateField(blank=True, null=True, )
    matricorig = models.CharField(max_length=30, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Empresa de Origem do Dirigente Sindical'
        db_table = r's2300_infodirigentesindical'       
        managed = True # s2300_infodirigentesindical #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300infoDirigenteSindical", u"Pode ver listagem do modelo S2300INFODIRIGENTESINDICAL"),
            ("can_see_data_s2300infoDirigenteSindical", u"Pode visualizar o conteúdo do modelo S2300INFODIRIGENTESINDICAL"),
            ("can_see_menu_s2300infoDirigenteSindical", u"Pode visualizar no menu o modelo S2300INFODIRIGENTESINDICAL"),
            ("can_print_list_s2300infoDirigenteSindical", u"Pode imprimir listagem do modelo S2300INFODIRIGENTESINDICAL"),
            ("can_print_data_s2300infoDirigenteSindical", u"Pode imprimir o conteúdo do modelo S2300INFODIRIGENTESINDICAL"), )
            
        ordering = [
            's2300_infocomplementares',
            'categorig',]



class s2300infoDirigenteSindicalSerializer(ModelSerializer):

    class Meta:
    
        model = s2300infoDirigenteSindical
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300infoEstagiario(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    natestagio = models.CharField(choices=CHOICES_S2300_NATESTAGIO, max_length=1, null=True, )
    nivestagio = models.IntegerField(choices=CHOICES_S2300_NIVESTAGIO, null=True, )
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
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao estagiário'
        db_table = r's2300_infoestagiario'       
        managed = True # s2300_infoestagiario #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300infoEstagiario", u"Pode ver listagem do modelo S2300INFOESTAGIARIO"),
            ("can_see_data_s2300infoEstagiario", u"Pode visualizar o conteúdo do modelo S2300INFOESTAGIARIO"),
            ("can_see_menu_s2300infoEstagiario", u"Pode visualizar no menu o modelo S2300INFOESTAGIARIO"),
            ("can_print_list_s2300infoEstagiario", u"Pode imprimir listagem do modelo S2300INFOESTAGIARIO"),
            ("can_print_data_s2300infoEstagiario", u"Pode imprimir o conteúdo do modelo S2300INFOESTAGIARIO"), )
            
        ordering = [
            's2300_infocomplementares',
            'natestagio',
            'nivestagio',
            'dtprevterm',
            'nmrazao',]



class s2300infoEstagiarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2300infoEstagiario
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300infoTrabCedido(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    categorig = models.IntegerField(null=True, )
    cnpjcednt = models.CharField(max_length=14, null=True, )
    matricced = models.CharField(max_length=30, null=True, )
    dtadmced = models.DateField(null=True, )
    tpregtrab = models.IntegerField(choices=CHOICES_S2300_TPREGTRAB, null=True, )
    tpregprev = models.IntegerField(choices=CHOICES_S2300_TPREGPREV, null=True, )
    infonus = models.IntegerField(choices=CHOICES_S2300_INFONUS, null=True, )
    indremuncargo = models.CharField(choices=CHOICES_S2300_INDREMUNCARGO, max_length=1, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao trabalhador cedido, preenchidas exclusivamente pelo cessionário.'
        db_table = r's2300_infotrabcedido'       
        managed = True # s2300_infotrabcedido #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300infoTrabCedido", u"Pode ver listagem do modelo S2300INFOTRABCEDIDO"),
            ("can_see_data_s2300infoTrabCedido", u"Pode visualizar o conteúdo do modelo S2300INFOTRABCEDIDO"),
            ("can_see_menu_s2300infoTrabCedido", u"Pode visualizar no menu o modelo S2300INFOTRABCEDIDO"),
            ("can_print_list_s2300infoTrabCedido", u"Pode imprimir listagem do modelo S2300INFOTRABCEDIDO"),
            ("can_print_data_s2300infoTrabCedido", u"Pode imprimir o conteúdo do modelo S2300INFOTRABCEDIDO"), )
            
        ordering = [
            's2300_infocomplementares',
            'categorig',
            'cnpjcednt',
            'matricced',
            'dtadmced',
            'tpregtrab',
            'tpregprev',
            'infonus',]



class s2300infoTrabCedidoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300infoTrabCedido
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300mudancaCPF(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    cpfant = models.CharField(max_length=11, null=True, )
    dtaltcpf = models.DateField(null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de mudança de CPF do trabalhador.'
        db_table = r's2300_mudancacpf'       
        managed = True # s2300_mudancacpf #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300mudancaCPF", u"Pode ver listagem do modelo S2300MUDANCACPF"),
            ("can_see_data_s2300mudancaCPF", u"Pode visualizar o conteúdo do modelo S2300MUDANCACPF"),
            ("can_see_menu_s2300mudancaCPF", u"Pode visualizar no menu o modelo S2300MUDANCACPF"),
            ("can_print_list_s2300mudancaCPF", u"Pode imprimir listagem do modelo S2300MUDANCACPF"),
            ("can_print_data_s2300mudancaCPF", u"Pode imprimir o conteúdo do modelo S2300MUDANCACPF"), )
            
        ordering = [
            's2300_evttsvinicio',
            'cpfant',
            'dtaltcpf',]



class s2300mudancaCPFSerializer(ModelSerializer):

    class Meta:
    
        model = s2300mudancaCPF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300remuneracao(SoftDeletionModel):

    s2300_infocomplementares = models.ForeignKey('s2300.s2300infoComplementares', 
        related_name='%(class)s_s2300_infocomplementares', )
    
    def evento(self): 
        return self.s2300_infocomplementares.evento()
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    undsalfixo = models.IntegerField(choices=CHOICES_S2300_UNDSALFIXO, null=True, )
    dscsalvar = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações da remuneração e periodicidade de pagamento'
        db_table = r's2300_remuneracao'       
        managed = True # s2300_remuneracao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300remuneracao", u"Pode ver listagem do modelo S2300REMUNERACAO"),
            ("can_see_data_s2300remuneracao", u"Pode visualizar o conteúdo do modelo S2300REMUNERACAO"),
            ("can_see_menu_s2300remuneracao", u"Pode visualizar no menu o modelo S2300REMUNERACAO"),
            ("can_print_list_s2300remuneracao", u"Pode imprimir listagem do modelo S2300REMUNERACAO"),
            ("can_print_data_s2300remuneracao", u"Pode imprimir o conteúdo do modelo S2300REMUNERACAO"), )
            
        ordering = [
            's2300_infocomplementares',
            'vrsalfx',
            'undsalfixo',]



class s2300remuneracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300remuneracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300supervisorEstagio(SoftDeletionModel):

    s2300_infoestagiario = models.ForeignKey('s2300.s2300infoEstagiario', 
        related_name='%(class)s_s2300_infoestagiario', )
    
    def evento(self): 
        return self.s2300_infoestagiario.evento()
    cpfsupervisor = models.CharField(max_length=11, null=True, )
    nmsuperv = models.CharField(max_length=70, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Supervisor do Estágio'
        db_table = r's2300_supervisorestagio'       
        managed = True # s2300_supervisorestagio #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300supervisorEstagio", u"Pode ver listagem do modelo S2300SUPERVISORESTAGIO"),
            ("can_see_data_s2300supervisorEstagio", u"Pode visualizar o conteúdo do modelo S2300SUPERVISORESTAGIO"),
            ("can_see_menu_s2300supervisorEstagio", u"Pode visualizar no menu o modelo S2300SUPERVISORESTAGIO"),
            ("can_print_list_s2300supervisorEstagio", u"Pode imprimir listagem do modelo S2300SUPERVISORESTAGIO"),
            ("can_print_data_s2300supervisorEstagio", u"Pode imprimir o conteúdo do modelo S2300SUPERVISORESTAGIO"), )
            
        ordering = [
            's2300_infoestagiario',
            'cpfsupervisor',
            'nmsuperv',]



class s2300supervisorEstagioSerializer(ModelSerializer):

    class Meta:
    
        model = s2300supervisorEstagio
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300termino(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    dtterm = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de término do TSVE'
        db_table = r's2300_termino'       
        managed = True # s2300_termino #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300termino", u"Pode ver listagem do modelo S2300TERMINO"),
            ("can_see_data_s2300termino", u"Pode visualizar o conteúdo do modelo S2300TERMINO"),
            ("can_see_menu_s2300termino", u"Pode visualizar no menu o modelo S2300TERMINO"),
            ("can_print_list_s2300termino", u"Pode imprimir listagem do modelo S2300TERMINO"),
            ("can_print_data_s2300termino", u"Pode imprimir o conteúdo do modelo S2300TERMINO"), )
            
        ordering = [
            's2300_evttsvinicio',
            'dtterm',]



class s2300terminoSerializer(ModelSerializer):

    class Meta:
    
        model = s2300termino
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300trabEstrangeiro(SoftDeletionModel):

    s2300_evttsvinicio = models.ForeignKey('esocial.s2300evtTSVInicio', 
        related_name='%(class)s_s2300_evttsvinicio', )
    
    def evento(self): 
        return self.s2300_evttsvinicio.evento()
    dtchegada = models.DateField(blank=True, null=True, )
    classtrabestrang = models.IntegerField(choices=CHOICES_S2300_CLASSTRABESTRANG, null=True, )
    casadobr = models.CharField(choices=CHOICES_S2300_CASADOBR, max_length=1, null=True, )
    filhosbr = models.CharField(choices=CHOICES_S2300_FILHOSBR, max_length=1, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Grupo de informações do Trabalhador Estrangeiro'
        db_table = r's2300_trabestrangeiro'       
        managed = True # s2300_trabestrangeiro #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300trabEstrangeiro", u"Pode ver listagem do modelo S2300TRABESTRANGEIRO"),
            ("can_see_data_s2300trabEstrangeiro", u"Pode visualizar o conteúdo do modelo S2300TRABESTRANGEIRO"),
            ("can_see_menu_s2300trabEstrangeiro", u"Pode visualizar no menu o modelo S2300TRABESTRANGEIRO"),
            ("can_print_list_s2300trabEstrangeiro", u"Pode imprimir listagem do modelo S2300TRABESTRANGEIRO"),
            ("can_print_data_s2300trabEstrangeiro", u"Pode imprimir o conteúdo do modelo S2300TRABESTRANGEIRO"), )
            
        ordering = [
            's2300_evttsvinicio',
            'classtrabestrang',
            'casadobr',
            'filhosbr',]



class s2300trabEstrangeiroSerializer(ModelSerializer):

    class Meta:
    
        model = s2300trabEstrangeiro
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')