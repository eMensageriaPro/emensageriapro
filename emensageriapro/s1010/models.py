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
from emensageriapro.s1010.choices import *
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





class s1010alteracao(SoftDeletionModel):

    s1010_evttabrubrica = models.ForeignKey('esocial.s1010evtTabRubrica', 
        related_name='%(class)s_s1010_evttabrubrica', )
    
    def evento(self): 
        return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    dscrubr = models.CharField(max_length=100, null=True, )
    natrubr = models.IntegerField(null=True, )
    tprubr = models.IntegerField(choices=CHOICES_S1010_TPRUBR_ALTERACAO, null=True, )
    codinccp = models.TextField(null=True, )
    codincirrf = models.TextField(null=True, )
    codincfgts = models.CharField(choices=CHOICES_S1010_CODINCFGTS_ALTERACAO, max_length=2, null=True, )
    codincsind = models.CharField(choices=CHOICES_S1010_CODINCSIND_ALTERACAO, max_length=2, null=True, )
    codinccprp = models.TextField(blank=True, null=True, )
    tetoremun = models.CharField(choices=CHOICES_S1010_TETOREMUN_ALTERACAO, max_length=1, blank=True, null=True, )
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
            unicode(self.s1010_evttabrubrica),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.inivalid),
            unicode(self.dscrubr),
            unicode(self.natrubr),
            unicode(self.tprubr),
            unicode(self.codinccp),
            unicode(self.codincirrf),
            unicode(self.codincfgts),
            unicode(self.codincsind),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1010_alteracao'       
        managed = True # s1010_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao", "Can view s1010_alteracao"), )
            
        ordering = [
            's1010_evttabrubrica',
            'codrubr',
            'idetabrubr',
            'inivalid',
            'dscrubr',
            'natrubr',
            'tprubr',
            'codinccp',
            'codincirrf',
            'codincfgts',
            'codincsind',]



class s1010alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaoideProcessoCP(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_ALTERACAO, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_alteracao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.extdecisao),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo administrativo ou judicial com decisão/sentença favorável, determinando a não incidência de contribuição previdenciária relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_alteracao_ideprocessocp'       
        managed = True # s1010_alteracao_ideprocessocp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_ideprocessocp", "Can view s1010_alteracao_ideprocessocp"), )
            
        ordering = [
            's1010_alteracao',
            'tpproc',
            'nrproc',
            'extdecisao',
            'codsusp',]



class s1010alteracaoideProcessoCPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaoideProcessoCPRP(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_ALTERACAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_alteracao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.extdecisao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso o órgão público possua processo administrativo ou judicial com decisão/sentença favorável, determinando a não incidência de contribuição para RPPS/regime militar relativa à rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_alteracao_ideprocessocprp'       
        managed = True # s1010_alteracao_ideprocessocprp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_ideprocessocprp", "Can view s1010_alteracao_ideprocessocprp"), )
            
        ordering = [
            's1010_alteracao',
            'tpproc',
            'nrproc',
            'extdecisao',]



class s1010alteracaoideProcessoCPRPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoCPRP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaoideProcessoFGTS(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_alteracao),
            unicode(self.nrproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de FGTS relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_alteracao_ideprocessofgts'       
        managed = True # s1010_alteracao_ideprocessofgts #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_ideprocessofgts", "Can view s1010_alteracao_ideprocessofgts"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',]



class s1010alteracaoideProcessoFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaoideProcessoIRRF(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_alteracao),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de imposto de renda relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_alteracao_ideprocessoirrf'       
        managed = True # s1010_alteracao_ideprocessoirrf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_ideprocessoirrf", "Can view s1010_alteracao_ideprocessoirrf"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',
            'codsusp',]



class s1010alteracaoideProcessoIRRFSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoIRRF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaoideProcessoSIND(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_alteracao),
            unicode(self.nrproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de contribuição sindical relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_alteracao_ideprocessosind'       
        managed = True # s1010_alteracao_ideprocessosind #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_ideprocessosind", "Can view s1010_alteracao_ideprocessosind"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',]



class s1010alteracaoideProcessoSINDSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoSIND
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010alteracaonovaValidade(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
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
            unicode(self.s1010_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1010_alteracao_novavalidade'       
        managed = True # s1010_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_alteracao_novavalidade", "Can view s1010_alteracao_novavalidade"), )
            
        ordering = [
            's1010_alteracao',
            'inivalid',]



class s1010alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010exclusao(SoftDeletionModel):

    s1010_evttabrubrica = models.ForeignKey('esocial.s1010evtTabRubrica', 
        related_name='%(class)s_s1010_evttabrubrica', )
    
    def evento(self): 
        return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
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
            unicode(self.s1010_evttabrubrica),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1010_exclusao'       
        managed = True # s1010_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_exclusao", "Can view s1010_exclusao"), )
            
        ordering = [
            's1010_evttabrubrica',
            'codrubr',
            'idetabrubr',
            'inivalid',]



class s1010exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1010exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusao(SoftDeletionModel):

    s1010_evttabrubrica = models.ForeignKey('esocial.s1010evtTabRubrica', 
        related_name='%(class)s_s1010_evttabrubrica', )
    
    def evento(self): 
        return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    dscrubr = models.CharField(max_length=100, null=True, )
    natrubr = models.IntegerField(null=True, )
    tprubr = models.IntegerField(choices=CHOICES_S1010_TPRUBR_INCLUSAO, null=True, )
    codinccp = models.TextField(null=True, )
    codincirrf = models.TextField(null=True, )
    codincfgts = models.CharField(choices=CHOICES_S1010_CODINCFGTS_INCLUSAO, max_length=2, null=True, )
    codincsind = models.CharField(choices=CHOICES_S1010_CODINCSIND_INCLUSAO, max_length=2, null=True, )
    codinccprp = models.TextField(blank=True, null=True, )
    tetoremun = models.CharField(choices=CHOICES_S1010_TETOREMUN_INCLUSAO, max_length=1, blank=True, null=True, )
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
            unicode(self.s1010_evttabrubrica),
            unicode(self.codrubr),
            unicode(self.idetabrubr),
            unicode(self.inivalid),
            unicode(self.dscrubr),
            unicode(self.natrubr),
            unicode(self.tprubr),
            unicode(self.codinccp),
            unicode(self.codincirrf),
            unicode(self.codincfgts),
            unicode(self.codincsind),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1010_inclusao'       
        managed = True # s1010_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao", "Can view s1010_inclusao"), )
            
        ordering = [
            's1010_evttabrubrica',
            'codrubr',
            'idetabrubr',
            'inivalid',
            'dscrubr',
            'natrubr',
            'tprubr',
            'codinccp',
            'codincirrf',
            'codincfgts',
            'codincsind',]



class s1010inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusaoideProcessoCP(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_INCLUSAO, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_inclusao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.extdecisao),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo administrativo ou judicial com decisão/sentença favorável, determinando a não incidência de contribuição previdenciária relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_inclusao_ideprocessocp'       
        managed = True # s1010_inclusao_ideprocessocp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao_ideprocessocp", "Can view s1010_inclusao_ideprocessocp"), )
            
        ordering = [
            's1010_inclusao',
            'tpproc',
            'nrproc',
            'extdecisao',
            'codsusp',]



class s1010inclusaoideProcessoCPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusaoideProcessoCPRP(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_INCLUSAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_inclusao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.extdecisao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso o órgão público possua processo administrativo ou judicial com decisão/sentença favorável, determinando a não incidência de contribuição para RPPS/regime militar relativa à rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_inclusao_ideprocessocprp'       
        managed = True # s1010_inclusao_ideprocessocprp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao_ideprocessocprp", "Can view s1010_inclusao_ideprocessocprp"), )
            
        ordering = [
            's1010_inclusao',
            'tpproc',
            'nrproc',
            'extdecisao',]



class s1010inclusaoideProcessoCPRPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoCPRP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusaoideProcessoFGTS(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_inclusao),
            unicode(self.nrproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de FGTS relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_inclusao_ideprocessofgts'       
        managed = True # s1010_inclusao_ideprocessofgts #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao_ideprocessofgts", "Can view s1010_inclusao_ideprocessofgts"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',]



class s1010inclusaoideProcessoFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoFGTS
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusaoideProcessoIRRF(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_inclusao),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de imposto de renda relativo a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_inclusao_ideprocessoirrf'       
        managed = True # s1010_inclusao_ideprocessoirrf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao_ideprocessoirrf", "Can view s1010_inclusao_ideprocessoirrf"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',
            'codsusp',]



class s1010inclusaoideProcessoIRRFSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoIRRF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1010inclusaoideProcessoSIND(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1010_inclusao),
            unicode(self.nrproc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Caso a empresa possua processo judicial com decisão/sentença favorável, determinando a não incidência de contribuição sindical relativa a rubrica identificada no evento, as informações deverão ser incluídas neste registro, e o detalhamento do processo deverá ser efetuado através de evento específico na tabela de processos.'
        db_table = r's1010_inclusao_ideprocessosind'       
        managed = True # s1010_inclusao_ideprocessosind #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1010_inclusao_ideprocessosind", "Can view s1010_inclusao_ideprocessosind"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',]



class s1010inclusaoideProcessoSINDSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoSIND
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()