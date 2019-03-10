#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S2399_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2399_INDMV = (
    (1, u'1 - O declarante aplica a alíquota de desconto do segurado sobre a remuneração por ele informada (o percentual da alíquota será obtido considerando a remuneração total do trabalhador)'),
    (2, u'2 - O declarante aplica a alíquota de desconto do segurado sobre a diferença entre o limite máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'),
    (3, u'3 - O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite máximo de salário de contribuição em outra(s) empresa(s)'),
)

CHOICES_S2399_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2399_TPDEP = (
    ('01', u'01 - Cônjuge'),
    ('02', u'02 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável'),
    ('03', u'03 - Filho(a) ou enteado(a)'),
    ('04', u'04 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau'),
    ('06', u'06 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'),
    ('07', u'07 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2° grau, do(a) qual detenha a guarda judicial'),
    ('09', u'09 - Pais, avós e bisavós'),
    ('10', u'10 - Menor pobre do qual detenha a guarda judicial'),
    ('11', u'11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'),
    ('12', u'12 - Ex-cônjuge'),
    ('99', u'99 - Agregado/Outros'),
)

CHOICES_S2399_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2399_TPTRIB = (
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (4, u'4 - IRRF'),
    (4, u'4 - Contribuição sindical'),
)

class s2399detOper(SoftDeletionModel):
    s2399_ideestablot = models.ForeignKey('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    def evento(self): return self.s2399_ideestablot.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s2399_detoper_custom#

    class Meta:
        db_table = r's2399_detoper'       
        managed = True # s2399_detoper #
        unique_together = (
            #custom_unique_together_s2399_detoper#
            
        )
        index_together = (
            #custom_index_together_s2399_detoper
            #index_together_s2399_detoper
        )
        permissions = (
            ("can_view_s2399_detoper", "Can view s2399_detoper"),
            #custom_permissions_s2399_detoper
        )
        ordering = ['s2399_ideestablot', 'cnpjoper', 'regans', 'vrpgtit']



class s2399detOperSerializer(ModelSerializer):
    class Meta:
        model = s2399detOper
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399detPlano(SoftDeletionModel):
    s2399_detoper = models.ForeignKey('s2399detOper',
        related_name='%(class)s_s2399_detoper')
    def evento(self): return self.s2399_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S2399_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s2399_detplano_custom#

    class Meta:
        db_table = r's2399_detplano'       
        managed = True # s2399_detplano #
        unique_together = (
            #custom_unique_together_s2399_detplano#
            
        )
        index_together = (
            #custom_index_together_s2399_detplano
            #index_together_s2399_detplano
        )
        permissions = (
            ("can_view_s2399_detplano", "Can view s2399_detplano"),
            #custom_permissions_s2399_detplano
        )
        ordering = ['s2399_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep']



class s2399detPlanoSerializer(ModelSerializer):
    class Meta:
        model = s2399detPlano
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399detVerbas(SoftDeletionModel):
    s2399_ideestablot = models.ForeignKey('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    def evento(self): return self.s2399_ideestablot.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s2399_detverbas_custom#

    class Meta:
        db_table = r's2399_detverbas'       
        managed = True # s2399_detverbas #
        unique_together = (
            #custom_unique_together_s2399_detverbas#
            
        )
        index_together = (
            #custom_index_together_s2399_detverbas
            #index_together_s2399_detverbas
        )
        permissions = (
            ("can_view_s2399_detverbas", "Can view s2399_detverbas"),
            #custom_permissions_s2399_detverbas
        )
        ordering = ['s2399_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr']



class s2399detVerbasSerializer(ModelSerializer):
    class Meta:
        model = s2399detVerbas
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399dmDev(SoftDeletionModel):
    s2399_evttsvtermino = models.ForeignKey('esocial.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    def evento(self): return self.s2399_evttsvtermino.evento()
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.idedmdev)
    #s2399_dmdev_custom#

    class Meta:
        db_table = r's2399_dmdev'       
        managed = True # s2399_dmdev #
        unique_together = (
            #custom_unique_together_s2399_dmdev#
            
        )
        index_together = (
            #custom_index_together_s2399_dmdev
            #index_together_s2399_dmdev
        )
        permissions = (
            ("can_view_s2399_dmdev", "Can view s2399_dmdev"),
            #custom_permissions_s2399_dmdev
        )
        ordering = ['s2399_evttsvtermino', 'idedmdev']



class s2399dmDevSerializer(ModelSerializer):
    class Meta:
        model = s2399dmDev
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399ideEstabLot(SoftDeletionModel):
    s2399_dmdev = models.ForeignKey('s2399dmDev',
        related_name='%(class)s_s2399_dmdev')
    def evento(self): return self.s2399_dmdev.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_dmdev) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2399_ideestablot_custom#

    class Meta:
        db_table = r's2399_ideestablot'       
        managed = True # s2399_ideestablot #
        unique_together = (
            #custom_unique_together_s2399_ideestablot#
            
        )
        index_together = (
            #custom_index_together_s2399_ideestablot
            #index_together_s2399_ideestablot
        )
        permissions = (
            ("can_view_s2399_ideestablot", "Can view s2399_ideestablot"),
            #custom_permissions_s2399_ideestablot
        )
        ordering = ['s2399_dmdev', 'tpinsc', 'nrinsc', 'codlotacao']



class s2399ideEstabLotSerializer(ModelSerializer):
    class Meta:
        model = s2399ideEstabLot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399infoAgNocivo(SoftDeletionModel):
    s2399_ideestablot = models.OneToOneField('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    def evento(self): return self.s2399_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2399_GRAUEXP)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2399_infoagnocivo_custom#

    class Meta:
        db_table = r's2399_infoagnocivo'       
        managed = True # s2399_infoagnocivo #
        unique_together = (
            #custom_unique_together_s2399_infoagnocivo#
            
        )
        index_together = (
            #custom_index_together_s2399_infoagnocivo
            #index_together_s2399_infoagnocivo
        )
        permissions = (
            ("can_view_s2399_infoagnocivo", "Can view s2399_infoagnocivo"),
            #custom_permissions_s2399_infoagnocivo
        )
        ordering = ['s2399_ideestablot', 'grauexp']



class s2399infoAgNocivoSerializer(ModelSerializer):
    class Meta:
        model = s2399infoAgNocivo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399infoMV(SoftDeletionModel):
    s2399_evttsvtermino = models.OneToOneField('esocial.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    def evento(self): return self.s2399_evttsvtermino.evento()
    indmv = models.IntegerField(choices=CHOICES_S2399_INDMV)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.indmv)
    #s2399_infomv_custom#

    class Meta:
        db_table = r's2399_infomv'       
        managed = True # s2399_infomv #
        unique_together = (
            #custom_unique_together_s2399_infomv#
            
        )
        index_together = (
            #custom_index_together_s2399_infomv
            #index_together_s2399_infomv
        )
        permissions = (
            ("can_view_s2399_infomv", "Can view s2399_infomv"),
            #custom_permissions_s2399_infomv
        )
        ordering = ['s2399_evttsvtermino', 'indmv']



class s2399infoMVSerializer(ModelSerializer):
    class Meta:
        model = s2399infoMV
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399infoSimples(SoftDeletionModel):
    s2399_ideestablot = models.OneToOneField('s2399ideEstabLot',
        related_name='%(class)s_s2399_ideestablot')
    def evento(self): return self.s2399_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2399_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2399_infosimples_custom#

    class Meta:
        db_table = r's2399_infosimples'       
        managed = True # s2399_infosimples #
        unique_together = (
            #custom_unique_together_s2399_infosimples#
            
        )
        index_together = (
            #custom_index_together_s2399_infosimples
            #index_together_s2399_infosimples
        )
        permissions = (
            ("can_view_s2399_infosimples", "Can view s2399_infosimples"),
            #custom_permissions_s2399_infosimples
        )
        ordering = ['s2399_ideestablot', 'indsimples']



class s2399infoSimplesSerializer(ModelSerializer):
    class Meta:
        model = s2399infoSimples
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399mudancaCPF(SoftDeletionModel):
    s2399_evttsvtermino = models.OneToOneField('esocial.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    def evento(self): return self.s2399_evttsvtermino.evento()
    novocpf = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.novocpf)
    #s2399_mudancacpf_custom#

    class Meta:
        db_table = r's2399_mudancacpf'       
        managed = True # s2399_mudancacpf #
        unique_together = (
            #custom_unique_together_s2399_mudancacpf#
            
        )
        index_together = (
            #custom_index_together_s2399_mudancacpf
            #index_together_s2399_mudancacpf
        )
        permissions = (
            ("can_view_s2399_mudancacpf", "Can view s2399_mudancacpf"),
            #custom_permissions_s2399_mudancacpf
        )
        ordering = ['s2399_evttsvtermino', 'novocpf']



class s2399mudancaCPFSerializer(ModelSerializer):
    class Meta:
        model = s2399mudancaCPF
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399procJudTrab(SoftDeletionModel):
    s2399_evttsvtermino = models.ForeignKey('esocial.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    def evento(self): return self.s2399_evttsvtermino.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2399_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud)
    #s2399_procjudtrab_custom#

    class Meta:
        db_table = r's2399_procjudtrab'       
        managed = True # s2399_procjudtrab #
        unique_together = (
            #custom_unique_together_s2399_procjudtrab#
            
        )
        index_together = (
            #custom_index_together_s2399_procjudtrab
            #index_together_s2399_procjudtrab
        )
        permissions = (
            ("can_view_s2399_procjudtrab", "Can view s2399_procjudtrab"),
            #custom_permissions_s2399_procjudtrab
        )
        ordering = ['s2399_evttsvtermino', 'tptrib', 'nrprocjud']



class s2399procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s2399procJudTrab
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399quarentena(SoftDeletionModel):
    s2399_evttsvtermino = models.OneToOneField('esocial.s2399evtTSVTermino',
        related_name='%(class)s_s2399_evttsvtermino')
    def evento(self): return self.s2399_evttsvtermino.evento()
    dtfimquar = models.DateField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_evttsvtermino) + ' - ' + unicode(self.dtfimquar)
    #s2399_quarentena_custom#

    class Meta:
        db_table = r's2399_quarentena'       
        managed = True # s2399_quarentena #
        unique_together = (
            #custom_unique_together_s2399_quarentena#
            
        )
        index_together = (
            #custom_index_together_s2399_quarentena
            #index_together_s2399_quarentena
        )
        permissions = (
            ("can_view_s2399_quarentena", "Can view s2399_quarentena"),
            #custom_permissions_s2399_quarentena
        )
        ordering = ['s2399_evttsvtermino', 'dtfimquar']



class s2399quarentenaSerializer(ModelSerializer):
    class Meta:
        model = s2399quarentena
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class s2399remunOutrEmpr(SoftDeletionModel):
    s2399_infomv = models.ForeignKey('s2399infoMV',
        related_name='%(class)s_s2399_infomv')
    def evento(self): return self.s2399_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2399_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.TextField(max_length=3)
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s2399_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s2399_remunoutrempr_custom#

    class Meta:
        db_table = r's2399_remunoutrempr'       
        managed = True # s2399_remunoutrempr #
        unique_together = (
            #custom_unique_together_s2399_remunoutrempr#
            
        )
        index_together = (
            #custom_index_together_s2399_remunoutrempr
            #index_together_s2399_remunoutrempr
        )
        permissions = (
            ("can_view_s2399_remunoutrempr", "Can view s2399_remunoutrempr"),
            #custom_permissions_s2399_remunoutrempr
        )
        ordering = ['s2399_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']



class s2399remunOutrEmprSerializer(ModelSerializer):
    class Meta:
        model = s2399remunOutrEmpr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
