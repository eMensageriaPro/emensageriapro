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
from emensageriapro.esocial.choices import *
get_model = apps.get_model

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





class s1000evtInfoEmpregador(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1000_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1000_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1000_evtinfoempregador_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1000 - Informações do Empregador/Contribuinte/Órgão Público'
        db_table = r's1000_evtinfoempregador'       
        managed = True  # s1000_evtinfoempregador #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1000evtInfoEmpregador", u"Pode ver listagem do modelo S1000EVTINFOEMPREGADOR"),
            ("can_see_data_s1000evtInfoEmpregador", u"Pode visualizar o conteúdo do modelo S1000EVTINFOEMPREGADOR"),
            ("can_see_menu_s1000evtInfoEmpregador", u"Pode visualizar no menu o modelo S1000EVTINFOEMPREGADOR"),
            ("can_print_list_s1000evtInfoEmpregador", u"Pode imprimir listagem do modelo S1000EVTINFOEMPREGADOR"),
            ("can_print_data_s1000evtInfoEmpregador", u"Pode imprimir o conteúdo do modelo S1000EVTINFOEMPREGADOR"),
            ("can_open_s1000evtInfoEmpregador", u"Pode abrir o evento S1000EVTINFOEMPREGADOR para edição"),
            ("can_duplicate_s1000evtInfoEmpregador", u"Pode duplicar o evento S1000EVTINFOEMPREGADOR"),
            ("can_create_change_s1000evtInfoEmpregador", u"Pode criar evento de alteração do evento S1000EVTINFOEMPREGADOR com base em evento existente"),
            ("can_create_delete_s1000evtInfoEmpregador", u"Pode criar evento de exclusão do evento S1000EVTINFOEMPREGADOR com base em evento existente"), 
            ("can_validate_s1000evtInfoEmpregador", u"Pode validar o evento S1000EVTINFOEMPREGADOR"),
            ("can_change_identity_s1000evtInfoEmpregador", u"Pode alterar identidade do evento S1000EVTINFOEMPREGADOR"),
            ("can_see_layout_s1000evtInfoEmpregador", u"Pode ver layout do evento S1000EVTINFOEMPREGADOR"),
            ("can_see_receipt_s1000evtInfoEmpregador", u"Pode ver recibo do evento S1000EVTINFOEMPREGADOR"),
            ("can_see_xml_s1000evtInfoEmpregador", u"Pode ver xml do evento S1000EVTINFOEMPREGADOR"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1000evtInfoEmpregadorSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1000evtInfoEmpregador
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1005evtTabEstab(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1005_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1005_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1005_evttabestab_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1005 - Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos'
        db_table = r's1005_evttabestab'       
        managed = True  # s1005_evttabestab #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1005evtTabEstab", u"Pode ver listagem do modelo S1005EVTTABESTAB"),
            ("can_see_data_s1005evtTabEstab", u"Pode visualizar o conteúdo do modelo S1005EVTTABESTAB"),
            ("can_see_menu_s1005evtTabEstab", u"Pode visualizar no menu o modelo S1005EVTTABESTAB"),
            ("can_print_list_s1005evtTabEstab", u"Pode imprimir listagem do modelo S1005EVTTABESTAB"),
            ("can_print_data_s1005evtTabEstab", u"Pode imprimir o conteúdo do modelo S1005EVTTABESTAB"),
            ("can_open_s1005evtTabEstab", u"Pode abrir o evento S1005EVTTABESTAB para edição"),
            ("can_duplicate_s1005evtTabEstab", u"Pode duplicar o evento S1005EVTTABESTAB"),
            ("can_create_change_s1005evtTabEstab", u"Pode criar evento de alteração do evento S1005EVTTABESTAB com base em evento existente"),
            ("can_create_delete_s1005evtTabEstab", u"Pode criar evento de exclusão do evento S1005EVTTABESTAB com base em evento existente"), 
            ("can_validate_s1005evtTabEstab", u"Pode validar o evento S1005EVTTABESTAB"),
            ("can_change_identity_s1005evtTabEstab", u"Pode alterar identidade do evento S1005EVTTABESTAB"),
            ("can_see_layout_s1005evtTabEstab", u"Pode ver layout do evento S1005EVTTABESTAB"),
            ("can_see_receipt_s1005evtTabEstab", u"Pode ver recibo do evento S1005EVTTABESTAB"),
            ("can_see_xml_s1005evtTabEstab", u"Pode ver xml do evento S1005EVTTABESTAB"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1005evtTabEstabSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1005evtTabEstab
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1010evtTabRubrica(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1010_evttabrubrica_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1010 - Tabela de Rubricas'
        db_table = r's1010_evttabrubrica'       
        managed = True  # s1010_evttabrubrica #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1010evtTabRubrica", u"Pode ver listagem do modelo S1010EVTTABRUBRICA"),
            ("can_see_data_s1010evtTabRubrica", u"Pode visualizar o conteúdo do modelo S1010EVTTABRUBRICA"),
            ("can_see_menu_s1010evtTabRubrica", u"Pode visualizar no menu o modelo S1010EVTTABRUBRICA"),
            ("can_print_list_s1010evtTabRubrica", u"Pode imprimir listagem do modelo S1010EVTTABRUBRICA"),
            ("can_print_data_s1010evtTabRubrica", u"Pode imprimir o conteúdo do modelo S1010EVTTABRUBRICA"),
            ("can_open_s1010evtTabRubrica", u"Pode abrir o evento S1010EVTTABRUBRICA para edição"),
            ("can_duplicate_s1010evtTabRubrica", u"Pode duplicar o evento S1010EVTTABRUBRICA"),
            ("can_create_change_s1010evtTabRubrica", u"Pode criar evento de alteração do evento S1010EVTTABRUBRICA com base em evento existente"),
            ("can_create_delete_s1010evtTabRubrica", u"Pode criar evento de exclusão do evento S1010EVTTABRUBRICA com base em evento existente"), 
            ("can_validate_s1010evtTabRubrica", u"Pode validar o evento S1010EVTTABRUBRICA"),
            ("can_change_identity_s1010evtTabRubrica", u"Pode alterar identidade do evento S1010EVTTABRUBRICA"),
            ("can_see_layout_s1010evtTabRubrica", u"Pode ver layout do evento S1010EVTTABRUBRICA"),
            ("can_see_receipt_s1010evtTabRubrica", u"Pode ver recibo do evento S1010EVTTABRUBRICA"),
            ("can_see_xml_s1010evtTabRubrica", u"Pode ver xml do evento S1010EVTTABRUBRICA"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1010evtTabRubricaSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1010evtTabRubrica
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1020evtTabLotacao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1020_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1020_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1020_evttablotacao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1020 - Tabela de Lotações Tributárias'
        db_table = r's1020_evttablotacao'       
        managed = True  # s1020_evttablotacao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1020evtTabLotacao", u"Pode ver listagem do modelo S1020EVTTABLOTACAO"),
            ("can_see_data_s1020evtTabLotacao", u"Pode visualizar o conteúdo do modelo S1020EVTTABLOTACAO"),
            ("can_see_menu_s1020evtTabLotacao", u"Pode visualizar no menu o modelo S1020EVTTABLOTACAO"),
            ("can_print_list_s1020evtTabLotacao", u"Pode imprimir listagem do modelo S1020EVTTABLOTACAO"),
            ("can_print_data_s1020evtTabLotacao", u"Pode imprimir o conteúdo do modelo S1020EVTTABLOTACAO"),
            ("can_open_s1020evtTabLotacao", u"Pode abrir o evento S1020EVTTABLOTACAO para edição"),
            ("can_duplicate_s1020evtTabLotacao", u"Pode duplicar o evento S1020EVTTABLOTACAO"),
            ("can_create_change_s1020evtTabLotacao", u"Pode criar evento de alteração do evento S1020EVTTABLOTACAO com base em evento existente"),
            ("can_create_delete_s1020evtTabLotacao", u"Pode criar evento de exclusão do evento S1020EVTTABLOTACAO com base em evento existente"), 
            ("can_validate_s1020evtTabLotacao", u"Pode validar o evento S1020EVTTABLOTACAO"),
            ("can_change_identity_s1020evtTabLotacao", u"Pode alterar identidade do evento S1020EVTTABLOTACAO"),
            ("can_see_layout_s1020evtTabLotacao", u"Pode ver layout do evento S1020EVTTABLOTACAO"),
            ("can_see_receipt_s1020evtTabLotacao", u"Pode ver recibo do evento S1020EVTTABLOTACAO"),
            ("can_see_xml_s1020evtTabLotacao", u"Pode ver xml do evento S1020EVTTABLOTACAO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1020evtTabLotacaoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1020evtTabLotacao
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1030evtTabCargo(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1030_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1030_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1030_evttabcargo_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1030 - Tabela de Cargos/Empregos Públicos'
        db_table = r's1030_evttabcargo'       
        managed = True  # s1030_evttabcargo #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1030evtTabCargo", u"Pode ver listagem do modelo S1030EVTTABCARGO"),
            ("can_see_data_s1030evtTabCargo", u"Pode visualizar o conteúdo do modelo S1030EVTTABCARGO"),
            ("can_see_menu_s1030evtTabCargo", u"Pode visualizar no menu o modelo S1030EVTTABCARGO"),
            ("can_print_list_s1030evtTabCargo", u"Pode imprimir listagem do modelo S1030EVTTABCARGO"),
            ("can_print_data_s1030evtTabCargo", u"Pode imprimir o conteúdo do modelo S1030EVTTABCARGO"),
            ("can_open_s1030evtTabCargo", u"Pode abrir o evento S1030EVTTABCARGO para edição"),
            ("can_duplicate_s1030evtTabCargo", u"Pode duplicar o evento S1030EVTTABCARGO"),
            ("can_create_change_s1030evtTabCargo", u"Pode criar evento de alteração do evento S1030EVTTABCARGO com base em evento existente"),
            ("can_create_delete_s1030evtTabCargo", u"Pode criar evento de exclusão do evento S1030EVTTABCARGO com base em evento existente"), 
            ("can_validate_s1030evtTabCargo", u"Pode validar o evento S1030EVTTABCARGO"),
            ("can_change_identity_s1030evtTabCargo", u"Pode alterar identidade do evento S1030EVTTABCARGO"),
            ("can_see_layout_s1030evtTabCargo", u"Pode ver layout do evento S1030EVTTABCARGO"),
            ("can_see_receipt_s1030evtTabCargo", u"Pode ver recibo do evento S1030EVTTABCARGO"),
            ("can_see_xml_s1030evtTabCargo", u"Pode ver xml do evento S1030EVTTABCARGO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1030evtTabCargoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1030evtTabCargo
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1035evtTabCarreira(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1035_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1035_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1035_evttabcarreira_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1035 - Tabela de Carreiras Públicas'
        db_table = r's1035_evttabcarreira'       
        managed = True  # s1035_evttabcarreira #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1035evtTabCarreira", u"Pode ver listagem do modelo S1035EVTTABCARREIRA"),
            ("can_see_data_s1035evtTabCarreira", u"Pode visualizar o conteúdo do modelo S1035EVTTABCARREIRA"),
            ("can_see_menu_s1035evtTabCarreira", u"Pode visualizar no menu o modelo S1035EVTTABCARREIRA"),
            ("can_print_list_s1035evtTabCarreira", u"Pode imprimir listagem do modelo S1035EVTTABCARREIRA"),
            ("can_print_data_s1035evtTabCarreira", u"Pode imprimir o conteúdo do modelo S1035EVTTABCARREIRA"),
            ("can_open_s1035evtTabCarreira", u"Pode abrir o evento S1035EVTTABCARREIRA para edição"),
            ("can_duplicate_s1035evtTabCarreira", u"Pode duplicar o evento S1035EVTTABCARREIRA"),
            ("can_create_change_s1035evtTabCarreira", u"Pode criar evento de alteração do evento S1035EVTTABCARREIRA com base em evento existente"),
            ("can_create_delete_s1035evtTabCarreira", u"Pode criar evento de exclusão do evento S1035EVTTABCARREIRA com base em evento existente"), 
            ("can_validate_s1035evtTabCarreira", u"Pode validar o evento S1035EVTTABCARREIRA"),
            ("can_change_identity_s1035evtTabCarreira", u"Pode alterar identidade do evento S1035EVTTABCARREIRA"),
            ("can_see_layout_s1035evtTabCarreira", u"Pode ver layout do evento S1035EVTTABCARREIRA"),
            ("can_see_receipt_s1035evtTabCarreira", u"Pode ver recibo do evento S1035EVTTABCARREIRA"),
            ("can_see_xml_s1035evtTabCarreira", u"Pode ver xml do evento S1035EVTTABCARREIRA"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1035evtTabCarreiraSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1035evtTabCarreira
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1040evtTabFuncao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1040_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1040_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1040_evttabfuncao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1040 - Tabela de Funções/Cargos em Comissão'
        db_table = r's1040_evttabfuncao'       
        managed = True  # s1040_evttabfuncao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1040evtTabFuncao", u"Pode ver listagem do modelo S1040EVTTABFUNCAO"),
            ("can_see_data_s1040evtTabFuncao", u"Pode visualizar o conteúdo do modelo S1040EVTTABFUNCAO"),
            ("can_see_menu_s1040evtTabFuncao", u"Pode visualizar no menu o modelo S1040EVTTABFUNCAO"),
            ("can_print_list_s1040evtTabFuncao", u"Pode imprimir listagem do modelo S1040EVTTABFUNCAO"),
            ("can_print_data_s1040evtTabFuncao", u"Pode imprimir o conteúdo do modelo S1040EVTTABFUNCAO"),
            ("can_open_s1040evtTabFuncao", u"Pode abrir o evento S1040EVTTABFUNCAO para edição"),
            ("can_duplicate_s1040evtTabFuncao", u"Pode duplicar o evento S1040EVTTABFUNCAO"),
            ("can_create_change_s1040evtTabFuncao", u"Pode criar evento de alteração do evento S1040EVTTABFUNCAO com base em evento existente"),
            ("can_create_delete_s1040evtTabFuncao", u"Pode criar evento de exclusão do evento S1040EVTTABFUNCAO com base em evento existente"), 
            ("can_validate_s1040evtTabFuncao", u"Pode validar o evento S1040EVTTABFUNCAO"),
            ("can_change_identity_s1040evtTabFuncao", u"Pode alterar identidade do evento S1040EVTTABFUNCAO"),
            ("can_see_layout_s1040evtTabFuncao", u"Pode ver layout do evento S1040EVTTABFUNCAO"),
            ("can_see_receipt_s1040evtTabFuncao", u"Pode ver recibo do evento S1040EVTTABFUNCAO"),
            ("can_see_xml_s1040evtTabFuncao", u"Pode ver xml do evento S1040EVTTABFUNCAO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1040evtTabFuncaoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1040evtTabFuncao
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1050evtTabHorTur(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1050_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1050_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1050_evttabhortur_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1050 - Tabela de Horários/Turnos de Trabalho'
        db_table = r's1050_evttabhortur'       
        managed = True  # s1050_evttabhortur #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1050evtTabHorTur", u"Pode ver listagem do modelo S1050EVTTABHORTUR"),
            ("can_see_data_s1050evtTabHorTur", u"Pode visualizar o conteúdo do modelo S1050EVTTABHORTUR"),
            ("can_see_menu_s1050evtTabHorTur", u"Pode visualizar no menu o modelo S1050EVTTABHORTUR"),
            ("can_print_list_s1050evtTabHorTur", u"Pode imprimir listagem do modelo S1050EVTTABHORTUR"),
            ("can_print_data_s1050evtTabHorTur", u"Pode imprimir o conteúdo do modelo S1050EVTTABHORTUR"),
            ("can_open_s1050evtTabHorTur", u"Pode abrir o evento S1050EVTTABHORTUR para edição"),
            ("can_duplicate_s1050evtTabHorTur", u"Pode duplicar o evento S1050EVTTABHORTUR"),
            ("can_create_change_s1050evtTabHorTur", u"Pode criar evento de alteração do evento S1050EVTTABHORTUR com base em evento existente"),
            ("can_create_delete_s1050evtTabHorTur", u"Pode criar evento de exclusão do evento S1050EVTTABHORTUR com base em evento existente"), 
            ("can_validate_s1050evtTabHorTur", u"Pode validar o evento S1050EVTTABHORTUR"),
            ("can_change_identity_s1050evtTabHorTur", u"Pode alterar identidade do evento S1050EVTTABHORTUR"),
            ("can_see_layout_s1050evtTabHorTur", u"Pode ver layout do evento S1050EVTTABHORTUR"),
            ("can_see_receipt_s1050evtTabHorTur", u"Pode ver recibo do evento S1050EVTTABHORTUR"),
            ("can_see_xml_s1050evtTabHorTur", u"Pode ver xml do evento S1050EVTTABHORTUR"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1050evtTabHorTurSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1050evtTabHorTur
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1060evtTabAmbiente(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1060_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1060_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1060_evttabambiente_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1060 - Tabela de Ambientes de Trabalho'
        db_table = r's1060_evttabambiente'       
        managed = True  # s1060_evttabambiente #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1060evtTabAmbiente", u"Pode ver listagem do modelo S1060EVTTABAMBIENTE"),
            ("can_see_data_s1060evtTabAmbiente", u"Pode visualizar o conteúdo do modelo S1060EVTTABAMBIENTE"),
            ("can_see_menu_s1060evtTabAmbiente", u"Pode visualizar no menu o modelo S1060EVTTABAMBIENTE"),
            ("can_print_list_s1060evtTabAmbiente", u"Pode imprimir listagem do modelo S1060EVTTABAMBIENTE"),
            ("can_print_data_s1060evtTabAmbiente", u"Pode imprimir o conteúdo do modelo S1060EVTTABAMBIENTE"),
            ("can_open_s1060evtTabAmbiente", u"Pode abrir o evento S1060EVTTABAMBIENTE para edição"),
            ("can_duplicate_s1060evtTabAmbiente", u"Pode duplicar o evento S1060EVTTABAMBIENTE"),
            ("can_create_change_s1060evtTabAmbiente", u"Pode criar evento de alteração do evento S1060EVTTABAMBIENTE com base em evento existente"),
            ("can_create_delete_s1060evtTabAmbiente", u"Pode criar evento de exclusão do evento S1060EVTTABAMBIENTE com base em evento existente"), 
            ("can_validate_s1060evtTabAmbiente", u"Pode validar o evento S1060EVTTABAMBIENTE"),
            ("can_change_identity_s1060evtTabAmbiente", u"Pode alterar identidade do evento S1060EVTTABAMBIENTE"),
            ("can_see_layout_s1060evtTabAmbiente", u"Pode ver layout do evento S1060EVTTABAMBIENTE"),
            ("can_see_receipt_s1060evtTabAmbiente", u"Pode ver recibo do evento S1060EVTTABAMBIENTE"),
            ("can_see_xml_s1060evtTabAmbiente", u"Pode ver xml do evento S1060EVTTABAMBIENTE"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1060evtTabAmbienteSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1060evtTabAmbiente
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1070evtTabProcesso(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1070_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1070_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1070_evttabprocesso_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1070 - Tabela de Processos Administrativos/Judiciais'
        db_table = r's1070_evttabprocesso'       
        managed = True  # s1070_evttabprocesso #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1070evtTabProcesso", u"Pode ver listagem do modelo S1070EVTTABPROCESSO"),
            ("can_see_data_s1070evtTabProcesso", u"Pode visualizar o conteúdo do modelo S1070EVTTABPROCESSO"),
            ("can_see_menu_s1070evtTabProcesso", u"Pode visualizar no menu o modelo S1070EVTTABPROCESSO"),
            ("can_print_list_s1070evtTabProcesso", u"Pode imprimir listagem do modelo S1070EVTTABPROCESSO"),
            ("can_print_data_s1070evtTabProcesso", u"Pode imprimir o conteúdo do modelo S1070EVTTABPROCESSO"),
            ("can_open_s1070evtTabProcesso", u"Pode abrir o evento S1070EVTTABPROCESSO para edição"),
            ("can_duplicate_s1070evtTabProcesso", u"Pode duplicar o evento S1070EVTTABPROCESSO"),
            ("can_create_change_s1070evtTabProcesso", u"Pode criar evento de alteração do evento S1070EVTTABPROCESSO com base em evento existente"),
            ("can_create_delete_s1070evtTabProcesso", u"Pode criar evento de exclusão do evento S1070EVTTABPROCESSO com base em evento existente"), 
            ("can_validate_s1070evtTabProcesso", u"Pode validar o evento S1070EVTTABPROCESSO"),
            ("can_change_identity_s1070evtTabProcesso", u"Pode alterar identidade do evento S1070EVTTABPROCESSO"),
            ("can_see_layout_s1070evtTabProcesso", u"Pode ver layout do evento S1070EVTTABPROCESSO"),
            ("can_see_receipt_s1070evtTabProcesso", u"Pode ver recibo do evento S1070EVTTABPROCESSO"),
            ("can_see_xml_s1070evtTabProcesso", u"Pode ver xml do evento S1070EVTTABPROCESSO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1070evtTabProcessoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1070evtTabProcesso
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1080evtTabOperPort(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1080_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1080_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1080_evttaboperport_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1080 - Tabela de Operadores Portuários'
        db_table = r's1080_evttaboperport'       
        managed = True  # s1080_evttaboperport #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1080evtTabOperPort", u"Pode ver listagem do modelo S1080EVTTABOPERPORT"),
            ("can_see_data_s1080evtTabOperPort", u"Pode visualizar o conteúdo do modelo S1080EVTTABOPERPORT"),
            ("can_see_menu_s1080evtTabOperPort", u"Pode visualizar no menu o modelo S1080EVTTABOPERPORT"),
            ("can_print_list_s1080evtTabOperPort", u"Pode imprimir listagem do modelo S1080EVTTABOPERPORT"),
            ("can_print_data_s1080evtTabOperPort", u"Pode imprimir o conteúdo do modelo S1080EVTTABOPERPORT"),
            ("can_open_s1080evtTabOperPort", u"Pode abrir o evento S1080EVTTABOPERPORT para edição"),
            ("can_duplicate_s1080evtTabOperPort", u"Pode duplicar o evento S1080EVTTABOPERPORT"),
            ("can_create_change_s1080evtTabOperPort", u"Pode criar evento de alteração do evento S1080EVTTABOPERPORT com base em evento existente"),
            ("can_create_delete_s1080evtTabOperPort", u"Pode criar evento de exclusão do evento S1080EVTTABOPERPORT com base em evento existente"), 
            ("can_validate_s1080evtTabOperPort", u"Pode validar o evento S1080EVTTABOPERPORT"),
            ("can_change_identity_s1080evtTabOperPort", u"Pode alterar identidade do evento S1080EVTTABOPERPORT"),
            ("can_see_layout_s1080evtTabOperPort", u"Pode ver layout do evento S1080EVTTABOPERPORT"),
            ("can_see_receipt_s1080evtTabOperPort", u"Pode ver recibo do evento S1080EVTTABOPERPORT"),
            ("can_see_xml_s1080evtTabOperPort", u"Pode ver xml do evento S1080EVTTABOPERPORT"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1080evtTabOperPortSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1080evtTabOperPort
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1200evtRemun(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1200_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1200_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1200_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1200_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1200_evtremun_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social'
        db_table = r's1200_evtremun'       
        managed = True  # s1200_evtremun #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1200evtRemun", u"Pode ver listagem do modelo S1200EVTREMUN"),
            ("can_see_data_s1200evtRemun", u"Pode visualizar o conteúdo do modelo S1200EVTREMUN"),
            ("can_see_menu_s1200evtRemun", u"Pode visualizar no menu o modelo S1200EVTREMUN"),
            ("can_print_list_s1200evtRemun", u"Pode imprimir listagem do modelo S1200EVTREMUN"),
            ("can_print_data_s1200evtRemun", u"Pode imprimir o conteúdo do modelo S1200EVTREMUN"),
            ("can_open_s1200evtRemun", u"Pode abrir o evento S1200EVTREMUN para edição"),
            ("can_duplicate_s1200evtRemun", u"Pode duplicar o evento S1200EVTREMUN"),
            ("can_validate_s1200evtRemun", u"Pode validar o evento S1200EVTREMUN"),
            ("can_change_identity_s1200evtRemun", u"Pode alterar identidade do evento S1200EVTREMUN"),
            ("can_see_layout_s1200evtRemun", u"Pode ver layout do evento S1200EVTREMUN"),
            ("can_see_receipt_s1200evtRemun", u"Pode ver recibo do evento S1200EVTREMUN"),
            ("can_see_xml_s1200evtRemun", u"Pode ver xml do evento S1200EVTREMUN"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s1200evtRemunSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1200evtRemun
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1202evtRmnRPPS(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1202_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1202_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1202_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1202_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    qtddepfp = models.IntegerField(blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1202_evtrmnrpps_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1202 - Remuneração de servidor vinculado a Regime Próprio de Previd. Social'
        db_table = r's1202_evtrmnrpps'       
        managed = True  # s1202_evtrmnrpps #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1202evtRmnRPPS", u"Pode ver listagem do modelo S1202EVTRMNRPPS"),
            ("can_see_data_s1202evtRmnRPPS", u"Pode visualizar o conteúdo do modelo S1202EVTRMNRPPS"),
            ("can_see_menu_s1202evtRmnRPPS", u"Pode visualizar no menu o modelo S1202EVTRMNRPPS"),
            ("can_print_list_s1202evtRmnRPPS", u"Pode imprimir listagem do modelo S1202EVTRMNRPPS"),
            ("can_print_data_s1202evtRmnRPPS", u"Pode imprimir o conteúdo do modelo S1202EVTRMNRPPS"),
            ("can_open_s1202evtRmnRPPS", u"Pode abrir o evento S1202EVTRMNRPPS para edição"),
            ("can_duplicate_s1202evtRmnRPPS", u"Pode duplicar o evento S1202EVTRMNRPPS"),
            ("can_validate_s1202evtRmnRPPS", u"Pode validar o evento S1202EVTRMNRPPS"),
            ("can_change_identity_s1202evtRmnRPPS", u"Pode alterar identidade do evento S1202EVTRMNRPPS"),
            ("can_see_layout_s1202evtRmnRPPS", u"Pode ver layout do evento S1202EVTRMNRPPS"),
            ("can_see_receipt_s1202evtRmnRPPS", u"Pode ver recibo do evento S1202EVTRMNRPPS"),
            ("can_see_xml_s1202evtRmnRPPS", u"Pode ver xml do evento S1202EVTRMNRPPS"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s1202evtRmnRPPSSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1202evtRmnRPPS
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1207evtBenPrRP(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1207_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1207_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1207_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1207_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1207_evtbenprrp_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1207 - Benefícios previdenciários - RPPS'
        db_table = r's1207_evtbenprrp'       
        managed = True  # s1207_evtbenprrp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1207evtBenPrRP", u"Pode ver listagem do modelo S1207EVTBENPRRP"),
            ("can_see_data_s1207evtBenPrRP", u"Pode visualizar o conteúdo do modelo S1207EVTBENPRRP"),
            ("can_see_menu_s1207evtBenPrRP", u"Pode visualizar no menu o modelo S1207EVTBENPRRP"),
            ("can_print_list_s1207evtBenPrRP", u"Pode imprimir listagem do modelo S1207EVTBENPRRP"),
            ("can_print_data_s1207evtBenPrRP", u"Pode imprimir o conteúdo do modelo S1207EVTBENPRRP"),
            ("can_open_s1207evtBenPrRP", u"Pode abrir o evento S1207EVTBENPRRP para edição"),
            ("can_duplicate_s1207evtBenPrRP", u"Pode duplicar o evento S1207EVTBENPRRP"),
            ("can_validate_s1207evtBenPrRP", u"Pode validar o evento S1207EVTBENPRRP"),
            ("can_change_identity_s1207evtBenPrRP", u"Pode alterar identidade do evento S1207EVTBENPRRP"),
            ("can_see_layout_s1207evtBenPrRP", u"Pode ver layout do evento S1207EVTBENPRRP"),
            ("can_see_receipt_s1207evtBenPrRP", u"Pode ver recibo do evento S1207EVTBENPRRP"),
            ("can_see_xml_s1207evtBenPrRP", u"Pode ver xml do evento S1207EVTBENPRRP"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef', ]



class s1207evtBenPrRPSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1207evtBenPrRP
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1210evtPgtos(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1210_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1210_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1210_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1210_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1210_evtpgtos_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1210 - Pagamentos de Rendimentos do Trabalho'
        db_table = r's1210_evtpgtos'       
        managed = True  # s1210_evtpgtos #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1210evtPgtos", u"Pode ver listagem do modelo S1210EVTPGTOS"),
            ("can_see_data_s1210evtPgtos", u"Pode visualizar o conteúdo do modelo S1210EVTPGTOS"),
            ("can_see_menu_s1210evtPgtos", u"Pode visualizar no menu o modelo S1210EVTPGTOS"),
            ("can_print_list_s1210evtPgtos", u"Pode imprimir listagem do modelo S1210EVTPGTOS"),
            ("can_print_data_s1210evtPgtos", u"Pode imprimir o conteúdo do modelo S1210EVTPGTOS"),
            ("can_open_s1210evtPgtos", u"Pode abrir o evento S1210EVTPGTOS para edição"),
            ("can_duplicate_s1210evtPgtos", u"Pode duplicar o evento S1210EVTPGTOS"),
            ("can_validate_s1210evtPgtos", u"Pode validar o evento S1210EVTPGTOS"),
            ("can_change_identity_s1210evtPgtos", u"Pode alterar identidade do evento S1210EVTPGTOS"),
            ("can_see_layout_s1210evtPgtos", u"Pode ver layout do evento S1210EVTPGTOS"),
            ("can_see_receipt_s1210evtPgtos", u"Pode ver recibo do evento S1210EVTPGTOS"),
            ("can_see_xml_s1210evtPgtos", u"Pode ver xml do evento S1210EVTPGTOS"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef', ]



class s1210evtPgtosSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1210evtPgtos
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1250evtAqProd(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1250_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1250_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1250_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1250_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    tpinscadq = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinscadq = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1250_evtaqprod_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1250 - Aquisição de Produção Rural'
        db_table = r's1250_evtaqprod'       
        managed = True  # s1250_evtaqprod #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1250evtAqProd", u"Pode ver listagem do modelo S1250EVTAQPROD"),
            ("can_see_data_s1250evtAqProd", u"Pode visualizar o conteúdo do modelo S1250EVTAQPROD"),
            ("can_see_menu_s1250evtAqProd", u"Pode visualizar no menu o modelo S1250EVTAQPROD"),
            ("can_print_list_s1250evtAqProd", u"Pode imprimir listagem do modelo S1250EVTAQPROD"),
            ("can_print_data_s1250evtAqProd", u"Pode imprimir o conteúdo do modelo S1250EVTAQPROD"),
            ("can_open_s1250evtAqProd", u"Pode abrir o evento S1250EVTAQPROD para edição"),
            ("can_duplicate_s1250evtAqProd", u"Pode duplicar o evento S1250EVTAQPROD"),
            ("can_validate_s1250evtAqProd", u"Pode validar o evento S1250EVTAQPROD"),
            ("can_change_identity_s1250evtAqProd", u"Pode alterar identidade do evento S1250EVTAQPROD"),
            ("can_see_layout_s1250evtAqProd", u"Pode ver layout do evento S1250EVTAQPROD"),
            ("can_see_receipt_s1250evtAqProd", u"Pode ver recibo do evento S1250EVTAQPROD"),
            ("can_see_xml_s1250evtAqProd", u"Pode ver xml do evento S1250EVTAQPROD"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscadq',
            'nrinscadq', ]



class s1250evtAqProdSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1250evtAqProd
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1260evtComProd(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1260_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1260_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1260_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1260_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    nrinscestabrural = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1260_evtcomprod_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1260 - Comercialização da Produção Rural Pessoa Física'
        db_table = r's1260_evtcomprod'       
        managed = True  # s1260_evtcomprod #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1260evtComProd", u"Pode ver listagem do modelo S1260EVTCOMPROD"),
            ("can_see_data_s1260evtComProd", u"Pode visualizar o conteúdo do modelo S1260EVTCOMPROD"),
            ("can_see_menu_s1260evtComProd", u"Pode visualizar no menu o modelo S1260EVTCOMPROD"),
            ("can_print_list_s1260evtComProd", u"Pode imprimir listagem do modelo S1260EVTCOMPROD"),
            ("can_print_data_s1260evtComProd", u"Pode imprimir o conteúdo do modelo S1260EVTCOMPROD"),
            ("can_open_s1260evtComProd", u"Pode abrir o evento S1260EVTCOMPROD para edição"),
            ("can_duplicate_s1260evtComProd", u"Pode duplicar o evento S1260EVTCOMPROD"),
            ("can_validate_s1260evtComProd", u"Pode validar o evento S1260EVTCOMPROD"),
            ("can_change_identity_s1260evtComProd", u"Pode alterar identidade do evento S1260EVTCOMPROD"),
            ("can_see_layout_s1260evtComProd", u"Pode ver layout do evento S1260EVTCOMPROD"),
            ("can_see_receipt_s1260evtComProd", u"Pode ver recibo do evento S1260EVTCOMPROD"),
            ("can_see_xml_s1260evtComProd", u"Pode ver xml do evento S1260EVTCOMPROD"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'nrinscestabrural', ]



class s1260evtComProdSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1260evtComProd
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1270evtContratAvNP(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1270_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1270_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1270_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1270_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1270_evtcontratavnp_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1270 - Contratação de Trabalhadores Avulsos Não Portuários'
        db_table = r's1270_evtcontratavnp'       
        managed = True  # s1270_evtcontratavnp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1270evtContratAvNP", u"Pode ver listagem do modelo S1270EVTCONTRATAVNP"),
            ("can_see_data_s1270evtContratAvNP", u"Pode visualizar o conteúdo do modelo S1270EVTCONTRATAVNP"),
            ("can_see_menu_s1270evtContratAvNP", u"Pode visualizar no menu o modelo S1270EVTCONTRATAVNP"),
            ("can_print_list_s1270evtContratAvNP", u"Pode imprimir listagem do modelo S1270EVTCONTRATAVNP"),
            ("can_print_data_s1270evtContratAvNP", u"Pode imprimir o conteúdo do modelo S1270EVTCONTRATAVNP"),
            ("can_open_s1270evtContratAvNP", u"Pode abrir o evento S1270EVTCONTRATAVNP para edição"),
            ("can_duplicate_s1270evtContratAvNP", u"Pode duplicar o evento S1270EVTCONTRATAVNP"),
            ("can_validate_s1270evtContratAvNP", u"Pode validar o evento S1270EVTCONTRATAVNP"),
            ("can_change_identity_s1270evtContratAvNP", u"Pode alterar identidade do evento S1270EVTCONTRATAVNP"),
            ("can_see_layout_s1270evtContratAvNP", u"Pode ver layout do evento S1270EVTCONTRATAVNP"),
            ("can_see_receipt_s1270evtContratAvNP", u"Pode ver recibo do evento S1270EVTCONTRATAVNP"),
            ("can_see_xml_s1270evtContratAvNP", u"Pode ver xml do evento S1270EVTCONTRATAVNP"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1270evtContratAvNPSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1270evtContratAvNP
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1280evtInfoComplPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1280_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1280_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1280_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1280_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1280_evtinfocomplper_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1280 - Informações Complementares aos Eventos Periódicos'
        db_table = r's1280_evtinfocomplper'       
        managed = True  # s1280_evtinfocomplper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1280evtInfoComplPer", u"Pode ver listagem do modelo S1280EVTINFOCOMPLPER"),
            ("can_see_data_s1280evtInfoComplPer", u"Pode visualizar o conteúdo do modelo S1280EVTINFOCOMPLPER"),
            ("can_see_menu_s1280evtInfoComplPer", u"Pode visualizar no menu o modelo S1280EVTINFOCOMPLPER"),
            ("can_print_list_s1280evtInfoComplPer", u"Pode imprimir listagem do modelo S1280EVTINFOCOMPLPER"),
            ("can_print_data_s1280evtInfoComplPer", u"Pode imprimir o conteúdo do modelo S1280EVTINFOCOMPLPER"),
            ("can_open_s1280evtInfoComplPer", u"Pode abrir o evento S1280EVTINFOCOMPLPER para edição"),
            ("can_duplicate_s1280evtInfoComplPer", u"Pode duplicar o evento S1280EVTINFOCOMPLPER"),
            ("can_validate_s1280evtInfoComplPer", u"Pode validar o evento S1280EVTINFOCOMPLPER"),
            ("can_change_identity_s1280evtInfoComplPer", u"Pode alterar identidade do evento S1280EVTINFOCOMPLPER"),
            ("can_see_layout_s1280evtInfoComplPer", u"Pode ver layout do evento S1280EVTINFOCOMPLPER"),
            ("can_see_receipt_s1280evtInfoComplPer", u"Pode ver recibo do evento S1280EVTINFOCOMPLPER"),
            ("can_see_xml_s1280evtInfoComplPer", u"Pode ver xml do evento S1280EVTINFOCOMPLPER"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1280evtInfoComplPerSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1280evtInfoComplPer
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1295evtTotConting(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1295_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1295_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1295_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1295_evttotconting_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1295 - Solicitação de Totalização para Pagamento em Contingência'
        db_table = r's1295_evttotconting'       
        managed = True  # s1295_evttotconting #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1295evtTotConting", u"Pode ver listagem do modelo S1295EVTTOTCONTING"),
            ("can_see_data_s1295evtTotConting", u"Pode visualizar o conteúdo do modelo S1295EVTTOTCONTING"),
            ("can_see_menu_s1295evtTotConting", u"Pode visualizar no menu o modelo S1295EVTTOTCONTING"),
            ("can_print_list_s1295evtTotConting", u"Pode imprimir listagem do modelo S1295EVTTOTCONTING"),
            ("can_print_data_s1295evtTotConting", u"Pode imprimir o conteúdo do modelo S1295EVTTOTCONTING"),
            ("can_open_s1295evtTotConting", u"Pode abrir o evento S1295EVTTOTCONTING para edição"),
            ("can_duplicate_s1295evtTotConting", u"Pode duplicar o evento S1295EVTTOTCONTING"),
            ("can_validate_s1295evtTotConting", u"Pode validar o evento S1295EVTTOTCONTING"),
            ("can_change_identity_s1295evtTotConting", u"Pode alterar identidade do evento S1295EVTTOTCONTING"),
            ("can_see_layout_s1295evtTotConting", u"Pode ver layout do evento S1295EVTTOTCONTING"),
            ("can_see_receipt_s1295evtTotConting", u"Pode ver recibo do evento S1295EVTTOTCONTING"),
            ("can_see_xml_s1295evtTotConting", u"Pode ver xml do evento S1295EVTTOTCONTING"),)
            
        ordering = [
            'identidade',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1295evtTotContingSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1295evtTotConting
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1298evtReabreEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1298_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1298_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1298_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1298_evtreabreevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1298 - Reabertura dos Eventos Periódicos'
        db_table = r's1298_evtreabreevper'       
        managed = True  # s1298_evtreabreevper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1298evtReabreEvPer", u"Pode ver listagem do modelo S1298EVTREABREEVPER"),
            ("can_see_data_s1298evtReabreEvPer", u"Pode visualizar o conteúdo do modelo S1298EVTREABREEVPER"),
            ("can_see_menu_s1298evtReabreEvPer", u"Pode visualizar no menu o modelo S1298EVTREABREEVPER"),
            ("can_print_list_s1298evtReabreEvPer", u"Pode imprimir listagem do modelo S1298EVTREABREEVPER"),
            ("can_print_data_s1298evtReabreEvPer", u"Pode imprimir o conteúdo do modelo S1298EVTREABREEVPER"),
            ("can_open_s1298evtReabreEvPer", u"Pode abrir o evento S1298EVTREABREEVPER para edição"),
            ("can_duplicate_s1298evtReabreEvPer", u"Pode duplicar o evento S1298EVTREABREEVPER"),
            ("can_validate_s1298evtReabreEvPer", u"Pode validar o evento S1298EVTREABREEVPER"),
            ("can_change_identity_s1298evtReabreEvPer", u"Pode alterar identidade do evento S1298EVTREABREEVPER"),
            ("can_see_layout_s1298evtReabreEvPer", u"Pode ver layout do evento S1298EVTREABREEVPER"),
            ("can_see_receipt_s1298evtReabreEvPer", u"Pode ver recibo do evento S1298EVTREABREEVPER"),
            ("can_see_xml_s1298evtReabreEvPer", u"Pode ver xml do evento S1298EVTREABREEVPER"),)
            
        ordering = [
            'identidade',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1298evtReabreEvPerSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1298evtReabreEvPer
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1299evtFechaEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1299_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1299_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1299_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    evtremun = models.CharField(choices=CHOICES_S1299_EVTREMUN, max_length=1, null=True, )
    evtpgtos = models.CharField(choices=CHOICES_S1299_EVTPGTOS, max_length=1, null=True, )
    evtaqprod = models.CharField(choices=CHOICES_S1299_EVTAQPROD, max_length=1, null=True, )
    evtcomprod = models.CharField(choices=CHOICES_S1299_EVTCOMPROD, max_length=1, null=True, )
    evtcontratavnp = models.CharField(choices=CHOICES_S1299_EVTCONTRATAVNP, max_length=1, null=True, )
    evtinfocomplper = models.CharField(choices=CHOICES_S1299_EVTINFOCOMPLPER, max_length=1, null=True, )
    compsemmovto = models.CharField(max_length=7, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1299_evtfechaevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1299 - Fechamento dos Eventos Periódicos'
        db_table = r's1299_evtfechaevper'       
        managed = True  # s1299_evtfechaevper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1299evtFechaEvPer", u"Pode ver listagem do modelo S1299EVTFECHAEVPER"),
            ("can_see_data_s1299evtFechaEvPer", u"Pode visualizar o conteúdo do modelo S1299EVTFECHAEVPER"),
            ("can_see_menu_s1299evtFechaEvPer", u"Pode visualizar no menu o modelo S1299EVTFECHAEVPER"),
            ("can_print_list_s1299evtFechaEvPer", u"Pode imprimir listagem do modelo S1299EVTFECHAEVPER"),
            ("can_print_data_s1299evtFechaEvPer", u"Pode imprimir o conteúdo do modelo S1299EVTFECHAEVPER"),
            ("can_open_s1299evtFechaEvPer", u"Pode abrir o evento S1299EVTFECHAEVPER para edição"),
            ("can_duplicate_s1299evtFechaEvPer", u"Pode duplicar o evento S1299EVTFECHAEVPER"),
            ("can_validate_s1299evtFechaEvPer", u"Pode validar o evento S1299EVTFECHAEVPER"),
            ("can_change_identity_s1299evtFechaEvPer", u"Pode alterar identidade do evento S1299EVTFECHAEVPER"),
            ("can_see_layout_s1299evtFechaEvPer", u"Pode ver layout do evento S1299EVTFECHAEVPER"),
            ("can_see_receipt_s1299evtFechaEvPer", u"Pode ver recibo do evento S1299EVTFECHAEVPER"),
            ("can_see_xml_s1299evtFechaEvPer", u"Pode ver xml do evento S1299EVTFECHAEVPER"),)
            
        ordering = [
            'identidade',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'evtremun',
            'evtpgtos',
            'evtaqprod',
            'evtcomprod',
            'evtcontratavnp',
            'evtinfocomplper', ]



class s1299evtFechaEvPerSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1299evtFechaEvPer
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s1300evtContrSindPatr(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S1300_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S1300_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S1300_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S1300_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s1300_evtcontrsindpatr_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-1300 - Contribuição Sindical Patronal'
        db_table = r's1300_evtcontrsindpatr'       
        managed = True  # s1300_evtcontrsindpatr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s1300evtContrSindPatr", u"Pode ver listagem do modelo S1300EVTCONTRSINDPATR"),
            ("can_see_data_s1300evtContrSindPatr", u"Pode visualizar o conteúdo do modelo S1300EVTCONTRSINDPATR"),
            ("can_see_menu_s1300evtContrSindPatr", u"Pode visualizar no menu o modelo S1300EVTCONTRSINDPATR"),
            ("can_print_list_s1300evtContrSindPatr", u"Pode imprimir listagem do modelo S1300EVTCONTRSINDPATR"),
            ("can_print_data_s1300evtContrSindPatr", u"Pode imprimir o conteúdo do modelo S1300EVTCONTRSINDPATR"),
            ("can_open_s1300evtContrSindPatr", u"Pode abrir o evento S1300EVTCONTRSINDPATR para edição"),
            ("can_duplicate_s1300evtContrSindPatr", u"Pode duplicar o evento S1300EVTCONTRSINDPATR"),
            ("can_validate_s1300evtContrSindPatr", u"Pode validar o evento S1300EVTCONTRSINDPATR"),
            ("can_change_identity_s1300evtContrSindPatr", u"Pode alterar identidade do evento S1300EVTCONTRSINDPATR"),
            ("can_see_layout_s1300evtContrSindPatr", u"Pode ver layout do evento S1300EVTCONTRSINDPATR"),
            ("can_see_receipt_s1300evtContrSindPatr", u"Pode ver recibo do evento S1300EVTCONTRSINDPATR"),
            ("can_see_xml_s1300evtContrSindPatr", u"Pode ver xml do evento S1300EVTCONTRSINDPATR"),)
            
        ordering = [
            'identidade',
            'indretif',
            'indapuracao',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class s1300evtContrSindPatrSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s1300evtContrSindPatr
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2190evtAdmPrelim(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2190_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2190_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    dtnascto = models.DateField(null=True, )
    dtadm = models.DateField(null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2190_evtadmprelim_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2190 - Admissão de Trabalhador - Registro Preliminar'
        db_table = r's2190_evtadmprelim'       
        managed = True  # s2190_evtadmprelim #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2190evtAdmPrelim", u"Pode ver listagem do modelo S2190EVTADMPRELIM"),
            ("can_see_data_s2190evtAdmPrelim", u"Pode visualizar o conteúdo do modelo S2190EVTADMPRELIM"),
            ("can_see_menu_s2190evtAdmPrelim", u"Pode visualizar no menu o modelo S2190EVTADMPRELIM"),
            ("can_print_list_s2190evtAdmPrelim", u"Pode imprimir listagem do modelo S2190EVTADMPRELIM"),
            ("can_print_data_s2190evtAdmPrelim", u"Pode imprimir o conteúdo do modelo S2190EVTADMPRELIM"),
            ("can_open_s2190evtAdmPrelim", u"Pode abrir o evento S2190EVTADMPRELIM para edição"),
            ("can_duplicate_s2190evtAdmPrelim", u"Pode duplicar o evento S2190EVTADMPRELIM"),
            ("can_validate_s2190evtAdmPrelim", u"Pode validar o evento S2190EVTADMPRELIM"),
            ("can_change_identity_s2190evtAdmPrelim", u"Pode alterar identidade do evento S2190EVTADMPRELIM"),
            ("can_see_layout_s2190evtAdmPrelim", u"Pode ver layout do evento S2190EVTADMPRELIM"),
            ("can_see_receipt_s2190evtAdmPrelim", u"Pode ver recibo do evento S2190EVTADMPRELIM"),
            ("can_see_xml_s2190evtAdmPrelim", u"Pode ver xml do evento S2190EVTADMPRELIM"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'dtnascto',
            'dtadm', ]



class s2190evtAdmPrelimSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2190evtAdmPrelim
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2200evtAdmissao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2200_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2200_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2200_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    nmtrab = models.CharField(max_length=70, null=True, )
    sexo = models.CharField(choices=CHOICES_S2200_SEXO, max_length=1, null=True, )
    racacor = models.IntegerField(choices=CHOICES_S2200_RACACOR, null=True, )
    estciv = models.IntegerField(choices=CHOICES_S2200_ESTCIV, blank=True, null=True, )
    grauinstr = models.CharField(choices=CHOICES_S2200_GRAUINSTR, max_length=2, null=True, )
    indpriempr = models.CharField(choices=CHOICES_S2200_INDPRIEMPR, max_length=1, blank=True, null=True, )
    nmsoc = models.CharField(max_length=70, blank=True, null=True, )
    dtnascto = models.DateField(null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    paisnascto = models.TextField(null=True, )
    paisnac = models.TextField(null=True, )
    nmmae = models.CharField(max_length=70, blank=True, null=True, )
    nmpai = models.CharField(max_length=70, blank=True, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    tpregtrab = models.IntegerField(choices=CHOICES_S2200_TPREGTRAB, null=True, )
    tpregprev = models.IntegerField(choices=CHOICES_S2200_TPREGPREV, null=True, )
    nrrecinfprelim = models.CharField(max_length=40, blank=True, null=True, )
    cadini = models.CharField(choices=CHOICES_S2200_CADINI, max_length=1, null=True, )
    codcargo = models.CharField(max_length=30, blank=True, null=True, )
    dtingrcargo = models.DateField(blank=True, null=True, )
    codfuncao = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    codcarreira = models.CharField(max_length=30, blank=True, null=True, )
    dtingrcarr = models.DateField(blank=True, null=True, )
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    undsalfixo = models.IntegerField(choices=CHOICES_S2200_UNDSALFIXO, null=True, )
    dscsalvar = models.CharField(max_length=255, blank=True, null=True, )
    tpcontr = models.IntegerField(choices=CHOICES_S2200_TPCONTR, null=True, )
    dtterm = models.DateField(blank=True, null=True, )
    clauassec = models.CharField(choices=CHOICES_S2200_CLAUASSEC, max_length=1, blank=True, null=True, )
    objdet = models.CharField(max_length=255, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2200_evtadmissao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador'
        db_table = r's2200_evtadmissao'       
        managed = True  # s2200_evtadmissao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2200evtAdmissao", u"Pode ver listagem do modelo S2200EVTADMISSAO"),
            ("can_see_data_s2200evtAdmissao", u"Pode visualizar o conteúdo do modelo S2200EVTADMISSAO"),
            ("can_see_menu_s2200evtAdmissao", u"Pode visualizar no menu o modelo S2200EVTADMISSAO"),
            ("can_print_list_s2200evtAdmissao", u"Pode imprimir listagem do modelo S2200EVTADMISSAO"),
            ("can_print_data_s2200evtAdmissao", u"Pode imprimir o conteúdo do modelo S2200EVTADMISSAO"),
            ("can_open_s2200evtAdmissao", u"Pode abrir o evento S2200EVTADMISSAO para edição"),
            ("can_duplicate_s2200evtAdmissao", u"Pode duplicar o evento S2200EVTADMISSAO"),
            ("can_validate_s2200evtAdmissao", u"Pode validar o evento S2200EVTADMISSAO"),
            ("can_change_identity_s2200evtAdmissao", u"Pode alterar identidade do evento S2200EVTADMISSAO"),
            ("can_see_layout_s2200evtAdmissao", u"Pode ver layout do evento S2200EVTADMISSAO"),
            ("can_see_receipt_s2200evtAdmissao", u"Pode ver recibo do evento S2200EVTADMISSAO"),
            ("can_see_xml_s2200evtAdmissao", u"Pode ver xml do evento S2200EVTADMISSAO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'nmtrab',
            'sexo',
            'racacor',
            'grauinstr',
            'dtnascto',
            'paisnascto',
            'paisnac',
            'matricula',
            'tpregtrab',
            'tpregprev',
            'cadini',
            'codcateg',
            'vrsalfx',
            'undsalfixo',
            'tpcontr', ]



class s2200evtAdmissaoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2200evtAdmissao
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2205evtAltCadastral(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2205_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2205_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2205_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    dtalteracao = models.DateField(null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    nmtrab = models.CharField(max_length=70, null=True, )
    sexo = models.CharField(choices=CHOICES_S2205_SEXO, max_length=1, null=True, )
    racacor = models.IntegerField(choices=CHOICES_S2205_RACACOR, null=True, )
    estciv = models.IntegerField(choices=CHOICES_S2205_ESTCIV, blank=True, null=True, )
    grauinstr = models.CharField(choices=CHOICES_S2205_GRAUINSTR, max_length=2, null=True, )
    nmsoc = models.CharField(max_length=70, blank=True, null=True, )
    dtnascto = models.DateField(null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    paisnascto = models.TextField(null=True, )
    paisnac = models.TextField(null=True, )
    nmmae = models.CharField(max_length=70, blank=True, null=True, )
    nmpai = models.CharField(max_length=70, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2205_evtaltcadastral_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2205 - Alteração de Dados Cadastrais do Trabalhador'
        db_table = r's2205_evtaltcadastral'       
        managed = True  # s2205_evtaltcadastral #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2205evtAltCadastral", u"Pode ver listagem do modelo S2205EVTALTCADASTRAL"),
            ("can_see_data_s2205evtAltCadastral", u"Pode visualizar o conteúdo do modelo S2205EVTALTCADASTRAL"),
            ("can_see_menu_s2205evtAltCadastral", u"Pode visualizar no menu o modelo S2205EVTALTCADASTRAL"),
            ("can_print_list_s2205evtAltCadastral", u"Pode imprimir listagem do modelo S2205EVTALTCADASTRAL"),
            ("can_print_data_s2205evtAltCadastral", u"Pode imprimir o conteúdo do modelo S2205EVTALTCADASTRAL"),
            ("can_open_s2205evtAltCadastral", u"Pode abrir o evento S2205EVTALTCADASTRAL para edição"),
            ("can_duplicate_s2205evtAltCadastral", u"Pode duplicar o evento S2205EVTALTCADASTRAL"),
            ("can_validate_s2205evtAltCadastral", u"Pode validar o evento S2205EVTALTCADASTRAL"),
            ("can_change_identity_s2205evtAltCadastral", u"Pode alterar identidade do evento S2205EVTALTCADASTRAL"),
            ("can_see_layout_s2205evtAltCadastral", u"Pode ver layout do evento S2205EVTALTCADASTRAL"),
            ("can_see_receipt_s2205evtAltCadastral", u"Pode ver recibo do evento S2205EVTALTCADASTRAL"),
            ("can_see_xml_s2205evtAltCadastral", u"Pode ver xml do evento S2205EVTALTCADASTRAL"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'dtalteracao',
            'nmtrab',
            'sexo',
            'racacor',
            'grauinstr',
            'dtnascto',
            'paisnascto',
            'paisnac', ]



class s2205evtAltCadastralSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2205evtAltCadastral
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2206evtAltContratual(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2206_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2206_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2206_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    dtalteracao = models.DateField(null=True, )
    dtef = models.DateField(blank=True, null=True, )
    dscalt = models.CharField(max_length=150, blank=True, null=True, )
    tpregprev = models.IntegerField(choices=CHOICES_S2206_TPREGPREV, null=True, )
    codcargo = models.CharField(max_length=30, blank=True, null=True, )
    codfuncao = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    codcarreira = models.CharField(max_length=30, blank=True, null=True, )
    dtingrcarr = models.DateField(blank=True, null=True, )
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    undsalfixo = models.IntegerField(choices=CHOICES_S2206_UNDSALFIXO, null=True, )
    dscsalvar = models.CharField(max_length=255, blank=True, null=True, )
    tpcontr = models.IntegerField(choices=CHOICES_S2206_TPCONTR, null=True, )
    dtterm = models.DateField(blank=True, null=True, )
    objdet = models.CharField(max_length=255, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2206_evtaltcontratual_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2206 - Alteração de Contrato de Trabalho'
        db_table = r's2206_evtaltcontratual'       
        managed = True  # s2206_evtaltcontratual #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2206evtAltContratual", u"Pode ver listagem do modelo S2206EVTALTCONTRATUAL"),
            ("can_see_data_s2206evtAltContratual", u"Pode visualizar o conteúdo do modelo S2206EVTALTCONTRATUAL"),
            ("can_see_menu_s2206evtAltContratual", u"Pode visualizar no menu o modelo S2206EVTALTCONTRATUAL"),
            ("can_print_list_s2206evtAltContratual", u"Pode imprimir listagem do modelo S2206EVTALTCONTRATUAL"),
            ("can_print_data_s2206evtAltContratual", u"Pode imprimir o conteúdo do modelo S2206EVTALTCONTRATUAL"),
            ("can_open_s2206evtAltContratual", u"Pode abrir o evento S2206EVTALTCONTRATUAL para edição"),
            ("can_duplicate_s2206evtAltContratual", u"Pode duplicar o evento S2206EVTALTCONTRATUAL"),
            ("can_validate_s2206evtAltContratual", u"Pode validar o evento S2206EVTALTCONTRATUAL"),
            ("can_change_identity_s2206evtAltContratual", u"Pode alterar identidade do evento S2206EVTALTCONTRATUAL"),
            ("can_see_layout_s2206evtAltContratual", u"Pode ver layout do evento S2206EVTALTCONTRATUAL"),
            ("can_see_receipt_s2206evtAltContratual", u"Pode ver recibo do evento S2206EVTALTCONTRATUAL"),
            ("can_see_xml_s2206evtAltContratual", u"Pode ver xml do evento S2206EVTALTCONTRATUAL"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula',
            'dtalteracao',
            'tpregprev',
            'codcateg',
            'vrsalfx',
            'undsalfixo',
            'tpcontr', ]



class s2206evtAltContratualSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2206evtAltContratual
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2210evtCAT(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2210_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2210_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2210_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    dtacid = models.DateField(null=True, )
    tpacid = models.TextField(null=True, )
    hracid = models.CharField(max_length=4, blank=True, null=True, )
    hrstrabantesacid = models.CharField(max_length=4, null=True, )
    tpcat = models.IntegerField(choices=CHOICES_S2210_TPCAT, null=True, )
    indcatobito = models.CharField(choices=CHOICES_S2210_INDCATOBITO, max_length=1, null=True, )
    dtobito = models.DateField(blank=True, null=True, )
    indcomunpolicia = models.CharField(choices=CHOICES_S2210_INDCOMUNPOLICIA, max_length=1, null=True, )
    codsitgeradora = models.IntegerField(null=True, )
    iniciatcat = models.IntegerField(choices=CHOICES_S2210_INICIATCAT, null=True, )
    obscat = models.CharField(max_length=999, blank=True, null=True, )
    observacao = models.CharField(max_length=999, blank=True, null=True, )
    tplocal = models.IntegerField(choices=CHOICES_S2210_TPLOCAL, null=True, )
    dsclocal = models.CharField(max_length=255, blank=True, null=True, )
    codamb = models.CharField(max_length=30, blank=True, null=True, )
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, blank=True, null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    pais = models.TextField(blank=True, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2210_evtcat_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2210 - Comunicação de Acidente de Trabalho'
        db_table = r's2210_evtcat'       
        managed = True  # s2210_evtcat #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2210evtCAT", u"Pode ver listagem do modelo S2210EVTCAT"),
            ("can_see_data_s2210evtCAT", u"Pode visualizar o conteúdo do modelo S2210EVTCAT"),
            ("can_see_menu_s2210evtCAT", u"Pode visualizar no menu o modelo S2210EVTCAT"),
            ("can_print_list_s2210evtCAT", u"Pode imprimir listagem do modelo S2210EVTCAT"),
            ("can_print_data_s2210evtCAT", u"Pode imprimir o conteúdo do modelo S2210EVTCAT"),
            ("can_open_s2210evtCAT", u"Pode abrir o evento S2210EVTCAT para edição"),
            ("can_duplicate_s2210evtCAT", u"Pode duplicar o evento S2210EVTCAT"),
            ("can_validate_s2210evtCAT", u"Pode validar o evento S2210EVTCAT"),
            ("can_change_identity_s2210evtCAT", u"Pode alterar identidade do evento S2210EVTCAT"),
            ("can_see_layout_s2210evtCAT", u"Pode ver layout do evento S2210EVTCAT"),
            ("can_see_receipt_s2210evtCAT", u"Pode ver recibo do evento S2210EVTCAT"),
            ("can_see_xml_s2210evtCAT", u"Pode ver xml do evento S2210EVTCAT"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'dtacid',
            'tpacid',
            'hrstrabantesacid',
            'tpcat',
            'indcatobito',
            'indcomunpolicia',
            'codsitgeradora',
            'iniciatcat',
            'tplocal',
            'tplograd',
            'dsclograd',
            'nrlograd', ]



class s2210evtCATSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2210evtCAT
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2220evtMonit(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2220_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2220_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2220_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    tpexameocup = models.IntegerField(choices=CHOICES_S2220_TPEXAMEOCUP, null=True, )
    dtaso = models.DateField(null=True, )
    tpaso = models.IntegerField(choices=CHOICES_S2220_TPASO, null=True, )
    resaso = models.IntegerField(choices=CHOICES_S2220_RESASO, null=True, )
    cpfmed = models.CharField(max_length=11, blank=True, null=True, )
    nismed = models.CharField(max_length=11, blank=True, null=True, )
    nmmed = models.CharField(max_length=70, null=True, )
    nrcrm = models.CharField(max_length=8, null=True, )
    ufcrm = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    nisresp = models.CharField(max_length=11, null=True, )
    nrconsclasse = models.CharField(max_length=8, null=True, )
    ufconsclasse = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    cpfresp = models.CharField(max_length=11, blank=True, null=True, )
    nmresp = models.CharField(max_length=70, null=True, )
    nrcrm = models.CharField(max_length=8, null=True, )
    ufcrm = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2220_evtmonit_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2220 - Monitoramento da Saúde do Trabalhador'
        db_table = r's2220_evtmonit'       
        managed = True  # s2220_evtmonit #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2220evtMonit", u"Pode ver listagem do modelo S2220EVTMONIT"),
            ("can_see_data_s2220evtMonit", u"Pode visualizar o conteúdo do modelo S2220EVTMONIT"),
            ("can_see_menu_s2220evtMonit", u"Pode visualizar no menu o modelo S2220EVTMONIT"),
            ("can_print_list_s2220evtMonit", u"Pode imprimir listagem do modelo S2220EVTMONIT"),
            ("can_print_data_s2220evtMonit", u"Pode imprimir o conteúdo do modelo S2220EVTMONIT"),
            ("can_open_s2220evtMonit", u"Pode abrir o evento S2220EVTMONIT para edição"),
            ("can_duplicate_s2220evtMonit", u"Pode duplicar o evento S2220EVTMONIT"),
            ("can_validate_s2220evtMonit", u"Pode validar o evento S2220EVTMONIT"),
            ("can_change_identity_s2220evtMonit", u"Pode alterar identidade do evento S2220EVTMONIT"),
            ("can_see_layout_s2220evtMonit", u"Pode ver layout do evento S2220EVTMONIT"),
            ("can_see_receipt_s2220evtMonit", u"Pode ver recibo do evento S2220EVTMONIT"),
            ("can_see_xml_s2220evtMonit", u"Pode ver xml do evento S2220EVTMONIT"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'tpexameocup',
            'dtaso',
            'tpaso',
            'resaso',
            'nmmed',
            'nrcrm',
            'ufcrm',
            'nisresp',
            'nrconsclasse',
            'nmresp',
            'nrcrm',
            'ufcrm', ]



class s2220evtMonitSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2220evtMonit
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2221evtToxic(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2221_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2221_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2221_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    dtexame = models.DateField(null=True, )
    cnpjlab = models.CharField(max_length=14, blank=True, null=True, )
    codseqexame = models.CharField(max_length=11, blank=True, null=True, )
    nmmed = models.CharField(max_length=70, blank=True, null=True, )
    nrcrm = models.CharField(max_length=8, blank=True, null=True, )
    ufcrm = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    indrecusa = models.CharField(choices=CHOICES_S2221_INDRECUSA, max_length=1, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2221_evttoxic_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2221 - Exame Toxicológico do Motorista Profissional'
        db_table = r's2221_evttoxic'       
        managed = True  # s2221_evttoxic #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2221evtToxic", u"Pode ver listagem do modelo S2221EVTTOXIC"),
            ("can_see_data_s2221evtToxic", u"Pode visualizar o conteúdo do modelo S2221EVTTOXIC"),
            ("can_see_menu_s2221evtToxic", u"Pode visualizar no menu o modelo S2221EVTTOXIC"),
            ("can_print_list_s2221evtToxic", u"Pode imprimir listagem do modelo S2221EVTTOXIC"),
            ("can_print_data_s2221evtToxic", u"Pode imprimir o conteúdo do modelo S2221EVTTOXIC"),
            ("can_open_s2221evtToxic", u"Pode abrir o evento S2221EVTTOXIC para edição"),
            ("can_duplicate_s2221evtToxic", u"Pode duplicar o evento S2221EVTTOXIC"),
            ("can_validate_s2221evtToxic", u"Pode validar o evento S2221EVTTOXIC"),
            ("can_change_identity_s2221evtToxic", u"Pode alterar identidade do evento S2221EVTTOXIC"),
            ("can_see_layout_s2221evtToxic", u"Pode ver layout do evento S2221EVTTOXIC"),
            ("can_see_receipt_s2221evtToxic", u"Pode ver recibo do evento S2221EVTTOXIC"),
            ("can_see_xml_s2221evtToxic", u"Pode ver xml do evento S2221EVTTOXIC"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'dtexame',
            'indrecusa', ]



class s2221evtToxicSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2221evtToxic
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230evtAfastTemp(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2230_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2230_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2230_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2230_evtafasttemp_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2230 - Afastamento Temporário'
        db_table = r's2230_evtafasttemp'       
        managed = True  # s2230_evtafasttemp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230evtAfastTemp", u"Pode ver listagem do modelo S2230EVTAFASTTEMP"),
            ("can_see_data_s2230evtAfastTemp", u"Pode visualizar o conteúdo do modelo S2230EVTAFASTTEMP"),
            ("can_see_menu_s2230evtAfastTemp", u"Pode visualizar no menu o modelo S2230EVTAFASTTEMP"),
            ("can_print_list_s2230evtAfastTemp", u"Pode imprimir listagem do modelo S2230EVTAFASTTEMP"),
            ("can_print_data_s2230evtAfastTemp", u"Pode imprimir o conteúdo do modelo S2230EVTAFASTTEMP"),
            ("can_open_s2230evtAfastTemp", u"Pode abrir o evento S2230EVTAFASTTEMP para edição"),
            ("can_duplicate_s2230evtAfastTemp", u"Pode duplicar o evento S2230EVTAFASTTEMP"),
            ("can_validate_s2230evtAfastTemp", u"Pode validar o evento S2230EVTAFASTTEMP"),
            ("can_change_identity_s2230evtAfastTemp", u"Pode alterar identidade do evento S2230EVTAFASTTEMP"),
            ("can_see_layout_s2230evtAfastTemp", u"Pode ver layout do evento S2230EVTAFASTTEMP"),
            ("can_see_receipt_s2230evtAfastTemp", u"Pode ver recibo do evento S2230EVTAFASTTEMP"),
            ("can_see_xml_s2230evtAfastTemp", u"Pode ver xml do evento S2230EVTAFASTTEMP"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s2230evtAfastTempSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2230evtAfastTemp
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2231evtCessao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2231_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2231_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2231_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2231_evtcessao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2231 - Cessão/Exercício em Outro Órgão'
        db_table = r's2231_evtcessao'       
        managed = True  # s2231_evtcessao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2231evtCessao", u"Pode ver listagem do modelo S2231EVTCESSAO"),
            ("can_see_data_s2231evtCessao", u"Pode visualizar o conteúdo do modelo S2231EVTCESSAO"),
            ("can_see_menu_s2231evtCessao", u"Pode visualizar no menu o modelo S2231EVTCESSAO"),
            ("can_print_list_s2231evtCessao", u"Pode imprimir listagem do modelo S2231EVTCESSAO"),
            ("can_print_data_s2231evtCessao", u"Pode imprimir o conteúdo do modelo S2231EVTCESSAO"),
            ("can_open_s2231evtCessao", u"Pode abrir o evento S2231EVTCESSAO para edição"),
            ("can_duplicate_s2231evtCessao", u"Pode duplicar o evento S2231EVTCESSAO"),
            ("can_validate_s2231evtCessao", u"Pode validar o evento S2231EVTCESSAO"),
            ("can_change_identity_s2231evtCessao", u"Pode alterar identidade do evento S2231EVTCESSAO"),
            ("can_see_layout_s2231evtCessao", u"Pode ver layout do evento S2231EVTCESSAO"),
            ("can_see_receipt_s2231evtCessao", u"Pode ver recibo do evento S2231EVTCESSAO"),
            ("can_see_xml_s2231evtCessao", u"Pode ver xml do evento S2231EVTCESSAO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula', ]



class s2231evtCessaoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2231evtCessao
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2240evtExpRisco(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2240_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2240_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2240_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    dtinicondicao = models.DateField(null=True, )
    dscativdes = models.CharField(max_length=999, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2240_evtexprisco_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2240 - Condições Ambientais do Trabalho - Fatores de Risco'
        db_table = r's2240_evtexprisco'       
        managed = True  # s2240_evtexprisco #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2240evtExpRisco", u"Pode ver listagem do modelo S2240EVTEXPRISCO"),
            ("can_see_data_s2240evtExpRisco", u"Pode visualizar o conteúdo do modelo S2240EVTEXPRISCO"),
            ("can_see_menu_s2240evtExpRisco", u"Pode visualizar no menu o modelo S2240EVTEXPRISCO"),
            ("can_print_list_s2240evtExpRisco", u"Pode imprimir listagem do modelo S2240EVTEXPRISCO"),
            ("can_print_data_s2240evtExpRisco", u"Pode imprimir o conteúdo do modelo S2240EVTEXPRISCO"),
            ("can_open_s2240evtExpRisco", u"Pode abrir o evento S2240EVTEXPRISCO para edição"),
            ("can_duplicate_s2240evtExpRisco", u"Pode duplicar o evento S2240EVTEXPRISCO"),
            ("can_validate_s2240evtExpRisco", u"Pode validar o evento S2240EVTEXPRISCO"),
            ("can_change_identity_s2240evtExpRisco", u"Pode alterar identidade do evento S2240EVTEXPRISCO"),
            ("can_see_layout_s2240evtExpRisco", u"Pode ver layout do evento S2240EVTEXPRISCO"),
            ("can_see_receipt_s2240evtExpRisco", u"Pode ver recibo do evento S2240EVTEXPRISCO"),
            ("can_see_xml_s2240evtExpRisco", u"Pode ver xml do evento S2240EVTEXPRISCO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'dtinicondicao',
            'dscativdes', ]



class s2240evtExpRiscoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2240evtExpRisco
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241evtInsApo(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2241_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2241_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2241_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2241_evtinsapo_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2241 - Insalubridade, Periculosidade e Aposentadoria Especial'
        db_table = r's2241_evtinsapo'       
        managed = True  # s2241_evtinsapo #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241evtInsApo", u"Pode ver listagem do modelo S2241EVTINSAPO"),
            ("can_see_data_s2241evtInsApo", u"Pode visualizar o conteúdo do modelo S2241EVTINSAPO"),
            ("can_see_menu_s2241evtInsApo", u"Pode visualizar no menu o modelo S2241EVTINSAPO"),
            ("can_print_list_s2241evtInsApo", u"Pode imprimir listagem do modelo S2241EVTINSAPO"),
            ("can_print_data_s2241evtInsApo", u"Pode imprimir o conteúdo do modelo S2241EVTINSAPO"),
            ("can_open_s2241evtInsApo", u"Pode abrir o evento S2241EVTINSAPO para edição"),
            ("can_duplicate_s2241evtInsApo", u"Pode duplicar o evento S2241EVTINSAPO"),
            ("can_validate_s2241evtInsApo", u"Pode validar o evento S2241EVTINSAPO"),
            ("can_change_identity_s2241evtInsApo", u"Pode alterar identidade do evento S2241EVTINSAPO"),
            ("can_see_layout_s2241evtInsApo", u"Pode ver layout do evento S2241EVTINSAPO"),
            ("can_see_receipt_s2241evtInsApo", u"Pode ver recibo do evento S2241EVTINSAPO"),
            ("can_see_xml_s2241evtInsApo", u"Pode ver xml do evento S2241EVTINSAPO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s2241evtInsApoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2241evtInsApo
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2245evtTreiCap(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2245_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2245_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2245_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    codtreicap = models.TextField(null=True, )
    obstreicap = models.CharField(max_length=999, blank=True, null=True, )
    observacao = models.CharField(max_length=999, blank=True, null=True, )
    dttreicap = models.DateField(null=True, )
    durtreicap = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    modtreicap = models.IntegerField(choices=CHOICES_S2245_MODTREICAP, blank=True, null=True, )
    tptreicap = models.IntegerField(choices=CHOICES_S2245_TPTREICAP, blank=True, null=True, )
    indtreinant = models.CharField(choices=CHOICES_S2245_INDTREINANT, max_length=1, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2245_evttreicap_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2245 - Treinamentos, Capacitações e Exercícios Simulados'
        db_table = r's2245_evttreicap'       
        managed = True  # s2245_evttreicap #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2245evtTreiCap", u"Pode ver listagem do modelo S2245EVTTREICAP"),
            ("can_see_data_s2245evtTreiCap", u"Pode visualizar o conteúdo do modelo S2245EVTTREICAP"),
            ("can_see_menu_s2245evtTreiCap", u"Pode visualizar no menu o modelo S2245EVTTREICAP"),
            ("can_print_list_s2245evtTreiCap", u"Pode imprimir listagem do modelo S2245EVTTREICAP"),
            ("can_print_data_s2245evtTreiCap", u"Pode imprimir o conteúdo do modelo S2245EVTTREICAP"),
            ("can_open_s2245evtTreiCap", u"Pode abrir o evento S2245EVTTREICAP para edição"),
            ("can_duplicate_s2245evtTreiCap", u"Pode duplicar o evento S2245EVTTREICAP"),
            ("can_validate_s2245evtTreiCap", u"Pode validar o evento S2245EVTTREICAP"),
            ("can_change_identity_s2245evtTreiCap", u"Pode alterar identidade do evento S2245EVTTREICAP"),
            ("can_see_layout_s2245evtTreiCap", u"Pode ver layout do evento S2245EVTTREICAP"),
            ("can_see_receipt_s2245evtTreiCap", u"Pode ver recibo do evento S2245EVTTREICAP"),
            ("can_see_xml_s2245evtTreiCap", u"Pode ver xml do evento S2245EVTTREICAP"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'codtreicap',
            'dttreicap',
            'indtreinant', ]



class s2245evtTreiCapSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2245evtTreiCap
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2250evtAvPrevio(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2250_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2250_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2250_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2250_evtavprevio_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2250 - Aviso Prévio'
        db_table = r's2250_evtavprevio'       
        managed = True  # s2250_evtavprevio #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2250evtAvPrevio", u"Pode ver listagem do modelo S2250EVTAVPREVIO"),
            ("can_see_data_s2250evtAvPrevio", u"Pode visualizar o conteúdo do modelo S2250EVTAVPREVIO"),
            ("can_see_menu_s2250evtAvPrevio", u"Pode visualizar no menu o modelo S2250EVTAVPREVIO"),
            ("can_print_list_s2250evtAvPrevio", u"Pode imprimir listagem do modelo S2250EVTAVPREVIO"),
            ("can_print_data_s2250evtAvPrevio", u"Pode imprimir o conteúdo do modelo S2250EVTAVPREVIO"),
            ("can_open_s2250evtAvPrevio", u"Pode abrir o evento S2250EVTAVPREVIO para edição"),
            ("can_duplicate_s2250evtAvPrevio", u"Pode duplicar o evento S2250EVTAVPREVIO"),
            ("can_validate_s2250evtAvPrevio", u"Pode validar o evento S2250EVTAVPREVIO"),
            ("can_change_identity_s2250evtAvPrevio", u"Pode alterar identidade do evento S2250EVTAVPREVIO"),
            ("can_see_layout_s2250evtAvPrevio", u"Pode ver layout do evento S2250EVTAVPREVIO"),
            ("can_see_receipt_s2250evtAvPrevio", u"Pode ver recibo do evento S2250EVTAVPREVIO"),
            ("can_see_xml_s2250evtAvPrevio", u"Pode ver xml do evento S2250EVTAVPREVIO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula', ]



class s2250evtAvPrevioSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2250evtAvPrevio
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2260evtConvInterm(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2260_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2260_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2260_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    codconv = models.CharField(max_length=30, null=True, )
    dtinicio = models.DateField(null=True, )
    dtfim = models.DateField(null=True, )
    dtprevpgto = models.DateField(null=True, )
    codhorcontrat = models.CharField(max_length=30, blank=True, null=True, )
    dscjornada = models.CharField(max_length=999, blank=True, null=True, )
    indlocal = models.IntegerField(choices=CHOICES_S2260_INDLOCAL, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2260_evtconvinterm_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2260 - Convocação para Trabalho Intermitente'
        db_table = r's2260_evtconvinterm'       
        managed = True  # s2260_evtconvinterm #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2260evtConvInterm", u"Pode ver listagem do modelo S2260EVTCONVINTERM"),
            ("can_see_data_s2260evtConvInterm", u"Pode visualizar o conteúdo do modelo S2260EVTCONVINTERM"),
            ("can_see_menu_s2260evtConvInterm", u"Pode visualizar no menu o modelo S2260EVTCONVINTERM"),
            ("can_print_list_s2260evtConvInterm", u"Pode imprimir listagem do modelo S2260EVTCONVINTERM"),
            ("can_print_data_s2260evtConvInterm", u"Pode imprimir o conteúdo do modelo S2260EVTCONVINTERM"),
            ("can_open_s2260evtConvInterm", u"Pode abrir o evento S2260EVTCONVINTERM para edição"),
            ("can_duplicate_s2260evtConvInterm", u"Pode duplicar o evento S2260EVTCONVINTERM"),
            ("can_validate_s2260evtConvInterm", u"Pode validar o evento S2260EVTCONVINTERM"),
            ("can_change_identity_s2260evtConvInterm", u"Pode alterar identidade do evento S2260EVTCONVINTERM"),
            ("can_see_layout_s2260evtConvInterm", u"Pode ver layout do evento S2260EVTCONVINTERM"),
            ("can_see_receipt_s2260evtConvInterm", u"Pode ver recibo do evento S2260EVTCONVINTERM"),
            ("can_see_xml_s2260evtConvInterm", u"Pode ver xml do evento S2260EVTCONVINTERM"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula',
            'codconv',
            'dtinicio',
            'dtfim',
            'dtprevpgto',
            'indlocal', ]



class s2260evtConvIntermSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2260evtConvInterm
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2298evtReintegr(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2298_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2298_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2298_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    tpreint = models.IntegerField(choices=CHOICES_S2298_TPREINT, null=True, )
    nrprocjud = models.CharField(max_length=20, blank=True, null=True, )
    nrleianistia = models.CharField(max_length=13, blank=True, null=True, )
    dtefetretorno = models.DateField(null=True, )
    dtefeito = models.DateField(null=True, )
    indpagtojuizo = models.CharField(choices=CHOICES_S2298_INDPAGTOJUIZO, max_length=1, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2298_evtreintegr_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2298 - Reintegração'
        db_table = r's2298_evtreintegr'       
        managed = True  # s2298_evtreintegr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2298evtReintegr", u"Pode ver listagem do modelo S2298EVTREINTEGR"),
            ("can_see_data_s2298evtReintegr", u"Pode visualizar o conteúdo do modelo S2298EVTREINTEGR"),
            ("can_see_menu_s2298evtReintegr", u"Pode visualizar no menu o modelo S2298EVTREINTEGR"),
            ("can_print_list_s2298evtReintegr", u"Pode imprimir listagem do modelo S2298EVTREINTEGR"),
            ("can_print_data_s2298evtReintegr", u"Pode imprimir o conteúdo do modelo S2298EVTREINTEGR"),
            ("can_open_s2298evtReintegr", u"Pode abrir o evento S2298EVTREINTEGR para edição"),
            ("can_duplicate_s2298evtReintegr", u"Pode duplicar o evento S2298EVTREINTEGR"),
            ("can_validate_s2298evtReintegr", u"Pode validar o evento S2298EVTREINTEGR"),
            ("can_change_identity_s2298evtReintegr", u"Pode alterar identidade do evento S2298EVTREINTEGR"),
            ("can_see_layout_s2298evtReintegr", u"Pode ver layout do evento S2298EVTREINTEGR"),
            ("can_see_receipt_s2298evtReintegr", u"Pode ver recibo do evento S2298EVTREINTEGR"),
            ("can_see_xml_s2298evtReintegr", u"Pode ver xml do evento S2298EVTREINTEGR"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula',
            'tpreint',
            'dtefetretorno',
            'dtefeito',
            'indpagtojuizo', ]



class s2298evtReintegrSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2298evtReintegr
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2299evtDeslig(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2299_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2299_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2299_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, null=True, )
    mtvdeslig = models.TextField(null=True, )
    dtdeslig = models.DateField(null=True, )
    indpagtoapi = models.CharField(choices=CHOICES_S2299_INDPAGTOAPI, max_length=1, null=True, )
    dtprojfimapi = models.DateField(blank=True, null=True, )
    pensalim = models.IntegerField(choices=CHOICES_S2299_PENSALIM, null=True, )
    percaliment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vralim = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    nrcertobito = models.CharField(max_length=32, blank=True, null=True, )
    nrproctrab = models.CharField(max_length=20, blank=True, null=True, )
    indcumprparc = models.IntegerField(choices=CHOICES_S2299_INDCUMPRPARC, null=True, )
    qtddiasinterm = models.IntegerField(blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2299_evtdeslig_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2299 - Desligamento'
        db_table = r's2299_evtdeslig'       
        managed = True  # s2299_evtdeslig #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2299evtDeslig", u"Pode ver listagem do modelo S2299EVTDESLIG"),
            ("can_see_data_s2299evtDeslig", u"Pode visualizar o conteúdo do modelo S2299EVTDESLIG"),
            ("can_see_menu_s2299evtDeslig", u"Pode visualizar no menu o modelo S2299EVTDESLIG"),
            ("can_print_list_s2299evtDeslig", u"Pode imprimir listagem do modelo S2299EVTDESLIG"),
            ("can_print_data_s2299evtDeslig", u"Pode imprimir o conteúdo do modelo S2299EVTDESLIG"),
            ("can_open_s2299evtDeslig", u"Pode abrir o evento S2299EVTDESLIG para edição"),
            ("can_duplicate_s2299evtDeslig", u"Pode duplicar o evento S2299EVTDESLIG"),
            ("can_validate_s2299evtDeslig", u"Pode validar o evento S2299EVTDESLIG"),
            ("can_change_identity_s2299evtDeslig", u"Pode alterar identidade do evento S2299EVTDESLIG"),
            ("can_see_layout_s2299evtDeslig", u"Pode ver layout do evento S2299EVTDESLIG"),
            ("can_see_receipt_s2299evtDeslig", u"Pode ver recibo do evento S2299EVTDESLIG"),
            ("can_see_xml_s2299evtDeslig", u"Pode ver xml do evento S2299EVTDESLIG"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nistrab',
            'matricula',
            'mtvdeslig',
            'dtdeslig',
            'indpagtoapi',
            'pensalim',
            'indcumprparc', ]



class s2299evtDesligSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2299evtDeslig
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2300evtTSVInicio(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2300_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2300_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2300_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    nmtrab = models.CharField(max_length=70, null=True, )
    sexo = models.CharField(choices=CHOICES_S2300_SEXO, max_length=1, null=True, )
    racacor = models.IntegerField(choices=CHOICES_S2300_RACACOR, null=True, )
    estciv = models.IntegerField(choices=CHOICES_S2300_ESTCIV, blank=True, null=True, )
    grauinstr = models.CharField(choices=CHOICES_S2300_GRAUINSTR, max_length=2, null=True, )
    nmsoc = models.CharField(max_length=70, blank=True, null=True, )
    dtnascto = models.DateField(null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    paisnascto = models.TextField(null=True, )
    paisnac = models.TextField(null=True, )
    nmmae = models.CharField(max_length=70, blank=True, null=True, )
    nmpai = models.CharField(max_length=70, blank=True, null=True, )
    cadini = models.CharField(choices=CHOICES_S2300_CADINI, max_length=1, null=True, )
    codcateg = models.IntegerField(null=True, )
    dtinicio = models.DateField(null=True, )
    natatividade = models.IntegerField(choices=CHOICES_S2300_NATATIVIDADE, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2300_evttsvinicio_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início'
        db_table = r's2300_evttsvinicio'       
        managed = True  # s2300_evttsvinicio #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2300evtTSVInicio", u"Pode ver listagem do modelo S2300EVTTSVINICIO"),
            ("can_see_data_s2300evtTSVInicio", u"Pode visualizar o conteúdo do modelo S2300EVTTSVINICIO"),
            ("can_see_menu_s2300evtTSVInicio", u"Pode visualizar no menu o modelo S2300EVTTSVINICIO"),
            ("can_print_list_s2300evtTSVInicio", u"Pode imprimir listagem do modelo S2300EVTTSVINICIO"),
            ("can_print_data_s2300evtTSVInicio", u"Pode imprimir o conteúdo do modelo S2300EVTTSVINICIO"),
            ("can_open_s2300evtTSVInicio", u"Pode abrir o evento S2300EVTTSVINICIO para edição"),
            ("can_duplicate_s2300evtTSVInicio", u"Pode duplicar o evento S2300EVTTSVINICIO"),
            ("can_validate_s2300evtTSVInicio", u"Pode validar o evento S2300EVTTSVINICIO"),
            ("can_change_identity_s2300evtTSVInicio", u"Pode alterar identidade do evento S2300EVTTSVINICIO"),
            ("can_see_layout_s2300evtTSVInicio", u"Pode ver layout do evento S2300EVTTSVINICIO"),
            ("can_see_receipt_s2300evtTSVInicio", u"Pode ver recibo do evento S2300EVTTSVINICIO"),
            ("can_see_xml_s2300evtTSVInicio", u"Pode ver xml do evento S2300EVTTSVINICIO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'nmtrab',
            'sexo',
            'racacor',
            'grauinstr',
            'dtnascto',
            'paisnascto',
            'paisnac',
            'cadini',
            'codcateg',
            'dtinicio', ]



class s2300evtTSVInicioSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2300evtTSVInicio
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2306evtTSVAltContr(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2306_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2306_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2306_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    dtalteracao = models.DateField(null=True, )
    natatividade = models.IntegerField(choices=CHOICES_S2306_NATATIVIDADE, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2306_evttsvaltcontr_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2306 - Trabalhador Sem Vínculo de Emprego/Estatutário - Alteração Contratual'
        db_table = r's2306_evttsvaltcontr'       
        managed = True  # s2306_evttsvaltcontr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2306evtTSVAltContr", u"Pode ver listagem do modelo S2306EVTTSVALTCONTR"),
            ("can_see_data_s2306evtTSVAltContr", u"Pode visualizar o conteúdo do modelo S2306EVTTSVALTCONTR"),
            ("can_see_menu_s2306evtTSVAltContr", u"Pode visualizar no menu o modelo S2306EVTTSVALTCONTR"),
            ("can_print_list_s2306evtTSVAltContr", u"Pode imprimir listagem do modelo S2306EVTTSVALTCONTR"),
            ("can_print_data_s2306evtTSVAltContr", u"Pode imprimir o conteúdo do modelo S2306EVTTSVALTCONTR"),
            ("can_open_s2306evtTSVAltContr", u"Pode abrir o evento S2306EVTTSVALTCONTR para edição"),
            ("can_duplicate_s2306evtTSVAltContr", u"Pode duplicar o evento S2306EVTTSVALTCONTR"),
            ("can_validate_s2306evtTSVAltContr", u"Pode validar o evento S2306EVTTSVALTCONTR"),
            ("can_change_identity_s2306evtTSVAltContr", u"Pode alterar identidade do evento S2306EVTTSVALTCONTR"),
            ("can_see_layout_s2306evtTSVAltContr", u"Pode ver layout do evento S2306EVTTSVALTCONTR"),
            ("can_see_receipt_s2306evtTSVAltContr", u"Pode ver recibo do evento S2306EVTTSVALTCONTR"),
            ("can_see_xml_s2306evtTSVAltContr", u"Pode ver xml do evento S2306EVTTSVALTCONTR"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'codcateg',
            'dtalteracao', ]



class s2306evtTSVAltContrSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2306evtTSVAltContr
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399evtTSVTermino(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2399_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2399_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2399_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    codcateg = models.IntegerField(null=True, )
    dtterm = models.DateField(null=True, )
    mtvdesligtsv = models.CharField(choices=CHOICES_S2399_MTVDESLIGTSV, max_length=2, blank=True, null=True, )
    pensalim = models.IntegerField(choices=CHOICES_S2399_PENSALIM, blank=True, null=True, )
    percaliment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vralim = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2399_evttsvtermino_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término'
        db_table = r's2399_evttsvtermino'       
        managed = True  # s2399_evttsvtermino #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399evtTSVTermino", u"Pode ver listagem do modelo S2399EVTTSVTERMINO"),
            ("can_see_data_s2399evtTSVTermino", u"Pode visualizar o conteúdo do modelo S2399EVTTSVTERMINO"),
            ("can_see_menu_s2399evtTSVTermino", u"Pode visualizar no menu o modelo S2399EVTTSVTERMINO"),
            ("can_print_list_s2399evtTSVTermino", u"Pode imprimir listagem do modelo S2399EVTTSVTERMINO"),
            ("can_print_data_s2399evtTSVTermino", u"Pode imprimir o conteúdo do modelo S2399EVTTSVTERMINO"),
            ("can_open_s2399evtTSVTermino", u"Pode abrir o evento S2399EVTTSVTERMINO para edição"),
            ("can_duplicate_s2399evtTSVTermino", u"Pode duplicar o evento S2399EVTTSVTERMINO"),
            ("can_validate_s2399evtTSVTermino", u"Pode validar o evento S2399EVTTSVTERMINO"),
            ("can_change_identity_s2399evtTSVTermino", u"Pode alterar identidade do evento S2399EVTTSVTERMINO"),
            ("can_see_layout_s2399evtTSVTermino", u"Pode ver layout do evento S2399EVTTSVTERMINO"),
            ("can_see_receipt_s2399evtTSVTermino", u"Pode ver recibo do evento S2399EVTTSVTERMINO"),
            ("can_see_xml_s2399evtTSVTermino", u"Pode ver xml do evento S2399EVTTSVTERMINO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpftrab',
            'codcateg',
            'dtterm', ]



class s2399evtTSVTerminoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2399evtTSVTermino
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2400evtCdBenefIn(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2400_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2400_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2400_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    nisbenef = models.CharField(max_length=11, blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    dtinicio = models.DateField(null=True, )
    sexo = models.CharField(choices=CHOICES_S2400_SEXO, max_length=1, null=True, )
    racacor = models.IntegerField(choices=CHOICES_S2400_RACACOR, null=True, )
    estciv = models.IntegerField(choices=CHOICES_S2400_ESTCIV, blank=True, null=True, )
    incfismen = models.CharField(choices=CHOICES_S2400_INCFISMEN, max_length=1, null=True, )
    dtincfismen = models.DateField(blank=True, null=True, )
    dtnascto = models.DateField(null=True, )
    codmunic = models.TextField(blank=True, null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    paisnascto = models.TextField(blank=True, null=True, )
    paisnac = models.TextField(null=True, )
    nmmae = models.CharField(max_length=70, blank=True, null=True, )
    nmpai = models.CharField(max_length=70, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2400_evtcdbenefin_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2400 - Cadastro de Beneficiários - Entes Públicos - Início'
        db_table = r's2400_evtcdbenefin'       
        managed = True  # s2400_evtcdbenefin #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2400evtCdBenefIn", u"Pode ver listagem do modelo S2400EVTCDBENEFIN"),
            ("can_see_data_s2400evtCdBenefIn", u"Pode visualizar o conteúdo do modelo S2400EVTCDBENEFIN"),
            ("can_see_menu_s2400evtCdBenefIn", u"Pode visualizar no menu o modelo S2400EVTCDBENEFIN"),
            ("can_print_list_s2400evtCdBenefIn", u"Pode imprimir listagem do modelo S2400EVTCDBENEFIN"),
            ("can_print_data_s2400evtCdBenefIn", u"Pode imprimir o conteúdo do modelo S2400EVTCDBENEFIN"),
            ("can_open_s2400evtCdBenefIn", u"Pode abrir o evento S2400EVTCDBENEFIN para edição"),
            ("can_duplicate_s2400evtCdBenefIn", u"Pode duplicar o evento S2400EVTCDBENEFIN"),
            ("can_validate_s2400evtCdBenefIn", u"Pode validar o evento S2400EVTCDBENEFIN"),
            ("can_change_identity_s2400evtCdBenefIn", u"Pode alterar identidade do evento S2400EVTCDBENEFIN"),
            ("can_see_layout_s2400evtCdBenefIn", u"Pode ver layout do evento S2400EVTCDBENEFIN"),
            ("can_see_receipt_s2400evtCdBenefIn", u"Pode ver recibo do evento S2400EVTCDBENEFIN"),
            ("can_see_xml_s2400evtCdBenefIn", u"Pode ver xml do evento S2400EVTCDBENEFIN"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef',
            'nmbenefic',
            'dtinicio',
            'sexo',
            'racacor',
            'incfismen',
            'dtnascto',
            'paisnac', ]



class s2400evtCdBenefInSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2400evtCdBenefIn
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2405evtCdBenefAlt(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2405_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2405_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2405_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    dtalteracao = models.DateField(null=True, )
    nisbenef = models.CharField(max_length=11, blank=True, null=True, )
    nmbenefic = models.CharField(max_length=70, null=True, )
    sexo = models.CharField(choices=CHOICES_S2405_SEXO, max_length=1, null=True, )
    racacor = models.IntegerField(choices=CHOICES_S2405_RACACOR, null=True, )
    estciv = models.IntegerField(choices=CHOICES_S2405_ESTCIV, blank=True, null=True, )
    incfismen = models.CharField(choices=CHOICES_S2405_INCFISMEN, max_length=1, null=True, )
    dtincfismen = models.DateField(blank=True, null=True, )
    paisnac = models.TextField(null=True, )
    nmmae = models.CharField(max_length=70, blank=True, null=True, )
    nmpai = models.CharField(max_length=70, blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2405_evtcdbenefalt_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2405 - Cadastro de Beneficiários - Entes Públicos - Alteração'
        db_table = r's2405_evtcdbenefalt'       
        managed = True  # s2405_evtcdbenefalt #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2405evtCdBenefAlt", u"Pode ver listagem do modelo S2405EVTCDBENEFALT"),
            ("can_see_data_s2405evtCdBenefAlt", u"Pode visualizar o conteúdo do modelo S2405EVTCDBENEFALT"),
            ("can_see_menu_s2405evtCdBenefAlt", u"Pode visualizar no menu o modelo S2405EVTCDBENEFALT"),
            ("can_print_list_s2405evtCdBenefAlt", u"Pode imprimir listagem do modelo S2405EVTCDBENEFALT"),
            ("can_print_data_s2405evtCdBenefAlt", u"Pode imprimir o conteúdo do modelo S2405EVTCDBENEFALT"),
            ("can_open_s2405evtCdBenefAlt", u"Pode abrir o evento S2405EVTCDBENEFALT para edição"),
            ("can_duplicate_s2405evtCdBenefAlt", u"Pode duplicar o evento S2405EVTCDBENEFALT"),
            ("can_validate_s2405evtCdBenefAlt", u"Pode validar o evento S2405EVTCDBENEFALT"),
            ("can_change_identity_s2405evtCdBenefAlt", u"Pode alterar identidade do evento S2405EVTCDBENEFALT"),
            ("can_see_layout_s2405evtCdBenefAlt", u"Pode ver layout do evento S2405EVTCDBENEFALT"),
            ("can_see_receipt_s2405evtCdBenefAlt", u"Pode ver recibo do evento S2405EVTCDBENEFALT"),
            ("can_see_xml_s2405evtCdBenefAlt", u"Pode ver xml do evento S2405EVTCDBENEFALT"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef',
            'dtalteracao',
            'nmbenefic',
            'sexo',
            'racacor',
            'incfismen',
            'paisnac', ]



class s2405evtCdBenefAltSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2405evtCdBenefAlt
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2410evtCdBenIn(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2410_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2410_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2410_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    cnpjorigem = models.CharField(max_length=14, blank=True, null=True, )
    cadini = models.CharField(choices=CHOICES_S2410_CADINI, max_length=1, null=True, )
    nrbeneficio = models.CharField(max_length=20, null=True, )
    dtinibeneficio = models.DateField(null=True, )
    tpbeneficio = models.TextField(null=True, )
    vrbeneficio = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    tpplanrp = models.IntegerField(choices=CHOICES_S2410_TPPLANRP, null=True, )
    dsc = models.CharField(max_length=255, blank=True, null=True, )
    inddecjud = models.CharField(choices=CHOICES_S2410_INDDECJUD, max_length=1, null=True, )
    indhomologtc = models.CharField(choices=CHOICES_S2410_INDHOMOLOGTC, max_length=1, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2410_evtcdbenin_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2410 - Cadastro de Benefícios - Entes Públicos - Início'
        db_table = r's2410_evtcdbenin'       
        managed = True  # s2410_evtcdbenin #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2410evtCdBenIn", u"Pode ver listagem do modelo S2410EVTCDBENIN"),
            ("can_see_data_s2410evtCdBenIn", u"Pode visualizar o conteúdo do modelo S2410EVTCDBENIN"),
            ("can_see_menu_s2410evtCdBenIn", u"Pode visualizar no menu o modelo S2410EVTCDBENIN"),
            ("can_print_list_s2410evtCdBenIn", u"Pode imprimir listagem do modelo S2410EVTCDBENIN"),
            ("can_print_data_s2410evtCdBenIn", u"Pode imprimir o conteúdo do modelo S2410EVTCDBENIN"),
            ("can_open_s2410evtCdBenIn", u"Pode abrir o evento S2410EVTCDBENIN para edição"),
            ("can_duplicate_s2410evtCdBenIn", u"Pode duplicar o evento S2410EVTCDBENIN"),
            ("can_validate_s2410evtCdBenIn", u"Pode validar o evento S2410EVTCDBENIN"),
            ("can_change_identity_s2410evtCdBenIn", u"Pode alterar identidade do evento S2410EVTCDBENIN"),
            ("can_see_layout_s2410evtCdBenIn", u"Pode ver layout do evento S2410EVTCDBENIN"),
            ("can_see_receipt_s2410evtCdBenIn", u"Pode ver recibo do evento S2410EVTCDBENIN"),
            ("can_see_xml_s2410evtCdBenIn", u"Pode ver xml do evento S2410EVTCDBENIN"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef',
            'cadini',
            'nrbeneficio',
            'dtinibeneficio',
            'tpbeneficio',
            'vrbeneficio',
            'tpplanrp',
            'inddecjud',
            'indhomologtc', ]



class s2410evtCdBenInSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2410evtCdBenIn
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2416evtCdBenAlt(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2416_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2416_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2416_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    nrbeneficio = models.CharField(max_length=20, null=True, )
    dtaltbeneficio = models.DateField(null=True, )
    tpbeneficio = models.TextField(null=True, )
    tpplanrp = models.IntegerField(choices=CHOICES_S2416_TPPLANRP, null=True, )
    dsc = models.CharField(max_length=255, blank=True, null=True, )
    inddecjud = models.CharField(choices=CHOICES_S2416_INDDECJUD, max_length=1, null=True, )
    indhomologtc = models.CharField(choices=CHOICES_S2416_INDHOMOLOGTC, max_length=1, null=True, )
    indsuspensao = models.CharField(choices=CHOICES_S2416_INDSUSPENSAO, max_length=1, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2416_evtcdbenalt_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2416 - Cadastro de Benefícios - Entes Públicos - Alteração'
        db_table = r's2416_evtcdbenalt'       
        managed = True  # s2416_evtcdbenalt #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2416evtCdBenAlt", u"Pode ver listagem do modelo S2416EVTCDBENALT"),
            ("can_see_data_s2416evtCdBenAlt", u"Pode visualizar o conteúdo do modelo S2416EVTCDBENALT"),
            ("can_see_menu_s2416evtCdBenAlt", u"Pode visualizar no menu o modelo S2416EVTCDBENALT"),
            ("can_print_list_s2416evtCdBenAlt", u"Pode imprimir listagem do modelo S2416EVTCDBENALT"),
            ("can_print_data_s2416evtCdBenAlt", u"Pode imprimir o conteúdo do modelo S2416EVTCDBENALT"),
            ("can_open_s2416evtCdBenAlt", u"Pode abrir o evento S2416EVTCDBENALT para edição"),
            ("can_duplicate_s2416evtCdBenAlt", u"Pode duplicar o evento S2416EVTCDBENALT"),
            ("can_validate_s2416evtCdBenAlt", u"Pode validar o evento S2416EVTCDBENALT"),
            ("can_change_identity_s2416evtCdBenAlt", u"Pode alterar identidade do evento S2416EVTCDBENALT"),
            ("can_see_layout_s2416evtCdBenAlt", u"Pode ver layout do evento S2416EVTCDBENALT"),
            ("can_see_receipt_s2416evtCdBenAlt", u"Pode ver recibo do evento S2416EVTCDBENALT"),
            ("can_see_xml_s2416evtCdBenAlt", u"Pode ver xml do evento S2416EVTCDBENALT"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef',
            'nrbeneficio',
            'dtaltbeneficio',
            'tpbeneficio',
            'tpplanrp',
            'inddecjud',
            'indhomologtc',
            'indsuspensao', ]



class s2416evtCdBenAltSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2416evtCdBenAlt
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2420evtCdBenTerm(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_S2420_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=40, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S2420_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S2420_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpfbenef = models.CharField(max_length=11, null=True, )
    nrbeneficio = models.CharField(max_length=20, null=True, )
    dttermbeneficio = models.DateField(null=True, )
    mtvtermino = models.CharField(choices=CHOICES_ESOCIALBENEFICIOSPREVIDENCIARIOSCESSACAOMOTIVOS, max_length=2, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s2420_evtcdbenterm_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-2420 - Cadastro de Benefícios - Entes Públicos - Término'
        db_table = r's2420_evtcdbenterm'       
        managed = True  # s2420_evtcdbenterm #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2420evtCdBenTerm", u"Pode ver listagem do modelo S2420EVTCDBENTERM"),
            ("can_see_data_s2420evtCdBenTerm", u"Pode visualizar o conteúdo do modelo S2420EVTCDBENTERM"),
            ("can_see_menu_s2420evtCdBenTerm", u"Pode visualizar no menu o modelo S2420EVTCDBENTERM"),
            ("can_print_list_s2420evtCdBenTerm", u"Pode imprimir listagem do modelo S2420EVTCDBENTERM"),
            ("can_print_data_s2420evtCdBenTerm", u"Pode imprimir o conteúdo do modelo S2420EVTCDBENTERM"),
            ("can_open_s2420evtCdBenTerm", u"Pode abrir o evento S2420EVTCDBENTERM para edição"),
            ("can_duplicate_s2420evtCdBenTerm", u"Pode duplicar o evento S2420EVTCDBENTERM"),
            ("can_validate_s2420evtCdBenTerm", u"Pode validar o evento S2420EVTCDBENTERM"),
            ("can_change_identity_s2420evtCdBenTerm", u"Pode alterar identidade do evento S2420EVTCDBENTERM"),
            ("can_see_layout_s2420evtCdBenTerm", u"Pode ver layout do evento S2420EVTCDBENTERM"),
            ("can_see_receipt_s2420evtCdBenTerm", u"Pode ver recibo do evento S2420EVTCDBENTERM"),
            ("can_see_xml_s2420evtCdBenTerm", u"Pode ver xml do evento S2420EVTCDBENTERM"),)
            
        ordering = [
            'identidade',
            'indretif',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'cpfbenef',
            'nrbeneficio',
            'dttermbeneficio',
            'mtvtermino', ]



class s2420evtCdBenTermSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s2420evtCdBenTerm
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s3000evtExclusao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_S3000_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_S3000_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    tpevento = models.TextField(null=True, )
    nrrecevt = models.CharField(max_length=40, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s3000_evtexclusao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-3000 - Exclusão de eventos'
        db_table = r's3000_evtexclusao'       
        managed = True  # s3000_evtexclusao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s3000evtExclusao", u"Pode ver listagem do modelo S3000EVTEXCLUSAO"),
            ("can_see_data_s3000evtExclusao", u"Pode visualizar o conteúdo do modelo S3000EVTEXCLUSAO"),
            ("can_see_menu_s3000evtExclusao", u"Pode visualizar no menu o modelo S3000EVTEXCLUSAO"),
            ("can_print_list_s3000evtExclusao", u"Pode imprimir listagem do modelo S3000EVTEXCLUSAO"),
            ("can_print_data_s3000evtExclusao", u"Pode imprimir o conteúdo do modelo S3000EVTEXCLUSAO"),
            ("can_open_s3000evtExclusao", u"Pode abrir o evento S3000EVTEXCLUSAO para edição"),
            ("can_duplicate_s3000evtExclusao", u"Pode duplicar o evento S3000EVTEXCLUSAO"),
            ("can_validate_s3000evtExclusao", u"Pode validar o evento S3000EVTEXCLUSAO"),
            ("can_change_identity_s3000evtExclusao", u"Pode alterar identidade do evento S3000EVTEXCLUSAO"),
            ("can_see_layout_s3000evtExclusao", u"Pode ver layout do evento S3000EVTEXCLUSAO"),
            ("can_see_receipt_s3000evtExclusao", u"Pode ver recibo do evento S3000EVTEXCLUSAO"),
            ("can_see_xml_s3000evtExclusao", u"Pode ver xml do evento S3000EVTEXCLUSAO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpevento',
            'nrrecevt', ]



class s3000evtExclusaoSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s3000evtExclusao
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5001evtBasesTrab(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S5001_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5001_evtbasestrab_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5001 - Informações das contribuições sociais por trabalhador'
        db_table = r's5001_evtbasestrab'       
        managed = True  # s5001_evtbasestrab #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5001evtBasesTrab", u"Pode ver listagem do modelo S5001EVTBASESTRAB"),
            ("can_see_data_s5001evtBasesTrab", u"Pode visualizar o conteúdo do modelo S5001EVTBASESTRAB"),
            ("can_see_menu_s5001evtBasesTrab", u"Pode visualizar no menu o modelo S5001EVTBASESTRAB"),
            ("can_print_list_s5001evtBasesTrab", u"Pode imprimir listagem do modelo S5001EVTBASESTRAB"),
            ("can_print_data_s5001evtBasesTrab", u"Pode imprimir o conteúdo do modelo S5001EVTBASESTRAB"),
            ("can_open_s5001evtBasesTrab", u"Pode abrir o evento S5001EVTBASESTRAB para edição"),
            ("can_duplicate_s5001evtBasesTrab", u"Pode duplicar o evento S5001EVTBASESTRAB"),
            ("can_validate_s5001evtBasesTrab", u"Pode validar o evento S5001EVTBASESTRAB"),
            ("can_change_identity_s5001evtBasesTrab", u"Pode alterar identidade do evento S5001EVTBASESTRAB"),
            ("can_see_layout_s5001evtBasesTrab", u"Pode ver layout do evento S5001EVTBASESTRAB"),
            ("can_see_receipt_s5001evtBasesTrab", u"Pode ver recibo do evento S5001EVTBASESTRAB"),
            ("can_see_xml_s5001evtBasesTrab", u"Pode ver xml do evento S5001EVTBASESTRAB"),)
            
        ordering = [
            'identidade',
            'nrrecarqbase',
            'indapuracao',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s5001evtBasesTrabSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5001evtBasesTrab
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5002evtIrrfBenef(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5002_evtirrfbenef_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5002 - Imposto de Renda Retido na Fonte'
        db_table = r's5002_evtirrfbenef'       
        managed = True  # s5002_evtirrfbenef #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5002evtIrrfBenef", u"Pode ver listagem do modelo S5002EVTIRRFBENEF"),
            ("can_see_data_s5002evtIrrfBenef", u"Pode visualizar o conteúdo do modelo S5002EVTIRRFBENEF"),
            ("can_see_menu_s5002evtIrrfBenef", u"Pode visualizar no menu o modelo S5002EVTIRRFBENEF"),
            ("can_print_list_s5002evtIrrfBenef", u"Pode imprimir listagem do modelo S5002EVTIRRFBENEF"),
            ("can_print_data_s5002evtIrrfBenef", u"Pode imprimir o conteúdo do modelo S5002EVTIRRFBENEF"),
            ("can_open_s5002evtIrrfBenef", u"Pode abrir o evento S5002EVTIRRFBENEF para edição"),
            ("can_duplicate_s5002evtIrrfBenef", u"Pode duplicar o evento S5002EVTIRRFBENEF"),
            ("can_validate_s5002evtIrrfBenef", u"Pode validar o evento S5002EVTIRRFBENEF"),
            ("can_change_identity_s5002evtIrrfBenef", u"Pode alterar identidade do evento S5002EVTIRRFBENEF"),
            ("can_see_layout_s5002evtIrrfBenef", u"Pode ver layout do evento S5002EVTIRRFBENEF"),
            ("can_see_receipt_s5002evtIrrfBenef", u"Pode ver recibo do evento S5002EVTIRRFBENEF"),
            ("can_see_xml_s5002evtIrrfBenef", u"Pode ver xml do evento S5002EVTIRRFBENEF"),)
            
        ordering = [
            'identidade',
            'nrrecarqbase',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s5002evtIrrfBenefSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5002evtIrrfBenef
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5003evtBasesFGTS(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    cpftrab = models.CharField(max_length=11, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    dtvenc = models.DateField(blank=True, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5003_evtbasesfgts_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5003 - Informações do FGTS por Trabalhador'
        db_table = r's5003_evtbasesfgts'       
        managed = True  # s5003_evtbasesfgts #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5003evtBasesFGTS", u"Pode ver listagem do modelo S5003EVTBASESFGTS"),
            ("can_see_data_s5003evtBasesFGTS", u"Pode visualizar o conteúdo do modelo S5003EVTBASESFGTS"),
            ("can_see_menu_s5003evtBasesFGTS", u"Pode visualizar no menu o modelo S5003EVTBASESFGTS"),
            ("can_print_list_s5003evtBasesFGTS", u"Pode imprimir listagem do modelo S5003EVTBASESFGTS"),
            ("can_print_data_s5003evtBasesFGTS", u"Pode imprimir o conteúdo do modelo S5003EVTBASESFGTS"),
            ("can_open_s5003evtBasesFGTS", u"Pode abrir o evento S5003EVTBASESFGTS para edição"),
            ("can_duplicate_s5003evtBasesFGTS", u"Pode duplicar o evento S5003EVTBASESFGTS"),
            ("can_validate_s5003evtBasesFGTS", u"Pode validar o evento S5003EVTBASESFGTS"),
            ("can_change_identity_s5003evtBasesFGTS", u"Pode alterar identidade do evento S5003EVTBASESFGTS"),
            ("can_see_layout_s5003evtBasesFGTS", u"Pode ver layout do evento S5003EVTBASESFGTS"),
            ("can_see_receipt_s5003evtBasesFGTS", u"Pode ver recibo do evento S5003EVTBASESFGTS"),
            ("can_see_xml_s5003evtBasesFGTS", u"Pode ver xml do evento S5003EVTBASESFGTS"),)
            
        ordering = [
            'identidade',
            'nrrecarqbase',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cpftrab', ]



class s5003evtBasesFGTSSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5003evtBasesFGTS
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5011evtCS(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indapuracao = models.IntegerField(choices=CHOICES_S5011_INDAPURACAO, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_S5011_INDEXISTINFO, null=True, )
    classtrib = models.CharField(choices=CHOICES_ESOCIALCLASSIFICACOESTRIBUTARIAS, max_length=2, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5011_evtcs_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5011 - Informações das contribuições sociais consolidadas por contribuinte'
        db_table = r's5011_evtcs'       
        managed = True  # s5011_evtcs #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5011evtCS", u"Pode ver listagem do modelo S5011EVTCS"),
            ("can_see_data_s5011evtCS", u"Pode visualizar o conteúdo do modelo S5011EVTCS"),
            ("can_see_menu_s5011evtCS", u"Pode visualizar no menu o modelo S5011EVTCS"),
            ("can_print_list_s5011evtCS", u"Pode imprimir listagem do modelo S5011EVTCS"),
            ("can_print_data_s5011evtCS", u"Pode imprimir o conteúdo do modelo S5011EVTCS"),
            ("can_open_s5011evtCS", u"Pode abrir o evento S5011EVTCS para edição"),
            ("can_duplicate_s5011evtCS", u"Pode duplicar o evento S5011EVTCS"),
            ("can_validate_s5011evtCS", u"Pode validar o evento S5011EVTCS"),
            ("can_change_identity_s5011evtCS", u"Pode alterar identidade do evento S5011EVTCS"),
            ("can_see_layout_s5011evtCS", u"Pode ver layout do evento S5011EVTCS"),
            ("can_see_receipt_s5011evtCS", u"Pode ver recibo do evento S5011EVTCS"),
            ("can_see_xml_s5011evtCS", u"Pode ver xml do evento S5011EVTCS"),)
            
        ordering = [
            'identidade',
            'indapuracao',
            'perapur',
            'tpinsc',
            'nrinsc',
            'nrrecarqbase',
            'indexistinfo',
            'classtrib', ]



class s5011evtCSSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5011evtCS
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5012evtIrrf(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_S5012_INDEXISTINFO, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5012_evtirrf_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5012 - Informações do IRRF consolidadas por contribuinte'
        db_table = r's5012_evtirrf'       
        managed = True  # s5012_evtirrf #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5012evtIrrf", u"Pode ver listagem do modelo S5012EVTIRRF"),
            ("can_see_data_s5012evtIrrf", u"Pode visualizar o conteúdo do modelo S5012EVTIRRF"),
            ("can_see_menu_s5012evtIrrf", u"Pode visualizar no menu o modelo S5012EVTIRRF"),
            ("can_print_list_s5012evtIrrf", u"Pode imprimir listagem do modelo S5012EVTIRRF"),
            ("can_print_data_s5012evtIrrf", u"Pode imprimir o conteúdo do modelo S5012EVTIRRF"),
            ("can_open_s5012evtIrrf", u"Pode abrir o evento S5012EVTIRRF para edição"),
            ("can_duplicate_s5012evtIrrf", u"Pode duplicar o evento S5012EVTIRRF"),
            ("can_validate_s5012evtIrrf", u"Pode validar o evento S5012EVTIRRF"),
            ("can_change_identity_s5012evtIrrf", u"Pode alterar identidade do evento S5012EVTIRRF"),
            ("can_see_layout_s5012evtIrrf", u"Pode ver layout do evento S5012EVTIRRF"),
            ("can_see_receipt_s5012evtIrrf", u"Pode ver recibo do evento S5012EVTIRRF"),
            ("can_see_xml_s5012evtIrrf", u"Pode ver xml do evento S5012EVTIRRF"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'nrrecarqbase',
            'indexistinfo', ]



class s5012evtIrrfSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5012evtIrrf
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s5013evtFGTS(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    nrrecarqbase = models.CharField(max_length=40, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_S5013_INDEXISTINFO, null=True, )
    versao = models.CharField(choices=ESOCIAL_VERSOES, max_length=20, blank=True, default='v02_05_00', )
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True, )
    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    
    def __unicode__(self):
        
        return self.identidade

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.esocial.views.s5013_evtfgts_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'S-5013 - Informações do FGTS consolidadas por contribuinte'
        db_table = r's5013_evtfgts'       
        managed = True  # s5013_evtfgts #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s5013evtFGTS", u"Pode ver listagem do modelo S5013EVTFGTS"),
            ("can_see_data_s5013evtFGTS", u"Pode visualizar o conteúdo do modelo S5013EVTFGTS"),
            ("can_see_menu_s5013evtFGTS", u"Pode visualizar no menu o modelo S5013EVTFGTS"),
            ("can_print_list_s5013evtFGTS", u"Pode imprimir listagem do modelo S5013EVTFGTS"),
            ("can_print_data_s5013evtFGTS", u"Pode imprimir o conteúdo do modelo S5013EVTFGTS"),
            ("can_open_s5013evtFGTS", u"Pode abrir o evento S5013EVTFGTS para edição"),
            ("can_duplicate_s5013evtFGTS", u"Pode duplicar o evento S5013EVTFGTS"),
            ("can_validate_s5013evtFGTS", u"Pode validar o evento S5013EVTFGTS"),
            ("can_change_identity_s5013evtFGTS", u"Pode alterar identidade do evento S5013EVTFGTS"),
            ("can_see_layout_s5013evtFGTS", u"Pode ver layout do evento S5013EVTFGTS"),
            ("can_see_receipt_s5013evtFGTS", u"Pode ver recibo do evento S5013EVTFGTS"),
            ("can_see_xml_s5013evtFGTS", u"Pode ver xml do evento S5013EVTFGTS"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'nrrecarqbase',
            'indexistinfo', ]



class s5013evtFGTSSerializer(ModelSerializer):

    from rest_framework import serializers
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_ESOCIAL
    from constance import config

    tpamb = serializers.IntegerField(default=config.ESOCIAL_TP_AMB, initial=config.ESOCIAL_TP_AMB, read_only=True)
    verproc = serializers.CharField(default=VERSAO_EMENSAGERIA, initial=VERSAO_EMENSAGERIA, read_only=True)
    procemi = serializers.IntegerField(default=1, initial=1, read_only=True)
    versao = serializers.CharField(default=VERSAO_LAYOUT_ESOCIAL, initial=VERSAO_LAYOUT_ESOCIAL, read_only=True)
    arquivo_original = serializers.IntegerField(default=0, initial=0, read_only=True)
    status = serializers.IntegerField(default=0, initial=0, read_only=True)

    class Meta:
    
        model = s5013evtFGTS
        fields = '__all__'
        read_only_fields = ('id', 'verproc',
                            'tpamb', 'procemi',
                            'versao', 'arquivo_original',
                            'status', 'transmissor_lote_esocial',
                            'retornos_eventos', 'ocorrencias',
                            'validacao_precedencia', 'validacoes',
                            'arquivo_original', 'arquivo',
                            'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')