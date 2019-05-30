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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_evtinfocontri),
            unicode(self.inivalid),
            unicode(self.classtrib),
            unicode(self.indescrituracao),
            unicode(self.inddesoneracao),
            unicode(self.indacordoisenmulta),
            unicode(self.nmctt),
            unicode(self.cpfctt),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r'r1000_alteracao'       
        managed = True # r1000_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_alteracao", "Can view r1000_alteracao"), )
            
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
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1000alteracaoinfoEFR(SoftDeletionModel):

    r1000_alteracao = models.ForeignKey('r1000.r1000alteracao', 
        related_name='%(class)s_r1000_alteracao', )
    
    def evento(self): 
        return self.r1000_alteracao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_IDEEFR_ALTERACAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_alteracao),
            unicode(self.ideefr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR'
        db_table = r'r1000_alteracao_infoefr'       
        managed = True # r1000_alteracao_infoefr #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_alteracao_infoefr", "Can view r1000_alteracao_infoefr"), )
            
        ordering = [
            'r1000_alteracao',
            'ideefr',]



class r1000alteracaoinfoEFRSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaoinfoEFR
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1000alteracaonovaValidade(SoftDeletionModel):

    r1000_alteracao = models.ForeignKey('r1000.r1000alteracao', 
        related_name='%(class)s_r1000_alteracao', )
    
    def evento(self): 
        return self.r1000_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade'
        db_table = r'r1000_alteracao_novavalidade'       
        managed = True # r1000_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_alteracao_novavalidade", "Can view r1000_alteracao_novavalidade"), )
            
        ordering = [
            'r1000_alteracao',
            'inivalid',]



class r1000alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_alteracao),
            unicode(self.cnpjsofthouse),
            unicode(self.nmrazao),
            unicode(self.nmcont),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da(s) empresa(s) desenvolvedora(s) da(s) aplicação(ões) que gera(m) os arquivos transmitidos para o ambiente nacional da EFD-Reinf.'
        db_table = r'r1000_alteracao_softhouse'       
        managed = True # r1000_alteracao_softhouse #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_alteracao_softhouse", "Can view r1000_alteracao_softhouse"), )
            
        ordering = [
            'r1000_alteracao',
            'cnpjsofthouse',
            'nmrazao',
            'nmcont',]



class r1000alteracaosoftHouseSerializer(ModelSerializer):

    class Meta:
    
        model = r1000alteracaosoftHouse
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1000exclusao(SoftDeletionModel):

    r1000_evtinfocontri = models.ForeignKey('efdreinf.r1000evtInfoContri', 
        related_name='%(class)s_r1000_evtinfocontri', )
    
    def evento(self): 
        return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_evtinfocontri),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r'r1000_exclusao'       
        managed = True # r1000_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_exclusao", "Can view r1000_exclusao"), )
            
        ordering = [
            'r1000_evtinfocontri',
            'inivalid',]



class r1000exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1000exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_evtinfocontri),
            unicode(self.inivalid),
            unicode(self.classtrib),
            unicode(self.indescrituracao),
            unicode(self.inddesoneracao),
            unicode(self.indacordoisenmulta),
            unicode(self.nmctt),
            unicode(self.cpfctt),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r'r1000_inclusao'       
        managed = True # r1000_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_inclusao", "Can view r1000_inclusao"), )
            
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
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1000inclusaoinfoEFR(SoftDeletionModel):

    r1000_inclusao = models.ForeignKey('r1000.r1000inclusao', 
        related_name='%(class)s_r1000_inclusao', )
    
    def evento(self): 
        return self.r1000_inclusao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_IDEEFR_INCLUSAO, max_length=1, null=True, )
    cnpjefr = models.CharField(max_length=14, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_inclusao),
            unicode(self.ideefr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de órgãos públicos estaduais e municipais relativas a Ente Federativo Responsável - EFR'
        db_table = r'r1000_inclusao_infoefr'       
        managed = True # r1000_inclusao_infoefr #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_inclusao_infoefr", "Can view r1000_inclusao_infoefr"), )
            
        ordering = [
            'r1000_inclusao',
            'ideefr',]



class r1000inclusaoinfoEFRSerializer(ModelSerializer):

    class Meta:
    
        model = r1000inclusaoinfoEFR
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1000_inclusao),
            unicode(self.cnpjsofthouse),
            unicode(self.nmrazao),
            unicode(self.nmcont),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da(s) empresa(s) desenvolvedora(s) da(s) aplicação(ões) que gera(m) os arquivos transmitidos para o ambiente nacional da EFD-Reinf.'
        db_table = r'r1000_inclusao_softhouse'       
        managed = True # r1000_inclusao_softhouse #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1000_inclusao_softhouse", "Can view r1000_inclusao_softhouse"), )
            
        ordering = [
            'r1000_inclusao',
            'cnpjsofthouse',
            'nmrazao',
            'nmcont',]



class r1000inclusaosoftHouseSerializer(ModelSerializer):

    class Meta:
    
        model = r1000inclusaosoftHouse
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()