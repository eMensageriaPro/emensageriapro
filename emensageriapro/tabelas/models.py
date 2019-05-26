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
from emensageriapro.tabelas.choices import *
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





class CBO(SoftDeletionModel):

    codigo = models.CharField(max_length=6, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'CBO'
        db_table = r'cbo'       
        managed = True # cbo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_cbo", "Can view cbo"), )
        
        ordering = [
            'codigo',
            'descricao',]



class CBOSerializer(ModelSerializer):

    class Meta:
    
        model = CBO
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class CID(SoftDeletionModel):

    codigo = models.CharField(max_length=6, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    descricao_resumida = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'CID'
        db_table = r'cid'       
        managed = True # cid #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_cid", "Can view cid"), )
        
        ordering = [
            'codigo',
            'descricao',]



class CIDSerializer(ModelSerializer):

    class Meta:
    
        model = CID
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class CNAE(SoftDeletionModel):

    codigo = models.CharField(max_length=7, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    aliquota = models.DecimalField(max_digits=15, decimal_places=2, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'CNAE'
        db_table = r'cnae'       
        managed = True # cnae #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_cnae", "Can view cnae"), )
        
        ordering = [
            'codigo',
            'descricao',]



class CNAESerializer(ModelSerializer):

    class Meta:
    
        model = CNAE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfClassificacaoServicosPrestados(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 06 – Classificação de Serviços Prestados mediante cessão de mão de obra/Empreitada'
        db_table = r'efdreinf_classificacao_servicos_prestados'       
        managed = True # efdreinf_classificacao_servicos_prestados #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_classificacao_servicos_prestados", "Can view efdreinf_classificacao_servicos_prestados"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfClassificacaoServicosPrestadosSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfClassificacaoServicosPrestados
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfClassificacaoTributaria(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 08 - Classificação Tributária'
        db_table = r'efdreinf_classificacao_tributaria'       
        managed = True # efdreinf_classificacao_tributaria #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_classificacao_tributaria", "Can view efdreinf_classificacao_tributaria"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfClassificacaoTributariaSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfClassificacaoTributaria
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfCodigosAtividadesProdutosServicosCPRB(SoftDeletionModel):

    grupo = models.IntegerField(choices=GRUPO_CODIGO_ATIV_PROD_SERV, )
    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    incidencia = models.TextField(blank=True, null=True, )
    cr = models.CharField(max_length=12, blank=True, null=True, )
    ncm = models.CharField(max_length=12, blank=True, null=True, )
    aliquota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    inicio_escrituracao = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.descricao),
            unicode(self.incidencia),
            unicode(self.cr),
            unicode(self.ncm),
            unicode(self.aliquota),
            unicode(self.inicio_escrituracao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 09 – Código de Atividades, Produtos e Serviços Sujeitos à CPRB'
        db_table = r'efdreinf_codigos_atividades_produtos_servicos_cprb'       
        managed = True # efdreinf_codigos_atividades_produtos_servicos_cprb #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_codigos_atividades_produtos_servicos_cprb", "Can view efdreinf_codigos_atividades_produtos_servicos_cprb"), )
        
        ordering = [
            'grupo',
            'codigo',
            'descricao',
            'incidencia',
            'cr',
            'ncm',
            'aliquota',
            'inicio_escrituracao',]



class EFDReinfCodigosAtividadesProdutosServicosCPRBSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfCodigosAtividadesProdutosServicosCPRB
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfEventos(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 10 - Eventos da EFD-Reinf'
        db_table = r'efdreinf_eventos'       
        managed = True # efdreinf_eventos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_eventos", "Can view efdreinf_eventos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfEventosSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfEventos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfInformacoesBeneficiariosExterior(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 05 - Informações sobre os beneficiários de Rendimentos no Exterior'
        db_table = r'efdreinf_informacoes_beneficiarios_exterior'       
        managed = True # efdreinf_informacoes_beneficiarios_exterior #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_informacoes_beneficiarios_exterior", "Can view efdreinf_informacoes_beneficiarios_exterior"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfInformacoesBeneficiariosExteriorSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfInformacoesBeneficiariosExterior
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfPagamentosCodigos(SoftDeletionModel):

    grupo = models.IntegerField(choices=GRUPO_PAGAMENTOS_CODIGOS, )
    codigo = models.CharField(max_length=4, )
    beneficiario_pj = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    beneficiario_pf = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.beneficiario_pj),
            unicode(self.beneficiario_pf),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 01 – Códigos de Pagamentos'
        db_table = r'efdreinf_pagamentos_codigos'       
        managed = True # efdreinf_pagamentos_codigos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_pagamentos_codigos", "Can view efdreinf_pagamentos_codigos"), )
        
        ordering = [
            'grupo',
            'codigo',
            'beneficiario_pj',
            'beneficiario_pf',
            'descricao',]



class EFDReinfPagamentosCodigosSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfPagamentosCodigos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfPaises(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 07 – Países'
        db_table = r'efdreinf_paises'       
        managed = True # efdreinf_paises #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_paises", "Can view efdreinf_paises"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfPaisesSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfPaises
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfRegrasPagamentosCodigos(SoftDeletionModel):

    classificacao = models.IntegerField(choices=CLASSIFICACAO_REGRAS_PAGAMENTOS_CODIGOS, )
    codigo = models.CharField(max_length=4, )
    decimo_terceiro = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True, )
    deducoes = models.CharField(max_length=10, blank=True, null=True, )
    rendimentos_isentos = models.CharField(max_length=10, blank=True, null=True, )
    compensacao_imposto_por_decisao_judicial = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True, )
    tributacao_com_exigibilidade_suspensa = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.classificacao),
            unicode(self.codigo),
            unicode(self.decimo_terceiro),
            unicode(self.deducoes),
            unicode(self.rendimentos_isentos),
            unicode(self.compensacao_imposto_por_decisao_judicial),
            unicode(self.tributacao_com_exigibilidade_suspensa),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 02 - Regras para utilização dos códigos de pagamento a Pessoas Físicas'
        db_table = r'efdreinf_regras_pagamentos_codigos'       
        managed = True # efdreinf_regras_pagamentos_codigos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_regras_pagamentos_codigos", "Can view efdreinf_regras_pagamentos_codigos"), )
        
        ordering = [
            'classificacao',
            'codigo',
            'decimo_terceiro',
            'deducoes',
            'rendimentos_isentos',
            'compensacao_imposto_por_decisao_judicial',
            'tributacao_com_exigibilidade_suspensa',
            'descricao',]



class EFDReinfRegrasPagamentosCodigosSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfRegrasPagamentosCodigos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfRendimentosBeneficiariosExterior(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 03 – Rendimentos de Beneficiários no Exterior'
        db_table = r'efdreinf_rendimentos_beneficiarios_exterior'       
        managed = True # efdreinf_rendimentos_beneficiarios_exterior #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_rendimentos_beneficiarios_exterior", "Can view efdreinf_rendimentos_beneficiarios_exterior"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfRendimentosBeneficiariosExteriorSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfRendimentosBeneficiariosExterior
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class EFDReinfRendimentosBeneficiariosExteriorTributacao(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'EFD-Reinf 04 - Forma de Tributação para rendimentos de beneficiários no Exterior'
        db_table = r'efdreinf_rendimentos_beneficiarios_exterior_tributacao'       
        managed = True # efdreinf_rendimentos_beneficiarios_exterior_tributacao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_efdreinf_rendimentos_beneficiarios_exterior_tributacao", "Can view efdreinf_rendimentos_beneficiarios_exterior_tributacao"), )
        
        ordering = [
            'codigo',
            'descricao',]



class EFDReinfRendimentosBeneficiariosExteriorTributacaoSerializer(ModelSerializer):

    class Meta:
    
        model = EFDReinfRendimentosBeneficiariosExteriorTributacao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class Municipios(SoftDeletionModel):

    codigo = models.CharField(max_length=7, )
    titulo = models.CharField(max_length=300, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.titulo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Municipios'
        db_table = r'municipios'       
        managed = True # municipios #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_municipios", "Can view municipios"), )
        
        ordering = [
            'titulo',]



class MunicipiosSerializer(ModelSerializer):

    class Meta:
    
        model = Municipios
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialAcidentesSituacoesGeradoras(SoftDeletionModel):

    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 16 - Situação Geradora do Acidente de Trabalho'
        db_table = r'esocial_acidentes_situacoes_geradoras'       
        managed = True # esocial_acidentes_situacoes_geradoras #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_acidentes_situacoes_geradoras", "Can view esocial_acidentes_situacoes_geradoras"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialAcidentesSituacoesGeradorasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialAcidentesSituacoesGeradoras
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialAfastamentosMotivos(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),
            unicode(self.data_inicio),
            unicode(self.data_termino),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 18 - Motivos de Afastamento'
        db_table = r'esocial_afastamentos_motivos'       
        managed = True # esocial_afastamentos_motivos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_afastamentos_motivos", "Can view esocial_afastamentos_motivos"), )
        
        ordering = [
            'codigo',
            'descricao',
            'data_inicio',
            'data_termino',]



class eSocialAfastamentosMotivosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialAfastamentosMotivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialAgentesCausadoresAcidentesTrabalho(SoftDeletionModel):

    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 14 - Agente Causador do Acidente de Trabalho'
        db_table = r'esocial_agentes_causadores_acidentes_trabalho'       
        managed = True # esocial_agentes_causadores_acidentes_trabalho #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_agentes_causadores_acidentes_trabalho", "Can view esocial_agentes_causadores_acidentes_trabalho"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialAgentesCausadoresAcidentesTrabalhoSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialAgentesCausadoresAcidentesTrabalho
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialAgentesCausadoresDoencasProfissionais(SoftDeletionModel):

    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 15 - Agente Causador / Situação Geradora de Doença Profissional'
        db_table = r'esocial_agentes_causadores_doencas_profissionais'       
        managed = True # esocial_agentes_causadores_doencas_profissionais #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_agentes_causadores_doencas_profissionais", "Can view esocial_agentes_causadores_doencas_profissionais"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialAgentesCausadoresDoencasProfissionaisSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialAgentesCausadoresDoencasProfissionais
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialArquivosEsocialTipos(SoftDeletionModel):

    codigo = models.CharField(max_length=6, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 09 - Tipos de Arquivo do eSocial'
        db_table = r'esocial_arquivos_esocial_tipos'       
        managed = True # esocial_arquivos_esocial_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_arquivos_esocial_tipos", "Can view esocial_arquivos_esocial_tipos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialArquivosEsocialTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialArquivosEsocialTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialAtividadesPericulosasInsalubresEspeciais(SoftDeletionModel):

    grupo = models.IntegerField(choices=GRUPO_ATIVIDADES_PERICULOSAS, )
    codigo = models.CharField(max_length=6, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 28 - Atividades Periculosas, Insalubres e/ou Especiais'
        db_table = r'esocial_atividades_periculosas_insalubres_especiais'       
        managed = True # esocial_atividades_periculosas_insalubres_especiais #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_atividades_periculosas_insalubres_especiais", "Can view esocial_atividades_periculosas_insalubres_especiais"), )
        
        ordering = [
            'grupo',
            'codigo',
            'descricao',]



class eSocialAtividadesPericulosasInsalubresEspeciaisSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialAtividadesPericulosasInsalubresEspeciais
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialBeneficiosPrevidenciariosCessacaoMotivos(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 26 - Motivos de Cessação de Benefícios'
        db_table = r'esocial_beneficios_previdenciarios_cessacao_motivos'       
        managed = True # esocial_beneficios_previdenciarios_cessacao_motivos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_beneficios_previdenciarios_cessacao_motivos", "Can view esocial_beneficios_previdenciarios_cessacao_motivos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialBeneficiosPrevidenciariosCessacaoMotivosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialBeneficiosPrevidenciariosCessacaoMotivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialBeneficiosPrevidenciariosTipos(SoftDeletionModel):

    grupo = models.IntegerField(choices=ESOCIAL_BENEFICIOS_PREVIDENCIARIOS_TIPOS_GRUPOS, )
    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 25 - Tipos de Benefícios'
        db_table = r'esocial_beneficios_previdenciarios_tipos'       
        managed = True # esocial_beneficios_previdenciarios_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_beneficios_previdenciarios_tipos", "Can view esocial_beneficios_previdenciarios_tipos"), )
        
        ordering = [
            'grupo',
            'codigo',
            'descricao',]



class eSocialBeneficiosPrevidenciariosTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialBeneficiosPrevidenciariosTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialClassificacoesTributarias(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 08 - Classificação Tributária'
        db_table = r'esocial_classificacoes_tributarias'       
        managed = True # esocial_classificacoes_tributarias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_classificacoes_tributarias", "Can view esocial_classificacoes_tributarias"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialClassificacoesTributariasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialClassificacoesTributarias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialCodificacoesAcidenteTrabalho(SoftDeletionModel):

    codigo = models.CharField(max_length=6, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 24 - Codificação de Acidente de Trabalho'
        db_table = r'esocial_codificacoes_acidente_trabalho'       
        managed = True # esocial_codificacoes_acidente_trabalho #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_codificacoes_acidente_trabalho", "Can view esocial_codificacoes_acidente_trabalho"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialCodificacoesAcidenteTrabalhoSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialCodificacoesAcidenteTrabalho
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialCodigoAliquotasFPASTerceiros(SoftDeletionModel):

    codigo = models.CharField(max_length=3, )
    descricao = models.TextField()
    tipo_empresa = models.CharField(max_length=20, )
    base_calculo = models.CharField(max_length=50, )
    terceiros = models.CharField(max_length=20, )
    codigo_terceiro = models.CharField(max_length=4, )
    aliquota = models.DecimalField(max_digits=15, decimal_places=2, )
    ind_total = models.IntegerField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 04 - Códigos e Alíquotas de FPAS/Terceiros'
        db_table = r'esocial_codigo_aliquotas_fpas_terceiros'       
        managed = True # esocial_codigo_aliquotas_fpas_terceiros #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_codigo_aliquotas_fpas_terceiros", "Can view esocial_codigo_aliquotas_fpas_terceiros"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialCodigoAliquotasFPASTerceirosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialCodigoAliquotasFPASTerceiros
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialCompatibilidadesCategoriasClassificacoesLotacoes(SoftDeletionModel):

    codigo = models.CharField(max_length=3, )
    classificacao_tributaria = models.TextField()
    tipo_lotacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_05 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_24 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_90 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_lotacao_tributaria_91 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.classificacao_tributaria),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 11 - Compatibilidade entre Categoria de Trabalhadores, Classif. Tributária e Tipos de Lotação'
        db_table = r'esocial_compatibilidades_categorias_classificacoes_lotacoes'       
        managed = True # esocial_compatibilidades_categorias_classificacoes_lotacoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_compatibilidades_categorias_classificacoes_lotacoes", "Can view esocial_compatibilidades_categorias_classificacoes_lotacoes"), )
        
        ordering = [
            'codigo',
            'classificacao_tributaria',]



class eSocialCompatibilidadesCategoriasClassificacoesLotacoesSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialCompatibilidadesCategoriasClassificacoesLotacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialCompatibilidadesFPASClassificacoesTributarias(SoftDeletionModel):

    codigo = models.CharField(max_length=3, )
    classificacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_11 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_13 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_14 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_22 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_60 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_70 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_80 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_85 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    classificacao_tributaria_99 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 22 - Compatibilidade entre FPAS e Classificação Tributária'
        db_table = r'esocial_compatibilidades_fpas_classificacoes_tributarias'       
        managed = True # esocial_compatibilidades_fpas_classificacoes_tributarias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_compatibilidades_fpas_classificacoes_tributarias", "Can view esocial_compatibilidades_fpas_classificacoes_tributarias"), )
        
        ordering = [
            'codigo',]



class eSocialCompatibilidadesFPASClassificacoesTributariasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialCompatibilidadesFPASClassificacoesTributarias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialCompatibilidadesLotacoesClassificacoes(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    tipo_classificacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_11 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_13 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_14 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_22 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_60 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_70 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_80 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_85 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    tipo_classificacao_tributaria_99 = models.CharField(choices=SIM_NAO_TXT, max_length=1, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 12 - Compatibilidade entre Tipos de Lotação e Classificação Tributária'
        db_table = r'esocial_compatibilidades_lotacoes_classificacoes'       
        managed = True # esocial_compatibilidades_lotacoes_classificacoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_compatibilidades_lotacoes_classificacoes", "Can view esocial_compatibilidades_lotacoes_classificacoes"), )
        
        ordering = [
            'codigo',]



class eSocialCompatibilidadesLotacoesClassificacoesSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialCompatibilidadesLotacoesClassificacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialDependentesTipos(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 07 - Tipos de Dependente'
        db_table = r'esocial_dependentes_tipos'       
        managed = True # esocial_dependentes_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_dependentes_tipos", "Can view esocial_dependentes_tipos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialDependentesTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialDependentesTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialDesligamentosMotivos(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),
            unicode(self.data_inicio),
            unicode(self.data_termino),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 19 - Motivos de Desligamento'
        db_table = r'esocial_desligamentos_motivos'       
        managed = True # esocial_desligamentos_motivos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_desligamentos_motivos", "Can view esocial_desligamentos_motivos"), )
        
        ordering = [
            'codigo',
            'descricao',
            'data_inicio',
            'data_termino',]



class eSocialDesligamentosMotivosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialDesligamentosMotivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialFatoresRisco(SoftDeletionModel):

    grupo = models.IntegerField(choices=GRUPOS_FATORES_RISCOS, )
    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 23 - Fatores de Riscos do Meio Ambiente do Trabalho'
        db_table = r'esocial_fatores_risco'       
        managed = True # esocial_fatores_risco #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_fatores_risco", "Can view esocial_fatores_risco"), )
        
        ordering = [
            'grupo',
            'codigo',
            'descricao',]



class eSocialFatoresRiscoSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialFatoresRisco
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialFinanciamentosAposentadoriasEspeciais(SoftDeletionModel):

    codigo = models.CharField(max_length=14, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 02 - Financiamento da Aposent. Especial e Redução do Tempo de Contrib.'
        db_table = r'esocial_financiamentos_aposentadorias_especiais'       
        managed = True # esocial_financiamentos_aposentadorias_especiais #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_financiamentos_aposentadorias_especiais", "Can view esocial_financiamentos_aposentadorias_especiais"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialFinanciamentosAposentadoriasEspeciaisSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialFinanciamentosAposentadoriasEspeciais
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialInscricoesTipos(SoftDeletionModel):

    codigo = models.CharField(max_length=14, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 05 - Tipos de Inscrição'
        db_table = r'esocial_inscricoes_tipos'       
        managed = True # esocial_inscricoes_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_inscricoes_tipos", "Can view esocial_inscricoes_tipos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialInscricoesTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialInscricoesTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialLogradourosTipos(SoftDeletionModel):

    codigo = models.CharField(max_length=5, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 20 - Tipos de Logradouro'
        db_table = r'esocial_logradouros_tipos'       
        managed = True # esocial_logradouros_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_logradouros_tipos", "Can view esocial_logradouros_tipos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialLogradourosTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialLogradourosTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialLotacoesTributariasTipos(SoftDeletionModel):

    codigo = models.CharField(max_length=2, )
    descricao = models.TextField()
    preenchimento_campo_nr_insc = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 10 - Tipos de Lotação Tributária'
        db_table = r'esocial_lotacoes_tributarias_tipos'       
        managed = True # esocial_lotacoes_tributarias_tipos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_lotacoes_tributarias_tipos", "Can view esocial_lotacoes_tributarias_tipos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialLotacoesTributariasTiposSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialLotacoesTributariasTipos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialNaturezasJuridicas(SoftDeletionModel):

    grupo = models.IntegerField(choices=GRUPO_NATUREZAS_JURIDICAS, )
    codigo = models.CharField(max_length=20, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 21 - Natureza Jurídica'
        db_table = r'esocial_naturezas_juridicas'       
        managed = True # esocial_naturezas_juridicas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_naturezas_juridicas", "Can view esocial_naturezas_juridicas"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialNaturezasJuridicasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialNaturezasJuridicas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialNaturezasLesoes(SoftDeletionModel):

    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 17 - Descrição da Natureza da Lesão'
        db_table = r'esocial_naturezas_lesoes'       
        managed = True # esocial_naturezas_lesoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_naturezas_lesoes", "Can view esocial_naturezas_lesoes"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialNaturezasLesoesSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialNaturezasLesoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialNaturezasRubricas(SoftDeletionModel):

    codigo = models.CharField(max_length=14, )
    titulo = models.CharField(max_length=200, )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.titulo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 03 - Natureza das Rubricas da Folha de Pagamento'
        db_table = r'esocial_naturezas_rubricas'       
        managed = True # esocial_naturezas_rubricas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_naturezas_rubricas", "Can view esocial_naturezas_rubricas"), )
        
        ordering = [
            'codigo',
            'titulo',]



class eSocialNaturezasRubricasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialNaturezasRubricas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialPaises(SoftDeletionModel):

    codigo = models.CharField(max_length=14, )
    nome = models.CharField(max_length=200, )
    data_criacao = models.DateField(blank=True, null=True, )
    data_extincao = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.nome),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 06 - Países'
        db_table = r'esocial_paises'       
        managed = True # esocial_paises #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_paises", "Can view esocial_paises"), )
        
        ordering = [
            'codigo',
            'nome',]



class eSocialPaisesSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialPaises
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialPartesCorpoAtingidas(SoftDeletionModel):

    codigo = models.CharField(max_length=9, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 13 - Parte do corpo atingida'
        db_table = r'esocial_partes_corpo_atingidas'       
        managed = True # esocial_partes_corpo_atingidas #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_partes_corpo_atingidas", "Can view esocial_partes_corpo_atingidas"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialPartesCorpoAtingidasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialPartesCorpoAtingidas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialProcedimentosDiagnosticos(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 27 - Procedimentos Diagnósticos'
        db_table = r'esocial_procedimentos_diagnosticos'       
        managed = True # esocial_procedimentos_diagnosticos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_procedimentos_diagnosticos", "Can view esocial_procedimentos_diagnosticos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialProcedimentosDiagnosticosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialProcedimentosDiagnosticos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialProgramasPlanosDocumentos(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 30 - Programas, Planos e Documentos'
        db_table = r'esocial_programas_planos_documentos'       
        managed = True # esocial_programas_planos_documentos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_programas_planos_documentos", "Can view esocial_programas_planos_documentos"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialProgramasPlanosDocumentosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialProgramasPlanosDocumentos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialTrabalhadoresCategorias(SoftDeletionModel):

    grupo = models.IntegerField(choices=TRABALHADORES_CATEGORIAS_GRUPO, )
    codigo = models.CharField(max_length=14, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.grupo),
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 01 - Categorias de Trabalhadores'
        db_table = r'esocial_trabalhadores_categorias'       
        managed = True # esocial_trabalhadores_categorias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_trabalhadores_categorias", "Can view esocial_trabalhadores_categorias"), )
        
        ordering = [
            'grupo',
            'codigo',
            'descricao',]



class eSocialTrabalhadoresCategoriasSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialTrabalhadoresCategorias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class eSocialTreinamentosCapacitacoesExerciciosSimulados(SoftDeletionModel):

    codigo = models.CharField(max_length=4, )
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.codigo),
            unicode(self.descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'eSocial 29 - Treinamentos, Capacitações e Exercícios Simulados'
        db_table = r'esocial_treinamentos_capacitacoes_exercicios_simulados'       
        managed = True # esocial_treinamentos_capacitacoes_exercicios_simulados #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_esocial_treinamentos_capacitacoes_exercicios_simulados", "Can view esocial_treinamentos_capacitacoes_exercicios_simulados"), )
        
        ordering = [
            'codigo',
            'descricao',]



class eSocialTreinamentosCapacitacoesExerciciosSimuladosSerializer(ModelSerializer):

    class Meta:
    
        model = eSocialTreinamentosCapacitacoesExerciciosSimulados
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()