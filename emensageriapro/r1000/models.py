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
from emensageriapro.r1000.choices import *
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





class r1000alteracao(SoftDeletionModel):

    r1000_evtinfocontri = models.ForeignKey('efdreinf.r1000evtInfoContri', 
        related_name='%(class)s_r1000_evtinfocontri', )
    
    def evento(self): 
        return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    classtrib = models.CharField(choices=CHOICES_EFDREINFCLASSIFICACAOTRIBUTARIA, max_length=2, null=True, )
    indescrituracao = models.IntegerField(choices=CHOICES_R1000_INDESCRITURACAO_ALTERACAO, null=True, )
    inddesoneracao = models.IntegerField(choices=CHOICES_R1000_INDDESONERACAO_ALTERACAO, null=True, )
    indacordoisenmulta = models.IntegerField(choices=CHOICES_R1000_INDACORDOISENMULTA_ALTERACAO, null=True, )
    indsitpj = models.IntegerField(choices=CHOICES_R1000_INDSITPJ_ALTERACAO, blank=True, null=True, )
    nmctt = models.CharField(max_length=70, null=True, )
    cpfctt = models.CharField(max_length=11, null=True, )
    fonefixo = models.CharField(max_length=13, blank=True, null=True, )
    fonecel = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r'r1000_alteracao'       
        managed = True # r1000_alteracao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000alteracao", u"Pode ver listagem do modelo R1000ALTERACAO"),
            ("can_see_data_r1000alteracao", u"Pode visualizar o conteúdo do modelo R1000ALTERACAO"),
            ("can_see_menu_r1000alteracao", u"Pode visualizar no menu o modelo R1000ALTERACAO"),
            ("can_print_list_r1000alteracao", u"Pode imprimir listagem do modelo R1000ALTERACAO"),
            ("can_print_data_r1000alteracao", u"Pode imprimir o conteúdo do modelo R1000ALTERACAO"), )
            
        ordering = [
            'r1000_evtinfocontri',
            'inivalid',
            'classtrib',
            'indescrituracao',
            'inddesoneracao',
            'indacordoisenmulta',
            'nmctt',
            'cpfctt',]



class r1000alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000alteracaoinfoEFR(SoftDeletionModel):

    r1000_alteracao = models.ForeignKey('r1000.r1000alteracao', 
        related_name='%(class)s_r1000_alteracao', )
    
    def evento(self): 
        return self.r1000_alteracao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_IDEEFR_ALTERACAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR'
        db_table = r'r1000_alteracao_infoefr'       
        managed = True # r1000_alteracao_infoefr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000alteracaoinfoEFR", u"Pode ver listagem do modelo R1000ALTERACAOINFOEFR"),
            ("can_see_data_r1000alteracaoinfoEFR", u"Pode visualizar o conteúdo do modelo R1000ALTERACAOINFOEFR"),
            ("can_see_menu_r1000alteracaoinfoEFR", u"Pode visualizar no menu o modelo R1000ALTERACAOINFOEFR"),
            ("can_print_list_r1000alteracaoinfoEFR", u"Pode imprimir listagem do modelo R1000ALTERACAOINFOEFR"),
            ("can_print_data_r1000alteracaoinfoEFR", u"Pode imprimir o conteúdo do modelo R1000ALTERACAOINFOEFR"), )
            
        ordering = [
            'r1000_alteracao',
            'ideefr',]



class r1000alteracaoinfoEFRSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaoinfoEFR
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000alteracaonovaValidade(SoftDeletionModel):

    r1000_alteracao = models.ForeignKey('r1000.r1000alteracao', 
        related_name='%(class)s_r1000_alteracao', )
    
    def evento(self): 
        return self.r1000_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade'
        db_table = r'r1000_alteracao_novavalidade'       
        managed = True # r1000_alteracao_novavalidade #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000alteracaonovaValidade", u"Pode ver listagem do modelo R1000ALTERACAONOVAVALIDADE"),
            ("can_see_data_r1000alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo R1000ALTERACAONOVAVALIDADE"),
            ("can_see_menu_r1000alteracaonovaValidade", u"Pode visualizar no menu o modelo R1000ALTERACAONOVAVALIDADE"),
            ("can_print_list_r1000alteracaonovaValidade", u"Pode imprimir listagem do modelo R1000ALTERACAONOVAVALIDADE"),
            ("can_print_data_r1000alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo R1000ALTERACAONOVAVALIDADE"), )
            
        ordering = [
            'r1000_alteracao',
            'inivalid',]



class r1000alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000alteracaosoftHouse(SoftDeletionModel):

    r1000_alteracao = models.ForeignKey('r1000.r1000alteracao', 
        related_name='%(class)s_r1000_alteracao', )
    
    def evento(self): 
        return self.r1000_alteracao.evento()
    cnpjsofthouse = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=115, null=True, )
    nmcont = models.CharField(max_length=70, null=True, )
    telefone = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações da(s) empresa(s) desenvolvedora(s) da(s) aplicação(ões) que gera(m) os arquivos transmitidos para o ambiente nacional da EFD-Reinf.'
        db_table = r'r1000_alteracao_softhouse'       
        managed = True # r1000_alteracao_softhouse #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000alteracaosoftHouse", u"Pode ver listagem do modelo R1000ALTERACAOSOFTHOUSE"),
            ("can_see_data_r1000alteracaosoftHouse", u"Pode visualizar o conteúdo do modelo R1000ALTERACAOSOFTHOUSE"),
            ("can_see_menu_r1000alteracaosoftHouse", u"Pode visualizar no menu o modelo R1000ALTERACAOSOFTHOUSE"),
            ("can_print_list_r1000alteracaosoftHouse", u"Pode imprimir listagem do modelo R1000ALTERACAOSOFTHOUSE"),
            ("can_print_data_r1000alteracaosoftHouse", u"Pode imprimir o conteúdo do modelo R1000ALTERACAOSOFTHOUSE"), )
            
        ordering = [
            'r1000_alteracao',
            'cnpjsofthouse',
            'nmrazao',
            'nmcont',]



class r1000alteracaosoftHouseSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaosoftHouse
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000exclusao(SoftDeletionModel):

    r1000_evtinfocontri = models.ForeignKey('efdreinf.r1000evtInfoContri', 
        related_name='%(class)s_r1000_evtinfocontri', )
    
    def evento(self): 
        return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r'r1000_exclusao'       
        managed = True # r1000_exclusao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000exclusao", u"Pode ver listagem do modelo R1000EXCLUSAO"),
            ("can_see_data_r1000exclusao", u"Pode visualizar o conteúdo do modelo R1000EXCLUSAO"),
            ("can_see_menu_r1000exclusao", u"Pode visualizar no menu o modelo R1000EXCLUSAO"),
            ("can_print_list_r1000exclusao", u"Pode imprimir listagem do modelo R1000EXCLUSAO"),
            ("can_print_data_r1000exclusao", u"Pode imprimir o conteúdo do modelo R1000EXCLUSAO"), )
            
        ordering = [
            'r1000_evtinfocontri',
            'inivalid',]



class r1000exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1000exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000inclusao(SoftDeletionModel):

    r1000_evtinfocontri = models.ForeignKey('efdreinf.r1000evtInfoContri', 
        related_name='%(class)s_r1000_evtinfocontri', )
    
    def evento(self): 
        return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    classtrib = models.CharField(choices=CHOICES_EFDREINFCLASSIFICACAOTRIBUTARIA, max_length=2, null=True, )
    indescrituracao = models.IntegerField(choices=CHOICES_R1000_INDESCRITURACAO_INCLUSAO, null=True, )
    inddesoneracao = models.IntegerField(choices=CHOICES_R1000_INDDESONERACAO_INCLUSAO, null=True, )
    indacordoisenmulta = models.IntegerField(choices=CHOICES_R1000_INDACORDOISENMULTA_INCLUSAO, null=True, )
    indsitpj = models.IntegerField(choices=CHOICES_R1000_INDSITPJ_INCLUSAO, blank=True, null=True, )
    nmctt = models.CharField(max_length=70, null=True, )
    cpfctt = models.CharField(max_length=11, null=True, )
    fonefixo = models.CharField(max_length=13, blank=True, null=True, )
    fonecel = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r'r1000_inclusao'       
        managed = True # r1000_inclusao #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000inclusao", u"Pode ver listagem do modelo R1000INCLUSAO"),
            ("can_see_data_r1000inclusao", u"Pode visualizar o conteúdo do modelo R1000INCLUSAO"),
            ("can_see_menu_r1000inclusao", u"Pode visualizar no menu o modelo R1000INCLUSAO"),
            ("can_print_list_r1000inclusao", u"Pode imprimir listagem do modelo R1000INCLUSAO"),
            ("can_print_data_r1000inclusao", u"Pode imprimir o conteúdo do modelo R1000INCLUSAO"), )
            
        ordering = [
            'r1000_evtinfocontri',
            'inivalid',
            'classtrib',
            'indescrituracao',
            'inddesoneracao',
            'indacordoisenmulta',
            'nmctt',
            'cpfctt',]



class r1000inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1000inclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000inclusaoinfoEFR(SoftDeletionModel):

    r1000_inclusao = models.ForeignKey('r1000.r1000inclusao', 
        related_name='%(class)s_r1000_inclusao', )
    
    def evento(self): 
        return self.r1000_inclusao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_IDEEFR_INCLUSAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR'
        db_table = r'r1000_inclusao_infoefr'       
        managed = True # r1000_inclusao_infoefr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000inclusaoinfoEFR", u"Pode ver listagem do modelo R1000INCLUSAOINFOEFR"),
            ("can_see_data_r1000inclusaoinfoEFR", u"Pode visualizar o conteúdo do modelo R1000INCLUSAOINFOEFR"),
            ("can_see_menu_r1000inclusaoinfoEFR", u"Pode visualizar no menu o modelo R1000INCLUSAOINFOEFR"),
            ("can_print_list_r1000inclusaoinfoEFR", u"Pode imprimir listagem do modelo R1000INCLUSAOINFOEFR"),
            ("can_print_data_r1000inclusaoinfoEFR", u"Pode imprimir o conteúdo do modelo R1000INCLUSAOINFOEFR"), )
            
        ordering = [
            'r1000_inclusao',
            'ideefr',]



class r1000inclusaoinfoEFRSerializer(ModelSerializer):

    class Meta:
    
        model = r1000inclusaoinfoEFR
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class r1000inclusaosoftHouse(SoftDeletionModel):

    r1000_inclusao = models.ForeignKey('r1000.r1000inclusao', 
        related_name='%(class)s_r1000_inclusao', )
    
    def evento(self): 
        return self.r1000_inclusao.evento()
    cnpjsofthouse = models.CharField(max_length=14, null=True, )
    nmrazao = models.CharField(max_length=115, null=True, )
    nmcont = models.CharField(max_length=70, null=True, )
    telefone = models.CharField(max_length=13, blank=True, null=True, )
    email = models.CharField(max_length=60, blank=True, null=True, )
    
    def __unicode__(self):
        
        return self.evento['identidade']
        
    class Meta:
    
        # verbose_name = u'Informações da(s) empresa(s) desenvolvedora(s) da(s) aplicação(ões) que gera(m) os arquivos transmitidos para o ambiente nacional da EFD-Reinf.'
        db_table = r'r1000_inclusao_softhouse'       
        managed = True # r1000_inclusao_softhouse #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_r1000inclusaosoftHouse", u"Pode ver listagem do modelo R1000INCLUSAOSOFTHOUSE"),
            ("can_see_data_r1000inclusaosoftHouse", u"Pode visualizar o conteúdo do modelo R1000INCLUSAOSOFTHOUSE"),
            ("can_see_menu_r1000inclusaosoftHouse", u"Pode visualizar no menu o modelo R1000INCLUSAOSOFTHOUSE"),
            ("can_print_list_r1000inclusaosoftHouse", u"Pode imprimir listagem do modelo R1000INCLUSAOSOFTHOUSE"),
            ("can_print_data_r1000inclusaosoftHouse", u"Pode imprimir o conteúdo do modelo R1000INCLUSAOSOFTHOUSE"), )
            
        ordering = [
            'r1000_inclusao',
            'cnpjsofthouse',
            'nmrazao',
            'nmcont',]



class r1000inclusaosoftHouseSerializer(ModelSerializer):

    class Meta:
    
        model = r1000inclusaosoftHouse
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')