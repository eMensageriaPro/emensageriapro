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
from emensageriapro.r4010.choices import *
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





class r4010FCI(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
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
            unicode(self.r4010_infopgto),
            unicode(self.nrinscfci),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Fundo ou clube de investimento do qual o beneficiário faça parte e seja administrado pelo declarante'
        db_table = r'r4010_fci'       
        managed = True # r4010_fci #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_fci", "Can view r4010_fci"), )
            
        ordering = [
            'r4010_infopgto',
            'nrinscfci',]



class r4010FCISerializer(ModelSerializer):

    class Meta:
    
        model = r4010FCI
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010SCP(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
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
            unicode(self.r4010_infopgto),
            unicode(self.nrinscscp),
            unicode(self.percscp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Sociedade em conta de participação do qual o beneficiário faça parte e o declarante seja sócio ostensivo'
        db_table = r'r4010_scp'       
        managed = True # r4010_scp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_scp", "Can view r4010_scp"), )
            
        ordering = [
            'r4010_infopgto',
            'nrinscscp',
            'percscp',]



class r4010SCPSerializer(ModelSerializer):

    class Meta:
    
        model = r4010SCP
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010benefPen(SoftDeletionModel):

    r4010_detded = models.ForeignKey('r4010.r4010detDed', 
        related_name='%(class)s_r4010_detded', )
    
    def evento(self): 
        return self.r4010_detded.evento()
    cpf = models.CharField(max_length=11, blank=True, null=True, )
    dtnascto = models.DateField(blank=True, null=True, )
    nome = models.CharField(max_length=60, null=True, )
    reldep = models.IntegerField(choices=CHOICES_R4010_RELDEP, null=True, )
    descrdep = models.CharField(max_length=60, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_detded),
            unicode(self.nome),
            unicode(self.reldep),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação dos beneficiários da pensão alimentícia'
        db_table = r'r4010_benefpen'       
        managed = True # r4010_benefpen #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_benefpen", "Can view r4010_benefpen"), )
            
        ordering = [
            'r4010_detded',
            'nome',
            'reldep',]



class r4010benefPenSerializer(ModelSerializer):

    class Meta:
    
        model = r4010benefPen
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010detDed(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
    indtpdeducao = models.IntegerField(choices=CHOICES_R4010_INDTPDEDUCAO, null=True, )
    vlrdeducao = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrdedsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    nrinscprevcomp = models.CharField(max_length=14, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_infopgto),
            unicode(self.indtpdeducao),
            unicode(self.vlrdeducao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das deduções'
        db_table = r'r4010_detded'       
        managed = True # r4010_detded #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_detded", "Can view r4010_detded"), )
            
        ordering = [
            'r4010_infopgto',
            'indtpdeducao',
            'vlrdeducao',]



class r4010detDedSerializer(ModelSerializer):

    class Meta:
    
        model = r4010detDed
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010ideOpSaude(SoftDeletionModel):

    r4010_evtretpf = models.ForeignKey('efdreinf.r4010evtRetPF', 
        related_name='%(class)s_r4010_evtretpf', )
    
    def evento(self): 
        return self.r4010_evtretpf.evento()
    nrinsc = models.CharField(max_length=14, null=True, )
    regans = models.IntegerField(blank=True, null=True, )
    vlrsaude = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_evtretpf),
            unicode(self.nrinsc),
            unicode(self.vlrsaude),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação da operadora do plano privado coletivo empresarial de assistência à saúde'
        db_table = r'r4010_ideopsaude'       
        managed = True # r4010_ideopsaude #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_ideopsaude", "Can view r4010_ideopsaude"), )
            
        ordering = [
            'r4010_evtretpf',
            'nrinsc',
            'vlrsaude',]



class r4010ideOpSaudeSerializer(ModelSerializer):

    class Meta:
    
        model = r4010ideOpSaude
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010idePgto(SoftDeletionModel):

    r4010_evtretpf = models.ForeignKey('efdreinf.r4010evtRetPF', 
        related_name='%(class)s_r4010_evtretpf', )
    
    def evento(self): 
        return self.r4010_evtretpf.evento()
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
            unicode(self.r4010_evtretpf),
            unicode(self.natrend),
            unicode(self.paisresid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do rendimento'
        db_table = r'r4010_idepgto'       
        managed = True # r4010_idepgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_idepgto", "Can view r4010_idepgto"), )
            
        ordering = [
            'r4010_evtretpf',
            'natrend',
            'paisresid',]



class r4010idePgtoSerializer(ModelSerializer):

    class Meta:
    
        model = r4010idePgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoDependPl(SoftDeletionModel):

    r4010_ideopsaude = models.ForeignKey('r4010.r4010ideOpSaude', 
        related_name='%(class)s_r4010_ideopsaude', )
    
    def evento(self): 
        return self.r4010_ideopsaude.evento()
    cpf = models.CharField(max_length=11, blank=True, null=True, )
    dtnascto = models.DateField(blank=True, null=True, )
    nome = models.CharField(max_length=60, null=True, )
    reldep = models.IntegerField(choices=CHOICES_R4010_RELDEP, null=True, )
    vlrsaude = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_ideopsaude),
            unicode(self.nome),
            unicode(self.reldep),
            unicode(self.vlrsaude),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de dependente do plano de saúde coletivo empresarial'
        db_table = r'r4010_infodependpl'       
        managed = True # r4010_infodependpl #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infodependpl", "Can view r4010_infodependpl"), )
            
        ordering = [
            'r4010_ideopsaude',
            'nome',
            'reldep',
            'vlrsaude',]



class r4010infoDependPlSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoDependPl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoPgto(SoftDeletionModel):

    r4010_idepgto = models.ForeignKey('r4010.r4010idePgto', 
        related_name='%(class)s_r4010_idepgto', )
    
    def evento(self): 
        return self.r4010_idepgto.evento()
    dtfg = models.DateField(null=True, )
    inddecterc = models.CharField(choices=CHOICES_R4010_INDDECTERC, max_length=1, null=True, )
    vlrrendbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrrendtrib = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrrendsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrnir = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdeposito = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcompanocalend = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcompanoant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_idepgto),
            unicode(self.dtfg),
            unicode(self.inddecterc),
            unicode(self.vlrrendbruto),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Pagamento'
        db_table = r'r4010_infopgto'       
        managed = True # r4010_infopgto #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infopgto", "Can view r4010_infopgto"), )
            
        ordering = [
            'r4010_idepgto',
            'dtfg',
            'inddecterc',
            'vlrrendbruto',]



class r4010infoPgtoSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoPgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoPgtoExt(SoftDeletionModel):

    r4010_idepgto = models.ForeignKey('r4010.r4010idePgto', 
        related_name='%(class)s_r4010_idepgto', )
    
    def evento(self): 
        return self.r4010_idepgto.evento()
    dsclograd = models.CharField(max_length=80, null=True, )
    nrlograd = models.CharField(max_length=10, blank=True, null=True, )
    complem = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=60, blank=True, null=True, )
    cidade = models.CharField(max_length=30, blank=True, null=True, )
    estado = models.CharField(max_length=30, blank=True, null=True, )
    codpostal = models.CharField(max_length=12, blank=True, null=True, )
    telef = models.CharField(max_length=15, blank=True, null=True, )
    indnif = models.IntegerField(choices=CHOICES_R4010_INDNIF, null=True, )
    nifbenef = models.CharField(max_length=20, blank=True, null=True, )
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
            unicode(self.r4010_idepgto),
            unicode(self.dsclograd),
            unicode(self.indnif),
            unicode(self.frmtribut),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações complementares relativas a pagamentos a residente fiscal no Exterior'
        db_table = r'r4010_infopgtoext'       
        managed = True # r4010_infopgtoext #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infopgtoext", "Can view r4010_infopgtoext"), )
            
        ordering = [
            'r4010_idepgto',
            'dsclograd',
            'indnif',
            'frmtribut',]



class r4010infoPgtoExtSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoPgtoExt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoProcJud(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    indorigrec = models.IntegerField(choices=CHOICES_R4010_INDORIGREC_INFOPROCJUD, null=True, )
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
            unicode(self.r4010_infopgto),
            unicode(self.nrproc),
            unicode(self.indorigrec),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares - Demais rendimentos decorrentes de Decisão Judicial'
        db_table = r'r4010_infoprocjud'       
        managed = True # r4010_infoprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infoprocjud", "Can view r4010_infoprocjud"), )
            
        ordering = [
            'r4010_infopgto',
            'nrproc',
            'indorigrec',]



class r4010infoProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoProcJuddespProcJud(SoftDeletionModel):

    r4010_infoprocjud = models.ForeignKey('r4010.r4010infoProcJud', 
        related_name='%(class)s_r4010_infoprocjud', )
    
    def evento(self): 
        return self.r4010_infoprocjud.evento()
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
            unicode(self.r4010_infoprocjud),
            unicode(self.vlrdespcustas),
            unicode(self.vlrdespadvogados),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r4010_infoprocjud_despprocjud'       
        managed = True # r4010_infoprocjud_despprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infoprocjud_despprocjud", "Can view r4010_infoprocjud_despprocjud"), )
            
        ordering = [
            'r4010_infoprocjud',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r4010infoProcJuddespProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoProcJuddespProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoProcJudideAdv(SoftDeletionModel):

    r4010_infoprocjud_despprocjud = models.ForeignKey('r4010.r4010infoProcJuddespProcJud', 
        related_name='%(class)s_r4010_infoprocjud_despprocjud', )
    
    def evento(self): 
        return self.r4010_infoprocjud_despprocjud.evento()
    tpinscadv = models.IntegerField(choices=CHOICES_R4010_TPINSCADV_INFOPROCJUD, null=True, )
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
            unicode(self.r4010_infoprocjud_despprocjud),
            unicode(self.tpinscadv),
            unicode(self.nrinscadv),
            unicode(self.vlradv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do advogado'
        db_table = r'r4010_infoprocjud_ideadv'       
        managed = True # r4010_infoprocjud_ideadv #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infoprocjud_ideadv", "Can view r4010_infoprocjud_ideadv"), )
            
        ordering = [
            'r4010_infoprocjud_despprocjud',
            'tpinscadv',
            'nrinscadv',
            'vlradv',]



class r4010infoProcJudideAdvSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoProcJudideAdv
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoProcJudorigemRec(SoftDeletionModel):

    r4010_infoprocjud = models.ForeignKey('r4010.r4010infoProcJud', 
        related_name='%(class)s_r4010_infoprocjud', )
    
    def evento(self): 
        return self.r4010_infoprocjud.evento()
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
            unicode(self.r4010_infoprocjud),
            unicode(self.cnpjorigrecurso),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a origem dos recursos'
        db_table = r'r4010_infoprocjud_origemrec'       
        managed = True # r4010_infoprocjud_origemrec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infoprocjud_origemrec", "Can view r4010_infoprocjud_origemrec"), )
            
        ordering = [
            'r4010_infoprocjud',
            'cnpjorigrecurso',]



class r4010infoProcJudorigemRecSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoProcJudorigemRec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoProcRet(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
    tpprocret = models.IntegerField(choices=CHOICES_R4010_TPPROCRET, null=True, )
    nrprocret = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrnretido = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrdep = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_infopgto),
            unicode(self.tpprocret),
            unicode(self.nrprocret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de tributos ou depósitos judiciais'
        db_table = r'r4010_infoprocret'       
        managed = True # r4010_infoprocret #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_infoprocret", "Can view r4010_infoprocret"), )
            
        ordering = [
            'r4010_infopgto',
            'tpprocret',
            'nrprocret',]



class r4010infoProcRetSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoProcRet
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoRRA(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
    tpprocrra = models.IntegerField(choices=CHOICES_R4010_TPPROCRRA_INFORRA, null=True, )
    nrprocrra = models.CharField(max_length=21, blank=True, null=True, )
    indorigrec = models.IntegerField(choices=CHOICES_R4010_INDORIGREC_INFORRA, null=True, )
    descrra = models.CharField(max_length=50, null=True, )
    qtdmesesrra = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_infopgto),
            unicode(self.tpprocrra),
            unicode(self.indorigrec),
            unicode(self.descrra),
            unicode(self.qtdmesesrra),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares - Rendimentos Recebidos Acumuladamente'
        db_table = r'r4010_inforra'       
        managed = True # r4010_inforra #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforra", "Can view r4010_inforra"), )
            
        ordering = [
            'r4010_infopgto',
            'tpprocrra',
            'indorigrec',
            'descrra',
            'qtdmesesrra',]



class r4010infoRRASerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoRRA
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoRRAdespProcJud(SoftDeletionModel):

    r4010_inforra = models.ForeignKey('r4010.r4010infoRRA', 
        related_name='%(class)s_r4010_inforra', )
    
    def evento(self): 
        return self.r4010_inforra.evento()
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
            unicode(self.r4010_inforra),
            unicode(self.vlrdespcustas),
            unicode(self.vlrdespadvogados),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das despesas de processo judicial'
        db_table = r'r4010_inforra_despprocjud'       
        managed = True # r4010_inforra_despprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforra_despprocjud", "Can view r4010_inforra_despprocjud"), )
            
        ordering = [
            'r4010_inforra',
            'vlrdespcustas',
            'vlrdespadvogados',]



class r4010infoRRAdespProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoRRAdespProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoRRAideAdv(SoftDeletionModel):

    r4010_inforra_despprocjud = models.ForeignKey('r4010.r4010infoRRAdespProcJud', 
        related_name='%(class)s_r4010_inforra_despprocjud', )
    
    def evento(self): 
        return self.r4010_inforra_despprocjud.evento()
    tpinscadv = models.IntegerField(choices=CHOICES_R4010_TPINSCADV_INFORRA, null=True, )
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
            unicode(self.r4010_inforra_despprocjud),
            unicode(self.tpinscadv),
            unicode(self.nrinscadv),
            unicode(self.vlradv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação do advogado'
        db_table = r'r4010_inforra_ideadv'       
        managed = True # r4010_inforra_ideadv #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforra_ideadv", "Can view r4010_inforra_ideadv"), )
            
        ordering = [
            'r4010_inforra_despprocjud',
            'tpinscadv',
            'nrinscadv',
            'vlradv',]



class r4010infoRRAideAdvSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoRRAideAdv
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoRRAorigemRec(SoftDeletionModel):

    r4010_inforra = models.ForeignKey('r4010.r4010infoRRA', 
        related_name='%(class)s_r4010_inforra', )
    
    def evento(self): 
        return self.r4010_inforra.evento()
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
            unicode(self.r4010_inforra),
            unicode(self.cnpjorigrecurso),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a origem dos recursos'
        db_table = r'r4010_inforra_origemrec'       
        managed = True # r4010_inforra_origemrec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforra_origemrec", "Can view r4010_inforra_origemrec"), )
            
        ordering = [
            'r4010_inforra',
            'cnpjorigrecurso',]



class r4010infoRRAorigemRecSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoRRAorigemRec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoReemb(SoftDeletionModel):

    r4010_ideopsaude = models.ForeignKey('r4010.r4010ideOpSaude', 
        related_name='%(class)s_r4010_ideopsaude', )
    
    def evento(self): 
        return self.r4010_ideopsaude.evento()
    tpinsc = models.IntegerField(choices=CHOICES_R4010_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    vlrreemb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrreembant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_ideopsaude),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.vlrreemb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação de reembolso do titular do plano de saúde coletivo empresarial'
        db_table = r'r4010_inforeemb'       
        managed = True # r4010_inforeemb #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforeemb", "Can view r4010_inforeemb"), )
            
        ordering = [
            'r4010_ideopsaude',
            'tpinsc',
            'nrinsc',
            'vlrreemb',]



class r4010infoReembSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoReemb
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010infoReembDep(SoftDeletionModel):

    r4010_infodependpl = models.ForeignKey('r4010.r4010infoDependPl', 
        related_name='%(class)s_r4010_infodependpl', )
    
    def evento(self): 
        return self.r4010_infodependpl.evento()
    tpinsc = models.IntegerField(choices=CHOICES_R4010_TPINSC, null=True, )
    nrinsc = models.CharField(max_length=14, null=True, )
    vlrreemb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrreembant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_infodependpl),
            unicode(self.tpinsc),
            unicode(self.nrinsc),
            unicode(self.vlrreemb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação de reembolso do dependente do plano de saúde coletivo empresarial'
        db_table = r'r4010_inforeembdep'       
        managed = True # r4010_inforeembdep #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_inforeembdep", "Can view r4010_inforeembdep"), )
            
        ordering = [
            'r4010_infodependpl',
            'tpinsc',
            'nrinsc',
            'vlrreemb',]



class r4010infoReembDepSerializer(ModelSerializer):

    class Meta:
    
        model = r4010infoReembDep
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r4010rendIsento(SoftDeletionModel):

    r4010_infopgto = models.ForeignKey('r4010.r4010infoPgto', 
        related_name='%(class)s_r4010_infopgto', )
    
    def evento(self): 
        return self.r4010_infopgto.evento()
    tpisencao = models.IntegerField(choices=CHOICES_R4010_TPISENCAO, null=True, )
    vlrisento = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    descrendimento = models.CharField(max_length=100, blank=True, null=True, )
    dtlaudo = models.DateField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r4010_infopgto),
            unicode(self.tpisencao),
            unicode(self.vlrisento),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Rendimentos Isentos/Não Tributáveis'
        db_table = r'r4010_rendisento'       
        managed = True # r4010_rendisento #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r4010_rendisento", "Can view r4010_rendisento"), )
            
        ordering = [
            'r4010_infopgto',
            'tpisencao',
            'vlrisento',]



class r4010rendIsentoSerializer(ModelSerializer):

    class Meta:
    
        model = r4010rendIsento
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()