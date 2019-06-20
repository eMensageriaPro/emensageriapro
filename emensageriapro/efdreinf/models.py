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
from emensageriapro.efdreinf.choices import *
get_model = apps.get_model

from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


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





class r1000evtInfoContri(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R1000_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R1000_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r1000_evtinfocontri_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-1000 - Informações do Contribuinte'
        db_table = r'r1000_evtinfocontri'       
        managed = True  # r1000_evtinfocontri #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000evtInfoContri", u"Pode ver listagem do modelo R1000EVTINFOCONTRI"),
            ("can_see_data_r1000evtInfoContri", u"Pode visualizar o conteúdo do modelo R1000EVTINFOCONTRI"),
            ("can_see_menu_r1000evtInfoContri", u"Pode visualizar no menu o modelo R1000EVTINFOCONTRI"),
            ("can_print_list_r1000evtInfoContri", u"Pode imprimir listagem do modelo R1000EVTINFOCONTRI"),
            ("can_print_data_r1000evtInfoContri", u"Pode imprimir o conteúdo do modelo R1000EVTINFOCONTRI"),
            ("can_open_r1000evtInfoContri", u"Pode abrir o evento R1000EVTINFOCONTRI para edição"),
            ("can_duplicate_r1000evtInfoContri", u"Pode duplicar o evento R1000EVTINFOCONTRI"),
            ("can_create_change_r1000evtInfoContri", u"Pode criar evento de alteração do evento R1000EVTINFOCONTRI com base em evento existente"),
            ("can_create_delete_r1000evtInfoContri", u"Pode criar evento de exclusão do evento R1000EVTINFOCONTRI com base em evento existente"), 
            ("can_validate_r1000evtInfoContri", u"Pode validar o evento R1000EVTINFOCONTRI"),
            ("can_change_identity_r1000evtInfoContri", u"Pode alterar identidade do evento R1000EVTINFOCONTRI"),
            ("can_see_layout_r1000evtInfoContri", u"Pode ver layout do evento R1000EVTINFOCONTRI"),
            ("can_see_receipt_r1000evtInfoContri", u"Pode ver recibo do evento R1000EVTINFOCONTRI"),
            ("can_see_xml_r1000evtInfoContri", u"Pode ver xml do evento R1000EVTINFOCONTRI"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class r1000evtInfoContriSerializer(ModelSerializer):

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
    
        model = r1000evtInfoContri
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


class r1070evtTabProcesso(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R1070_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R1070_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    operacao = models.IntegerField(choices=OPERACOES, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r1070_evttabprocesso_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-1070 - Tabela de Processos Administrativos/Judiciais'
        db_table = r'r1070_evttabprocesso'       
        managed = True  # r1070_evttabprocesso #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1070evtTabProcesso", u"Pode ver listagem do modelo R1070EVTTABPROCESSO"),
            ("can_see_data_r1070evtTabProcesso", u"Pode visualizar o conteúdo do modelo R1070EVTTABPROCESSO"),
            ("can_see_menu_r1070evtTabProcesso", u"Pode visualizar no menu o modelo R1070EVTTABPROCESSO"),
            ("can_print_list_r1070evtTabProcesso", u"Pode imprimir listagem do modelo R1070EVTTABPROCESSO"),
            ("can_print_data_r1070evtTabProcesso", u"Pode imprimir o conteúdo do modelo R1070EVTTABPROCESSO"),
            ("can_open_r1070evtTabProcesso", u"Pode abrir o evento R1070EVTTABPROCESSO para edição"),
            ("can_duplicate_r1070evtTabProcesso", u"Pode duplicar o evento R1070EVTTABPROCESSO"),
            ("can_create_change_r1070evtTabProcesso", u"Pode criar evento de alteração do evento R1070EVTTABPROCESSO com base em evento existente"),
            ("can_create_delete_r1070evtTabProcesso", u"Pode criar evento de exclusão do evento R1070EVTTABPROCESSO com base em evento existente"), 
            ("can_validate_r1070evtTabProcesso", u"Pode validar o evento R1070EVTTABPROCESSO"),
            ("can_change_identity_r1070evtTabProcesso", u"Pode alterar identidade do evento R1070EVTTABPROCESSO"),
            ("can_see_layout_r1070evtTabProcesso", u"Pode ver layout do evento R1070EVTTABPROCESSO"),
            ("can_see_receipt_r1070evtTabProcesso", u"Pode ver recibo do evento R1070EVTTABPROCESSO"),
            ("can_see_xml_r1070evtTabProcesso", u"Pode ver xml do evento R1070EVTTABPROCESSO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class r1070evtTabProcessoSerializer(ModelSerializer):

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
    
        model = r1070evtTabProcesso
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


class r2010evtServTom(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    indobra = models.IntegerField(choices=CHOICES_R2010_INDOBRA, null=True, )
    cnpjprestador = models.CharField(max_length=14, null=True, )
    vlrtotalbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    indcprb = models.IntegerField(choices=CHOICES_R2010_INDCPRB, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2010_evtservtom_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2010 - Retenção Contribuição Previdenciária - Serviços Tomados'
        db_table = r'r2010_evtservtom'       
        managed = True  # r2010_evtservtom #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2010evtServTom", u"Pode ver listagem do modelo R2010EVTSERVTOM"),
            ("can_see_data_r2010evtServTom", u"Pode visualizar o conteúdo do modelo R2010EVTSERVTOM"),
            ("can_see_menu_r2010evtServTom", u"Pode visualizar no menu o modelo R2010EVTSERVTOM"),
            ("can_print_list_r2010evtServTom", u"Pode imprimir listagem do modelo R2010EVTSERVTOM"),
            ("can_print_data_r2010evtServTom", u"Pode imprimir o conteúdo do modelo R2010EVTSERVTOM"),
            ("can_open_r2010evtServTom", u"Pode abrir o evento R2010EVTSERVTOM para edição"),
            ("can_duplicate_r2010evtServTom", u"Pode duplicar o evento R2010EVTSERVTOM"),
            ("can_validate_r2010evtServTom", u"Pode validar o evento R2010EVTSERVTOM"),
            ("can_change_identity_r2010evtServTom", u"Pode alterar identidade do evento R2010EVTSERVTOM"),
            ("can_see_layout_r2010evtServTom", u"Pode ver layout do evento R2010EVTSERVTOM"),
            ("can_see_receipt_r2010evtServTom", u"Pode ver recibo do evento R2010EVTSERVTOM"),
            ("can_see_xml_r2010evtServTom", u"Pode ver xml do evento R2010EVTSERVTOM"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab',
            'indobra',
            'cnpjprestador',
            'vlrtotalbruto',
            'vlrtotalbaseret',
            'vlrtotalretprinc',
            'indcprb', ]



class r2010evtServTomSerializer(ModelSerializer):

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
    
        model = r2010evtServTom
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


class r2020evtServPrest(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2020_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2020_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2020_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestabprest = models.IntegerField(null=True, )
    nrinscestabprest = models.CharField(max_length=14, null=True, )
    tpinsctomador = models.IntegerField(null=True, )
    nrinsctomador = models.CharField(max_length=14, null=True, )
    indobra = models.IntegerField(choices=CHOICES_R2020_INDOBRA, null=True, )
    vlrtotalbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2020_evtservprest_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2020 - Retenção Contribuição Previdenciária - Serviços Prestados'
        db_table = r'r2020_evtservprest'       
        managed = True  # r2020_evtservprest #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2020evtServPrest", u"Pode ver listagem do modelo R2020EVTSERVPREST"),
            ("can_see_data_r2020evtServPrest", u"Pode visualizar o conteúdo do modelo R2020EVTSERVPREST"),
            ("can_see_menu_r2020evtServPrest", u"Pode visualizar no menu o modelo R2020EVTSERVPREST"),
            ("can_print_list_r2020evtServPrest", u"Pode imprimir listagem do modelo R2020EVTSERVPREST"),
            ("can_print_data_r2020evtServPrest", u"Pode imprimir o conteúdo do modelo R2020EVTSERVPREST"),
            ("can_open_r2020evtServPrest", u"Pode abrir o evento R2020EVTSERVPREST para edição"),
            ("can_duplicate_r2020evtServPrest", u"Pode duplicar o evento R2020EVTSERVPREST"),
            ("can_validate_r2020evtServPrest", u"Pode validar o evento R2020EVTSERVPREST"),
            ("can_change_identity_r2020evtServPrest", u"Pode alterar identidade do evento R2020EVTSERVPREST"),
            ("can_see_layout_r2020evtServPrest", u"Pode ver layout do evento R2020EVTSERVPREST"),
            ("can_see_receipt_r2020evtServPrest", u"Pode ver recibo do evento R2020EVTSERVPREST"),
            ("can_see_xml_r2020evtServPrest", u"Pode ver xml do evento R2020EVTSERVPREST"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestabprest',
            'nrinscestabprest',
            'tpinsctomador',
            'nrinsctomador',
            'indobra',
            'vlrtotalbruto',
            'vlrtotalbaseret',
            'vlrtotalretprinc', ]



class r2020evtServPrestSerializer(ModelSerializer):

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
    
        model = r2020evtServPrest
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


class r2030evtAssocDespRec(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2030_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2030_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2030_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2030_evtassocdesprec_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2030 - Recursos Recebidos por Associação Desportiva'
        db_table = r'r2030_evtassocdesprec'       
        managed = True  # r2030_evtassocdesprec #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2030evtAssocDespRec", u"Pode ver listagem do modelo R2030EVTASSOCDESPREC"),
            ("can_see_data_r2030evtAssocDespRec", u"Pode visualizar o conteúdo do modelo R2030EVTASSOCDESPREC"),
            ("can_see_menu_r2030evtAssocDespRec", u"Pode visualizar no menu o modelo R2030EVTASSOCDESPREC"),
            ("can_print_list_r2030evtAssocDespRec", u"Pode imprimir listagem do modelo R2030EVTASSOCDESPREC"),
            ("can_print_data_r2030evtAssocDespRec", u"Pode imprimir o conteúdo do modelo R2030EVTASSOCDESPREC"),
            ("can_open_r2030evtAssocDespRec", u"Pode abrir o evento R2030EVTASSOCDESPREC para edição"),
            ("can_duplicate_r2030evtAssocDespRec", u"Pode duplicar o evento R2030EVTASSOCDESPREC"),
            ("can_validate_r2030evtAssocDespRec", u"Pode validar o evento R2030EVTASSOCDESPREC"),
            ("can_change_identity_r2030evtAssocDespRec", u"Pode alterar identidade do evento R2030EVTASSOCDESPREC"),
            ("can_see_layout_r2030evtAssocDespRec", u"Pode ver layout do evento R2030EVTASSOCDESPREC"),
            ("can_see_receipt_r2030evtAssocDespRec", u"Pode ver recibo do evento R2030EVTASSOCDESPREC"),
            ("can_see_xml_r2030evtAssocDespRec", u"Pode ver xml do evento R2030EVTASSOCDESPREC"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab', ]



class r2030evtAssocDespRecSerializer(ModelSerializer):

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
    
        model = r2030evtAssocDespRec
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


class r2040evtAssocDespRep(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2040_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2040_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2040_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2040_evtassocdesprep_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2040 - Recursos Repassados para Associação Desportiva'
        db_table = r'r2040_evtassocdesprep'       
        managed = True  # r2040_evtassocdesprep #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2040evtAssocDespRep", u"Pode ver listagem do modelo R2040EVTASSOCDESPREP"),
            ("can_see_data_r2040evtAssocDespRep", u"Pode visualizar o conteúdo do modelo R2040EVTASSOCDESPREP"),
            ("can_see_menu_r2040evtAssocDespRep", u"Pode visualizar no menu o modelo R2040EVTASSOCDESPREP"),
            ("can_print_list_r2040evtAssocDespRep", u"Pode imprimir listagem do modelo R2040EVTASSOCDESPREP"),
            ("can_print_data_r2040evtAssocDespRep", u"Pode imprimir o conteúdo do modelo R2040EVTASSOCDESPREP"),
            ("can_open_r2040evtAssocDespRep", u"Pode abrir o evento R2040EVTASSOCDESPREP para edição"),
            ("can_duplicate_r2040evtAssocDespRep", u"Pode duplicar o evento R2040EVTASSOCDESPREP"),
            ("can_validate_r2040evtAssocDespRep", u"Pode validar o evento R2040EVTASSOCDESPREP"),
            ("can_change_identity_r2040evtAssocDespRep", u"Pode alterar identidade do evento R2040EVTASSOCDESPREP"),
            ("can_see_layout_r2040evtAssocDespRep", u"Pode ver layout do evento R2040EVTASSOCDESPREP"),
            ("can_see_receipt_r2040evtAssocDespRep", u"Pode ver recibo do evento R2040EVTASSOCDESPREP"),
            ("can_see_xml_r2040evtAssocDespRep", u"Pode ver xml do evento R2040EVTASSOCDESPREP"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab', ]



class r2040evtAssocDespRepSerializer(ModelSerializer):

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
    
        model = r2040evtAssocDespRep
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


class r2050evtComProd(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2050_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2050_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2050_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    vlrrecbrutatotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcpapur = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrratapur = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrsenarapur = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcpsusptotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrratsusptotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrsenarsusptotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2050_evtcomprod_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2050 - Comercialização da Produção por Produtor Rural PJ/Agroindústria'
        db_table = r'r2050_evtcomprod'       
        managed = True  # r2050_evtcomprod #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2050evtComProd", u"Pode ver listagem do modelo R2050EVTCOMPROD"),
            ("can_see_data_r2050evtComProd", u"Pode visualizar o conteúdo do modelo R2050EVTCOMPROD"),
            ("can_see_menu_r2050evtComProd", u"Pode visualizar no menu o modelo R2050EVTCOMPROD"),
            ("can_print_list_r2050evtComProd", u"Pode imprimir listagem do modelo R2050EVTCOMPROD"),
            ("can_print_data_r2050evtComProd", u"Pode imprimir o conteúdo do modelo R2050EVTCOMPROD"),
            ("can_open_r2050evtComProd", u"Pode abrir o evento R2050EVTCOMPROD para edição"),
            ("can_duplicate_r2050evtComProd", u"Pode duplicar o evento R2050EVTCOMPROD"),
            ("can_validate_r2050evtComProd", u"Pode validar o evento R2050EVTCOMPROD"),
            ("can_change_identity_r2050evtComProd", u"Pode alterar identidade do evento R2050EVTCOMPROD"),
            ("can_see_layout_r2050evtComProd", u"Pode ver layout do evento R2050EVTCOMPROD"),
            ("can_see_receipt_r2050evtComProd", u"Pode ver recibo do evento R2050EVTCOMPROD"),
            ("can_see_xml_r2050evtComProd", u"Pode ver xml do evento R2050EVTCOMPROD"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab',
            'vlrrecbrutatotal',
            'vlrcpapur',
            'vlrratapur',
            'vlrsenarapur', ]



class r2050evtComProdSerializer(ModelSerializer):

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
    
        model = r2050evtComProd
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


class r2060evtCPRB(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2060_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2060_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2060_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    vlrrecbrutatotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcpapurtotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcprbsusptotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2060_evtcprb_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2060 - Contribuição Previdenciária sobre a Receita Bruta - CPRB'
        db_table = r'r2060_evtcprb'       
        managed = True  # r2060_evtcprb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2060evtCPRB", u"Pode ver listagem do modelo R2060EVTCPRB"),
            ("can_see_data_r2060evtCPRB", u"Pode visualizar o conteúdo do modelo R2060EVTCPRB"),
            ("can_see_menu_r2060evtCPRB", u"Pode visualizar no menu o modelo R2060EVTCPRB"),
            ("can_print_list_r2060evtCPRB", u"Pode imprimir listagem do modelo R2060EVTCPRB"),
            ("can_print_data_r2060evtCPRB", u"Pode imprimir o conteúdo do modelo R2060EVTCPRB"),
            ("can_open_r2060evtCPRB", u"Pode abrir o evento R2060EVTCPRB para edição"),
            ("can_duplicate_r2060evtCPRB", u"Pode duplicar o evento R2060EVTCPRB"),
            ("can_validate_r2060evtCPRB", u"Pode validar o evento R2060EVTCPRB"),
            ("can_change_identity_r2060evtCPRB", u"Pode alterar identidade do evento R2060EVTCPRB"),
            ("can_see_layout_r2060evtCPRB", u"Pode ver layout do evento R2060EVTCPRB"),
            ("can_see_receipt_r2060evtCPRB", u"Pode ver recibo do evento R2060EVTCPRB"),
            ("can_see_xml_r2060evtCPRB", u"Pode ver xml do evento R2060EVTCPRB"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab',
            'vlrrecbrutatotal',
            'vlrcpapurtotal', ]



class r2060evtCPRBSerializer(ModelSerializer):

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
    
        model = r2060evtCPRB
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


class r2070evtPgtosDivs(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2070_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2070_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2070_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    codpgto = models.IntegerField(null=True, )
    tpinscbenef = models.IntegerField(choices=CHOICES_R2070_TPINSCBENEF, blank=True, null=True, )
    nrinscbenef = models.CharField(max_length=14, blank=True, null=True, )
    nmrazaobenef = models.CharField(max_length=150, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2070 - Retenções na Fonte - IR, CSLL, Cofins, PIS/PASEP'
        db_table = r'r2070_evtpgtosdivs'       
        managed = True  # r2070_evtpgtosdivs #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2070evtPgtosDivs", u"Pode ver listagem do modelo R2070EVTPGTOSDIVS"),
            ("can_see_data_r2070evtPgtosDivs", u"Pode visualizar o conteúdo do modelo R2070EVTPGTOSDIVS"),
            ("can_see_menu_r2070evtPgtosDivs", u"Pode visualizar no menu o modelo R2070EVTPGTOSDIVS"),
            ("can_print_list_r2070evtPgtosDivs", u"Pode imprimir listagem do modelo R2070EVTPGTOSDIVS"),
            ("can_print_data_r2070evtPgtosDivs", u"Pode imprimir o conteúdo do modelo R2070EVTPGTOSDIVS"),
            ("can_open_r2070evtPgtosDivs", u"Pode abrir o evento R2070EVTPGTOSDIVS para edição"),
            ("can_duplicate_r2070evtPgtosDivs", u"Pode duplicar o evento R2070EVTPGTOSDIVS"),
            ("can_validate_r2070evtPgtosDivs", u"Pode validar o evento R2070EVTPGTOSDIVS"),
            ("can_change_identity_r2070evtPgtosDivs", u"Pode alterar identidade do evento R2070EVTPGTOSDIVS"),
            ("can_see_layout_r2070evtPgtosDivs", u"Pode ver layout do evento R2070EVTPGTOSDIVS"),
            ("can_see_receipt_r2070evtPgtosDivs", u"Pode ver recibo do evento R2070EVTPGTOSDIVS"),
            ("can_see_xml_r2070evtPgtosDivs", u"Pode ver xml do evento R2070EVTPGTOSDIVS"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'codpgto',
            'nmrazaobenef', ]



class r2070evtPgtosDivsSerializer(ModelSerializer):

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
    
        model = r2070evtPgtosDivs
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


class r2098evtReabreEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2098_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2098_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2098_evtreabreevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2098 - Reabertura dos Eventos Periódicos'
        db_table = r'r2098_evtreabreevper'       
        managed = True  # r2098_evtreabreevper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2098evtReabreEvPer", u"Pode ver listagem do modelo R2098EVTREABREEVPER"),
            ("can_see_data_r2098evtReabreEvPer", u"Pode visualizar o conteúdo do modelo R2098EVTREABREEVPER"),
            ("can_see_menu_r2098evtReabreEvPer", u"Pode visualizar no menu o modelo R2098EVTREABREEVPER"),
            ("can_print_list_r2098evtReabreEvPer", u"Pode imprimir listagem do modelo R2098EVTREABREEVPER"),
            ("can_print_data_r2098evtReabreEvPer", u"Pode imprimir o conteúdo do modelo R2098EVTREABREEVPER"),
            ("can_open_r2098evtReabreEvPer", u"Pode abrir o evento R2098EVTREABREEVPER para edição"),
            ("can_duplicate_r2098evtReabreEvPer", u"Pode duplicar o evento R2098EVTREABREEVPER"),
            ("can_validate_r2098evtReabreEvPer", u"Pode validar o evento R2098EVTREABREEVPER"),
            ("can_change_identity_r2098evtReabreEvPer", u"Pode alterar identidade do evento R2098EVTREABREEVPER"),
            ("can_see_layout_r2098evtReabreEvPer", u"Pode ver layout do evento R2098EVTREABREEVPER"),
            ("can_see_receipt_r2098evtReabreEvPer", u"Pode ver recibo do evento R2098EVTREABREEVPER"),
            ("can_see_xml_r2098evtReabreEvPer", u"Pode ver xml do evento R2098EVTREABREEVPER"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class r2098evtReabreEvPerSerializer(ModelSerializer):

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
    
        model = r2098evtReabreEvPer
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


class r2099evtFechaEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2099_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2099_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    evtservtm = models.CharField(choices=CHOICES_R2099_EVTSERVTM, max_length=1, null=True, )
    evtservpr = models.CharField(choices=CHOICES_R2099_EVTSERVPR, max_length=1, null=True, )
    evtassdesprec = models.CharField(choices=CHOICES_R2099_EVTASSDESPREC, max_length=1, null=True, )
    evtassdesprep = models.CharField(choices=CHOICES_R2099_EVTASSDESPREP, max_length=1, null=True, )
    evtcomprod = models.CharField(choices=CHOICES_R2099_EVTCOMPROD, max_length=1, null=True, )
    evtcprb = models.CharField(choices=CHOICES_R2099_EVTCPRB, max_length=1, null=True, )
    evtpgtos = models.CharField(choices=CHOICES_R2099_EVTPGTOS, max_length=1, blank=True, null=True, )
    compsemmovto = models.CharField(max_length=7, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r2099_evtfechaevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-2099 - Fechamento dos Eventos Periódicos'
        db_table = r'r2099_evtfechaevper'       
        managed = True  # r2099_evtfechaevper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r2099evtFechaEvPer", u"Pode ver listagem do modelo R2099EVTFECHAEVPER"),
            ("can_see_data_r2099evtFechaEvPer", u"Pode visualizar o conteúdo do modelo R2099EVTFECHAEVPER"),
            ("can_see_menu_r2099evtFechaEvPer", u"Pode visualizar no menu o modelo R2099EVTFECHAEVPER"),
            ("can_print_list_r2099evtFechaEvPer", u"Pode imprimir listagem do modelo R2099EVTFECHAEVPER"),
            ("can_print_data_r2099evtFechaEvPer", u"Pode imprimir o conteúdo do modelo R2099EVTFECHAEVPER"),
            ("can_open_r2099evtFechaEvPer", u"Pode abrir o evento R2099EVTFECHAEVPER para edição"),
            ("can_duplicate_r2099evtFechaEvPer", u"Pode duplicar o evento R2099EVTFECHAEVPER"),
            ("can_validate_r2099evtFechaEvPer", u"Pode validar o evento R2099EVTFECHAEVPER"),
            ("can_change_identity_r2099evtFechaEvPer", u"Pode alterar identidade do evento R2099EVTFECHAEVPER"),
            ("can_see_layout_r2099evtFechaEvPer", u"Pode ver layout do evento R2099EVTFECHAEVPER"),
            ("can_see_receipt_r2099evtFechaEvPer", u"Pode ver recibo do evento R2099EVTFECHAEVPER"),
            ("can_see_xml_r2099evtFechaEvPer", u"Pode ver xml do evento R2099EVTFECHAEVPER"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'evtservtm',
            'evtservpr',
            'evtassdesprec',
            'evtassdesprep',
            'evtcomprod',
            'evtcprb', ]



class r2099evtFechaEvPerSerializer(ModelSerializer):

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
    
        model = r2099evtFechaEvPer
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


class r3010evtEspDesportivo(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R3010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    dtapuracao = models.DateField(null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R3010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R3010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(choices=CHOICES_R3010_TPINSCESTAB, null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcpsusptotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrreceitaclubes = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrretparc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r3010_evtespdesportivo_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-3010 - Receita de Espetáculo Desportivo'
        db_table = r'r3010_evtespdesportivo'       
        managed = True  # r3010_evtespdesportivo #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r3010evtEspDesportivo", u"Pode ver listagem do modelo R3010EVTESPDESPORTIVO"),
            ("can_see_data_r3010evtEspDesportivo", u"Pode visualizar o conteúdo do modelo R3010EVTESPDESPORTIVO"),
            ("can_see_menu_r3010evtEspDesportivo", u"Pode visualizar no menu o modelo R3010EVTESPDESPORTIVO"),
            ("can_print_list_r3010evtEspDesportivo", u"Pode imprimir listagem do modelo R3010EVTESPDESPORTIVO"),
            ("can_print_data_r3010evtEspDesportivo", u"Pode imprimir o conteúdo do modelo R3010EVTESPDESPORTIVO"),
            ("can_open_r3010evtEspDesportivo", u"Pode abrir o evento R3010EVTESPDESPORTIVO para edição"),
            ("can_duplicate_r3010evtEspDesportivo", u"Pode duplicar o evento R3010EVTESPDESPORTIVO"),
            ("can_validate_r3010evtEspDesportivo", u"Pode validar o evento R3010EVTESPDESPORTIVO"),
            ("can_change_identity_r3010evtEspDesportivo", u"Pode alterar identidade do evento R3010EVTESPDESPORTIVO"),
            ("can_see_layout_r3010evtEspDesportivo", u"Pode ver layout do evento R3010EVTESPDESPORTIVO"),
            ("can_see_receipt_r3010evtEspDesportivo", u"Pode ver recibo do evento R3010EVTESPDESPORTIVO"),
            ("can_see_xml_r3010evtEspDesportivo", u"Pode ver xml do evento R3010EVTESPDESPORTIVO"),)
            
        ordering = [
            'identidade',
            'indretif',
            'dtapuracao',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab',
            'vlrreceitatotal',
            'vlrcp',
            'vlrreceitaclubes',
            'vlrretparc', ]



class r3010evtEspDesportivoSerializer(ModelSerializer):

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
    
        model = r3010evtEspDesportivo
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


class r4010evtRetPF(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(choices=CHOICES_R4010_TPINSCESTAB, null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    cpfbenef = models.CharField(max_length=11, blank=True, null=True, )
    nmbenef = models.CharField(max_length=70, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r4010_evtretpf_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-4010 - Retenções na Fonte - Pessoa Física'
        db_table = r'r4010_evtretpf'       
        managed = True  # r4010_evtretpf #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r4010evtRetPF", u"Pode ver listagem do modelo R4010EVTRETPF"),
            ("can_see_data_r4010evtRetPF", u"Pode visualizar o conteúdo do modelo R4010EVTRETPF"),
            ("can_see_menu_r4010evtRetPF", u"Pode visualizar no menu o modelo R4010EVTRETPF"),
            ("can_print_list_r4010evtRetPF", u"Pode imprimir listagem do modelo R4010EVTRETPF"),
            ("can_print_data_r4010evtRetPF", u"Pode imprimir o conteúdo do modelo R4010EVTRETPF"),
            ("can_open_r4010evtRetPF", u"Pode abrir o evento R4010EVTRETPF para edição"),
            ("can_duplicate_r4010evtRetPF", u"Pode duplicar o evento R4010EVTRETPF"),
            ("can_validate_r4010evtRetPF", u"Pode validar o evento R4010EVTRETPF"),
            ("can_change_identity_r4010evtRetPF", u"Pode alterar identidade do evento R4010EVTRETPF"),
            ("can_see_layout_r4010evtRetPF", u"Pode ver layout do evento R4010EVTRETPF"),
            ("can_see_receipt_r4010evtRetPF", u"Pode ver recibo do evento R4010EVTRETPF"),
            ("can_see_xml_r4010evtRetPF", u"Pode ver xml do evento R4010EVTRETPF"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab', ]



class r4010evtRetPFSerializer(ModelSerializer):

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
    
        model = r4010evtRetPF
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


class r4020evtRetPJ(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4020_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4020_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4020_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    cnpjbenef = models.CharField(max_length=14, blank=True, null=True, )
    nmbenef = models.CharField(max_length=70, blank=True, null=True, )
    isenimun = models.IntegerField(choices=CHOICES_R4020_ISENIMUN, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r4020_evtretpj_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-4020 - Retenções na Fonte - Pessoa Jurídica'
        db_table = r'r4020_evtretpj'       
        managed = True  # r4020_evtretpj #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r4020evtRetPJ", u"Pode ver listagem do modelo R4020EVTRETPJ"),
            ("can_see_data_r4020evtRetPJ", u"Pode visualizar o conteúdo do modelo R4020EVTRETPJ"),
            ("can_see_menu_r4020evtRetPJ", u"Pode visualizar no menu o modelo R4020EVTRETPJ"),
            ("can_print_list_r4020evtRetPJ", u"Pode imprimir listagem do modelo R4020EVTRETPJ"),
            ("can_print_data_r4020evtRetPJ", u"Pode imprimir o conteúdo do modelo R4020EVTRETPJ"),
            ("can_open_r4020evtRetPJ", u"Pode abrir o evento R4020EVTRETPJ para edição"),
            ("can_duplicate_r4020evtRetPJ", u"Pode duplicar o evento R4020EVTRETPJ"),
            ("can_validate_r4020evtRetPJ", u"Pode validar o evento R4020EVTRETPJ"),
            ("can_change_identity_r4020evtRetPJ", u"Pode alterar identidade do evento R4020EVTRETPJ"),
            ("can_see_layout_r4020evtRetPJ", u"Pode ver layout do evento R4020EVTRETPJ"),
            ("can_see_receipt_r4020evtRetPJ", u"Pode ver recibo do evento R4020EVTRETPJ"),
            ("can_see_xml_r4020evtRetPJ", u"Pode ver xml do evento R4020EVTRETPJ"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab',
            'isenimun', ]



class r4020evtRetPJSerializer(ModelSerializer):

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
    
        model = r4020evtRetPJ
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


class r4040evtBenefNId(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4040_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4040_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4040_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpinscestab = models.IntegerField(null=True, )
    nrinscestab = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r4040_evtbenefnid_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-4040 - Retenções na Fonte - Beneficiários não identificados'
        db_table = r'r4040_evtbenefnid'       
        managed = True  # r4040_evtbenefnid #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r4040evtBenefNId", u"Pode ver listagem do modelo R4040EVTBENEFNID"),
            ("can_see_data_r4040evtBenefNId", u"Pode visualizar o conteúdo do modelo R4040EVTBENEFNID"),
            ("can_see_menu_r4040evtBenefNId", u"Pode visualizar no menu o modelo R4040EVTBENEFNID"),
            ("can_print_list_r4040evtBenefNId", u"Pode imprimir listagem do modelo R4040EVTBENEFNID"),
            ("can_print_data_r4040evtBenefNId", u"Pode imprimir o conteúdo do modelo R4040EVTBENEFNID"),
            ("can_open_r4040evtBenefNId", u"Pode abrir o evento R4040EVTBENEFNID para edição"),
            ("can_duplicate_r4040evtBenefNId", u"Pode duplicar o evento R4040EVTBENEFNID"),
            ("can_validate_r4040evtBenefNId", u"Pode validar o evento R4040EVTBENEFNID"),
            ("can_change_identity_r4040evtBenefNId", u"Pode alterar identidade do evento R4040EVTBENEFNID"),
            ("can_see_layout_r4040evtBenefNId", u"Pode ver layout do evento R4040EVTBENEFNID"),
            ("can_see_receipt_r4040evtBenefNId", u"Pode ver recibo do evento R4040EVTBENEFNID"),
            ("can_see_xml_r4040evtBenefNId", u"Pode ver xml do evento R4040EVTBENEFNID"),)
            
        ordering = [
            'identidade',
            'indretif',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpinscestab',
            'nrinscestab', ]



class r4040evtBenefNIdSerializer(ModelSerializer):

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
    
        model = r4040evtBenefNId
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


class r4098evtReab(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4098_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4098_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r4098_evtreab_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-4098 - Reabertura dos Eventos Periódicos Série R-4000'
        db_table = r'r4098_evtreab'       
        managed = True  # r4098_evtreab #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r4098evtReab", u"Pode ver listagem do modelo R4098EVTREAB"),
            ("can_see_data_r4098evtReab", u"Pode visualizar o conteúdo do modelo R4098EVTREAB"),
            ("can_see_menu_r4098evtReab", u"Pode visualizar no menu o modelo R4098EVTREAB"),
            ("can_print_list_r4098evtReab", u"Pode imprimir listagem do modelo R4098EVTREAB"),
            ("can_print_data_r4098evtReab", u"Pode imprimir o conteúdo do modelo R4098EVTREAB"),
            ("can_open_r4098evtReab", u"Pode abrir o evento R4098EVTREAB para edição"),
            ("can_duplicate_r4098evtReab", u"Pode duplicar o evento R4098EVTREAB"),
            ("can_validate_r4098evtReab", u"Pode validar o evento R4098EVTREAB"),
            ("can_change_identity_r4098evtReab", u"Pode alterar identidade do evento R4098EVTREAB"),
            ("can_see_layout_r4098evtReab", u"Pode ver layout do evento R4098EVTREAB"),
            ("can_see_receipt_r4098evtReab", u"Pode ver recibo do evento R4098EVTREAB"),
            ("can_see_xml_r4098evtReab", u"Pode ver xml do evento R4098EVTREAB"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class r4098evtReabSerializer(ModelSerializer):

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
    
        model = r4098evtReab
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


class r4099evtFech(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4099_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4099_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    evtretpf = models.CharField(choices=CHOICES_R4099_EVTRETPF, max_length=1, blank=True, null=True, )
    evtretpj = models.CharField(choices=CHOICES_R4099_EVTRETPJ, max_length=1, blank=True, null=True, )
    evtpgtosnid = models.CharField(choices=CHOICES_R4099_EVTPGTOSNID, max_length=1, blank=True, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r4099_evtfech_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-4099 - Fechamento dos Eventos Periódicos Série R-4000'
        db_table = r'r4099_evtfech'       
        managed = True  # r4099_evtfech #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r4099evtFech", u"Pode ver listagem do modelo R4099EVTFECH"),
            ("can_see_data_r4099evtFech", u"Pode visualizar o conteúdo do modelo R4099EVTFECH"),
            ("can_see_menu_r4099evtFech", u"Pode visualizar no menu o modelo R4099EVTFECH"),
            ("can_print_list_r4099evtFech", u"Pode imprimir listagem do modelo R4099EVTFECH"),
            ("can_print_data_r4099evtFech", u"Pode imprimir o conteúdo do modelo R4099EVTFECH"),
            ("can_open_r4099evtFech", u"Pode abrir o evento R4099EVTFECH para edição"),
            ("can_duplicate_r4099evtFech", u"Pode duplicar o evento R4099EVTFECH"),
            ("can_validate_r4099evtFech", u"Pode validar o evento R4099EVTFECH"),
            ("can_change_identity_r4099evtFech", u"Pode alterar identidade do evento R4099EVTFECH"),
            ("can_see_layout_r4099evtFech", u"Pode ver layout do evento R4099EVTFECH"),
            ("can_see_receipt_r4099evtFech", u"Pode ver recibo do evento R4099EVTFECH"),
            ("can_see_xml_r4099evtFech", u"Pode ver xml do evento R4099EVTFECH"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc', ]



class r4099evtFechSerializer(ModelSerializer):

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
    
        model = r4099evtFech
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


class r5001evtTotal(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.CharField(choices=CHOICES_R5001_CDRETORNO, max_length=1, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, blank=True, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r5001_evttotal_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-5001 - Informações de bases e tributos por evento'
        db_table = r'r5001_evttotal'       
        managed = True  # r5001_evttotal #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r5001evtTotal", u"Pode ver listagem do modelo R5001EVTTOTAL"),
            ("can_see_data_r5001evtTotal", u"Pode visualizar o conteúdo do modelo R5001EVTTOTAL"),
            ("can_see_menu_r5001evtTotal", u"Pode visualizar no menu o modelo R5001EVTTOTAL"),
            ("can_print_list_r5001evtTotal", u"Pode imprimir listagem do modelo R5001EVTTOTAL"),
            ("can_print_data_r5001evtTotal", u"Pode imprimir o conteúdo do modelo R5001EVTTOTAL"),
            ("can_open_r5001evtTotal", u"Pode abrir o evento R5001EVTTOTAL para edição"),
            ("can_duplicate_r5001evtTotal", u"Pode duplicar o evento R5001EVTTOTAL"),
            ("can_validate_r5001evtTotal", u"Pode validar o evento R5001EVTTOTAL"),
            ("can_change_identity_r5001evtTotal", u"Pode alterar identidade do evento R5001EVTTOTAL"),
            ("can_see_layout_r5001evtTotal", u"Pode ver layout do evento R5001EVTTOTAL"),
            ("can_see_receipt_r5001evtTotal", u"Pode ver recibo do evento R5001EVTTOTAL"),
            ("can_see_xml_r5001evtTotal", u"Pode ver xml do evento R5001EVTTOTAL"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r5001evtTotalSerializer(ModelSerializer):

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
    
        model = r5001evtTotal
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


class r5011evtTotalContrib(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.CharField(max_length=1, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-5011 - Informações de bases e tributos consolidadas por período de apuração'
        db_table = r'r5011_evttotalcontrib'       
        managed = True  # r5011_evttotalcontrib #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r5011evtTotalContrib", u"Pode ver listagem do modelo R5011EVTTOTALCONTRIB"),
            ("can_see_data_r5011evtTotalContrib", u"Pode visualizar o conteúdo do modelo R5011EVTTOTALCONTRIB"),
            ("can_see_menu_r5011evtTotalContrib", u"Pode visualizar no menu o modelo R5011EVTTOTALCONTRIB"),
            ("can_print_list_r5011evtTotalContrib", u"Pode imprimir listagem do modelo R5011EVTTOTALCONTRIB"),
            ("can_print_data_r5011evtTotalContrib", u"Pode imprimir o conteúdo do modelo R5011EVTTOTALCONTRIB"),
            ("can_open_r5011evtTotalContrib", u"Pode abrir o evento R5011EVTTOTALCONTRIB para edição"),
            ("can_duplicate_r5011evtTotalContrib", u"Pode duplicar o evento R5011EVTTOTALCONTRIB"),
            ("can_validate_r5011evtTotalContrib", u"Pode validar o evento R5011EVTTOTALCONTRIB"),
            ("can_change_identity_r5011evtTotalContrib", u"Pode alterar identidade do evento R5011EVTTOTALCONTRIB"),
            ("can_see_layout_r5011evtTotalContrib", u"Pode ver layout do evento R5011EVTTOTALCONTRIB"),
            ("can_see_receipt_r5011evtTotalContrib", u"Pode ver recibo do evento R5011EVTTOTALCONTRIB"),
            ("can_see_xml_r5011evtTotalContrib", u"Pode ver xml do evento R5011EVTTOTALCONTRIB"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'nrprotentr',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r5011evtTotalContribSerializer(ModelSerializer):

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
    
        model = r5011evtTotalContrib
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


class r9000evtExclusao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R9000_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R9000_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpevento = models.TextField(null=True, )
    nrrecevt = models.CharField(max_length=52, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r9000_evtexclusao_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-9000 - Exclusão de Eventos'
        db_table = r'r9000_evtexclusao'       
        managed = True  # r9000_evtexclusao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9000evtExclusao", u"Pode ver listagem do modelo R9000EVTEXCLUSAO"),
            ("can_see_data_r9000evtExclusao", u"Pode visualizar o conteúdo do modelo R9000EVTEXCLUSAO"),
            ("can_see_menu_r9000evtExclusao", u"Pode visualizar no menu o modelo R9000EVTEXCLUSAO"),
            ("can_print_list_r9000evtExclusao", u"Pode imprimir listagem do modelo R9000EVTEXCLUSAO"),
            ("can_print_data_r9000evtExclusao", u"Pode imprimir o conteúdo do modelo R9000EVTEXCLUSAO"),
            ("can_open_r9000evtExclusao", u"Pode abrir o evento R9000EVTEXCLUSAO para edição"),
            ("can_duplicate_r9000evtExclusao", u"Pode duplicar o evento R9000EVTEXCLUSAO"),
            ("can_validate_r9000evtExclusao", u"Pode validar o evento R9000EVTEXCLUSAO"),
            ("can_change_identity_r9000evtExclusao", u"Pode alterar identidade do evento R9000EVTEXCLUSAO"),
            ("can_see_layout_r9000evtExclusao", u"Pode ver layout do evento R9000EVTEXCLUSAO"),
            ("can_see_receipt_r9000evtExclusao", u"Pode ver recibo do evento R9000EVTEXCLUSAO"),
            ("can_see_xml_r9000evtExclusao", u"Pode ver xml do evento R9000EVTEXCLUSAO"),)
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpevento',
            'nrrecevt',
            'perapur', ]



class r9000evtExclusaoSerializer(ModelSerializer):

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
    
        model = r9000evtExclusao
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


class r9001evtTotal(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.IntegerField(choices=CHOICES_R9001_CDRETORNO, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, blank=True, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r9001_evttotal_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-9001 - Informações de bases e tributos por evento - Contrib. Previdenc.'
        db_table = r'r9001_evttotal'       
        managed = True  # r9001_evttotal #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9001evtTotal", u"Pode ver listagem do modelo R9001EVTTOTAL"),
            ("can_see_data_r9001evtTotal", u"Pode visualizar o conteúdo do modelo R9001EVTTOTAL"),
            ("can_see_menu_r9001evtTotal", u"Pode visualizar no menu o modelo R9001EVTTOTAL"),
            ("can_print_list_r9001evtTotal", u"Pode imprimir listagem do modelo R9001EVTTOTAL"),
            ("can_print_data_r9001evtTotal", u"Pode imprimir o conteúdo do modelo R9001EVTTOTAL"),
            ("can_open_r9001evtTotal", u"Pode abrir o evento R9001EVTTOTAL para edição"),
            ("can_duplicate_r9001evtTotal", u"Pode duplicar o evento R9001EVTTOTAL"),
            ("can_validate_r9001evtTotal", u"Pode validar o evento R9001EVTTOTAL"),
            ("can_change_identity_r9001evtTotal", u"Pode alterar identidade do evento R9001EVTTOTAL"),
            ("can_see_layout_r9001evtTotal", u"Pode ver layout do evento R9001EVTTOTAL"),
            ("can_see_receipt_r9001evtTotal", u"Pode ver recibo do evento R9001EVTTOTAL"),
            ("can_see_xml_r9001evtTotal", u"Pode ver xml do evento R9001EVTTOTAL"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r9001evtTotalSerializer(ModelSerializer):

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
    
        model = r9001evtTotal
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


class r9002evtRet(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perref = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.IntegerField(choices=CHOICES_R9002_CDRETORNO, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, blank=True, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r9002_evtret_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-9002 - Informações de bases e tributos por evento - Retenções na fonte'
        db_table = r'r9002_evtret'       
        managed = True  # r9002_evtret #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9002evtRet", u"Pode ver listagem do modelo R9002EVTRET"),
            ("can_see_data_r9002evtRet", u"Pode visualizar o conteúdo do modelo R9002EVTRET"),
            ("can_see_menu_r9002evtRet", u"Pode visualizar no menu o modelo R9002EVTRET"),
            ("can_print_list_r9002evtRet", u"Pode imprimir listagem do modelo R9002EVTRET"),
            ("can_print_data_r9002evtRet", u"Pode imprimir o conteúdo do modelo R9002EVTRET"),
            ("can_open_r9002evtRet", u"Pode abrir o evento R9002EVTRET para edição"),
            ("can_duplicate_r9002evtRet", u"Pode duplicar o evento R9002EVTRET"),
            ("can_validate_r9002evtRet", u"Pode validar o evento R9002EVTRET"),
            ("can_change_identity_r9002evtRet", u"Pode alterar identidade do evento R9002EVTRET"),
            ("can_see_layout_r9002evtRet", u"Pode ver layout do evento R9002EVTRET"),
            ("can_see_receipt_r9002evtRet", u"Pode ver recibo do evento R9002EVTRET"),
            ("can_see_xml_r9002evtRet", u"Pode ver xml do evento R9002EVTRET"),)
            
        ordering = [
            'identidade',
            'perref',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r9002evtRetSerializer(ModelSerializer):

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
    
        model = r9002evtRet
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


class r9011evtTotalContrib(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.IntegerField(choices=CHOICES_R9011_CDRETORNO, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r9011_evttotalcontrib_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-9011 - Informações consolidadas de bases e tributos - Contrib. Previdenciária'
        db_table = r'r9011_evttotalcontrib'       
        managed = True  # r9011_evttotalcontrib #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9011evtTotalContrib", u"Pode ver listagem do modelo R9011EVTTOTALCONTRIB"),
            ("can_see_data_r9011evtTotalContrib", u"Pode visualizar o conteúdo do modelo R9011EVTTOTALCONTRIB"),
            ("can_see_menu_r9011evtTotalContrib", u"Pode visualizar no menu o modelo R9011EVTTOTALCONTRIB"),
            ("can_print_list_r9011evtTotalContrib", u"Pode imprimir listagem do modelo R9011EVTTOTALCONTRIB"),
            ("can_print_data_r9011evtTotalContrib", u"Pode imprimir o conteúdo do modelo R9011EVTTOTALCONTRIB"),
            ("can_open_r9011evtTotalContrib", u"Pode abrir o evento R9011EVTTOTALCONTRIB para edição"),
            ("can_duplicate_r9011evtTotalContrib", u"Pode duplicar o evento R9011EVTTOTALCONTRIB"),
            ("can_validate_r9011evtTotalContrib", u"Pode validar o evento R9011EVTTOTALCONTRIB"),
            ("can_change_identity_r9011evtTotalContrib", u"Pode alterar identidade do evento R9011EVTTOTALCONTRIB"),
            ("can_see_layout_r9011evtTotalContrib", u"Pode ver layout do evento R9011EVTTOTALCONTRIB"),
            ("can_see_receipt_r9011evtTotalContrib", u"Pode ver recibo do evento R9011EVTTOTALCONTRIB"),
            ("can_see_xml_r9011evtTotalContrib", u"Pode ver xml do evento R9011EVTTOTALCONTRIB"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'nrprotentr',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r9011evtTotalContribSerializer(ModelSerializer):

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
    
        model = r9011evtTotalContrib
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


class r9012evtRetCons(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    cdretorno = models.IntegerField(choices=CHOICES_R9012_CDRETORNO, null=True, )
    descretorno = models.CharField(max_length=1000, null=True, )
    nrprotentr = models.CharField(max_length=49, null=True, )
    dhprocess = models.DateField(null=True, )
    tpev = models.CharField(max_length=6, null=True, )
    idev = models.CharField(max_length=36, null=True, )
    hash = models.CharField(max_length=60, null=True, )
    versao = models.CharField(choices=EFDREINF_VERSOES, max_length=20, blank=True, default='v1_04_00', )
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True, )
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True, )
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True, )
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True, )
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True, )
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True, )
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True, )
    ocorrencias = models.TextField(blank=True, null=True, )
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )
    arquivo_original = models.IntegerField(choices=SIM_NAO, blank=True, null=True, default=0, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    status = models.IntegerField(choices=EVENTO_STATUS, blank=True, default=0, )
    cdretorno = models.CharField(max_length=6, blank=True, null=True, )
    descretorno = models.CharField(max_length=255, blank=True, null=True, )
    dhprocess = models.DateTimeField(blank=True, null=True, )
    
    def __unicode__(self):
        
        return unicode(self.identidade)

    def evento(self): 
    
        return self.__dict__
        
    def validar(self, request):
    
        from emensageriapro.efdreinf.views.r9012_evtretcons_validar_evento import validar_evento_funcao
        validar_evento_funcao(request, self.id)
        
    class Meta:
    
        # verbose_name = u'R-9012 - Informações consolidadas de bases e tributos - Retenções na fonte'
        db_table = r'r9012_evtretcons'       
        managed = True  # r9012_evtretcons #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r9012evtRetCons", u"Pode ver listagem do modelo R9012EVTRETCONS"),
            ("can_see_data_r9012evtRetCons", u"Pode visualizar o conteúdo do modelo R9012EVTRETCONS"),
            ("can_see_menu_r9012evtRetCons", u"Pode visualizar no menu o modelo R9012EVTRETCONS"),
            ("can_print_list_r9012evtRetCons", u"Pode imprimir listagem do modelo R9012EVTRETCONS"),
            ("can_print_data_r9012evtRetCons", u"Pode imprimir o conteúdo do modelo R9012EVTRETCONS"),
            ("can_open_r9012evtRetCons", u"Pode abrir o evento R9012EVTRETCONS para edição"),
            ("can_duplicate_r9012evtRetCons", u"Pode duplicar o evento R9012EVTRETCONS"),
            ("can_validate_r9012evtRetCons", u"Pode validar o evento R9012EVTRETCONS"),
            ("can_change_identity_r9012evtRetCons", u"Pode alterar identidade do evento R9012EVTRETCONS"),
            ("can_see_layout_r9012evtRetCons", u"Pode ver layout do evento R9012EVTRETCONS"),
            ("can_see_receipt_r9012evtRetCons", u"Pode ver recibo do evento R9012EVTRETCONS"),
            ("can_see_xml_r9012evtRetCons", u"Pode ver xml do evento R9012EVTRETCONS"),)
            
        ordering = [
            'identidade',
            'perapur',
            'tpinsc',
            'nrinsc',
            'cdretorno',
            'descretorno',
            'nrprotentr',
            'dhprocess',
            'tpev',
            'idev',
            'hash', ]



class r9012evtRetConsSerializer(ModelSerializer):

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
    
        model = r9012evtRetCons
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