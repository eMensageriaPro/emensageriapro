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
from emensageriapro.s2206.choices import *
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





class s2206alvaraJudicial(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    nrprocjud = models.CharField(max_length=20, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.nrprocjud),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do alvará judicial em caso de contratação de menores de 14 anos, em qualquer categoria, e de maiores de 14 e menores de 16, em categoria diferente de 'Aprendiz'.'
        db_table = r's2206_alvarajudicial'       
        managed = True # s2206_alvarajudicial #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206alvaraJudicial", "Can view S2206ALVARAJUDICIAL"),
            ("can_view_menu_s2206alvaraJudicial", "Can view menu S2206ALVARAJUDICIAL"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'nrprocjud',]



class s2206alvaraJudicialSerializer(ModelSerializer):

    class Meta:
    
        model = s2206alvaraJudicial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206aprend(SoftDeletionModel):

    s2206_infoceletista = models.ForeignKey('s2206.s2206infoCeletista', 
        related_name='%(class)s_s2206_infoceletista', )
    
    def evento(self): 
        return self.s2206_infoceletista.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_infoceletista),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações para identificação do empregador contratante de aprendiz'
        db_table = r's2206_aprend'       
        managed = True # s2206_aprend #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206aprend", "Can view S2206APREND"),
            ("can_view_menu_s2206aprend", "Can view menu S2206APREND"),)
            
        ordering = [
            's2206_infoceletista',
            'tpinsc',
            'nrinsc',]



class s2206aprendSerializer(ModelSerializer):

    class Meta:
    
        model = s2206aprend
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206filiacaoSindical(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    cnpjsindtrab = models.CharField(max_length=14, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.cnpjsindtrab),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Filiação Sindical do Trabalhador'
        db_table = r's2206_filiacaosindical'       
        managed = True # s2206_filiacaosindical #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206filiacaoSindical", "Can view S2206FILIACAOSINDICAL"),
            ("can_view_menu_s2206filiacaoSindical", "Can view menu S2206FILIACAOSINDICAL"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'cnpjsindtrab',]



class s2206filiacaoSindicalSerializer(ModelSerializer):

    class Meta:
    
        model = s2206filiacaoSindical
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206horContratual(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    tpjornada = models.IntegerField(choices=CHOICES_S2206_TPJORNADA, null=True, )
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True, )
    tmpparc = models.IntegerField(choices=CHOICES_S2206_TMPPARC, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.tpjornada),
            unicode(self.tmpparc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do Horário Contratual do Trabalhador. O preenchimento é obrigatório se {tpRegJor} = [1].'
        db_table = r's2206_horcontratual'       
        managed = True # s2206_horcontratual #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206horContratual", "Can view S2206HORCONTRATUAL"),
            ("can_view_menu_s2206horContratual", "Can view menu S2206HORCONTRATUAL"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'tpjornada',
            'tmpparc',]



class s2206horContratualSerializer(ModelSerializer):

    class Meta:
    
        model = s2206horContratual
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206horario(SoftDeletionModel):

    s2206_horcontratual = models.ForeignKey('s2206.s2206horContratual', 
        related_name='%(class)s_s2206_horcontratual', )
    
    def evento(self): 
        return self.s2206_horcontratual.evento()
    dia = models.IntegerField(choices=CHOICES_S2206_DIA, null=True, )
    codhorcontrat = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_horcontratual),
            unicode(self.dia),
            unicode(self.codhorcontrat),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações diárias do horário contratual'
        db_table = r's2206_horario'       
        managed = True # s2206_horario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206horario", "Can view S2206HORARIO"),
            ("can_view_menu_s2206horario", "Can view menu S2206HORARIO"),)
            
        ordering = [
            's2206_horcontratual',
            'dia',
            'codhorcontrat',]



class s2206horarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2206horario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206infoCeletista(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    tpregjor = models.IntegerField(choices=CHOICES_S2206_TPREGJOR, null=True, )
    natatividade = models.IntegerField(choices=CHOICES_S2206_NATATIVIDADE, null=True, )
    dtbase = models.IntegerField(blank=True, null=True, )
    cnpjsindcategprof = models.CharField(max_length=14, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.tpregjor),
            unicode(self.natatividade),
            unicode(self.cnpjsindcategprof),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Trabalhador Celetista'
        db_table = r's2206_infoceletista'       
        managed = True # s2206_infoceletista #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206infoCeletista", "Can view S2206INFOCELETISTA"),
            ("can_view_menu_s2206infoCeletista", "Can view menu S2206INFOCELETISTA"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'tpregjor',
            'natatividade',
            'cnpjsindcategprof',]



class s2206infoCeletistaSerializer(ModelSerializer):

    class Meta:
    
        model = s2206infoCeletista
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206infoEstatutario(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    tpplanrp = models.IntegerField(choices=CHOICES_S2206_TPPLANRP, null=True, )
    indtetorgps = models.CharField(choices=CHOICES_S2206_INDTETORGPS, max_length=1, blank=True, null=True, )
    indabonoperm = models.CharField(choices=CHOICES_S2206_INDABONOPERM, max_length=1, blank=True, null=True, )
    indparcremun = models.CharField(choices=CHOICES_S2206_INDPARCREMUN, max_length=1, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.tpplanrp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Trabalhador Estatutário'
        db_table = r's2206_infoestatutario'       
        managed = True # s2206_infoestatutario #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206infoEstatutario", "Can view S2206INFOESTATUTARIO"),
            ("can_view_menu_s2206infoEstatutario", "Can view menu S2206INFOESTATUTARIO"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'tpplanrp',]



class s2206infoEstatutarioSerializer(ModelSerializer):

    class Meta:
    
        model = s2206infoEstatutario
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206localTrabDom(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    tplograd = models.TextField(null=True, )
    dsclograd = models.CharField(max_length=100, null=True, )
    nrlograd = models.CharField(max_length=10, null=True, )
    complemento = models.CharField(max_length=30, blank=True, null=True, )
    bairro = models.CharField(max_length=90, blank=True, null=True, )
    cep = models.CharField(max_length=8, null=True, )
    codmunic = models.TextField(null=True, )
    uf = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
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
        db_table = r's2206_localtrabdom'       
        managed = True # s2206_localtrabdom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206localTrabDom", "Can view S2206LOCALTRABDOM"),
            ("can_view_menu_s2206localTrabDom", "Can view menu S2206LOCALTRABDOM"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'tplograd',
            'dsclograd',
            'nrlograd',
            'cep',
            'codmunic',
            'uf',]



class s2206localTrabDomSerializer(ModelSerializer):

    class Meta:
    
        model = s2206localTrabDom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206localTrabGeral(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    desccomp = models.CharField(max_length=80, blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.tpinsc),
            unicode(self.nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Estabelecimento (CNPJ, CNO, CAEPF) onde o trabalhador (exceto doméstico e temporário) exercerá suas atividades'
        db_table = r's2206_localtrabgeral'       
        managed = True # s2206_localtrabgeral #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206localTrabGeral", "Can view S2206LOCALTRABGERAL"),
            ("can_view_menu_s2206localTrabGeral", "Can view menu S2206LOCALTRABGERAL"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'tpinsc',
            'nrinsc',]



class s2206localTrabGeralSerializer(ModelSerializer):

    class Meta:
    
        model = s2206localTrabGeral
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206observacoes(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    observacao = models.CharField(max_length=255, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.observacao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Observações do contrato de trabalho'
        db_table = r's2206_observacoes'       
        managed = True # s2206_observacoes #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206observacoes", "Can view S2206OBSERVACOES"),
            ("can_view_menu_s2206observacoes", "Can view menu S2206OBSERVACOES"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'observacao',]



class s2206observacoesSerializer(ModelSerializer):

    class Meta:
    
        model = s2206observacoes
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206servPubl(SoftDeletionModel):

    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual', 
        related_name='%(class)s_s2206_evtaltcontratual', )
    
    def evento(self): 
        return self.s2206_evtaltcontratual.evento()
    mtvalter = models.IntegerField(choices=CHOICES_S2206_MTVALTER, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_evtaltcontratual),
            unicode(self.mtvalter),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alterações inerentes ao servidor público'
        db_table = r's2206_servpubl'       
        managed = True # s2206_servpubl #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206servPubl", "Can view S2206SERVPUBL"),
            ("can_view_menu_s2206servPubl", "Can view menu S2206SERVPUBL"),)
            
        ordering = [
            's2206_evtaltcontratual',
            'mtvalter',]



class s2206servPublSerializer(ModelSerializer):

    class Meta:
    
        model = s2206servPubl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s2206trabTemp(SoftDeletionModel):

    s2206_infoceletista = models.ForeignKey('s2206.s2206infoCeletista', 
        related_name='%(class)s_s2206_infoceletista', )
    
    def evento(self): 
        return self.s2206_infoceletista.evento()
    justprorr = models.CharField(max_length=999, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2206_infoceletista),
            unicode(self.justprorr),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Dados sobre trabalho temporário. Preenchimento obrigatório na prorrogação de contrato de trabalhador temporário'
        db_table = r's2206_trabtemp'       
        managed = True # s2206_trabtemp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s2206trabTemp", "Can view S2206TRABTEMP"),
            ("can_view_menu_s2206trabTemp", "Can view menu S2206TRABTEMP"),)
            
        ordering = [
            's2206_infoceletista',
            'justprorr',]



class s2206trabTempSerializer(ModelSerializer):

    class Meta:
    
        model = s2206trabTemp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()