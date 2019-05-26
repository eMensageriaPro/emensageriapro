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
from emensageriapro.s2200.choices import *
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





class s2200CNH(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nrregcnh = models.CharField(max_length=12, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    ufcnh = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    dtvalid = models.DateField(null=True, )
    dtprihab = models.DateField(blank=True, null=True, )
    categoriacnh = models.CharField(choices=CHOICES_S2200_CATEGORIACNH, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nrregcnh),
            unicode(self.ufcnh),
            unicode(self.dtvalid),
            unicode(self.categoriacnh),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da Carteira Nacional de Habilitação (CNH)'
        db_table = r's2200_cnh'       
        managed = True # s2200_cnh #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_cnh", "Can view s2200_cnh"), )
            
        ordering = [
            's2200_documentos',
            'nrregcnh',
            'ufcnh',
            'dtvalid',
            'categoriacnh',]



class s2200CNHSerializer(ModelSerializer):

    class Meta:
    
        model = s2200CNH
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200CTPS(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nrctps = models.CharField(max_length=11, null=True, )
    seriectps = models.CharField(max_length=5, null=True, )
    ufctps = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nrctps),
            unicode(self.seriectps),
            unicode(self.ufctps),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações da Carteira de Trabalho e Previdência Social'
        db_table = r's2200_ctps'       
        managed = True # s2200_ctps #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_ctps", "Can view s2200_ctps"), )
            
        ordering = [
            's2200_documentos',
            'nrctps',
            'seriectps',
            'ufctps',]



class s2200CTPSSerializer(ModelSerializer):

    class Meta:
    
        model = s2200CTPS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200OC(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nroc = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    dtvalid = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nroc),
            unicode(self.orgaoemissor),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do número de registro em Órgão de Classe (OC)'
        db_table = r's2200_oc'       
        managed = True # s2200_oc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_oc", "Can view s2200_oc"), )
            
        ordering = [
            's2200_documentos',
            'nroc',
            'orgaoemissor',]



class s2200OCSerializer(ModelSerializer):

    class Meta:
    
        model = s2200OC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200RG(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nrrg = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nrrg),
            unicode(self.orgaoemissor),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Registro Geral (RG)'
        db_table = r's2200_rg'       
        managed = True # s2200_rg #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_rg", "Can view s2200_rg"), )
            
        ordering = [
            's2200_documentos',
            'nrrg',
            'orgaoemissor',]



class s2200RGSerializer(ModelSerializer):

    class Meta:
    
        model = s2200RG
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200RIC(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nrric = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nrric),
            unicode(self.orgaoemissor),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Documento Nacional de Identidade - DNI (Registro de Identificação Civil - RIC)'
        db_table = r's2200_ric'       
        managed = True # s2200_ric #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_ric", "Can view s2200_ric"), )
            
        ordering = [
            's2200_documentos',
            'nrric',
            'orgaoemissor',]



class s2200RICSerializer(ModelSerializer):

    class Meta:
    
        model = s2200RIC
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200RNE(SoftDeletionModel):

    s2200_documentos = models.ForeignKey('s2200.s2200documentos', 
        related_name='%(class)s_s2200_documentos', )
    
    def evento(self): 
        return self.s2200_documentos.evento()
    nrrne = models.CharField(max_length=14, null=True, )
    orgaoemissor = models.CharField(max_length=20, null=True, )
    dtexped = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_documentos),
            unicode(self.nrrne),
            unicode(self.orgaoemissor),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Registro Nacional de Estrangeiro'
        db_table = r's2200_rne'       
        managed = True # s2200_rne #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_rne", "Can view s2200_rne"), )
            
        ordering = [
            's2200_documentos',
            'nrrne',
            'orgaoemissor',]



class s2200RNESerializer(ModelSerializer):

    class Meta:
    
        model = s2200RNE
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200afastamento(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    dtiniafast = models.DateField(null=True, )
    codmotafast = models.CharField(choices=CHOICES_S2200_CODMOTAFAST, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.dtiniafast),
            unicode(self.codmotafast),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de afastamento do trabalhador'
        db_table = r's2200_afastamento'       
        managed = True # s2200_afastamento #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_afastamento", "Can view s2200_afastamento"), )
            
        ordering = [
            's2200_evtadmissao',
            'dtiniafast',
            'codmotafast',]



class s2200afastamentoSerializer(ModelSerializer):

    class Meta:
    
        model = s2200afastamento
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200alvaraJudicial(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
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
            unicode(self.s2200_evtadmissao),
            unicode(self.nrprocjud),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do alvará judicial em caso de contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e menores de 16, em categoria diferente de 'Aprendiz'.'
        db_table = r's2200_alvarajudicial'       
        managed = True # s2200_alvarajudicial #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_alvarajudicial", "Can view s2200_alvarajudicial"), )
            
        ordering = [
            's2200_evtadmissao',
            'nrprocjud',]



class s2200alvaraJudicialSerializer(ModelSerializer):

    class Meta:
    
        model = s2200alvaraJudicial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200aposentadoria(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    trabaposent = models.CharField(choices=CHOICES_S2200_TRABAPOSENT, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.trabaposent),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação de aposentadoria do trabalhador'
        db_table = r's2200_aposentadoria'       
        managed = True # s2200_aposentadoria #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_aposentadoria", "Can view s2200_aposentadoria"), )
            
        ordering = [
            's2200_evtadmissao',
            'trabaposent',]



class s2200aposentadoriaSerializer(ModelSerializer):

    class Meta:
    
        model = s2200aposentadoria
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200aprend(SoftDeletionModel):

    s2200_infoceletista = models.ForeignKey('s2200.s2200infoCeletista', 
        related_name='%(class)s_s2200_infoceletista', )
    
    def evento(self): 
        return self.s2200_infoceletista.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_infoceletista),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações para identificação do empregador contratante de aprendiz'
        db_table = r's2200_aprend'       
        managed = True # s2200_aprend #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_aprend", "Can view s2200_aprend"), )
            
        ordering = [
            's2200_infoceletista',
            'tpinsc',
            'nrinsc',]



class s2200aprendSerializer(ModelSerializer):

    class Meta:
    
        model = s2200aprend
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200brasil(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tplograd),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.cep),
            unicode(self.codmunic),
            unicode(self.uf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Preenchimento obrigatório para trabalhador residente no Brasil.'
        db_table = r's2200_brasil'       
        managed = True # s2200_brasil #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_brasil", "Can view s2200_brasil"), )
            
        ordering = [
            's2200_evtadmissao',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2200brasilSerializer(ModelSerializer):

    class Meta:
    
        model = s2200brasil
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200cessao(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    dtinicessao = models.DateField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.dtinicessao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de cessão/exercício em outro órgão do trabalhador'
        db_table = r's2200_cessao'       
        managed = True # s2200_cessao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_cessao", "Can view s2200_cessao"), )
            
        ordering = [
            's2200_evtadmissao',
            'dtinicessao',]



class s2200cessaoSerializer(ModelSerializer):

    class Meta:
    
        model = s2200cessao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200contato(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True, )
    fonealternat = models.CharField(max_length=13, blank=True, null=True, )
    emailprinc = models.CharField(max_length=60, blank=True, null=True, )
    emailalternat = models.CharField(max_length=60, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de contato'
        db_table = r's2200_contato'       
        managed = True # s2200_contato #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_contato", "Can view s2200_contato"), )
            
        ordering = [
            's2200_evtadmissao',]



class s2200contatoSerializer(ModelSerializer):

    class Meta:
    
        model = s2200contato
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200dependente(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    tpdep = models.CharField(choices=CHOICES_S2200_TPDEP, max_length=2, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    sexodep = models.CharField(choices=CHOICES_S2200_SEXODEP, max_length=1, blank=True, null=True, )
    depirrf = models.CharField(choices=CHOICES_S2200_DEPIRRF, max_length=1, null=True, )
    depsf = models.CharField(choices=CHOICES_S2200_DEPSF, max_length=1, null=True, )
    inctrab = models.CharField(choices=CHOICES_S2200_INCTRAB, max_length=1, null=True, )
    depfinsprev = models.CharField(choices=CHOICES_S2200_DEPFINSPREV, max_length=1, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tpdep),
            unicode(self.nmdep),
            unicode(self.dtnascto),
            unicode(self.depirrf),
            unicode(self.depsf),
            unicode(self.inctrab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações dos dependentes'
        db_table = r's2200_dependente'       
        managed = True # s2200_dependente #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_dependente", "Can view s2200_dependente"), )
            
        ordering = [
            's2200_evtadmissao',
            'tpdep',
            'nmdep',
            'dtnascto',
            'depirrf',
            'depsf',
            'inctrab',]



class s2200dependenteSerializer(ModelSerializer):

    class Meta:
    
        model = s2200dependente
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200desligamento(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    dtdeslig = models.DateField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.dtdeslig),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do desligamento do trabalhador'
        db_table = r's2200_desligamento'       
        managed = True # s2200_desligamento #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_desligamento", "Can view s2200_desligamento"), )
            
        ordering = [
            's2200_evtadmissao',
            'dtdeslig',]



class s2200desligamentoSerializer(ModelSerializer):

    class Meta:
    
        model = s2200desligamento
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200documentos(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações dos documentos pessoais do trabalhador'
        db_table = r's2200_documentos'       
        managed = True # s2200_documentos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_documentos", "Can view s2200_documentos"), )
            
        ordering = [
            's2200_evtadmissao',]



class s2200documentosSerializer(ModelSerializer):

    class Meta:
    
        model = s2200documentos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200exterior(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    paisresid = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    nmcid = models.CharField(max_length=50, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.paisresid),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.nmcid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Preenchido em caso de trabalhador residente no exterior.'
        db_table = r's2200_exterior'       
        managed = True # s2200_exterior #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_exterior", "Can view s2200_exterior"), )
            
        ordering = [
            's2200_evtadmissao',
            'paisresid',
            'dsclograd',
            'nrlograd',
            'nmcid',]



class s2200exteriorSerializer(ModelSerializer):

    class Meta:
    
        model = s2200exterior
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200filiacaoSindical(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    cnpjsindtrab = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.cnpjsindtrab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Filiação Sindical do Trabalhador'
        db_table = r's2200_filiacaosindical'       
        managed = True # s2200_filiacaosindical #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_filiacaosindical", "Can view s2200_filiacaosindical"), )
            
        ordering = [
            's2200_evtadmissao',
            'cnpjsindtrab',]



class s2200filiacaoSindicalSerializer(ModelSerializer):

    class Meta:
    
        model = s2200filiacaoSindical
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200horContratual(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    tpjornada = models.IntegerField(choices=CHOICES_S2200_TPJORNADA, null=True, )
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True, )
    tmpparc = models.IntegerField(choices=CHOICES_S2200_TMPPARC, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tpjornada),
            unicode(self.tmpparc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Horário Contratual do Trabalhador. O preenchimento é obrigatório se {tpRegJor} = [1].'
        db_table = r's2200_horcontratual'       
        managed = True # s2200_horcontratual #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_horcontratual", "Can view s2200_horcontratual"), )
            
        ordering = [
            's2200_evtadmissao',
            'tpjornada',
            'tmpparc',]



class s2200horContratualSerializer(ModelSerializer):

    class Meta:
    
        model = s2200horContratual
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200horario(SoftDeletionModel):

    s2200_horcontratual = models.ForeignKey('s2200.s2200horContratual', 
        related_name='%(class)s_s2200_horcontratual', )
    
    def evento(self): 
        return self.s2200_horcontratual.evento()
    dia = models.IntegerField(choices=CHOICES_S2200_DIA, null=True, )
    codhorcontrat = models.CharField(max_length=30, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_horcontratual),
            unicode(self.dia),
            unicode(self.codhorcontrat),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações diárias do horário contratual'
        db_table = r's2200_horario'       
        managed = True # s2200_horario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_horario", "Can view s2200_horario"), )
            
        ordering = [
            's2200_horcontratual',
            'dia',
            'codhorcontrat',]



class s2200horarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2200horario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200ideEstabVinc(SoftDeletionModel):

    s2200_trabtemporario = models.ForeignKey('s2200.s2200trabTemporario', 
        related_name='%(class)s_s2200_trabtemporario', )
    
    def evento(self): 
        return self.s2200_trabtemporario.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_trabtemporario),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do estabelecimento ao qual o trabalhador temporário está vinculado'
        db_table = r's2200_ideestabvinc'       
        managed = True # s2200_ideestabvinc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_ideestabvinc", "Can view s2200_ideestabvinc"), )
            
        ordering = [
            's2200_trabtemporario',
            'tpinsc',
            'nrinsc',]



class s2200ideEstabVincSerializer(ModelSerializer):

    class Meta:
    
        model = s2200ideEstabVinc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200ideTrabSubstituido(SoftDeletionModel):

    s2200_trabtemporario = models.ForeignKey('s2200.s2200trabTemporario', 
        related_name='%(class)s_s2200_trabtemporario', )
    
    def evento(self): 
        return self.s2200_trabtemporario.evento()
    cpftrabsubst = models.CharField(max_length=11, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_trabtemporario),
            unicode(self.cpftrabsubst),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do(s) trabalhador(es) substituído(s)'
        db_table = r's2200_idetrabsubstituido'       
        managed = True # s2200_idetrabsubstituido #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_idetrabsubstituido", "Can view s2200_idetrabsubstituido"), )
            
        ordering = [
            's2200_trabtemporario',
            'cpftrabsubst',]



class s2200ideTrabSubstituidoSerializer(ModelSerializer):

    class Meta:
    
        model = s2200ideTrabSubstituido
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200infoCeletista(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    dtadm = models.DateField(null=True, )
    tpadmissao = models.IntegerField(choices=CHOICES_S2200_TPADMISSAO, null=True, )
    indadmissao = models.IntegerField(choices=CHOICES_S2200_INDADMISSAO, null=True, )
    tpregjor = models.IntegerField(choices=CHOICES_S2200_TPREGJOR, null=True, )
    natatividade = models.IntegerField(choices=CHOICES_S2200_NATATIVIDADE, null=True, )
    dtbase = models.IntegerField(blank=True, null=True, )
    cnpjsindcategprof = models.CharField(max_length=14, null=True, )
    opcfgts = models.IntegerField(choices=CHOICES_S2200_OPCFGTS, null=True, )
    dtopcfgts = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.dtadm),
            unicode(self.tpadmissao),
            unicode(self.indadmissao),
            unicode(self.tpregjor),
            unicode(self.natatividade),
            unicode(self.cnpjsindcategprof),
            unicode(self.opcfgts),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Trabalhador Celetista'
        db_table = r's2200_infoceletista'       
        managed = True # s2200_infoceletista #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_infoceletista", "Can view s2200_infoceletista"), )
            
        ordering = [
            's2200_evtadmissao',
            'dtadm',
            'tpadmissao',
            'indadmissao',
            'tpregjor',
            'natatividade',
            'cnpjsindcategprof',
            'opcfgts',]



class s2200infoCeletistaSerializer(ModelSerializer):

    class Meta:
    
        model = s2200infoCeletista
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200infoDecJud(SoftDeletionModel):

    s2200_infoestatutario = models.ForeignKey('s2200.s2200infoEstatutario', 
        related_name='%(class)s_s2200_infoestatutario', )
    
    def evento(self): 
        return self.s2200_infoestatutario.evento()
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
            unicode(self.s2200_infoestatutario),
            unicode(self.nrprocjud),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre os dados da decisão judicial'
        db_table = r's2200_infodecjud'       
        managed = True # s2200_infodecjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_infodecjud", "Can view s2200_infodecjud"), )
            
        ordering = [
            's2200_infoestatutario',
            'nrprocjud',]



class s2200infoDecJudSerializer(ModelSerializer):

    class Meta:
    
        model = s2200infoDecJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200infoDeficiencia(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    deffisica = models.CharField(choices=CHOICES_S2200_DEFFISICA, max_length=1, null=True, )
    defvisual = models.CharField(choices=CHOICES_S2200_DEFVISUAL, max_length=1, null=True, )
    defauditiva = models.CharField(choices=CHOICES_S2200_DEFAUDITIVA, max_length=1, null=True, )
    defmental = models.CharField(choices=CHOICES_S2200_DEFMENTAL, max_length=1, null=True, )
    defintelectual = models.CharField(choices=CHOICES_S2200_DEFINTELECTUAL, max_length=1, null=True, )
    reabreadap = models.CharField(choices=CHOICES_S2200_REABREADAP, max_length=1, null=True, )
    infocota = models.CharField(choices=CHOICES_S2200_INFOCOTA, max_length=1, null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.deffisica),
            unicode(self.defvisual),
            unicode(self.defauditiva),
            unicode(self.defmental),
            unicode(self.defintelectual),
            unicode(self.reabreadap),
            unicode(self.infocota),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Pessoa com Deficiência'
        db_table = r's2200_infodeficiencia'       
        managed = True # s2200_infodeficiencia #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_infodeficiencia", "Can view s2200_infodeficiencia"), )
            
        ordering = [
            's2200_evtadmissao',
            'deffisica',
            'defvisual',
            'defauditiva',
            'defmental',
            'defintelectual',
            'reabreadap',
            'infocota',]



class s2200infoDeficienciaSerializer(ModelSerializer):

    class Meta:
    
        model = s2200infoDeficiencia
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200infoEstatutario(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    indprovim = models.IntegerField(choices=CHOICES_S2200_INDPROVIM, null=True, )
    tpprov = models.IntegerField(choices=CHOICES_S2200_TPPROV, null=True, )
    dtnomeacao = models.DateField(null=True, )
    dtposse = models.DateField(null=True, )
    dtexercicio = models.DateField(null=True, )
    dtingsvpub = models.DateField(null=True, )
    tpplanrp = models.IntegerField(choices=CHOICES_S2200_TPPLANRP, blank=True, null=True, )
    indtetorgps = models.CharField(choices=CHOICES_S2200_INDTETORGPS, max_length=1, blank=True, null=True, )
    indabonoperm = models.CharField(choices=CHOICES_S2200_INDABONOPERM, max_length=1, blank=True, null=True, )
    dtiniabono = models.DateField(blank=True, null=True, )
    indparcremun = models.CharField(choices=CHOICES_S2200_INDPARCREMUN, max_length=1, blank=True, null=True, )
    dtiniparc = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.indprovim),
            unicode(self.tpprov),
            unicode(self.dtnomeacao),
            unicode(self.dtposse),
            unicode(self.dtexercicio),
            unicode(self.dtingsvpub),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Trabalhador Estatutário'
        db_table = r's2200_infoestatutario'       
        managed = True # s2200_infoestatutario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_infoestatutario", "Can view s2200_infoestatutario"), )
            
        ordering = [
            's2200_evtadmissao',
            'indprovim',
            'tpprov',
            'dtnomeacao',
            'dtposse',
            'dtexercicio',
            'dtingsvpub',]



class s2200infoEstatutarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2200infoEstatutario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200localTrabDom(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tplograd),
            unicode(self.dsclograd),
            unicode(self.nrlograd),
            unicode(self.cep),
            unicode(self.codmunic),
            unicode(self.uf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em caso de trabalhador doméstico e trabalhador temporário, indicando o endereço onde o trabalhador exerce suas atividades.'
        db_table = r's2200_localtrabdom'       
        managed = True # s2200_localtrabdom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_localtrabdom", "Can view s2200_localtrabdom"), )
            
        ordering = [
            's2200_evtadmissao',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2200localTrabDomSerializer(ModelSerializer):

    class Meta:
    
        model = s2200localTrabDom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200localTrabGeral(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    desccomp = models.CharField(max_length=80, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador (exceto doméstico e temporário) exercerá suas atividades'
        db_table = r's2200_localtrabgeral'       
        managed = True # s2200_localtrabgeral #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_localtrabgeral", "Can view s2200_localtrabgeral"), )
            
        ordering = [
            's2200_evtadmissao',
            'tpinsc',
            'nrinsc',]



class s2200localTrabGeralSerializer(ModelSerializer):

    class Meta:
    
        model = s2200localTrabGeral
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200mudancaCPF(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    cpfant = models.CharField(max_length=11, null=True, )
    matricant = models.CharField(max_length=30, null=True, )
    dtaltcpf = models.DateField(null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.cpfant),
            unicode(self.matricant),
            unicode(self.dtaltcpf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de mudança de CPF do trabalhador.'
        db_table = r's2200_mudancacpf'       
        managed = True # s2200_mudancacpf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_mudancacpf", "Can view s2200_mudancacpf"), )
            
        ordering = [
            's2200_evtadmissao',
            'cpfant',
            'matricant',
            'dtaltcpf',]



class s2200mudancaCPFSerializer(ModelSerializer):

    class Meta:
    
        model = s2200mudancaCPF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200observacoes(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
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
            unicode(self.s2200_evtadmissao),
            unicode(self.observacao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Observações do contrato de trabalho'
        db_table = r's2200_observacoes'       
        managed = True # s2200_observacoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_observacoes", "Can view s2200_observacoes"), )
            
        ordering = [
            's2200_evtadmissao',
            'observacao',]



class s2200observacoesSerializer(ModelSerializer):

    class Meta:
    
        model = s2200observacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200sucessaoVinc(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    tpinscant = models.IntegerField(choices=CHOICES_S2200_TPINSCANT, null=True, )
    cnpjempregant = models.CharField(max_length=14, null=True, )
    matricant = models.CharField(max_length=30, blank=True, null=True, )
    dttransf = models.DateField(null=True, )
    observacao = models.CharField(max_length=255, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.tpinscant),
            unicode(self.cnpjempregant),
            unicode(self.dttransf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Grupo de informações da sucessão de vínculo trabalhista/estatutário'
        db_table = r's2200_sucessaovinc'       
        managed = True # s2200_sucessaovinc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_sucessaovinc", "Can view s2200_sucessaovinc"), )
            
        ordering = [
            's2200_evtadmissao',
            'tpinscant',
            'cnpjempregant',
            'dttransf',]



class s2200sucessaoVincSerializer(ModelSerializer):

    class Meta:
    
        model = s2200sucessaoVinc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200trabEstrangeiro(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    dtchegada = models.DateField(blank=True, null=True, )
    classtrabestrang = models.IntegerField(choices=CHOICES_S2200_CLASSTRABESTRANG, null=True, )
    casadobr = models.CharField(choices=CHOICES_S2200_CASADOBR, max_length=1, null=True, )
    filhosbr = models.CharField(choices=CHOICES_S2200_FILHOSBR, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.classtrabestrang),
            unicode(self.casadobr),
            unicode(self.filhosbr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Grupo de informações do Trabalhador Estrangeiro'
        db_table = r's2200_trabestrangeiro'       
        managed = True # s2200_trabestrangeiro #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_trabestrangeiro", "Can view s2200_trabestrangeiro"), )
            
        ordering = [
            's2200_evtadmissao',
            'classtrabestrang',
            'casadobr',
            'filhosbr',]



class s2200trabEstrangeiroSerializer(ModelSerializer):

    class Meta:
    
        model = s2200trabEstrangeiro
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200trabTemporario(SoftDeletionModel):

    s2200_infoceletista = models.ForeignKey('s2200.s2200infoCeletista', 
        related_name='%(class)s_s2200_infoceletista', )
    
    def evento(self): 
        return self.s2200_infoceletista.evento()
    hipleg = models.IntegerField(choices=CHOICES_S2200_HIPLEG, null=True, )
    justcontr = models.CharField(max_length=999, null=True, )
    tpinclcontr = models.IntegerField(choices=CHOICES_S2200_TPINCLCONTR, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_infoceletista),
            unicode(self.hipleg),
            unicode(self.justcontr),
            unicode(self.tpinclcontr),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Dados sobre trabalho temporário. Preenchimento obrigatório na contratação de trabalhador temporário.'
        db_table = r's2200_trabtemporario'       
        managed = True # s2200_trabtemporario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_trabtemporario", "Can view s2200_trabtemporario"), )
            
        ordering = [
            's2200_infoceletista',
            'hipleg',
            'justcontr',
            'tpinclcontr',
            'tpinsc',
            'nrinsc',]



class s2200trabTemporarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2200trabTemporario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2200transfDom(SoftDeletionModel):

    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao', 
        related_name='%(class)s_s2200_evtadmissao', )
    
    def evento(self): 
        return self.s2200_evtadmissao.evento()
    cpfsubstituido = models.CharField(max_length=11, null=True, )
    matricant = models.CharField(max_length=30, blank=True, null=True, )
    dttransf = models.DateField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2200_evtadmissao),
            unicode(self.cpfsubstituido),
            unicode(self.dttransf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do empregado doméstico transferido de outro representante da mesma unidade familiar'
        db_table = r's2200_transfdom'       
        managed = True # s2200_transfdom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2200_transfdom", "Can view s2200_transfdom"), )
            
        ordering = [
            's2200_evtadmissao',
            'cpfsubstituido',
            'dttransf',]



class s2200transfDomSerializer(ModelSerializer):

    class Meta:
    
        model = s2200transfDom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()