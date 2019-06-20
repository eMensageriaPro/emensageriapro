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
from emensageriapro.s2399.choices import *
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





class s2399detOper(SoftDeletionModel):

    s2399_infosaudecolet = models.ForeignKey('s2399.s2399infoSaudeColet', 
        related_name='%(class)s_s2399_infosaudecolet', )
    
    def evento(self): 
        return self.s2399_infosaudecolet.evento()
    cnpjoper = models.CharField(max_length=14, null=True, )
    regans = models.CharField(max_length=6, null=True, )
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_infosaudecolet), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos valores pagos a Operadoras de Planos de Saúde.'
        db_table = r's2399_detoper'       
        managed = True # s2399_detoper #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399detOper", u"Pode ver listagem do modelo S2399DETOPER"),
            ("can_see_data_s2399detOper", u"Pode visualizar o conteúdo do modelo S2399DETOPER"),
            ("can_see_menu_s2399detOper", u"Pode visualizar no menu o modelo S2399DETOPER"),
            ("can_print_list_s2399detOper", u"Pode imprimir listagem do modelo S2399DETOPER"),
            ("can_print_data_s2399detOper", u"Pode imprimir o conteúdo do modelo S2399DETOPER"), )
            
        ordering = [
            's2399_infosaudecolet',
            'cnpjoper',
            'regans',
            'vrpgtit',]



class s2399detOperSerializer(ModelSerializer):

    class Meta:
    
        model = s2399detOper
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399detPlano(SoftDeletionModel):

    s2399_detoper = models.ForeignKey('s2399.s2399detOper', 
        related_name='%(class)s_s2399_detoper', )
    
    def evento(self): 
        return self.s2399_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_ESOCIALDEPENDENTESTIPOS, max_length=2, null=True, )
    cpfdep = models.CharField(max_length=11, blank=True, null=True, )
    nmdep = models.CharField(max_length=70, null=True, )
    dtnascto = models.DateField(null=True, )
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_detoper), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações do dependente do plano privado de saúde.'
        db_table = r's2399_detplano'       
        managed = True # s2399_detplano #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399detPlano", u"Pode ver listagem do modelo S2399DETPLANO"),
            ("can_see_data_s2399detPlano", u"Pode visualizar o conteúdo do modelo S2399DETPLANO"),
            ("can_see_menu_s2399detPlano", u"Pode visualizar no menu o modelo S2399DETPLANO"),
            ("can_print_list_s2399detPlano", u"Pode imprimir listagem do modelo S2399DETPLANO"),
            ("can_print_data_s2399detPlano", u"Pode imprimir o conteúdo do modelo S2399DETPLANO"), )
            
        ordering = [
            's2399_detoper',
            'tpdep',
            'nmdep',
            'dtnascto',
            'vlrpgdep',]



class s2399detPlanoSerializer(ModelSerializer):

    class Meta:
    
        model = s2399detPlano
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399detVerbas(SoftDeletionModel):

    s2399_ideestablot = models.ForeignKey('s2399.s2399ideEstabLot', 
        related_name='%(class)s_s2399_ideestablot', )
    
    def evento(self): 
        return self.s2399_ideestablot.evento()
    codrubr = models.CharField(max_length=30, null=True, )
    idetabrubr = models.CharField(max_length=8, null=True, )
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_ideestablot), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento das verbas rescisórias devidas ao trabalhador'
        db_table = r's2399_detverbas'       
        managed = True # s2399_detverbas #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399detVerbas", u"Pode ver listagem do modelo S2399DETVERBAS"),
            ("can_see_data_s2399detVerbas", u"Pode visualizar o conteúdo do modelo S2399DETVERBAS"),
            ("can_see_menu_s2399detVerbas", u"Pode visualizar no menu o modelo S2399DETVERBAS"),
            ("can_print_list_s2399detVerbas", u"Pode imprimir listagem do modelo S2399DETVERBAS"),
            ("can_print_data_s2399detVerbas", u"Pode imprimir o conteúdo do modelo S2399DETVERBAS"), )
            
        ordering = [
            's2399_ideestablot',
            'codrubr',
            'idetabrubr',
            'vrrubr',]



class s2399detVerbasSerializer(ModelSerializer):

    class Meta:
    
        model = s2399detVerbas
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399dmDev(SoftDeletionModel):

    s2399_verbasresc = models.ForeignKey('s2399.s2399verbasResc', 
        related_name='%(class)s_s2399_verbasresc', )
    
    def evento(self): 
        return self.s2399_verbasresc.evento()
    idedmdev = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_verbasresc), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Identificação de cada um dos demonstrativos de valores devidos ao trabalhador antes das retenções de pensão alimentícia e IRRF'
        db_table = r's2399_dmdev'       
        managed = True # s2399_dmdev #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399dmDev", u"Pode ver listagem do modelo S2399DMDEV"),
            ("can_see_data_s2399dmDev", u"Pode visualizar o conteúdo do modelo S2399DMDEV"),
            ("can_see_menu_s2399dmDev", u"Pode visualizar no menu o modelo S2399DMDEV"),
            ("can_print_list_s2399dmDev", u"Pode imprimir listagem do modelo S2399DMDEV"),
            ("can_print_data_s2399dmDev", u"Pode imprimir o conteúdo do modelo S2399DMDEV"), )
            
        ordering = [
            's2399_verbasresc',
            'idedmdev',]



class s2399dmDevSerializer(ModelSerializer):

    class Meta:
    
        model = s2399dmDev
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399ideEstabLot(SoftDeletionModel):

    s2399_dmdev = models.ForeignKey('s2399.s2399dmDev', 
        related_name='%(class)s_s2399_dmdev', )
    
    def evento(self): 
        return self.s2399_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codlotacao = models.CharField(max_length=30, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_dmdev), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que identifica o Estabelecimento/Lotação no qual o trabalhador possui remuneração no período de apuração'
        db_table = r's2399_ideestablot'       
        managed = True # s2399_ideestablot #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399ideEstabLot", u"Pode ver listagem do modelo S2399IDEESTABLOT"),
            ("can_see_data_s2399ideEstabLot", u"Pode visualizar o conteúdo do modelo S2399IDEESTABLOT"),
            ("can_see_menu_s2399ideEstabLot", u"Pode visualizar no menu o modelo S2399IDEESTABLOT"),
            ("can_print_list_s2399ideEstabLot", u"Pode imprimir listagem do modelo S2399IDEESTABLOT"),
            ("can_print_data_s2399ideEstabLot", u"Pode imprimir o conteúdo do modelo S2399IDEESTABLOT"), )
            
        ordering = [
            's2399_dmdev',
            'tpinsc',
            'nrinsc',
            'codlotacao',]



class s2399ideEstabLotSerializer(ModelSerializer):

    class Meta:
    
        model = s2399ideEstabLot
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399infoAgNocivo(SoftDeletionModel):

    s2399_ideestablot = models.ForeignKey('s2399.s2399ideEstabLot', 
        related_name='%(class)s_s2399_ideestablot', )
    
    def evento(self): 
        return self.s2399_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2399_GRAUEXP, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_ideestablot), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em relação a remuneração de trabalhador enquadrado em uma das categorias relativas a Empregado, Servidor Público, Avulso, ou na categoria de Cooperado filiado a cooperativa de produção [738] ou Cooperado filiado a cooperativa de trabalho que presta serviço a empresa [731, 734], permitindo o detalhamento do grau de exposição do trabalhador aos agentes nocivos que ensejam a cobrança da contribuição adicional para financiamento dos benefícios de aposentadoria especial.'
        db_table = r's2399_infoagnocivo'       
        managed = True # s2399_infoagnocivo #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399infoAgNocivo", u"Pode ver listagem do modelo S2399INFOAGNOCIVO"),
            ("can_see_data_s2399infoAgNocivo", u"Pode visualizar o conteúdo do modelo S2399INFOAGNOCIVO"),
            ("can_see_menu_s2399infoAgNocivo", u"Pode visualizar no menu o modelo S2399INFOAGNOCIVO"),
            ("can_print_list_s2399infoAgNocivo", u"Pode imprimir listagem do modelo S2399INFOAGNOCIVO"),
            ("can_print_data_s2399infoAgNocivo", u"Pode imprimir o conteúdo do modelo S2399INFOAGNOCIVO"), )
            
        ordering = [
            's2399_ideestablot',
            'grauexp',]



class s2399infoAgNocivoSerializer(ModelSerializer):

    class Meta:
    
        model = s2399infoAgNocivo
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399infoMV(SoftDeletionModel):

    s2399_verbasresc = models.ForeignKey('s2399.s2399verbasResc', 
        related_name='%(class)s_s2399_verbasresc', )
    
    def evento(self): 
        return self.s2399_verbasresc.evento()
    indmv = models.IntegerField(choices=CHOICES_S2399_INDMV, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_verbasresc), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente em caso de trabalhador que possua outros vínculos/atividades para definição do limite do salário-de-contribuição e da alíquota a ser aplicada no desconto da contribuição previdenciária.'
        db_table = r's2399_infomv'       
        managed = True # s2399_infomv #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399infoMV", u"Pode ver listagem do modelo S2399INFOMV"),
            ("can_see_data_s2399infoMV", u"Pode visualizar o conteúdo do modelo S2399INFOMV"),
            ("can_see_menu_s2399infoMV", u"Pode visualizar no menu o modelo S2399INFOMV"),
            ("can_print_list_s2399infoMV", u"Pode imprimir listagem do modelo S2399INFOMV"),
            ("can_print_data_s2399infoMV", u"Pode imprimir o conteúdo do modelo S2399INFOMV"), )
            
        ordering = [
            's2399_verbasresc',
            'indmv',]



class s2399infoMVSerializer(ModelSerializer):

    class Meta:
    
        model = s2399infoMV
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399infoSaudeColet(SoftDeletionModel):

    s2399_ideestablot = models.ForeignKey('s2399.s2399ideEstabLot', 
        related_name='%(class)s_s2399_ideestablot', )
    
    def evento(self): 
        return self.s2399_ideestablot.evento()
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_ideestablot), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de plano privado coletivo empresarial de assistência à saúde'
        db_table = r's2399_infosaudecolet'       
        managed = True # s2399_infosaudecolet #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399infoSaudeColet", u"Pode ver listagem do modelo S2399INFOSAUDECOLET"),
            ("can_see_data_s2399infoSaudeColet", u"Pode visualizar o conteúdo do modelo S2399INFOSAUDECOLET"),
            ("can_see_menu_s2399infoSaudeColet", u"Pode visualizar no menu o modelo S2399INFOSAUDECOLET"),
            ("can_print_list_s2399infoSaudeColet", u"Pode imprimir listagem do modelo S2399INFOSAUDECOLET"),
            ("can_print_data_s2399infoSaudeColet", u"Pode imprimir o conteúdo do modelo S2399INFOSAUDECOLET"), )
            
        ordering = [
            's2399_ideestablot',]



class s2399infoSaudeColetSerializer(ModelSerializer):

    class Meta:
    
        model = s2399infoSaudeColet
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399infoSimples(SoftDeletionModel):

    s2399_ideestablot = models.ForeignKey('s2399.s2399ideEstabLot', 
        related_name='%(class)s_s2399_ideestablot', )
    
    def evento(self): 
        return self.s2399_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2399_INDSIMPLES, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_ideestablot), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação relativa a empresas enquadradas no Regime de Tributação Simples'
        db_table = r's2399_infosimples'       
        managed = True # s2399_infosimples #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399infoSimples", u"Pode ver listagem do modelo S2399INFOSIMPLES"),
            ("can_see_data_s2399infoSimples", u"Pode visualizar o conteúdo do modelo S2399INFOSIMPLES"),
            ("can_see_menu_s2399infoSimples", u"Pode visualizar no menu o modelo S2399INFOSIMPLES"),
            ("can_print_list_s2399infoSimples", u"Pode imprimir listagem do modelo S2399INFOSIMPLES"),
            ("can_print_data_s2399infoSimples", u"Pode imprimir o conteúdo do modelo S2399INFOSIMPLES"), )
            
        ordering = [
            's2399_ideestablot',
            'indsimples',]



class s2399infoSimplesSerializer(ModelSerializer):

    class Meta:
    
        model = s2399infoSimples
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399mudancaCPF(SoftDeletionModel):

    s2399_evttsvtermino = models.ForeignKey('esocial.s2399evtTSVTermino', 
        related_name='%(class)s_s2399_evttsvtermino', )
    
    def evento(self): 
        return self.s2399_evttsvtermino.evento()
    novocpf = models.CharField(max_length=11, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_evttsvtermino), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de mudança de CPF do trabalhador.'
        db_table = r's2399_mudancacpf'       
        managed = True # s2399_mudancacpf #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399mudancaCPF", u"Pode ver listagem do modelo S2399MUDANCACPF"),
            ("can_see_data_s2399mudancaCPF", u"Pode visualizar o conteúdo do modelo S2399MUDANCACPF"),
            ("can_see_menu_s2399mudancaCPF", u"Pode visualizar no menu o modelo S2399MUDANCACPF"),
            ("can_print_list_s2399mudancaCPF", u"Pode imprimir listagem do modelo S2399MUDANCACPF"),
            ("can_print_data_s2399mudancaCPF", u"Pode imprimir o conteúdo do modelo S2399MUDANCACPF"), )
            
        ordering = [
            's2399_evttsvtermino',
            'novocpf',]



class s2399mudancaCPFSerializer(ModelSerializer):

    class Meta:
    
        model = s2399mudancaCPF
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399procJudTrab(SoftDeletionModel):

    s2399_verbasresc = models.ForeignKey('s2399.s2399verbasResc', 
        related_name='%(class)s_s2399_verbasresc', )
    
    def evento(self): 
        return self.s2399_verbasresc.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2399_TPTRIB, null=True, )
    nrprocjud = models.CharField(max_length=20, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_verbasresc), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a existência de processos judiciais do trabalhador com decisão favorável quanto à não incidência ou alterações na incidência de contribuições sociais e/ou Imposto de Renda sobre as rubricas apresentadas nos subregistros de {dmDev}.'
        db_table = r's2399_procjudtrab'       
        managed = True # s2399_procjudtrab #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399procJudTrab", u"Pode ver listagem do modelo S2399PROCJUDTRAB"),
            ("can_see_data_s2399procJudTrab", u"Pode visualizar o conteúdo do modelo S2399PROCJUDTRAB"),
            ("can_see_menu_s2399procJudTrab", u"Pode visualizar no menu o modelo S2399PROCJUDTRAB"),
            ("can_print_list_s2399procJudTrab", u"Pode imprimir listagem do modelo S2399PROCJUDTRAB"),
            ("can_print_data_s2399procJudTrab", u"Pode imprimir o conteúdo do modelo S2399PROCJUDTRAB"), )
            
        ordering = [
            's2399_verbasresc',
            'tptrib',
            'nrprocjud',]



class s2399procJudTrabSerializer(ModelSerializer):

    class Meta:
    
        model = s2399procJudTrab
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399quarentena(SoftDeletionModel):

    s2399_evttsvtermino = models.ForeignKey('esocial.s2399evtTSVTermino', 
        related_name='%(class)s_s2399_evttsvtermino', )
    
    def evento(self): 
        return self.s2399_evttsvtermino.evento()
    dtfimquar = models.DateField(null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_evttsvtermino), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações sobre a 'quarentena' remunerada de trabalhador desligado'
        db_table = r's2399_quarentena'       
        managed = True # s2399_quarentena #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399quarentena", u"Pode ver listagem do modelo S2399QUARENTENA"),
            ("can_see_data_s2399quarentena", u"Pode visualizar o conteúdo do modelo S2399QUARENTENA"),
            ("can_see_menu_s2399quarentena", u"Pode visualizar no menu o modelo S2399QUARENTENA"),
            ("can_print_list_s2399quarentena", u"Pode imprimir listagem do modelo S2399QUARENTENA"),
            ("can_print_data_s2399quarentena", u"Pode imprimir o conteúdo do modelo S2399QUARENTENA"), )
            
        ordering = [
            's2399_evttsvtermino',
            'dtfimquar',]



class s2399quarentenaSerializer(ModelSerializer):

    class Meta:
    
        model = s2399quarentena
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399remunOutrEmpr(SoftDeletionModel):

    s2399_infomv = models.ForeignKey('s2399.s2399infoMV', 
        related_name='%(class)s_s2399_infomv', )
    
    def evento(self): 
        return self.s2399_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_ESOCIALINSCRICOESTIPOS, null=True, )
    nrinsc = models.CharField(max_length=15, null=True, )
    codcateg = models.IntegerField(null=True, )
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_infomv), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações relativas ao trabalhador que possui vínculo empregatício com outra(s) empresa(s) e/ou que exerce outras atividades como contribuinte individual, detalhando as empresas que efetuaram (ou efetuarão) desconto da contribuição, ou ainda valores recolhidos pelo próprio trabalhador como contribuinte individual'
        db_table = r's2399_remunoutrempr'       
        managed = True # s2399_remunoutrempr #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399remunOutrEmpr", u"Pode ver listagem do modelo S2399REMUNOUTREMPR"),
            ("can_see_data_s2399remunOutrEmpr", u"Pode visualizar o conteúdo do modelo S2399REMUNOUTREMPR"),
            ("can_see_menu_s2399remunOutrEmpr", u"Pode visualizar no menu o modelo S2399REMUNOUTREMPR"),
            ("can_print_list_s2399remunOutrEmpr", u"Pode imprimir listagem do modelo S2399REMUNOUTREMPR"),
            ("can_print_data_s2399remunOutrEmpr", u"Pode imprimir o conteúdo do modelo S2399REMUNOUTREMPR"), )
            
        ordering = [
            's2399_infomv',
            'tpinsc',
            'nrinsc',
            'codcateg',
            'vlrremunoe',]



class s2399remunOutrEmprSerializer(ModelSerializer):

    class Meta:
    
        model = s2399remunOutrEmpr
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class s2399verbasResc(SoftDeletionModel):

    s2399_evttsvtermino = models.ForeignKey('esocial.s2399evtTSVTermino', 
        related_name='%(class)s_s2399_evttsvtermino', )
    
    def evento(self): 
        return self.s2399_evttsvtermino.evento()
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s2399_evttsvtermino), ]
            
        if lista:
            if len(lista) == 1:
                return lista[0]
            else:
                return ' - '.join(lista)
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro onde são prestadas as informações relativas às verbas devidas ao trabalhador na rescisão contratual.'
        db_table = r's2399_verbasresc'       
        managed = True # s2399_verbasresc #
        
        unique_together = ( )
            
        index_together = ()
        
        permissions = (
            ("can_see_list_s2399verbasResc", u"Pode ver listagem do modelo S2399VERBASRESC"),
            ("can_see_data_s2399verbasResc", u"Pode visualizar o conteúdo do modelo S2399VERBASRESC"),
            ("can_see_menu_s2399verbasResc", u"Pode visualizar no menu o modelo S2399VERBASRESC"),
            ("can_print_list_s2399verbasResc", u"Pode imprimir listagem do modelo S2399VERBASRESC"),
            ("can_print_data_s2399verbasResc", u"Pode imprimir o conteúdo do modelo S2399VERBASRESC"), )
            
        ordering = [
            's2399_evttsvtermino',]



class s2399verbasRescSerializer(ModelSerializer):

    class Meta:
    
        model = s2399verbasResc
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por', 
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')