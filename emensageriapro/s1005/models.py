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
from emensageriapro.s1005.choices import *
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





class s1005alteracao(SoftDeletionModel):

    s1005_evttabestab = models.ForeignKey('esocial.s1005evtTabEstab', 
        related_name='%(class)s_s1005_evttabestab', )
    
    def evento(self): 
        return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_TPINSC_ALTERACAO, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    cnaeprep = models.IntegerField(null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S1005_ALIQRAT_ALTERACAO, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    regpt = models.IntegerField(choices=CHOICES_S1005_REGPT_ALTERACAO, null=True, )
    contapr = models.IntegerField(choices=CHOICES_S1005_CONTAPR_ALTERACAO, null=True, )
    nrprocjud = models.CharField(max_length=20, blank=True, null=True, )
    contented = models.CharField(choices=CHOICES_S1005_CONTENTED_ALTERACAO, max_length=1, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_evttabestab),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.inivalid),
            unicode(self.cnaeprep),
            unicode(self.aliqrat),
            unicode(self.regpt),
            unicode(self.contapr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1005_alteracao'       
        managed = True # s1005_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao", "Can view s1005_alteracao"), )
            
        ordering = [
            's1005_evttabestab',
            'tpinsc',
            'nrinsc',
            'inivalid',
            'cnaeprep',
            'aliqrat',
            'regpt',
            'contapr',]



class s1005alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoinfoCaepf(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
    tpcaepf = models.IntegerField(choices=CHOICES_S1005_TPCAEPF_ALTERACAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_alteracao),
            unicode(self.tpcaepf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao Cadastro da Atividade Econômica da Pessoa Física - CAEPF.'
        db_table = r's1005_alteracao_infocaepf'       
        managed = True # s1005_alteracao_infocaepf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_infocaepf", "Can view s1005_alteracao_infocaepf"), )
            
        ordering = [
            's1005_alteracao',
            'tpcaepf',]



class s1005alteracaoinfoCaepfSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoinfoCaepf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoinfoEntEduc(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
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
            unicode(self.s1005_alteracao),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação da(s) entidade(s) educativa(s) ou de prática desportiva'
        db_table = r's1005_alteracao_infoenteduc'       
        managed = True # s1005_alteracao_infoenteduc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_infoenteduc", "Can view s1005_alteracao_infoenteduc"), )
            
        ordering = [
            's1005_alteracao',
            'nrinsc',]



class s1005alteracaoinfoEntEducSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoinfoEntEduc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoinfoObra(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S1005_INDSUBSTPATROBRA_ALTERACAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_alteracao),
            unicode(self.indsubstpatrobra),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente por empresa construtora enquadrada nos Arts. 7 a 9 da Lei 12.546/2011, relacionando os estabelecimentos inscritos no CNO, para indicar a substituição ou não da contribuição patronal incidente sobre a remuneração dos trabalhadores de obra de construção civil.'
        db_table = r's1005_alteracao_infoobra'       
        managed = True # s1005_alteracao_infoobra #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_infoobra", "Can view s1005_alteracao_infoobra"), )
            
        ordering = [
            's1005_alteracao',
            'indsubstpatrobra',]



class s1005alteracaoinfoObraSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoinfoObra
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoinfoPCD(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
    contpcd = models.IntegerField(choices=CHOICES_S1005_CONTPCD_ALTERACAO, null=True, )
    nrprocjud = models.CharField(max_length=20, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_alteracao),
            unicode(self.contpcd),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a contratação de pessoa com deficiência (PCD). Essa informação deve ser prestada apenas no estabelecimento 'Matriz'.'
        db_table = r's1005_alteracao_infopcd'       
        managed = True # s1005_alteracao_infopcd #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_infopcd", "Can view s1005_alteracao_infopcd"), )
            
        ordering = [
            's1005_alteracao',
            'contpcd',]



class s1005alteracaoinfoPCDSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoinfoPCD
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaonovaValidade(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
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
            unicode(self.s1005_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1005_alteracao_novavalidade'       
        managed = True # s1005_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_novavalidade", "Can view s1005_alteracao_novavalidade"), )
            
        ordering = [
            's1005_alteracao',
            'inivalid',]



class s1005alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoprocAdmJudFap(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_TPPROC_ALTERACAO, null=True, )
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
            unicode(self.s1005_alteracao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica, em caso de existência, o processo administrativo/judicial em que houve decisão ou sentença favorável ao contribuinte suspendendo ou alterando a alíquota FAP aplicável ao contribuinte.'
        db_table = r's1005_alteracao_procadmjudfap'       
        managed = True # s1005_alteracao_procadmjudfap #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_procadmjudfap", "Can view s1005_alteracao_procadmjudfap"), )
            
        ordering = [
            's1005_alteracao',
            'tpproc',
            'nrproc',
            'codsusp',]



class s1005alteracaoprocAdmJudFapSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoprocAdmJudFap
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005alteracaoprocAdmJudRat(SoftDeletionModel):

    s1005_alteracao = models.ForeignKey('s1005.s1005alteracao', 
        related_name='%(class)s_s1005_alteracao', )
    
    def evento(self): 
        return self.s1005_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_TPPROC_ALTERACAO, null=True, )
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
            unicode(self.s1005_alteracao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica, em caso de existência, o processo administrativo ou judicial em que houve decisão/sentença favorável ao contribuinte modificando a alíquota RAT da empresa.'
        db_table = r's1005_alteracao_procadmjudrat'       
        managed = True # s1005_alteracao_procadmjudrat #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_alteracao_procadmjudrat", "Can view s1005_alteracao_procadmjudrat"), )
            
        ordering = [
            's1005_alteracao',
            'tpproc',
            'nrproc',
            'codsusp',]



class s1005alteracaoprocAdmJudRatSerializer(ModelSerializer):

    class Meta:
    
        model = s1005alteracaoprocAdmJudRat
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005exclusao(SoftDeletionModel):

    s1005_evttabestab = models.ForeignKey('esocial.s1005evtTabEstab', 
        related_name='%(class)s_s1005_evttabestab', )
    
    def evento(self): 
        return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_TPINSC_EXCLUSAO, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
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
            unicode(self.s1005_evttabestab),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1005_exclusao'       
        managed = True # s1005_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_exclusao", "Can view s1005_exclusao"), )
            
        ordering = [
            's1005_evttabestab',
            'tpinsc',
            'nrinsc',
            'inivalid',]



class s1005exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1005exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusao(SoftDeletionModel):

    s1005_evttabestab = models.ForeignKey('esocial.s1005evtTabEstab', 
        related_name='%(class)s_s1005_evttabestab', )
    
    def evento(self): 
        return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_TPINSC_INCLUSAO, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    cnaeprep = models.IntegerField(null=True, )
    aliqrat = models.IntegerField(choices=CHOICES_S1005_ALIQRAT_INCLUSAO, null=True, )
    fap = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    regpt = models.IntegerField(choices=CHOICES_S1005_REGPT_INCLUSAO, null=True, )
    contapr = models.IntegerField(choices=CHOICES_S1005_CONTAPR_INCLUSAO, null=True, )
    nrprocjud = models.CharField(max_length=20, blank=True, null=True, )
    contented = models.CharField(choices=CHOICES_S1005_CONTENTED_INCLUSAO, max_length=1, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_evttabestab),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.inivalid),
            unicode(self.cnaeprep),
            unicode(self.aliqrat),
            unicode(self.regpt),
            unicode(self.contapr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1005_inclusao'       
        managed = True # s1005_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao", "Can view s1005_inclusao"), )
            
        ordering = [
            's1005_evttabestab',
            'tpinsc',
            'nrinsc',
            'inivalid',
            'cnaeprep',
            'aliqrat',
            'regpt',
            'contapr',]



class s1005inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoinfoCaepf(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
    tpcaepf = models.IntegerField(choices=CHOICES_S1005_TPCAEPF_INCLUSAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_inclusao),
            unicode(self.tpcaepf),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao Cadastro da Atividade Econômica da Pessoa Física - CAEPF.'
        db_table = r's1005_inclusao_infocaepf'       
        managed = True # s1005_inclusao_infocaepf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_infocaepf", "Can view s1005_inclusao_infocaepf"), )
            
        ordering = [
            's1005_inclusao',
            'tpcaepf',]



class s1005inclusaoinfoCaepfSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoinfoCaepf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoinfoEntEduc(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
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
            unicode(self.s1005_inclusao),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação da(s) entidade(s) educativa(s) ou de prática desportiva'
        db_table = r's1005_inclusao_infoenteduc'       
        managed = True # s1005_inclusao_infoenteduc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_infoenteduc", "Can view s1005_inclusao_infoenteduc"), )
            
        ordering = [
            's1005_inclusao',
            'nrinsc',]



class s1005inclusaoinfoEntEducSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoinfoEntEduc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoinfoObra(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S1005_INDSUBSTPATROBRA_INCLUSAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_inclusao),
            unicode(self.indsubstpatrobra),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente por empresa construtora enquadrada nos Arts. 7 a 9 da Lei 12.546/2011, relacionando os estabelecimentos inscritos no CNO, para indicar a substituição ou não da contribuição patronal incidente sobre a remuneração dos trabalhadores de obra de construção civil.'
        db_table = r's1005_inclusao_infoobra'       
        managed = True # s1005_inclusao_infoobra #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_infoobra", "Can view s1005_inclusao_infoobra"), )
            
        ordering = [
            's1005_inclusao',
            'indsubstpatrobra',]



class s1005inclusaoinfoObraSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoinfoObra
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoinfoPCD(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
    contpcd = models.IntegerField(choices=CHOICES_S1005_CONTPCD_INCLUSAO, null=True, )
    nrprocjud = models.CharField(max_length=20, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1005_inclusao),
            unicode(self.contpcd),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a contratação de pessoa com deficiência (PCD). Essa informação deve ser prestada apenas no estabelecimento 'Matriz'.'
        db_table = r's1005_inclusao_infopcd'       
        managed = True # s1005_inclusao_infopcd #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_infopcd", "Can view s1005_inclusao_infopcd"), )
            
        ordering = [
            's1005_inclusao',
            'contpcd',]



class s1005inclusaoinfoPCDSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoinfoPCD
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoprocAdmJudFap(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_TPPROC_INCLUSAO, null=True, )
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
            unicode(self.s1005_inclusao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica, em caso de existência, o processo administrativo/judicial em que houve decisão ou sentença favorável ao contribuinte suspendendo ou alterando a alíquota FAP aplicável ao contribuinte.'
        db_table = r's1005_inclusao_procadmjudfap'       
        managed = True # s1005_inclusao_procadmjudfap #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_procadmjudfap", "Can view s1005_inclusao_procadmjudfap"), )
            
        ordering = [
            's1005_inclusao',
            'tpproc',
            'nrproc',
            'codsusp',]



class s1005inclusaoprocAdmJudFapSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoprocAdmJudFap
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1005inclusaoprocAdmJudRat(SoftDeletionModel):

    s1005_inclusao = models.ForeignKey('s1005.s1005inclusao', 
        related_name='%(class)s_s1005_inclusao', )
    
    def evento(self): 
        return self.s1005_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_TPPROC_INCLUSAO, null=True, )
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
            unicode(self.s1005_inclusao),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.codsusp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica, em caso de existência, o processo administrativo ou judicial em que houve decisão/sentença favorável ao contribuinte modificando a alíquota RAT da empresa.'
        db_table = r's1005_inclusao_procadmjudrat'       
        managed = True # s1005_inclusao_procadmjudrat #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1005_inclusao_procadmjudrat", "Can view s1005_inclusao_procadmjudrat"), )
            
        ordering = [
            's1005_inclusao',
            'tpproc',
            'nrproc',
            'codsusp',]



class s1005inclusaoprocAdmJudRatSerializer(ModelSerializer):

    class Meta:
    
        model = s1005inclusaoprocAdmJudRat
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()