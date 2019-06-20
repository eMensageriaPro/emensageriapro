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
            ("can_see_list_s1010alteracao", u"Pode ver listagem do modelo S1010ALTERACAO"),
            ("can_see_data_s1010alteracao", u"Pode visualizar o conteúdo do modelo S1010ALTERACAO"),
            ("can_see_menu_s1010alteracao", u"Pode visualizar no menu o modelo S1010ALTERACAO"),
            ("can_print_list_s1010alteracao", u"Pode imprimir listagem do modelo S1010ALTERACAO"),
            ("can_print_data_s1010alteracao", u"Pode imprimir o conteúdo do modelo S1010ALTERACAO"), )
            
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
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaoideProcessoCP(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_ALTERACAO, null=True, )
    codsusp = models.IntegerField(null=True, )
    
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
            ("can_see_list_s1010alteracaoideProcessoCP", u"Pode ver listagem do modelo S1010ALTERACAOIDEPROCESSOCP"),
            ("can_see_data_s1010alteracaoideProcessoCP", u"Pode visualizar o conteúdo do modelo S1010ALTERACAOIDEPROCESSOCP"),
            ("can_see_menu_s1010alteracaoideProcessoCP", u"Pode visualizar no menu o modelo S1010ALTERACAOIDEPROCESSOCP"),
            ("can_print_list_s1010alteracaoideProcessoCP", u"Pode imprimir listagem do modelo S1010ALTERACAOIDEPROCESSOCP"),
            ("can_print_data_s1010alteracaoideProcessoCP", u"Pode imprimir o conteúdo do modelo S1010ALTERACAOIDEPROCESSOCP"), )
            
        ordering = [
            's1010_alteracao',
            'tpproc',
            'nrproc',
            'extdecisao',
            'codsusp',]



class s1010alteracaoideProcessoCPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoCP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaoideProcessoCPRP(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_ALTERACAO, null=True, )
    
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
            ("can_see_list_s1010alteracaoideProcessoCPRP", u"Pode ver listagem do modelo S1010ALTERACAOIDEPROCESSOCPRP"),
            ("can_see_data_s1010alteracaoideProcessoCPRP", u"Pode visualizar o conteúdo do modelo S1010ALTERACAOIDEPROCESSOCPRP"),
            ("can_see_menu_s1010alteracaoideProcessoCPRP", u"Pode visualizar no menu o modelo S1010ALTERACAOIDEPROCESSOCPRP"),
            ("can_print_list_s1010alteracaoideProcessoCPRP", u"Pode imprimir listagem do modelo S1010ALTERACAOIDEPROCESSOCPRP"),
            ("can_print_data_s1010alteracaoideProcessoCPRP", u"Pode imprimir o conteúdo do modelo S1010ALTERACAOIDEPROCESSOCPRP"), )
            
        ordering = [
            's1010_alteracao',
            'tpproc',
            'nrproc',
            'extdecisao',]



class s1010alteracaoideProcessoCPRPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoCPRP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaoideProcessoFGTS(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
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
            ("can_see_list_s1010alteracaoideProcessoFGTS", u"Pode ver listagem do modelo S1010ALTERACAOIDEPROCESSOFGTS"),
            ("can_see_data_s1010alteracaoideProcessoFGTS", u"Pode visualizar o conteúdo do modelo S1010ALTERACAOIDEPROCESSOFGTS"),
            ("can_see_menu_s1010alteracaoideProcessoFGTS", u"Pode visualizar no menu o modelo S1010ALTERACAOIDEPROCESSOFGTS"),
            ("can_print_list_s1010alteracaoideProcessoFGTS", u"Pode imprimir listagem do modelo S1010ALTERACAOIDEPROCESSOFGTS"),
            ("can_print_data_s1010alteracaoideProcessoFGTS", u"Pode imprimir o conteúdo do modelo S1010ALTERACAOIDEPROCESSOFGTS"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',]



class s1010alteracaoideProcessoFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoFGTS
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaoideProcessoIRRF(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(null=True, )
    
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
            ("can_see_list_s1010alteracaoideProcessoIRRF", u"Pode ver listagem do modelo S1010ALTERACAOIDEPROCESSOIRRF"),
            ("can_see_data_s1010alteracaoideProcessoIRRF", u"Pode visualizar o conteúdo do modelo S1010ALTERACAOIDEPROCESSOIRRF"),
            ("can_see_menu_s1010alteracaoideProcessoIRRF", u"Pode visualizar no menu o modelo S1010ALTERACAOIDEPROCESSOIRRF"),
            ("can_print_list_s1010alteracaoideProcessoIRRF", u"Pode imprimir listagem do modelo S1010ALTERACAOIDEPROCESSOIRRF"),
            ("can_print_data_s1010alteracaoideProcessoIRRF", u"Pode imprimir o conteúdo do modelo S1010ALTERACAOIDEPROCESSOIRRF"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',
            'codsusp',]



class s1010alteracaoideProcessoIRRFSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoIRRF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaoideProcessoSIND(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
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
            ("can_see_list_s1010alteracaoideProcessoSIND", u"Pode ver listagem do modelo S1010ALTERACAOIDEPROCESSOSIND"),
            ("can_see_data_s1010alteracaoideProcessoSIND", u"Pode visualizar o conteúdo do modelo S1010ALTERACAOIDEPROCESSOSIND"),
            ("can_see_menu_s1010alteracaoideProcessoSIND", u"Pode visualizar no menu o modelo S1010ALTERACAOIDEPROCESSOSIND"),
            ("can_print_list_s1010alteracaoideProcessoSIND", u"Pode imprimir listagem do modelo S1010ALTERACAOIDEPROCESSOSIND"),
            ("can_print_data_s1010alteracaoideProcessoSIND", u"Pode imprimir o conteúdo do modelo S1010ALTERACAOIDEPROCESSOSIND"), )
            
        ordering = [
            's1010_alteracao',
            'nrproc',]



class s1010alteracaoideProcessoSINDSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaoideProcessoSIND
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010alteracaonovaValidade(SoftDeletionModel):

    s1010_alteracao = models.ForeignKey('s1010.s1010alteracao', 
        related_name='%(class)s_s1010_alteracao', )
    
    def evento(self): 
        return self.s1010_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
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
            ("can_see_list_s1010alteracaonovaValidade", u"Pode ver listagem do modelo S1010ALTERACAONOVAVALIDADE"),
            ("can_see_data_s1010alteracaonovaValidade", u"Pode visualizar o conteúdo do modelo S1010ALTERACAONOVAVALIDADE"),
            ("can_see_menu_s1010alteracaonovaValidade", u"Pode visualizar no menu o modelo S1010ALTERACAONOVAVALIDADE"),
            ("can_print_list_s1010alteracaonovaValidade", u"Pode imprimir listagem do modelo S1010ALTERACAONOVAVALIDADE"),
            ("can_print_data_s1010alteracaonovaValidade", u"Pode imprimir o conteúdo do modelo S1010ALTERACAONOVAVALIDADE"), )
            
        ordering = [
            's1010_alteracao',
            'inivalid',]



class s1010alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1010alteracaonovaValidade
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010exclusao(SoftDeletionModel):

    s1010_evttabrubrica = models.ForeignKey('esocial.s1010evtTabRubrica', 
        related_name='%(class)s_s1010_evttabrubrica', )
    
    def evento(self): 
        return self.s1010_evttabrubrica.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
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
            ("can_see_list_s1010exclusao", u"Pode ver listagem do modelo S1010EXCLUSAO"),
            ("can_see_data_s1010exclusao", u"Pode visualizar o conteúdo do modelo S1010EXCLUSAO"),
            ("can_see_menu_s1010exclusao", u"Pode visualizar no menu o modelo S1010EXCLUSAO"),
            ("can_print_list_s1010exclusao", u"Pode imprimir listagem do modelo S1010EXCLUSAO"),
            ("can_print_data_s1010exclusao", u"Pode imprimir o conteúdo do modelo S1010EXCLUSAO"), )
            
        ordering = [
            's1010_evttabrubrica',
            'codrubr',
            'idetabrubr',
            'inivalid',]



class s1010exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1010exclusao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


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
            ("can_see_list_s1010inclusao", u"Pode ver listagem do modelo S1010INCLUSAO"),
            ("can_see_data_s1010inclusao", u"Pode visualizar o conteúdo do modelo S1010INCLUSAO"),
            ("can_see_menu_s1010inclusao", u"Pode visualizar no menu o modelo S1010INCLUSAO"),
            ("can_print_list_s1010inclusao", u"Pode imprimir listagem do modelo S1010INCLUSAO"),
            ("can_print_data_s1010inclusao", u"Pode imprimir o conteúdo do modelo S1010INCLUSAO"), )
            
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
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010inclusaoideProcessoCP(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_INCLUSAO, null=True, )
    codsusp = models.IntegerField(null=True, )
    
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
            ("can_see_list_s1010inclusaoideProcessoCP", u"Pode ver listagem do modelo S1010INCLUSAOIDEPROCESSOCP"),
            ("can_see_data_s1010inclusaoideProcessoCP", u"Pode visualizar o conteúdo do modelo S1010INCLUSAOIDEPROCESSOCP"),
            ("can_see_menu_s1010inclusaoideProcessoCP", u"Pode visualizar no menu o modelo S1010INCLUSAOIDEPROCESSOCP"),
            ("can_print_list_s1010inclusaoideProcessoCP", u"Pode imprimir listagem do modelo S1010INCLUSAOIDEPROCESSOCP"),
            ("can_print_data_s1010inclusaoideProcessoCP", u"Pode imprimir o conteúdo do modelo S1010INCLUSAOIDEPROCESSOCP"), )
            
        ordering = [
            's1010_inclusao',
            'tpproc',
            'nrproc',
            'extdecisao',
            'codsusp',]



class s1010inclusaoideProcessoCPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoCP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010inclusaoideProcessoCPRP(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1010_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    extdecisao = models.IntegerField(choices=CHOICES_S1010_EXTDECISAO_INCLUSAO, null=True, )
    
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
            ("can_see_list_s1010inclusaoideProcessoCPRP", u"Pode ver listagem do modelo S1010INCLUSAOIDEPROCESSOCPRP"),
            ("can_see_data_s1010inclusaoideProcessoCPRP", u"Pode visualizar o conteúdo do modelo S1010INCLUSAOIDEPROCESSOCPRP"),
            ("can_see_menu_s1010inclusaoideProcessoCPRP", u"Pode visualizar no menu o modelo S1010INCLUSAOIDEPROCESSOCPRP"),
            ("can_print_list_s1010inclusaoideProcessoCPRP", u"Pode imprimir listagem do modelo S1010INCLUSAOIDEPROCESSOCPRP"),
            ("can_print_data_s1010inclusaoideProcessoCPRP", u"Pode imprimir o conteúdo do modelo S1010INCLUSAOIDEPROCESSOCPRP"), )
            
        ordering = [
            's1010_inclusao',
            'tpproc',
            'nrproc',
            'extdecisao',]



class s1010inclusaoideProcessoCPRPSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoCPRP
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010inclusaoideProcessoFGTS(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
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
            ("can_see_list_s1010inclusaoideProcessoFGTS", u"Pode ver listagem do modelo S1010INCLUSAOIDEPROCESSOFGTS"),
            ("can_see_data_s1010inclusaoideProcessoFGTS", u"Pode visualizar o conteúdo do modelo S1010INCLUSAOIDEPROCESSOFGTS"),
            ("can_see_menu_s1010inclusaoideProcessoFGTS", u"Pode visualizar no menu o modelo S1010INCLUSAOIDEPROCESSOFGTS"),
            ("can_print_list_s1010inclusaoideProcessoFGTS", u"Pode imprimir listagem do modelo S1010INCLUSAOIDEPROCESSOFGTS"),
            ("can_print_data_s1010inclusaoideProcessoFGTS", u"Pode imprimir o conteúdo do modelo S1010INCLUSAOIDEPROCESSOFGTS"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',]



class s1010inclusaoideProcessoFGTSSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoFGTS
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010inclusaoideProcessoIRRF(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(null=True, )
    
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
            ("can_see_list_s1010inclusaoideProcessoIRRF", u"Pode ver listagem do modelo S1010INCLUSAOIDEPROCESSOIRRF"),
            ("can_see_data_s1010inclusaoideProcessoIRRF", u"Pode visualizar o conteúdo do modelo S1010INCLUSAOIDEPROCESSOIRRF"),
            ("can_see_menu_s1010inclusaoideProcessoIRRF", u"Pode visualizar no menu o modelo S1010INCLUSAOIDEPROCESSOIRRF"),
            ("can_print_list_s1010inclusaoideProcessoIRRF", u"Pode imprimir listagem do modelo S1010INCLUSAOIDEPROCESSOIRRF"),
            ("can_print_data_s1010inclusaoideProcessoIRRF", u"Pode imprimir o conteúdo do modelo S1010INCLUSAOIDEPROCESSOIRRF"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',
            'codsusp',]



class s1010inclusaoideProcessoIRRFSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoIRRF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')


class s1010inclusaoideProcessoSIND(SoftDeletionModel):

    s1010_inclusao = models.ForeignKey('s1010.s1010inclusao', 
        related_name='%(class)s_s1010_inclusao', )
    
    def evento(self): 
        return self.s1010_inclusao.evento()
    nrproc = models.CharField(max_length=21, null=True, )
    
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
            ("can_see_list_s1010inclusaoideProcessoSIND", u"Pode ver listagem do modelo S1010INCLUSAOIDEPROCESSOSIND"),
            ("can_see_data_s1010inclusaoideProcessoSIND", u"Pode visualizar o conteúdo do modelo S1010INCLUSAOIDEPROCESSOSIND"),
            ("can_see_menu_s1010inclusaoideProcessoSIND", u"Pode visualizar no menu o modelo S1010INCLUSAOIDEPROCESSOSIND"),
            ("can_print_list_s1010inclusaoideProcessoSIND", u"Pode imprimir listagem do modelo S1010INCLUSAOIDEPROCESSOSIND"),
            ("can_print_data_s1010inclusaoideProcessoSIND", u"Pode imprimir o conteúdo do modelo S1010INCLUSAOIDEPROCESSOSIND"), )
            
        ordering = [
            's1010_inclusao',
            'nrproc',]



class s1010inclusaoideProcessoSINDSerializer(ModelSerializer):

    class Meta:
    
        model = s1010inclusaoideProcessoSIND
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')