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
    tpinsc = models.IntegerField(choices=CHOICES_R1000_TPINSC, null=True, )
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
    operacao = models.IntegerField(choices=OPERACOES, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r1000_evtinfocontri_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-1000 - Informações do Contribuinte'
        db_table = r'r1000_evtinfocontri'       
        managed = True  # r1000_evtinfocontri #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_evtinfocontri", "Can view r1000_evtinfocontri"), )
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',]



class r1000evtInfoContriSerializer(ModelSerializer):

    class Meta:
    
        model = r1000evtInfoContri
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070evtTabProcesso(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R1070_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R1070_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R1070_TPINSC, null=True, )
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
    operacao = models.IntegerField(choices=OPERACOES, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r1070_evttabprocesso_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-1070 - Tabela de Processos Administrativos/Judiciais'
        db_table = r'r1070_evttabprocesso'       
        managed = True  # r1070_evttabprocesso #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_evttabprocesso", "Can view r1070_evttabprocesso"), )
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',]



class r1070evtTabProcessoSerializer(ModelSerializer):

    class Meta:
    
        model = r1070evtTabProcesso
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2010evtServTom(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2010_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),
            unicode(self.indobra),
            unicode(self.cnpjprestador),
            unicode(self.vlrtotalbruto),
            unicode(self.vlrtotalbaseret),
            unicode(self.vlrtotalretprinc),
            unicode(self.indcprb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2010_evtservtom_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2010 - Retenção Contribuição Previdenciária - Serviços Tomados'
        db_table = r'r2010_evtservtom'       
        managed = True  # r2010_evtservtom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2010_evtservtom", "Can view r2010_evtservtom"), )
            
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
            'indcprb',]



class r2010evtServTomSerializer(ModelSerializer):

    class Meta:
    
        model = r2010evtServTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2020evtServPrest(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2020_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2020_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2020_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2020_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestabprest),
            unicode(self.nrinscestabprest),
            unicode(self.tpinsctomador),
            unicode(self.nrinsctomador),
            unicode(self.indobra),
            unicode(self.vlrtotalbruto),
            unicode(self.vlrtotalbaseret),
            unicode(self.vlrtotalretprinc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2020_evtservprest_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2020 - Retenção Contribuição Previdenciária - Serviços Prestados'
        db_table = r'r2020_evtservprest'       
        managed = True  # r2020_evtservprest #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2020_evtservprest", "Can view r2020_evtservprest"), )
            
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
            'vlrtotalretprinc',]



class r2020evtServPrestSerializer(ModelSerializer):

    class Meta:
    
        model = r2020evtServPrest
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2030evtAssocDespRec(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2030_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2030_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2030_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2030_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2030_evtassocdesprec_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2030 - Recursos Recebidos por Associação Desportiva'
        db_table = r'r2030_evtassocdesprec'       
        managed = True  # r2030_evtassocdesprec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2030_evtassocdesprec", "Can view r2030_evtassocdesprec"), )
            
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
            'nrinscestab',]



class r2030evtAssocDespRecSerializer(ModelSerializer):

    class Meta:
    
        model = r2030evtAssocDespRec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2040evtAssocDespRep(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2040_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2040_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2040_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2040_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2040_evtassocdesprep_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2040 - Recursos Repassados para Associação Desportiva'
        db_table = r'r2040_evtassocdesprep'       
        managed = True  # r2040_evtassocdesprep #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2040_evtassocdesprep", "Can view r2040_evtassocdesprep"), )
            
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
            'nrinscestab',]



class r2040evtAssocDespRepSerializer(ModelSerializer):

    class Meta:
    
        model = r2040evtAssocDespRep
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2050evtComProd(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2050_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2050_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2050_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2050_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),
            unicode(self.vlrrecbrutatotal),
            unicode(self.vlrcpapur),
            unicode(self.vlrratapur),
            unicode(self.vlrsenarapur),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2050_evtcomprod_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2050 - Comercialização da Produção por Produtor Rural PJ/Agroindústria'
        db_table = r'r2050_evtcomprod'       
        managed = True  # r2050_evtcomprod #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2050_evtcomprod", "Can view r2050_evtcomprod"), )
            
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
            'vlrsenarapur',]



class r2050evtComProdSerializer(ModelSerializer):

    class Meta:
    
        model = r2050evtComProd
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2060evtCPRB(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2060_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2060_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2060_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2060_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),
            unicode(self.vlrrecbrutatotal),
            unicode(self.vlrcpapurtotal),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2060_evtcprb_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2060 - Contribuição Previdenciária sobre a Receita Bruta - CPRB'
        db_table = r'r2060_evtcprb'       
        managed = True  # r2060_evtcprb #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2060_evtcprb", "Can view r2060_evtcprb"), )
            
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
            'vlrcpapurtotal',]



class r2060evtCPRBSerializer(ModelSerializer):

    class Meta:
    
        model = r2060evtCPRB
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2070evtPgtosDivs(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R2070_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2070_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2070_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2070_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.codpgto),
            unicode(self.nmrazaobenef),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2070_evtpgtosdivs_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2070 - Retenções na Fonte - IR, CSLL, Cofins, PIS/PASEP'
        db_table = r'r2070_evtpgtosdivs'       
        managed = True  # r2070_evtpgtosdivs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2070_evtpgtosdivs", "Can view r2070_evtpgtosdivs"), )
            
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
            'nmrazaobenef',]



class r2070evtPgtosDivsSerializer(ModelSerializer):

    class Meta:
    
        model = r2070evtPgtosDivs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2098evtReabreEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2098_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2098_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2098_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2098_evtreabreevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2098 - Reabertura dos Eventos Periódicos'
        db_table = r'r2098_evtreabreevper'       
        managed = True  # r2098_evtreabreevper #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2098_evtreabreevper", "Can view r2098_evtreabreevper"), )
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',]



class r2098evtReabreEvPerSerializer(ModelSerializer):

    class Meta:
    
        model = r2098evtReabreEvPer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2099evtFechaEvPer(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R2099_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R2099_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R2099_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.evtservtm),
            unicode(self.evtservpr),
            unicode(self.evtassdesprec),
            unicode(self.evtassdesprep),
            unicode(self.evtcomprod),
            unicode(self.evtcprb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r2099_evtfechaevper_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-2099 - Fechamento dos Eventos Periódicos'
        db_table = r'r2099_evtfechaevper'       
        managed = True  # r2099_evtfechaevper #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2099_evtfechaevper", "Can view r2099_evtfechaevper"), )
            
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
            'evtcprb',]



class r2099evtFechaEvPerSerializer(ModelSerializer):

    class Meta:
    
        model = r2099evtFechaEvPer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r3010evtEspDesportivo(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R3010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    dtapuracao = models.DateField(null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R3010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R3010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R3010_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.dtapuracao),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),
            unicode(self.vlrreceitatotal),
            unicode(self.vlrcp),
            unicode(self.vlrreceitaclubes),
            unicode(self.vlrretparc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r3010_evtespdesportivo_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-3010 - Receita de Espetáculo Desportivo'
        db_table = r'r3010_evtespdesportivo'       
        managed = True  # r3010_evtespdesportivo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r3010_evtespdesportivo", "Can view r3010_evtespdesportivo"), )
            
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
            'vlrretparc',]



class r3010evtEspDesportivoSerializer(ModelSerializer):

    class Meta:
    
        model = r3010evtEspDesportivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010evtRetPF(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4010_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4010_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4010_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R4010_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r4010_evtretpf_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-4010 - Retenções na Fonte - Pessoa Física'
        db_table = r'r4010_evtretpf'       
        managed = True  # r4010_evtretpf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_evtretpf", "Can view r4010_evtretpf"), )
            
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
            'nrinscestab',]



class r4010evtRetPFSerializer(ModelSerializer):

    class Meta:
    
        model = r4010evtRetPF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020evtRetPJ(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4020_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4020_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4020_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R4020_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),
            unicode(self.isenimun),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r4020_evtretpj_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-4020 - Retenções na Fonte - Pessoa Jurídica'
        db_table = r'r4020_evtretpj'       
        managed = True  # r4020_evtretpj #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_evtretpj", "Can view r4020_evtretpj"), )
            
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
            'isenimun',]



class r4020evtRetPJSerializer(ModelSerializer):

    class Meta:
    
        model = r4020evtRetPJ
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4040evtBenefNId(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    indretif = models.IntegerField(choices=CHOICES_R4040_INDRETIF, null=True, )
    nrrecibo = models.CharField(max_length=52, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4040_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4040_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R4040_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.indretif),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpinscestab),
            unicode(self.nrinscestab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r4040_evtbenefnid_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-4040 - Retenções na Fonte - Beneficiários não identificados'
        db_table = r'r4040_evtbenefnid'       
        managed = True  # r4040_evtbenefnid #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4040_evtbenefnid", "Can view r4040_evtbenefnid"), )
            
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
            'nrinscestab',]



class r4040evtBenefNIdSerializer(ModelSerializer):

    class Meta:
    
        model = r4040evtBenefNId
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4098evtReab(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4098_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4098_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R4098_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r4098_evtreab_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-4098 - Reabertura dos Eventos Periódicos Série R-4000'
        db_table = r'r4098_evtreab'       
        managed = True  # r4098_evtreab #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4098_evtreab", "Can view r4098_evtreab"), )
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',]



class r4098evtReabSerializer(ModelSerializer):

    class Meta:
    
        model = r4098evtReab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4099evtFech(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R4099_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R4099_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R4099_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r4099_evtfech_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-4099 - Fechamento dos Eventos Periódicos Série R-4000'
        db_table = r'r4099_evtfech'       
        managed = True  # r4099_evtfech #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4099_evtfech", "Can view r4099_evtfech"), )
            
        ordering = [
            'identidade',
            'perapur',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',]



class r4099evtFechSerializer(ModelSerializer):

    class Meta:
    
        model = r4099evtFech
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r5001evtTotal(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R5001_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r5001_evttotal_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-5001 - Informações de bases e tributos por evento'
        db_table = r'r5001_evttotal'       
        managed = True  # r5001_evttotal #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r5001_evttotal", "Can view r5001_evttotal"), )
            
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
            'hash',]



class r5001evtTotalSerializer(ModelSerializer):

    class Meta:
    
        model = r5001evtTotal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r5011evtTotalContrib(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R5011_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.nrprotentr),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r5011_evttotalcontrib_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-5011 - Informações de bases e tributos consolidadas por período de apuração'
        db_table = r'r5011_evttotalcontrib'       
        managed = True  # r5011_evttotalcontrib #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r5011_evttotalcontrib", "Can view r5011_evttotalcontrib"), )
            
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
            'hash',]



class r5011evtTotalContribSerializer(ModelSerializer):

    class Meta:
    
        model = r5011evtTotalContrib
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9000evtExclusao(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    tpamb = models.IntegerField(choices=CHOICES_R9000_TPAMB, null=True, )
    procemi = models.IntegerField(choices=CHOICES_R9000_PROCEMI, null=True, default=1, )
    verproc = models.CharField(max_length=20, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R9000_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    tpevento = models.CharField(choices=CHOICES_R9000_TPEVENTO, max_length=6, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.tpamb),
            unicode(self.procemi),
            unicode(self.verproc),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.tpevento),
            unicode(self.nrrecevt),
            unicode(self.perapur),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r9000_evtexclusao_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-9000 - Exclusão de Eventos'
        db_table = r'r9000_evtexclusao'       
        managed = True  # r9000_evtexclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9000_evtexclusao", "Can view r9000_evtexclusao"), )
            
        ordering = [
            'identidade',
            'tpamb',
            'procemi',
            'verproc',
            'tpinsc',
            'nrinsc',
            'tpevento',
            'nrrecevt',
            'perapur',]



class r9000evtExclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r9000evtExclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9001evtTotal(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R9001_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r9001_evttotal_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-9001 - Informações de bases e tributos por evento - Contrib. Previdenc.'
        db_table = r'r9001_evttotal'       
        managed = True  # r9001_evttotal #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9001_evttotal", "Can view r9001_evttotal"), )
            
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
            'hash',]



class r9001evtTotalSerializer(ModelSerializer):

    class Meta:
    
        model = r9001evtTotal
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9002evtRet(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perref = models.CharField(max_length=7, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R9002_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perref),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r9002_evtret_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-9002 - Informações de bases e tributos por evento - Retenções na fonte'
        db_table = r'r9002_evtret'       
        managed = True  # r9002_evtret #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9002_evtret", "Can view r9002_evtret"), )
            
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
            'hash',]



class r9002evtRetSerializer(ModelSerializer):

    class Meta:
    
        model = r9002evtRet
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011evtTotalContrib(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R9011_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.nrprotentr),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r9011_evttotalcontrib_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-9011 - Informações consolidadas de bases e tributos - Contrib. Previdenciária'
        db_table = r'r9011_evttotalcontrib'       
        managed = True  # r9011_evttotalcontrib #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_evttotalcontrib", "Can view r9011_evttotalcontrib"), )
            
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
            'hash',]



class r9011evtTotalContribSerializer(ModelSerializer):

    class Meta:
    
        model = r9011evtTotalContrib
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9012evtRetCons(SoftDeletionModel):

    identidade = models.CharField(max_length=36, blank=True, null=True, )
    perapur = models.CharField(max_length=10, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_R9012_TPINSC, null=True, )
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.identidade),
            unicode(self.perapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.cdretorno),
            unicode(self.descretorno),
            unicode(self.nrprotentr),
            unicode(self.dhprocess),
            unicode(self.tpev),
            unicode(self.idev),
            unicode(self.hash),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    def evento(self): 
    
        return self.__dict__
        
    def validar(self):
    
        from emensageriapro.efdreinf.views.r9012_evtretcons_validar_evento import validar_evento_funcao
        validar_evento_funcao(self.id)
        
    class Meta:
    
        # verbose_name = u'R-9012 - Informações consolidadas de bases e tributos - Retenções na fonte'
        db_table = r'r9012_evtretcons'       
        managed = True  # r9012_evtretcons #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9012_evtretcons", "Can view r9012_evtretcons"), )
            
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
            'hash',]



class r9012evtRetConsSerializer(ModelSerializer):

    class Meta:
    
        model = r9012evtRetCons
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()