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
from emensageriapro.r4020.choices import *
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





class r4020CSLL(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    vlrbasecsll = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcsll = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasencsll = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrncsll = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdepcsll = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.vlrbasecsll),
            unicode(self.vlrcsll),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas à CSLL'
        db_table = r'r4020_csll'       
        managed = True # r4020_csll #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_csll", "Can view r4020_csll"), )
            
        ordering = [
            'r4020_infopgto',
            'vlrbasecsll',
            'vlrcsll',]



class r4020CSLLSerializer(ModelSerializer):

    class Meta:
    
        model = r4020CSLL
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020Cofins(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    vlrbasecofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcofins = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasencofins = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrncofins = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdepcofins = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.vlrbasecofins),
            unicode(self.vlrcofins),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas à Cofins'
        db_table = r'r4020_cofins'       
        managed = True # r4020_cofins #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_cofins", "Can view r4020_cofins"), )
            
        ordering = [
            'r4020_infopgto',
            'vlrbasecofins',
            'vlrcofins',]



class r4020CofinsSerializer(ModelSerializer):

    class Meta:
    
        model = r4020Cofins
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020FCI(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    nrinscfci = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.nrinscfci),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Fundo ou clube de investimento do qual o beneficiário faça parte e seja administrado pelo declarante'
        db_table = r'r4020_fci'       
        managed = True # r4020_fci #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_fci", "Can view r4020_fci"), )
            
        ordering = [
            'r4020_infopgto',
            'nrinscfci',]



class r4020FCISerializer(ModelSerializer):

    class Meta:
    
        model = r4020FCI
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020IR(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    vlrbaseir = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrir = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasenir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrnir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdepir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.vlrbaseir),
            unicode(self.vlrir),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao Imposto de Renda'
        db_table = r'r4020_ir'       
        managed = True # r4020_ir #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_ir", "Can view r4020_ir"), )
            
        ordering = [
            'r4020_infopgto',
            'vlrbaseir',
            'vlrir',]



class r4020IRSerializer(ModelSerializer):

    class Meta:
    
        model = r4020IR
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020PP(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    vlrbasepp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrpp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrbasenpp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrnpp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdeppp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.vlrbasepp),
            unicode(self.vlrpp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao PIS/PASEP'
        db_table = r'r4020_pp'       
        managed = True # r4020_pp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_pp", "Can view r4020_pp"), )
            
        ordering = [
            'r4020_infopgto',
            'vlrbasepp',
            'vlrpp',]



class r4020PPSerializer(ModelSerializer):

    class Meta:
    
        model = r4020PP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020SCP(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    nrinscscp = models.CharField(max_length=14, null=True, )
    percscp = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.nrinscscp),
            unicode(self.percscp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Sociedade em conta de participação do qual o beneficiário faça parte e o declarante seja sócio ostensivo'
        db_table = r'r4020_scp'       
        managed = True # r4020_scp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_scp", "Can view r4020_scp"), )
            
        ordering = [
            'r4020_infopgto',
            'nrinscscp',
            'percscp',]



class r4020SCPSerializer(ModelSerializer):

    class Meta:
    
        model = r4020SCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020despProcJud(SoftDeletionModel):

    r4020_infoprocjud = models.ForeignKey('r4020.r4020infoProcJud', 
        related_name='%(class)s_r4020_infoprocjud', )
    
    def evento(self): 
        return self.r4020_infoprocjud.evento()
    vlrdespcustas = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrdespadvogados = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infoprocjud),
            unicode(self.vlrdespcustas),
            unicode(self.vlrdespadvogados),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r4020_despprocjud'       
        managed = True # r4020_despprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_despprocjud", "Can view r4020_despprocjud"), )
            
        ordering = [
            'r4020_infoprocjud',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r4020despProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r4020despProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020ideAdv(SoftDeletionModel):

    r4020_despprocjud = models.ForeignKey('r4020.r4020despProcJud', 
        related_name='%(class)s_r4020_despprocjud', )
    
    def evento(self): 
        return self.r4020_despprocjud.evento()
    tpinscadv = models.IntegerField(choices=CHOICES_R4020_TPINSCADV, null=True, )
    nrinscadv = models.CharField(max_length=14, null=True, )
    vlradv = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_despprocjud),
            unicode(self.tpinscadv),
            unicode(self.nrinscadv),
            unicode(self.vlradv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do advogado'
        db_table = r'r4020_ideadv'       
        managed = True # r4020_ideadv #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_ideadv", "Can view r4020_ideadv"), )
            
        ordering = [
            'r4020_despprocjud',
            'tpinscadv',
            'nrinscadv',
            'vlradv',]



class r4020ideAdvSerializer(ModelSerializer):

    class Meta:
    
        model = r4020ideAdv
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020idePgto(SoftDeletionModel):

    r4020_evtretpj = models.ForeignKey('efdreinf.r4020evtRetPJ', 
        related_name='%(class)s_r4020_evtretpj', )
    
    def evento(self): 
        return self.r4020_evtretpj.evento()
    natrend = models.TextField(null=True, )
    paisresid = models.TextField(null=True, )
    observ = models.CharField(max_length=200, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_evtretpj),
            unicode(self.natrend),
            unicode(self.paisresid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do rendimento'
        db_table = r'r4020_idepgto'       
        managed = True # r4020_idepgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_idepgto", "Can view r4020_idepgto"), )
            
        ordering = [
            'r4020_evtretpj',
            'natrend',
            'paisresid',]



class r4020idePgtoSerializer(ModelSerializer):

    class Meta:
    
        model = r4020idePgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020infoPgto(SoftDeletionModel):

    r4020_idepgto = models.ForeignKey('r4020.r4020idePgto', 
        related_name='%(class)s_r4020_idepgto', )
    
    def evento(self): 
        return self.r4020_idepgto.evento()
    dtfg = models.DateField(null=True, )
    vlrtotalpag = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalcred = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_idepgto),
            unicode(self.dtfg),
            unicode(self.vlrtotalpag),
            unicode(self.vlrtotalcred),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Pagamento'
        db_table = r'r4020_infopgto'       
        managed = True # r4020_infopgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_infopgto", "Can view r4020_infopgto"), )
            
        ordering = [
            'r4020_idepgto',
            'dtfg',
            'vlrtotalpag',
            'vlrtotalcred',]



class r4020infoPgtoSerializer(ModelSerializer):

    class Meta:
    
        model = r4020infoPgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020infoPgtoExt(SoftDeletionModel):

    r4020_idepgto = models.ForeignKey('r4020.r4020idePgto', 
        related_name='%(class)s_r4020_idepgto', )
    
    def evento(self): 
        return self.r4020_idepgto.evento()
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    cidade = models.CharField(max_length=30, blank=True, null=True, )
    estado = models.CharField(max_length=30, blank=True, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    telef = models.CharField(max_length=15, blank=True, null=True, )
    indnif = models.IntegerField(choices=CHOICES_R4020_INDNIF, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
    relfontpg = models.IntegerField(choices=CHOICES_EFDREINFINFORMACOESBENEFICIARIOSEXTERIOR, null=True, )
    frmtribut = models.CharField(choices=CHOICES_EFDREINFRENDIMENTOSBENEFICIARIOSEXTERIORTRIBUTACAO, max_length=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_idepgto),
            unicode(self.dsclograd),
            unicode(self.indnif),
            unicode(self.relfontpg),
            unicode(self.frmtribut),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares relativas a pagamentos a residente fiscal no Exterior'
        db_table = r'r4020_infopgtoext'       
        managed = True # r4020_infopgtoext #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_infopgtoext", "Can view r4020_infopgtoext"), )
            
        ordering = [
            'r4020_idepgto',
            'dsclograd',
            'indnif',
            'relfontpg',
            'frmtribut',]



class r4020infoPgtoExtSerializer(ModelSerializer):

    class Meta:
    
        model = r4020infoPgtoExt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020infoProcJud(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    indorigemrecursos = models.IntegerField(choices=CHOICES_R4020_INDORIGEMRECURSOS, null=True, )
    desc = models.CharField(max_length=50, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.nrproc),
            unicode(self.indorigemrecursos),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares - Demais rendimentos decorrentes de Decisão Judicial'
        db_table = r'r4020_infoprocjud'       
        managed = True # r4020_infoprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_infoprocjud", "Can view r4020_infoprocjud"), )
            
        ordering = [
            'r4020_infopgto',
            'nrproc',
            'indorigemrecursos',]



class r4020infoProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r4020infoProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020infoProcRet(SoftDeletionModel):

    r4020_infopgto = models.ForeignKey('r4020.r4020infoPgto', 
        related_name='%(class)s_r4020_infopgto', )
    
    def evento(self): 
        return self.r4020_infopgto.evento()
    tpprocret = models.IntegerField(choices=CHOICES_R4020_TPPROCRET, null=True, )
    nrprocret = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    nir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    depir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    ncsll = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    depcsll = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    ncofins = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    depcofins = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    npp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    deppp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infopgto),
            unicode(self.tpprocret),
            unicode(self.nrprocret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de tributos ou depósitos judiciais'
        db_table = r'r4020_infoprocret'       
        managed = True # r4020_infoprocret #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_infoprocret", "Can view r4020_infoprocret"), )
            
        ordering = [
            'r4020_infopgto',
            'tpprocret',
            'nrprocret',]



class r4020infoProcRetSerializer(ModelSerializer):

    class Meta:
    
        model = r4020infoProcRet
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4020origemRec(SoftDeletionModel):

    r4020_infoprocjud = models.ForeignKey('r4020.r4020infoProcJud', 
        related_name='%(class)s_r4020_infoprocjud', )
    
    def evento(self): 
        return self.r4020_infoprocjud.evento()
    cnpjorigrecurso = models.CharField(max_length=14, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4020_infoprocjud),
            unicode(self.cnpjorigrecurso),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a origem dos recursos'
        db_table = r'r4020_origemrec'       
        managed = True # r4020_origemrec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4020_origemrec", "Can view r4020_origemrec"), )
            
        ordering = [
            'r4020_infoprocjud',
            'cnpjorigrecurso',]



class r4020origemRecSerializer(ModelSerializer):

    class Meta:
    
        model = r4020origemRec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()