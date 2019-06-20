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
from emensageriapro.s2241.choices import *
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





class s2241altAposentEsp(SoftDeletionModel):

    s2241_aposentesp = models.ForeignKey('s2241.s2241aposentEsp', 
        related_name='%(class)s_s2241_aposentesp', )
    
    def evento(self): 
        return self.s2241_aposentesp.evento()
    dtaltcondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho que ensejam aposentadoria especial - Alteração'
        db_table = r's2241_altaposentesp'       
        managed = True # s2241_altaposentesp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altAposentEsp", u"Pode ver listagem do modelo S2241ALTAPOSENTESP"),
            ("can_see_data_s2241altAposentEsp", u"Pode visualizar o conteúdo do modelo S2241ALTAPOSENTESP"),
            ("can_see_menu_s2241altAposentEsp", u"Pode visualizar no menu o modelo S2241ALTAPOSENTESP"),
            ("can_print_list_s2241altAposentEsp", u"Pode imprimir listagem do modelo S2241ALTAPOSENTESP"),
            ("can_print_data_s2241altAposentEsp", u"Pode imprimir o conteúdo do modelo S2241ALTAPOSENTESP"), )
            
        ordering = [
            's2241_aposentesp',
            'dtaltcondicao',]



class s2241altAposentEspSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altAposentEsp
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241altAposentEspfatRisco(SoftDeletionModel):

    s2241_altaposentesp_infoamb = models.ForeignKey('s2241.s2241altAposentEspinfoamb', 
        related_name='%(class)s_s2241_altaposentesp_infoamb', )
    
    def evento(self): 
        return self.s2241_altaposentesp_infoamb.evento()
    codfatris = models.TextField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2241_altaposentesp_fatrisco'       
        managed = True # s2241_altaposentesp_fatrisco #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altAposentEspfatRisco", u"Pode ver listagem do modelo S2241ALTAPOSENTESPFATRISCO"),
            ("can_see_data_s2241altAposentEspfatRisco", u"Pode visualizar o conteúdo do modelo S2241ALTAPOSENTESPFATRISCO"),
            ("can_see_menu_s2241altAposentEspfatRisco", u"Pode visualizar no menu o modelo S2241ALTAPOSENTESPFATRISCO"),
            ("can_print_list_s2241altAposentEspfatRisco", u"Pode imprimir listagem do modelo S2241ALTAPOSENTESPFATRISCO"),
            ("can_print_data_s2241altAposentEspfatRisco", u"Pode imprimir o conteúdo do modelo S2241ALTAPOSENTESPFATRISCO"), )
            
        ordering = [
            's2241_altaposentesp_infoamb',
            'codfatris',]



class s2241altAposentEspfatRiscoSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altAposentEspfatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241altAposentEspinfoamb(SoftDeletionModel):

    s2241_altaposentesp = models.ForeignKey('s2241.s2241altAposentEsp', 
        related_name='%(class)s_s2241_altaposentesp', )
    
    def evento(self): 
        return self.s2241_altaposentesp.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações sobre as condições de trabalho insalubre/periculoso.'
        db_table = r's2241_altaposentesp_infoamb'       
        managed = True # s2241_altaposentesp_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altAposentEspinfoamb", u"Pode ver listagem do modelo S2241ALTAPOSENTESPINFOAMB"),
            ("can_see_data_s2241altAposentEspinfoamb", u"Pode visualizar o conteúdo do modelo S2241ALTAPOSENTESPINFOAMB"),
            ("can_see_menu_s2241altAposentEspinfoamb", u"Pode visualizar no menu o modelo S2241ALTAPOSENTESPINFOAMB"),
            ("can_print_list_s2241altAposentEspinfoamb", u"Pode imprimir listagem do modelo S2241ALTAPOSENTESPINFOAMB"),
            ("can_print_data_s2241altAposentEspinfoamb", u"Pode imprimir o conteúdo do modelo S2241ALTAPOSENTESPINFOAMB"), )
            
        ordering = [
            's2241_altaposentesp',
            'codamb',]



class s2241altAposentEspinfoambSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altAposentEspinfoamb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241altInsalPeric(SoftDeletionModel):

    s2241_insalperic = models.ForeignKey('s2241.s2241insalPeric', 
        related_name='%(class)s_s2241_insalperic', )
    
    def evento(self): 
        return self.s2241_insalperic.evento()
    dtaltcondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho insalubre/periculoso - Alteração'
        db_table = r's2241_altinsalperic'       
        managed = True # s2241_altinsalperic #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altInsalPeric", u"Pode ver listagem do modelo S2241ALTINSALPERIC"),
            ("can_see_data_s2241altInsalPeric", u"Pode visualizar o conteúdo do modelo S2241ALTINSALPERIC"),
            ("can_see_menu_s2241altInsalPeric", u"Pode visualizar no menu o modelo S2241ALTINSALPERIC"),
            ("can_print_list_s2241altInsalPeric", u"Pode imprimir listagem do modelo S2241ALTINSALPERIC"),
            ("can_print_data_s2241altInsalPeric", u"Pode imprimir o conteúdo do modelo S2241ALTINSALPERIC"), )
            
        ordering = [
            's2241_insalperic',
            'dtaltcondicao',]



class s2241altInsalPericSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altInsalPeric
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241altInsalPericfatRisco(SoftDeletionModel):

    s2241_altinsalperic_infoamb = models.ForeignKey('s2241.s2241altInsalPericinfoamb', 
        related_name='%(class)s_s2241_altinsalperic_infoamb', )
    
    def evento(self): 
        return self.s2241_altinsalperic_infoamb.evento()
    codfatris = models.TextField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2241_altinsalperic_fatrisco'       
        managed = True # s2241_altinsalperic_fatrisco #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altInsalPericfatRisco", u"Pode ver listagem do modelo S2241ALTINSALPERICFATRISCO"),
            ("can_see_data_s2241altInsalPericfatRisco", u"Pode visualizar o conteúdo do modelo S2241ALTINSALPERICFATRISCO"),
            ("can_see_menu_s2241altInsalPericfatRisco", u"Pode visualizar no menu o modelo S2241ALTINSALPERICFATRISCO"),
            ("can_print_list_s2241altInsalPericfatRisco", u"Pode imprimir listagem do modelo S2241ALTINSALPERICFATRISCO"),
            ("can_print_data_s2241altInsalPericfatRisco", u"Pode imprimir o conteúdo do modelo S2241ALTINSALPERICFATRISCO"), )
            
        ordering = [
            's2241_altinsalperic_infoamb',
            'codfatris',]



class s2241altInsalPericfatRiscoSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altInsalPericfatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241altInsalPericinfoamb(SoftDeletionModel):

    s2241_altinsalperic = models.ForeignKey('s2241.s2241altInsalPeric', 
        related_name='%(class)s_s2241_altinsalperic', )
    
    def evento(self): 
        return self.s2241_altinsalperic.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações sobre as condições de trabalho insalubre/periculoso.'
        db_table = r's2241_altinsalperic_infoamb'       
        managed = True # s2241_altinsalperic_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241altInsalPericinfoamb", u"Pode ver listagem do modelo S2241ALTINSALPERICINFOAMB"),
            ("can_see_data_s2241altInsalPericinfoamb", u"Pode visualizar o conteúdo do modelo S2241ALTINSALPERICINFOAMB"),
            ("can_see_menu_s2241altInsalPericinfoamb", u"Pode visualizar no menu o modelo S2241ALTINSALPERICINFOAMB"),
            ("can_print_list_s2241altInsalPericinfoamb", u"Pode imprimir listagem do modelo S2241ALTINSALPERICINFOAMB"),
            ("can_print_data_s2241altInsalPericinfoamb", u"Pode imprimir o conteúdo do modelo S2241ALTINSALPERICINFOAMB"), )
            
        ordering = [
            's2241_altinsalperic',
            'codamb',]



class s2241altInsalPericinfoambSerializer(ModelSerializer):

    class Meta:
    
        model = s2241altInsalPericinfoamb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241aposentEsp(SoftDeletionModel):

    s2241_evtinsapo = models.ForeignKey('esocial.s2241evtInsApo', 
        related_name='%(class)s_s2241_evtinsapo', )
    
    def evento(self): 
        return self.s2241_evtinsapo.evento()
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações sobre o trabalho exercido em condições que ensejam a aposentadoria especial.'
        db_table = r's2241_aposentesp'       
        managed = True # s2241_aposentesp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241aposentEsp", u"Pode ver listagem do modelo S2241APOSENTESP"),
            ("can_see_data_s2241aposentEsp", u"Pode visualizar o conteúdo do modelo S2241APOSENTESP"),
            ("can_see_menu_s2241aposentEsp", u"Pode visualizar no menu o modelo S2241APOSENTESP"),
            ("can_print_list_s2241aposentEsp", u"Pode imprimir listagem do modelo S2241APOSENTESP"),
            ("can_print_data_s2241aposentEsp", u"Pode imprimir o conteúdo do modelo S2241APOSENTESP"), )
            
        ordering = [
            's2241_evtinsapo',]



class s2241aposentEspSerializer(ModelSerializer):

    class Meta:
    
        model = s2241aposentEsp
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241fimAposentEsp(SoftDeletionModel):

    s2241_aposentesp = models.ForeignKey('s2241.s2241aposentEsp', 
        related_name='%(class)s_s2241_aposentesp', )
    
    def evento(self): 
        return self.s2241_aposentesp.evento()
    dtfimcondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho que ensejam aposentadoria especial - Término'
        db_table = r's2241_fimaposentesp'       
        managed = True # s2241_fimaposentesp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241fimAposentEsp", u"Pode ver listagem do modelo S2241FIMAPOSENTESP"),
            ("can_see_data_s2241fimAposentEsp", u"Pode visualizar o conteúdo do modelo S2241FIMAPOSENTESP"),
            ("can_see_menu_s2241fimAposentEsp", u"Pode visualizar no menu o modelo S2241FIMAPOSENTESP"),
            ("can_print_list_s2241fimAposentEsp", u"Pode imprimir listagem do modelo S2241FIMAPOSENTESP"),
            ("can_print_data_s2241fimAposentEsp", u"Pode imprimir o conteúdo do modelo S2241FIMAPOSENTESP"), )
            
        ordering = [
            's2241_aposentesp',
            'dtfimcondicao',]



class s2241fimAposentEspSerializer(ModelSerializer):

    class Meta:
    
        model = s2241fimAposentEsp
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241fimAposentEspinfoAmb(SoftDeletionModel):

    s2241_fimaposentesp = models.ForeignKey('s2241.s2241fimAposentEsp', 
        related_name='%(class)s_s2241_fimaposentesp', )
    
    def evento(self): 
        return self.s2241_fimaposentesp.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2241_fimaposentesp_infoamb'       
        managed = True # s2241_fimaposentesp_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241fimAposentEspinfoAmb", u"Pode ver listagem do modelo S2241FIMAPOSENTESPINFOAMB"),
            ("can_see_data_s2241fimAposentEspinfoAmb", u"Pode visualizar o conteúdo do modelo S2241FIMAPOSENTESPINFOAMB"),
            ("can_see_menu_s2241fimAposentEspinfoAmb", u"Pode visualizar no menu o modelo S2241FIMAPOSENTESPINFOAMB"),
            ("can_print_list_s2241fimAposentEspinfoAmb", u"Pode imprimir listagem do modelo S2241FIMAPOSENTESPINFOAMB"),
            ("can_print_data_s2241fimAposentEspinfoAmb", u"Pode imprimir o conteúdo do modelo S2241FIMAPOSENTESPINFOAMB"), )
            
        ordering = [
            's2241_fimaposentesp',
            'codamb',]



class s2241fimAposentEspinfoAmbSerializer(ModelSerializer):

    class Meta:
    
        model = s2241fimAposentEspinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241fimInsalPeric(SoftDeletionModel):

    s2241_insalperic = models.ForeignKey('s2241.s2241insalPeric', 
        related_name='%(class)s_s2241_insalperic', )
    
    def evento(self): 
        return self.s2241_insalperic.evento()
    dtfimcondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho insalubre/periculoso - Fim'
        db_table = r's2241_fiminsalperic'       
        managed = True # s2241_fiminsalperic #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241fimInsalPeric", u"Pode ver listagem do modelo S2241FIMINSALPERIC"),
            ("can_see_data_s2241fimInsalPeric", u"Pode visualizar o conteúdo do modelo S2241FIMINSALPERIC"),
            ("can_see_menu_s2241fimInsalPeric", u"Pode visualizar no menu o modelo S2241FIMINSALPERIC"),
            ("can_print_list_s2241fimInsalPeric", u"Pode imprimir listagem do modelo S2241FIMINSALPERIC"),
            ("can_print_data_s2241fimInsalPeric", u"Pode imprimir o conteúdo do modelo S2241FIMINSALPERIC"), )
            
        ordering = [
            's2241_insalperic',
            'dtfimcondicao',]



class s2241fimInsalPericSerializer(ModelSerializer):

    class Meta:
    
        model = s2241fimInsalPeric
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241fimInsalPericinfoAmb(SoftDeletionModel):

    s2241_fiminsalperic = models.ForeignKey('s2241.s2241fimInsalPeric', 
        related_name='%(class)s_s2241_fiminsalperic', )
    
    def evento(self): 
        return self.s2241_fiminsalperic.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2241_fiminsalperic_infoamb'       
        managed = True # s2241_fiminsalperic_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241fimInsalPericinfoAmb", u"Pode ver listagem do modelo S2241FIMINSALPERICINFOAMB"),
            ("can_see_data_s2241fimInsalPericinfoAmb", u"Pode visualizar o conteúdo do modelo S2241FIMINSALPERICINFOAMB"),
            ("can_see_menu_s2241fimInsalPericinfoAmb", u"Pode visualizar no menu o modelo S2241FIMINSALPERICINFOAMB"),
            ("can_print_list_s2241fimInsalPericinfoAmb", u"Pode imprimir listagem do modelo S2241FIMINSALPERICINFOAMB"),
            ("can_print_data_s2241fimInsalPericinfoAmb", u"Pode imprimir o conteúdo do modelo S2241FIMINSALPERICINFOAMB"), )
            
        ordering = [
            's2241_fiminsalperic',
            'codamb',]



class s2241fimInsalPericinfoAmbSerializer(ModelSerializer):

    class Meta:
    
        model = s2241fimInsalPericinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniAposentEsp(SoftDeletionModel):

    s2241_aposentesp = models.ForeignKey('s2241.s2241aposentEsp', 
        related_name='%(class)s_s2241_aposentesp', )
    
    def evento(self): 
        return self.s2241_aposentesp.evento()
    dtinicondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho que ensejam aposentadoria especial - Início'
        db_table = r's2241_iniaposentesp'       
        managed = True # s2241_iniaposentesp #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniAposentEsp", u"Pode ver listagem do modelo S2241INIAPOSENTESP"),
            ("can_see_data_s2241iniAposentEsp", u"Pode visualizar o conteúdo do modelo S2241INIAPOSENTESP"),
            ("can_see_menu_s2241iniAposentEsp", u"Pode visualizar no menu o modelo S2241INIAPOSENTESP"),
            ("can_print_list_s2241iniAposentEsp", u"Pode imprimir listagem do modelo S2241INIAPOSENTESP"),
            ("can_print_data_s2241iniAposentEsp", u"Pode imprimir o conteúdo do modelo S2241INIAPOSENTESP"), )
            
        ordering = [
            's2241_aposentesp',
            'dtinicondicao',]



class s2241iniAposentEspSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniAposentEsp
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniAposentEspfatRisco(SoftDeletionModel):

    s2241_iniaposentesp_infoamb = models.ForeignKey('s2241.s2241iniAposentEspinfoAmb', 
        related_name='%(class)s_s2241_iniaposentesp_infoamb', )
    
    def evento(self): 
        return self.s2241_iniaposentesp_infoamb.evento()
    codfatris = models.TextField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2241_iniaposentesp_fatrisco'       
        managed = True # s2241_iniaposentesp_fatrisco #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniAposentEspfatRisco", u"Pode ver listagem do modelo S2241INIAPOSENTESPFATRISCO"),
            ("can_see_data_s2241iniAposentEspfatRisco", u"Pode visualizar o conteúdo do modelo S2241INIAPOSENTESPFATRISCO"),
            ("can_see_menu_s2241iniAposentEspfatRisco", u"Pode visualizar no menu o modelo S2241INIAPOSENTESPFATRISCO"),
            ("can_print_list_s2241iniAposentEspfatRisco", u"Pode imprimir listagem do modelo S2241INIAPOSENTESPFATRISCO"),
            ("can_print_data_s2241iniAposentEspfatRisco", u"Pode imprimir o conteúdo do modelo S2241INIAPOSENTESPFATRISCO"), )
            
        ordering = [
            's2241_iniaposentesp_infoamb',
            'codfatris',]



class s2241iniAposentEspfatRiscoSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniAposentEspfatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniAposentEspinfoAmb(SoftDeletionModel):

    s2241_iniaposentesp = models.ForeignKey('s2241.s2241iniAposentEsp', 
        related_name='%(class)s_s2241_iniaposentesp', )
    
    def evento(self): 
        return self.s2241_iniaposentesp.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2241_iniaposentesp_infoamb'       
        managed = True # s2241_iniaposentesp_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniAposentEspinfoAmb", u"Pode ver listagem do modelo S2241INIAPOSENTESPINFOAMB"),
            ("can_see_data_s2241iniAposentEspinfoAmb", u"Pode visualizar o conteúdo do modelo S2241INIAPOSENTESPINFOAMB"),
            ("can_see_menu_s2241iniAposentEspinfoAmb", u"Pode visualizar no menu o modelo S2241INIAPOSENTESPINFOAMB"),
            ("can_print_list_s2241iniAposentEspinfoAmb", u"Pode imprimir listagem do modelo S2241INIAPOSENTESPINFOAMB"),
            ("can_print_data_s2241iniAposentEspinfoAmb", u"Pode imprimir o conteúdo do modelo S2241INIAPOSENTESPINFOAMB"), )
            
        ordering = [
            's2241_iniaposentesp',
            'codamb',]



class s2241iniAposentEspinfoAmbSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniAposentEspinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniInsalPeric(SoftDeletionModel):

    s2241_insalperic = models.ForeignKey('s2241.s2241insalPeric', 
        related_name='%(class)s_s2241_insalperic', )
    
    def evento(self): 
        return self.s2241_insalperic.evento()
    dtinicondicao = models.DateField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Condições do ambiente de trabalho insalubre/periculoso - Início'
        db_table = r's2241_iniinsalperic'       
        managed = True # s2241_iniinsalperic #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniInsalPeric", u"Pode ver listagem do modelo S2241INIINSALPERIC"),
            ("can_see_data_s2241iniInsalPeric", u"Pode visualizar o conteúdo do modelo S2241INIINSALPERIC"),
            ("can_see_menu_s2241iniInsalPeric", u"Pode visualizar no menu o modelo S2241INIINSALPERIC"),
            ("can_print_list_s2241iniInsalPeric", u"Pode imprimir listagem do modelo S2241INIINSALPERIC"),
            ("can_print_data_s2241iniInsalPeric", u"Pode imprimir o conteúdo do modelo S2241INIINSALPERIC"), )
            
        ordering = [
            's2241_insalperic',
            'dtinicondicao',]



class s2241iniInsalPericSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniInsalPeric
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniInsalPericfatRisco(SoftDeletionModel):

    s2241_iniinsalperic_infoamb = models.ForeignKey('s2241.s2241iniInsalPericinfoAmb', 
        related_name='%(class)s_s2241_iniinsalperic_infoamb', )
    
    def evento(self): 
        return self.s2241_iniinsalperic_infoamb.evento()
    codfatris = models.TextField(null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Fator de risco ao qual o trabalhador está exposto na atividade exercida no ambiente'
        db_table = r's2241_iniinsalperic_fatrisco'       
        managed = True # s2241_iniinsalperic_fatrisco #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniInsalPericfatRisco", u"Pode ver listagem do modelo S2241INIINSALPERICFATRISCO"),
            ("can_see_data_s2241iniInsalPericfatRisco", u"Pode visualizar o conteúdo do modelo S2241INIINSALPERICFATRISCO"),
            ("can_see_menu_s2241iniInsalPericfatRisco", u"Pode visualizar no menu o modelo S2241INIINSALPERICFATRISCO"),
            ("can_print_list_s2241iniInsalPericfatRisco", u"Pode imprimir listagem do modelo S2241INIINSALPERICFATRISCO"),
            ("can_print_data_s2241iniInsalPericfatRisco", u"Pode imprimir o conteúdo do modelo S2241INIINSALPERICFATRISCO"), )
            
        ordering = [
            's2241_iniinsalperic_infoamb',
            'codfatris',]



class s2241iniInsalPericfatRiscoSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniInsalPericfatRisco
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241iniInsalPericinfoAmb(SoftDeletionModel):

    s2241_iniinsalperic = models.ForeignKey('s2241.s2241iniInsalPeric', 
        related_name='%(class)s_s2241_iniinsalperic', )
    
    def evento(self): 
        return self.s2241_iniinsalperic.evento()
    codamb = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao ambiente de trabalho'
        db_table = r's2241_iniinsalperic_infoamb'       
        managed = True # s2241_iniinsalperic_infoamb #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241iniInsalPericinfoAmb", u"Pode ver listagem do modelo S2241INIINSALPERICINFOAMB"),
            ("can_see_data_s2241iniInsalPericinfoAmb", u"Pode visualizar o conteúdo do modelo S2241INIINSALPERICINFOAMB"),
            ("can_see_menu_s2241iniInsalPericinfoAmb", u"Pode visualizar no menu o modelo S2241INIINSALPERICINFOAMB"),
            ("can_print_list_s2241iniInsalPericinfoAmb", u"Pode imprimir listagem do modelo S2241INIINSALPERICINFOAMB"),
            ("can_print_data_s2241iniInsalPericinfoAmb", u"Pode imprimir o conteúdo do modelo S2241INIINSALPERICINFOAMB"), )
            
        ordering = [
            's2241_iniinsalperic',
            'codamb',]



class s2241iniInsalPericinfoAmbSerializer(ModelSerializer):

    class Meta:
    
        model = s2241iniInsalPericinfoAmb
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2241insalPeric(SoftDeletionModel):

    s2241_evtinsapo = models.ForeignKey('esocial.s2241evtInsApo', 
        related_name='%(class)s_s2241_evtinsapo', )
    
    def evento(self): 
        return self.s2241_evtinsapo.evento()
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações sobre o ambiente de trabalho insalubre/periculoso.'
        db_table = r's2241_insalperic'       
        managed = True # s2241_insalperic #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2241insalPeric", u"Pode ver listagem do modelo S2241INSALPERIC"),
            ("can_see_data_s2241insalPeric", u"Pode visualizar o conteúdo do modelo S2241INSALPERIC"),
            ("can_see_menu_s2241insalPeric", u"Pode visualizar no menu o modelo S2241INSALPERIC"),
            ("can_print_list_s2241insalPeric", u"Pode imprimir listagem do modelo S2241INSALPERIC"),
            ("can_print_data_s2241insalPeric", u"Pode imprimir o conteúdo do modelo S2241INSALPERIC"), )
            
        ordering = [
            's2241_evtinsapo',]



class s2241insalPericSerializer(ModelSerializer):

    class Meta:
    
        model = s2241insalPeric
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')