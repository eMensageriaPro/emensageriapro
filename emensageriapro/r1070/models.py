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



CHOICES_R1070_ALTERACAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade ou empresa'),
)

CHOICES_R1070_ALTERACAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R1070_ALTERACAO_INDSUSP = (
    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_R1070_ALTERACAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R1070_EXCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R1070_INCLUSAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade ou empresa'),
)

CHOICES_R1070_INCLUSAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R1070_INCLUSAO_INDSUSP = (
    ('01', u'01 - Liminar em Mandado de Segurança'),
    ('02', u'02 - Depósito Judicial do Montante Integral'),
    ('03', u'03 - Depósito Administrativo do Montante Integral'),
    ('04', u'04 - Antecipação de Tutela'),
    ('05', u'05 - Liminar em Medida Cautelar'),
    ('08', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('09', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_R1070_INCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

PERIODOS = (
    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
    ('2019-01', u'Janeiro/2019'),
    ('2019-02', u'Fevereiro/2019'),
    ('2019-03', u'Março/2019'),
    ('2019-04', u'Abril/2019'),
    ('2019-05', u'Maio/2019'),
    ('2019-06', u'Junho/2019'),
    ('2019-07', u'Julho/2019'),
    ('2019-08', u'Agosto/2019'),
    ('2019-09', u'Setembro/2019'),
    ('2019-10', u'Outubro/2019'),
    ('2019-11', u'Novembro/2019'),
    ('2019-12', u'Dezembro/2019'),
)

class r1070alteracao(SoftDeletionModel):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_R1070_ALTERACAO_INDAUTORIA)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.indautoria)
    #r1070_alteracao_custom#

    class Meta:
        db_table = r'r1070_alteracao'       
        managed = True # r1070_alteracao #
        unique_together = (
            #custom_unique_together_r1070_alteracao#
            
        )
        index_together = (
            #custom_index_together_r1070_alteracao
            #index_together_r1070_alteracao
        )
        permissions = (
            ("can_view_r1070_alteracao", "Can view r1070_alteracao"),
            #custom_permissions_r1070_alteracao
        )
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'indautoria']



class r1070alteracaoSerializer(ModelSerializer):
    class Meta:
        model = r1070alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070alteracaodadosProcJud(SoftDeletionModel):
    r1070_alteracao = models.OneToOneField('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.CharField(max_length=4)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #r1070_alteracao_dadosprocjud_custom#

    class Meta:
        db_table = r'r1070_alteracao_dadosprocjud'       
        managed = True # r1070_alteracao_dadosprocjud #
        unique_together = (
            #custom_unique_together_r1070_alteracao_dadosprocjud#
            
        )
        index_together = (
            #custom_index_together_r1070_alteracao_dadosprocjud
            #index_together_r1070_alteracao_dadosprocjud
        )
        permissions = (
            ("can_view_r1070_alteracao_dadosprocjud", "Can view r1070_alteracao_dadosprocjud"),
            #custom_permissions_r1070_alteracao_dadosprocjud
        )
        ordering = ['r1070_alteracao', 'ufvara', 'codmunic', 'idvara']



class r1070alteracaodadosProcJudSerializer(ModelSerializer):
    class Meta:
        model = r1070alteracaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070alteracaoinfoSusp(SoftDeletionModel):
    r1070_alteracao = models.ForeignKey('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    codsusp = models.IntegerField(blank=True, null=True)
    indsusp = models.CharField(choices=CHOICES_R1070_ALTERACAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_R1070_ALTERACAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #r1070_alteracao_infosusp_custom#

    class Meta:
        db_table = r'r1070_alteracao_infosusp'       
        managed = True # r1070_alteracao_infosusp #
        unique_together = (
            #custom_unique_together_r1070_alteracao_infosusp#
            
        )
        index_together = (
            #custom_index_together_r1070_alteracao_infosusp
            #index_together_r1070_alteracao_infosusp
        )
        permissions = (
            ("can_view_r1070_alteracao_infosusp", "Can view r1070_alteracao_infosusp"),
            #custom_permissions_r1070_alteracao_infosusp
        )
        ordering = ['r1070_alteracao', 'indsusp', 'dtdecisao', 'inddeposito']



class r1070alteracaoinfoSuspSerializer(ModelSerializer):
    class Meta:
        model = r1070alteracaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070alteracaonovaValidade(SoftDeletionModel):
    r1070_alteracao = models.OneToOneField('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.inivalid)
    #r1070_alteracao_novavalidade_custom#

    class Meta:
        db_table = r'r1070_alteracao_novavalidade'       
        managed = True # r1070_alteracao_novavalidade #
        unique_together = (
            #custom_unique_together_r1070_alteracao_novavalidade#
            
        )
        index_together = (
            #custom_index_together_r1070_alteracao_novavalidade
            #index_together_r1070_alteracao_novavalidade
        )
        permissions = (
            ("can_view_r1070_alteracao_novavalidade", "Can view r1070_alteracao_novavalidade"),
            #custom_permissions_r1070_alteracao_novavalidade
        )
        ordering = ['r1070_alteracao', 'inivalid']



class r1070alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = r1070alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070exclusao(SoftDeletionModel):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_EXCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid)
    #r1070_exclusao_custom#

    class Meta:
        db_table = r'r1070_exclusao'       
        managed = True # r1070_exclusao #
        unique_together = (
            #custom_unique_together_r1070_exclusao#
            
        )
        index_together = (
            #custom_index_together_r1070_exclusao
            #index_together_r1070_exclusao
        )
        permissions = (
            ("can_view_r1070_exclusao", "Can view r1070_exclusao"),
            #custom_permissions_r1070_exclusao
        )
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid']



class r1070exclusaoSerializer(ModelSerializer):
    class Meta:
        model = r1070exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070inclusao(SoftDeletionModel):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_R1070_INCLUSAO_INDAUTORIA)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.indautoria)
    #r1070_inclusao_custom#

    class Meta:
        db_table = r'r1070_inclusao'       
        managed = True # r1070_inclusao #
        unique_together = (
            #custom_unique_together_r1070_inclusao#
            
        )
        index_together = (
            #custom_index_together_r1070_inclusao
            #index_together_r1070_inclusao
        )
        permissions = (
            ("can_view_r1070_inclusao", "Can view r1070_inclusao"),
            #custom_permissions_r1070_inclusao
        )
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'indautoria']



class r1070inclusaoSerializer(ModelSerializer):
    class Meta:
        model = r1070inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070inclusaodadosProcJud(SoftDeletionModel):
    r1070_inclusao = models.OneToOneField('r1070inclusao',
        related_name='%(class)s_r1070_inclusao')
    def evento(self): return self.r1070_inclusao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.CharField(max_length=4)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_inclusao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #r1070_inclusao_dadosprocjud_custom#

    class Meta:
        db_table = r'r1070_inclusao_dadosprocjud'       
        managed = True # r1070_inclusao_dadosprocjud #
        unique_together = (
            #custom_unique_together_r1070_inclusao_dadosprocjud#
            
        )
        index_together = (
            #custom_index_together_r1070_inclusao_dadosprocjud
            #index_together_r1070_inclusao_dadosprocjud
        )
        permissions = (
            ("can_view_r1070_inclusao_dadosprocjud", "Can view r1070_inclusao_dadosprocjud"),
            #custom_permissions_r1070_inclusao_dadosprocjud
        )
        ordering = ['r1070_inclusao', 'ufvara', 'codmunic', 'idvara']



class r1070inclusaodadosProcJudSerializer(ModelSerializer):
    class Meta:
        model = r1070inclusaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1070inclusaoinfoSusp(SoftDeletionModel):
    r1070_inclusao = models.ForeignKey('r1070inclusao',
        related_name='%(class)s_r1070_inclusao')
    def evento(self): return self.r1070_inclusao.evento()
    codsusp = models.IntegerField(blank=True, null=True)
    indsusp = models.CharField(choices=CHOICES_R1070_INCLUSAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_R1070_INCLUSAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1070_inclusao) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #r1070_inclusao_infosusp_custom#

    class Meta:
        db_table = r'r1070_inclusao_infosusp'       
        managed = True # r1070_inclusao_infosusp #
        unique_together = (
            #custom_unique_together_r1070_inclusao_infosusp#
            
        )
        index_together = (
            #custom_index_together_r1070_inclusao_infosusp
            #index_together_r1070_inclusao_infosusp
        )
        permissions = (
            ("can_view_r1070_inclusao_infosusp", "Can view r1070_inclusao_infosusp"),
            #custom_permissions_r1070_inclusao_infosusp
        )
        ordering = ['r1070_inclusao', 'indsusp', 'dtdecisao', 'inddeposito']



class r1070inclusaoinfoSuspSerializer(ModelSerializer):
    class Meta:
        model = r1070inclusaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
