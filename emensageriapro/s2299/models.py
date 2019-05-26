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
from emensageriapro.s2299.choices import *
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





class s2299dmDev(SoftDeletionModel):

    s2299_verbasresc = models.ForeignKey('s2299.s2299verbasResc', 
        related_name='%(class)s_s2299_verbasresc', )
    
    def evento(self): 
        return self.s2299_verbasresc.evento()
    idedmdev = models.CharField(max_length=30, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_verbasresc),
            unicode(self.idedmdev),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação de cada um dos demonstrativos de valores devidos ao trabalhador antes das retenções de pensão alimentícia e IRRF'
        db_table = r's2299_dmdev'       
        managed = True # s2299_dmdev #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_dmdev", "Can view s2299_dmdev"), )
            
        ordering = [
            's2299_verbasresc',
            'idedmdev',]



class s2299dmDevSerializer(ModelSerializer):

    class Meta:
    
        model = s2299dmDev
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAnt(SoftDeletionModel):

    s2299_dmdev = models.ForeignKey('s2299.s2299dmDev', 
        related_name='%(class)s_s2299_dmdev', )
    
    def evento(self): 
        return self.s2299_dmdev.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_dmdev),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro destinado ao registro de: a) remuneração relativa a diferenças salariais provenientes de acordos coletivos, convenção coletiva e dissídio; b) remuneração relativa a diferenças de vencimento provenientes de disposições legais (órgãos públicos); c) bases de cálculo para efeitos de apuração de FGTS resultantes de conversão de licença saúde em acidente de trabalho. d) verbas de natureza salarial ou não salarial devidas após o desligamento'
        db_table = r's2299_infoperant'       
        managed = True # s2299_infoperant #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant", "Can view s2299_infoperant"), )
            
        ordering = [
            's2299_dmdev',]



class s2299infoPerAntSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAnt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntdetVerbas(SoftDeletionModel):

    s2299_infoperant_ideestablot = models.ForeignKey('s2299.s2299infoPerAntideEstabLot', 
        related_name='%(class)s_s2299_infoperant_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperant_ideestablot.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant_ideestablot),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das verbas rescisórias devidas ao trabalhador'
        db_table = r's2299_infoperant_detverbas'       
        managed = True # s2299_infoperant_detverbas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_detverbas", "Can view s2299_infoperant_detverbas"), )
            
        ordering = [
            's2299_infoperant_ideestablot',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s2299infoPerAntdetVerbasSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntdetVerbas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntideADC(SoftDeletionModel):

    s2299_infoperant = models.ForeignKey('s2299.s2299infoPerAnt', 
        related_name='%(class)s_s2299_infoperant', )
    
    def evento(self): 
        return self.s2299_infoperant.evento()
    dtacconv = models.DateField(null=True, )
    tpacconv = models.CharField(choices=CHOICES_S2299_TPACCONV_INFOPERANT, max_length=1, null=True, )
    compacconv = models.CharField(max_length=7, blank=True, null=True, )
    dtefacconv = models.DateField(null=True, )
    dsc = models.CharField(max_length=255, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant),
            unicode(self.dtacconv),
            unicode(self.tpacconv),
            unicode(self.dtefacconv),
            unicode(self.dsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do Instrumento ou situação ensejadora da remuneração relativa a Períodos de Apuração Anteriores.'
        db_table = r's2299_infoperant_ideadc'       
        managed = True # s2299_infoperant_ideadc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_ideadc", "Can view s2299_infoperant_ideadc"), )
            
        ordering = [
            's2299_infoperant',
            'dtacconv',
            'tpacconv',
            'dtefacconv',
            'dsc',]



class s2299infoPerAntideADCSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntideADC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntideEstabLot(SoftDeletionModel):

    s2299_infoperant_ideperiodo = models.ForeignKey('s2299.s2299infoPerAntidePeriodo', 
        related_name='%(class)s_s2299_infoperant_ideperiodo', )
    
    def evento(self): 
        return self.s2299_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_TPINSC_INFOPERANT, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant_ideperiodo),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.codlotacao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's2299_infoperant_ideestablot'       
        managed = True # s2299_infoperant_ideestablot #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_ideestablot", "Can view s2299_infoperant_ideestablot"), )
            
        ordering = [
            's2299_infoperant_ideperiodo',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s2299infoPerAntideEstabLotSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntidePeriodo(SoftDeletionModel):

    s2299_infoperant_ideadc = models.ForeignKey('s2299.s2299infoPerAntideADC', 
        related_name='%(class)s_s2299_infoperant_ideadc', )
    
    def evento(self): 
        return self.s2299_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant_ideadc),
            unicode(self.perref),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Período de validade das informações incluídas'
        db_table = r's2299_infoperant_ideperiodo'       
        managed = True # s2299_infoperant_ideperiodo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_ideperiodo", "Can view s2299_infoperant_ideperiodo"), )
            
        ordering = [
            's2299_infoperant_ideadc',
            'perref',]



class s2299infoPerAntidePeriodoSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntidePeriodo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntinfoAgNocivo(SoftDeletionModel):

    s2299_infoperant_ideestablot = models.ForeignKey('s2299.s2299infoPerAntideEstabLot', 
        related_name='%(class)s_s2299_infoperant_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperant_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_GRAUEXP_INFOPERANT, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant_ideestablot),
            unicode(self.grauexp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a cooperativa de trabalho que presta serviço a empresa [731, 734], permitindo o detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial.'
        db_table = r's2299_infoperant_infoagnocivo'       
        managed = True # s2299_infoperant_infoagnocivo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_infoagnocivo", "Can view s2299_infoperant_infoagnocivo"), )
            
        ordering = [
            's2299_infoperant_ideestablot',
            'grauexp',]



class s2299infoPerAntinfoAgNocivoSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntinfoAgNocivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerAntinfoSimples(SoftDeletionModel):

    s2299_infoperant_ideestablot = models.ForeignKey('s2299.s2299infoPerAntideEstabLot', 
        related_name='%(class)s_s2299_infoperant_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperant_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INDSIMPLES_INFOPERANT, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperant_ideestablot),
            unicode(self.indsimples),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação relativa a empresas enquadradas no Regime de Tributação Simples'
        db_table = r's2299_infoperant_infosimples'       
        managed = True # s2299_infoperant_infosimples #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperant_infosimples", "Can view s2299_infoperant_infosimples"), )
            
        ordering = [
            's2299_infoperant_ideestablot',
            'indsimples',]



class s2299infoPerAntinfoSimplesSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerAntinfoSimples
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApur(SoftDeletionModel):

    s2299_dmdev = models.ForeignKey('s2299.s2299dmDev', 
        related_name='%(class)s_s2299_dmdev', )
    
    def evento(self): 
        return self.s2299_dmdev.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_dmdev),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Remuneração no período de apuração'
        db_table = r's2299_infoperapur'       
        managed = True # s2299_infoperapur #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur", "Can view s2299_infoperapur"), )
            
        ordering = [
            's2299_dmdev',]



class s2299infoPerApurSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApur
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurdetOper(SoftDeletionModel):

    s2299_infoperapur_infosaudecolet = models.ForeignKey('s2299.s2299infoPerApurinfoSaudeColet', 
        related_name='%(class)s_s2299_infoperapur_infosaudecolet', )
    
    def evento(self): 
        return self.s2299_infoperapur_infosaudecolet.evento()
    cnpjoper = models.CharField(max_length=14, null=True, )
    regans = models.CharField(max_length=6, null=True, )
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_infosaudecolet),
            unicode(self.cnpjoper),
            unicode(self.regans),
            unicode(self.vrpgtit),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos valores pagos a Operadoras de Planos de Saúde.'
        db_table = r's2299_infoperapur_detoper'       
        managed = True # s2299_infoperapur_detoper #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_detoper", "Can view s2299_infoperapur_detoper"), )
            
        ordering = [
            's2299_infoperapur_infosaudecolet',
            'cnpjoper',
            'regans',
            'vrpgtit',]



class s2299infoPerApurdetOperSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurdetOper
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurdetPlano(SoftDeletionModel):

    s2299_infoperapur_detoper = models.ForeignKey('s2299.s2299infoPerApurdetOper', 
        related_name='%(class)s_s2299_infoperapur_detoper', )
    
    def evento(self): 
        return self.s2299_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S2299_TPDEP_INFOPERAPUR, max_length=2, null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_detoper),
            unicode(self.tpdep),
            unicode(self.nmdep),
            unicode(self.dtnascto),
            unicode(self.vlrpgdep),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do dependente do plano privado de saúde.'
        db_table = r's2299_infoperapur_detplano'       
        managed = True # s2299_infoperapur_detplano #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_detplano", "Can view s2299_infoperapur_detplano"), )
            
        ordering = [
            's2299_infoperapur_detoper',
            'tpdep',
            'nmdep',
            'dtnascto',
            'vlrpgdep',]



class s2299infoPerApurdetPlanoSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurdetPlano
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurdetVerbas(SoftDeletionModel):

    s2299_infoperapur_ideestablot = models.ForeignKey('s2299.s2299infoPerApurideEstabLot', 
        related_name='%(class)s_s2299_infoperapur_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperapur_ideestablot.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_ideestablot),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.vrrubr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das verbas rescisórias devidas ao trabalhador'
        db_table = r's2299_infoperapur_detverbas'       
        managed = True # s2299_infoperapur_detverbas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_detverbas", "Can view s2299_infoperapur_detverbas"), )
            
        ordering = [
            's2299_infoperapur_ideestablot',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s2299infoPerApurdetVerbasSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurdetVerbas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurideEstabLot(SoftDeletionModel):

    s2299_infoperapur = models.ForeignKey('s2299.s2299infoPerApur', 
        related_name='%(class)s_s2299_infoperapur', )
    
    def evento(self): 
        return self.s2299_infoperapur.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_TPINSC_INFOPERAPUR, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.codlotacao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's2299_infoperapur_ideestablot'       
        managed = True # s2299_infoperapur_ideestablot #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_ideestablot", "Can view s2299_infoperapur_ideestablot"), )
            
        ordering = [
            's2299_infoperapur',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s2299infoPerApurideEstabLotSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurinfoAgNocivo(SoftDeletionModel):

    s2299_infoperapur_ideestablot = models.ForeignKey('s2299.s2299infoPerApurideEstabLot', 
        related_name='%(class)s_s2299_infoperapur_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperapur_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_GRAUEXP_INFOPERAPUR, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_ideestablot),
            unicode(self.grauexp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a cooperativa de trabalho que presta serviço a empresa [731, 734], permitindo o detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial.'
        db_table = r's2299_infoperapur_infoagnocivo'       
        managed = True # s2299_infoperapur_infoagnocivo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_infoagnocivo", "Can view s2299_infoperapur_infoagnocivo"), )
            
        ordering = [
            's2299_infoperapur_ideestablot',
            'grauexp',]



class s2299infoPerApurinfoAgNocivoSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurinfoAgNocivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurinfoSaudeColet(SoftDeletionModel):

    s2299_infoperapur_ideestablot = models.ForeignKey('s2299.s2299infoPerApurideEstabLot', 
        related_name='%(class)s_s2299_infoperapur_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperapur_ideestablot.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_ideestablot),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de plano privado coletivo empresarial de assistência à saúde'
        db_table = r's2299_infoperapur_infosaudecolet'       
        managed = True # s2299_infoperapur_infosaudecolet #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_infosaudecolet", "Can view s2299_infoperapur_infosaudecolet"), )
            
        ordering = [
            's2299_infoperapur_ideestablot',]



class s2299infoPerApurinfoSaudeColetSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurinfoSaudeColet
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoPerApurinfoSimples(SoftDeletionModel):

    s2299_infoperapur_ideestablot = models.ForeignKey('s2299.s2299infoPerApurideEstabLot', 
        related_name='%(class)s_s2299_infoperapur_ideestablot', )
    
    def evento(self): 
        return self.s2299_infoperapur_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INDSIMPLES_INFOPERAPUR, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infoperapur_ideestablot),
            unicode(self.indsimples),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação relativa a empresas enquadradas no Regime de Tributação Simples'
        db_table = r's2299_infoperapur_infosimples'       
        managed = True # s2299_infoperapur_infosimples #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infoperapur_infosimples", "Can view s2299_infoperapur_infosimples"), )
            
        ordering = [
            's2299_infoperapur_ideestablot',
            'indsimples',]



class s2299infoPerApurinfoSimplesSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoPerApurinfoSimples
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabInterm(SoftDeletionModel):

    s2299_dmdev = models.ForeignKey('s2299.s2299dmDev', 
        related_name='%(class)s_s2299_dmdev', )
    
    def evento(self): 
        return self.s2299_dmdev.evento()
    codconv = models.CharField(max_length=30, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_dmdev),
            unicode(self.codconv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da(s) convocação(ões) de trabalho intermitente'
        db_table = r's2299_infotrabinterm'       
        managed = True # s2299_infotrabinterm #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm", "Can view s2299_infotrabinterm"), )
            
        ordering = [
            's2299_dmdev',
            'codconv',]



class s2299infoTrabIntermSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabInterm
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabIntermconsigFGTS(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    insconsig = models.CharField(max_length=5, null=True, )
    nrcontr = models.CharField(max_length=40, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.insconsig),
            unicode(self.nrcontr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre operação de crédito consignado com garantia de FGTS'
        db_table = r's2299_infotrabinterm_consigfgts'       
        managed = True # s2299_infotrabinterm_consigfgts #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_consigfgts", "Can view s2299_infotrabinterm_consigfgts"), )
            
        ordering = [
            's2299_evtdeslig',
            'insconsig',
            'nrcontr',]



class s2299infoTrabIntermconsigFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabIntermconsigFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabInterminfoMV(SoftDeletionModel):

    s2299_verbasresc = models.ForeignKey('s2299.s2299verbasResc', 
        related_name='%(class)s_s2299_verbasresc', )
    
    def evento(self): 
        return self.s2299_verbasresc.evento()
    indmv = models.IntegerField(choices=CHOICES_S2299_INDMV_INFOTRABINTERM, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_verbasresc),
            unicode(self.indmv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em caso de trabalhador que possua outros vínculos/atividades para definição do limite do salário-de-contribuição e da alíquota a ser aplicada no desconto da contribuição previdenciária.'
        db_table = r's2299_infotrabinterm_infomv'       
        managed = True # s2299_infotrabinterm_infomv #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_infomv", "Can view s2299_infotrabinterm_infomv"), )
            
        ordering = [
            's2299_verbasresc',
            'indmv',]



class s2299infoTrabInterminfoMVSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabInterminfoMV
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabIntermprocCS(SoftDeletionModel):

    s2299_verbasresc = models.ForeignKey('s2299.s2299verbasResc', 
        related_name='%(class)s_s2299_verbasresc', )
    
    def evento(self): 
        return self.s2299_verbasresc.evento()
    nrprocjud = models.CharField(max_length=20, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_verbasresc),
            unicode(self.nrprocjud),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação sobre processo judicial que suspende a exigibilidade da Contribuição Social Rescisória'
        db_table = r's2299_infotrabinterm_proccs'       
        managed = True # s2299_infotrabinterm_proccs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_proccs", "Can view s2299_infotrabinterm_proccs"), )
            
        ordering = [
            's2299_verbasresc',
            'nrprocjud',]



class s2299infoTrabIntermprocCSSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabIntermprocCS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabIntermprocJudTrab(SoftDeletionModel):

    s2299_verbasresc = models.ForeignKey('s2299.s2299verbasResc', 
        related_name='%(class)s_s2299_verbasresc', )
    
    def evento(self): 
        return self.s2299_verbasresc.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2299_TPTRIB_INFOTRABINTERM, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_verbasresc),
            unicode(self.tptrib),
            unicode(self.nrprocjud),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's2299_infotrabinterm_procjudtrab'       
        managed = True # s2299_infotrabinterm_procjudtrab #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_procjudtrab", "Can view s2299_infotrabinterm_procjudtrab"), )
            
        ordering = [
            's2299_verbasresc',
            'tptrib',
            'nrprocjud',]



class s2299infoTrabIntermprocJudTrabSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabIntermprocJudTrab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabIntermquarentena(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    dtfimquar = models.DateField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.dtfimquar),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a 'quarentena' remunerada de trabalhador desligado'
        db_table = r's2299_infotrabinterm_quarentena'       
        managed = True # s2299_infotrabinterm_quarentena #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_quarentena", "Can view s2299_infotrabinterm_quarentena"), )
            
        ordering = [
            's2299_evtdeslig',
            'dtfimquar',]



class s2299infoTrabIntermquarentenaSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabIntermquarentena
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299infoTrabIntermremunOutrEmpr(SoftDeletionModel):

    s2299_infotrabinterm_infomv = models.ForeignKey('s2299.s2299infoTrabInterminfoMV', 
        related_name='%(class)s_s2299_infotrabinterm_infomv', )
    
    def evento(self): 
        return self.s2299_infotrabinterm_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_TPINSC_INFOTRABINTERM, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codcateg = models.TextField(null=True, )
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_infotrabinterm_infomv),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.codcateg),
            unicode(self.vlrremunoe),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao trabalhador que possui vínculo empregatício com outra(s) empresa(s) e/ou que exerce outras atividades como contribuinte individual, detalhando as empresas que efetuaram (ou efetuarão) desconto da contribuição, ou ainda valores recolhidos pelo próprio trabalhador como contribuinte individual'
        db_table = r's2299_infotrabinterm_remunoutrempr'       
        managed = True # s2299_infotrabinterm_remunoutrempr #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_infotrabinterm_remunoutrempr", "Can view s2299_infotrabinterm_remunoutrempr"), )
            
        ordering = [
            's2299_infotrabinterm_infomv',
            'tpinsc',
            'nrinsc',
            'codcateg',
            'vlrremunoe',]



class s2299infoTrabIntermremunOutrEmprSerializer(ModelSerializer):

    class Meta:
    
        model = s2299infoTrabIntermremunOutrEmpr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299mudancaCPF(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    novocpf = models.CharField(max_length=11, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.novocpf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de mudança de CPF do trabalhador.'
        db_table = r's2299_mudancacpf'       
        managed = True # s2299_mudancacpf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_mudancacpf", "Can view s2299_mudancacpf"), )
            
        ordering = [
            's2299_evtdeslig',
            'novocpf',]



class s2299mudancaCPFSerializer(ModelSerializer):

    class Meta:
    
        model = s2299mudancaCPF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299observacoes(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    observacao = models.CharField(max_length=255, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.observacao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Observações do contrato de trabalho'
        db_table = r's2299_observacoes'       
        managed = True # s2299_observacoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_observacoes", "Can view s2299_observacoes"), )
            
        ordering = [
            's2299_evtdeslig',
            'observacao',]



class s2299observacoesSerializer(ModelSerializer):

    class Meta:
    
        model = s2299observacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299sucessaoVinc(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    tpinscsuc = models.IntegerField(choices=CHOICES_S2299_TPINSCSUC, null=True, )
    cnpjsucessora = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.tpinscsuc),
            unicode(self.cnpjsucessora),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Grupo de informações da sucessão de vínculo trabalhista/estatutário'
        db_table = r's2299_sucessaovinc'       
        managed = True # s2299_sucessaovinc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_sucessaovinc", "Can view s2299_sucessaovinc"), )
            
        ordering = [
            's2299_evtdeslig',
            'tpinscsuc',
            'cnpjsucessora',]



class s2299sucessaoVincSerializer(ModelSerializer):

    class Meta:
    
        model = s2299sucessaoVinc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299transfTit(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    cpfsubstituto = models.CharField(max_length=11, null=True, )
    dtnascto = models.DateField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),
            unicode(self.cpfsubstituto),
            unicode(self.dtnascto),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Transferência de titularidade do empregado doméstico para outro representante da mesma unidade familiar'
        db_table = r's2299_transftit'       
        managed = True # s2299_transftit #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_transftit", "Can view s2299_transftit"), )
            
        ordering = [
            's2299_evtdeslig',
            'cpfsubstituto',
            'dtnascto',]



class s2299transfTitSerializer(ModelSerializer):

    class Meta:
    
        model = s2299transfTit
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2299verbasResc(SoftDeletionModel):

    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig', 
        related_name='%(class)s_s2299_evtdeslig', )
    
    def evento(self): 
        return self.s2299_evtdeslig.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2299_evtdeslig),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro onde são prestadas as informações relativas às verbas devidas ao trabalhador na rescisão contratual.'
        db_table = r's2299_verbasresc'       
        managed = True # s2299_verbasresc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2299_verbasresc", "Can view s2299_verbasresc"), )
            
        ordering = [
            's2299_evtdeslig',]



class s2299verbasRescSerializer(ModelSerializer):

    class Meta:
    
        model = s2299verbasResc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()