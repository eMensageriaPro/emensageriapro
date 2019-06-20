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
from emensageriapro.s2230.choices import *
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





class s2230emitente(SoftDeletionModel):

    s2230_infoatestado = models.ForeignKey('s2230.s2230infoAtestado', 
        related_name='%(class)s_s2230_infoatestado', )
    
    def evento(self): 
        return self.s2230_infoatestado.evento()
    nmemit = models.CharField(max_length=70, null=True, )
    ideoc = models.IntegerField(choices=CHOICES_S2230_IDEOC, null=True, )
    nroc = models.CharField(max_length=14, null=True, )
    ufoc = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_infoatestado), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Médico/Dentista que emitiu o atestado'
        db_table = r's2230_emitente'       
        managed = True # s2230_emitente #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230emitente", u"Pode ver listagem do modelo S2230EMITENTE"),
            ("can_see_data_s2230emitente", u"Pode visualizar o conteúdo do modelo S2230EMITENTE"),
            ("can_see_menu_s2230emitente", u"Pode visualizar no menu o modelo S2230EMITENTE"),
            ("can_print_list_s2230emitente", u"Pode imprimir listagem do modelo S2230EMITENTE"),
            ("can_print_data_s2230emitente", u"Pode imprimir o conteúdo do modelo S2230EMITENTE"), )
            
        ordering = [
            's2230_infoatestado',
            'nmemit',
            'ideoc',
            'nroc',]



class s2230emitenteSerializer(ModelSerializer):

    class Meta:
    
        model = s2230emitente
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230fimAfastamento(SoftDeletionModel):

    s2230_evtafasttemp = models.ForeignKey('esocial.s2230evtAfastTemp', 
        related_name='%(class)s_s2230_evtafasttemp', )
    
    def evento(self): 
        return self.s2230_evtafasttemp.evento()
    dttermafast = models.DateField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_evtafasttemp), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Término do Afastamento'
        db_table = r's2230_fimafastamento'       
        managed = True # s2230_fimafastamento #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230fimAfastamento", u"Pode ver listagem do modelo S2230FIMAFASTAMENTO"),
            ("can_see_data_s2230fimAfastamento", u"Pode visualizar o conteúdo do modelo S2230FIMAFASTAMENTO"),
            ("can_see_menu_s2230fimAfastamento", u"Pode visualizar no menu o modelo S2230FIMAFASTAMENTO"),
            ("can_print_list_s2230fimAfastamento", u"Pode imprimir listagem do modelo S2230FIMAFASTAMENTO"),
            ("can_print_data_s2230fimAfastamento", u"Pode imprimir o conteúdo do modelo S2230FIMAFASTAMENTO"), )
            
        ordering = [
            's2230_evtafasttemp',
            'dttermafast',]



class s2230fimAfastamentoSerializer(ModelSerializer):

    class Meta:
    
        model = s2230fimAfastamento
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230infoAtestado(SoftDeletionModel):

    s2230_iniafastamento = models.ForeignKey('s2230.s2230iniAfastamento', 
        related_name='%(class)s_s2230_iniafastamento', )
    
    def evento(self): 
        return self.s2230_iniafastamento.evento()
    codcid = models.CharField(max_length=4, blank=True, null=True, )
    qtddiasafast = models.IntegerField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_iniafastamento), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares relativas ao atestado médico'
        db_table = r's2230_infoatestado'       
        managed = True # s2230_infoatestado #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230infoAtestado", u"Pode ver listagem do modelo S2230INFOATESTADO"),
            ("can_see_data_s2230infoAtestado", u"Pode visualizar o conteúdo do modelo S2230INFOATESTADO"),
            ("can_see_menu_s2230infoAtestado", u"Pode visualizar no menu o modelo S2230INFOATESTADO"),
            ("can_print_list_s2230infoAtestado", u"Pode imprimir listagem do modelo S2230INFOATESTADO"),
            ("can_print_data_s2230infoAtestado", u"Pode imprimir o conteúdo do modelo S2230INFOATESTADO"), )
            
        ordering = [
            's2230_iniafastamento',
            'qtddiasafast',]



class s2230infoAtestadoSerializer(ModelSerializer):

    class Meta:
    
        model = s2230infoAtestado
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230infoCessao(SoftDeletionModel):

    s2230_iniafastamento = models.ForeignKey('s2230.s2230iniAfastamento', 
        related_name='%(class)s_s2230_iniafastamento', )
    
    def evento(self): 
        return self.s2230_iniafastamento.evento()
    cnpjcess = models.CharField(max_length=14, null=True, )
    infonus = models.IntegerField(choices=CHOICES_S2230_INFONUS, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_iniafastamento), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido nos casos de afastamento por cessão ou requisição do trabalhador.'
        db_table = r's2230_infocessao'       
        managed = True # s2230_infocessao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230infoCessao", u"Pode ver listagem do modelo S2230INFOCESSAO"),
            ("can_see_data_s2230infoCessao", u"Pode visualizar o conteúdo do modelo S2230INFOCESSAO"),
            ("can_see_menu_s2230infoCessao", u"Pode visualizar no menu o modelo S2230INFOCESSAO"),
            ("can_print_list_s2230infoCessao", u"Pode imprimir listagem do modelo S2230INFOCESSAO"),
            ("can_print_data_s2230infoCessao", u"Pode imprimir o conteúdo do modelo S2230INFOCESSAO"), )
            
        ordering = [
            's2230_iniafastamento',
            'cnpjcess',
            'infonus',]



class s2230infoCessaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2230infoCessao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230infoMandSind(SoftDeletionModel):

    s2230_iniafastamento = models.ForeignKey('s2230.s2230iniAfastamento', 
        related_name='%(class)s_s2230_iniafastamento', )
    
    def evento(self): 
        return self.s2230_iniafastamento.evento()
    cnpjsind = models.CharField(max_length=14, null=True, )
    infonusremun = models.IntegerField(choices=CHOICES_S2230_INFONUSREMUN, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_iniafastamento), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares - afastamento para exercício de mandato sindical'
        db_table = r's2230_infomandsind'       
        managed = True # s2230_infomandsind #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230infoMandSind", u"Pode ver listagem do modelo S2230INFOMANDSIND"),
            ("can_see_data_s2230infoMandSind", u"Pode visualizar o conteúdo do modelo S2230INFOMANDSIND"),
            ("can_see_menu_s2230infoMandSind", u"Pode visualizar no menu o modelo S2230INFOMANDSIND"),
            ("can_print_list_s2230infoMandSind", u"Pode imprimir listagem do modelo S2230INFOMANDSIND"),
            ("can_print_data_s2230infoMandSind", u"Pode imprimir o conteúdo do modelo S2230INFOMANDSIND"), )
            
        ordering = [
            's2230_iniafastamento',
            'cnpjsind',
            'infonusremun',]



class s2230infoMandSindSerializer(ModelSerializer):

    class Meta:
    
        model = s2230infoMandSind
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230infoRetif(SoftDeletionModel):

    s2230_evtafasttemp = models.ForeignKey('esocial.s2230evtAfastTemp', 
        related_name='%(class)s_s2230_evtafasttemp', )
    
    def evento(self): 
        return self.s2230_evtafasttemp.evento()
    origretif = models.IntegerField(choices=CHOICES_S2230_ORIGRETIF, null=True, )
    tpproc = models.IntegerField(choices=CHOICES_S2230_TPPROC, blank=True, null=True, )
    nrproc = models.CharField(max_length=21, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_evtafasttemp), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de retificação do Afastamento Temporário'
        db_table = r's2230_inforetif'       
        managed = True # s2230_inforetif #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230infoRetif", u"Pode ver listagem do modelo S2230INFORETIF"),
            ("can_see_data_s2230infoRetif", u"Pode visualizar o conteúdo do modelo S2230INFORETIF"),
            ("can_see_menu_s2230infoRetif", u"Pode visualizar no menu o modelo S2230INFORETIF"),
            ("can_print_list_s2230infoRetif", u"Pode imprimir listagem do modelo S2230INFORETIF"),
            ("can_print_data_s2230infoRetif", u"Pode imprimir o conteúdo do modelo S2230INFORETIF"), )
            
        ordering = [
            's2230_evtafasttemp',
            'origretif',]



class s2230infoRetifSerializer(ModelSerializer):

    class Meta:
    
        model = s2230infoRetif
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2230iniAfastamento(SoftDeletionModel):

    s2230_evtafasttemp = models.ForeignKey('esocial.s2230evtAfastTemp', 
        related_name='%(class)s_s2230_evtafasttemp', )
    
    def evento(self): 
        return self.s2230_evtafasttemp.evento()
    dtiniafast = models.DateField(null=True, )
    codmotafast = models.TextField(null=True, )
    infomesmomtv = models.CharField(choices=CHOICES_S2230_INFOMESMOMTV, max_length=1, blank=True, null=True, )
    tpacidtransito = models.IntegerField(choices=CHOICES_S2230_TPACIDTRANSITO, blank=True, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2230_evtafasttemp), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Afastamento Temporário - Início'
        db_table = r's2230_iniafastamento'       
        managed = True # s2230_iniafastamento #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2230iniAfastamento", u"Pode ver listagem do modelo S2230INIAFASTAMENTO"),
            ("can_see_data_s2230iniAfastamento", u"Pode visualizar o conteúdo do modelo S2230INIAFASTAMENTO"),
            ("can_see_menu_s2230iniAfastamento", u"Pode visualizar no menu o modelo S2230INIAFASTAMENTO"),
            ("can_print_list_s2230iniAfastamento", u"Pode imprimir listagem do modelo S2230INIAFASTAMENTO"),
            ("can_print_data_s2230iniAfastamento", u"Pode imprimir o conteúdo do modelo S2230INIAFASTAMENTO"), )
            
        ordering = [
            's2230_evtafasttemp',
            'dtiniafast',
            'codmotafast',]



class s2230iniAfastamentoSerializer(ModelSerializer):

    class Meta:
    
        model = s2230iniAfastamento
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')