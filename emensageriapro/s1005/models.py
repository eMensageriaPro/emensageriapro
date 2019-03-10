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



CHOICES_S1005_ALTERACAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
)

CHOICES_S1005_ALTERACAO_CONTAPR = (
    (0, u'0 - Dispensado de acordo com a lei'),
    (1, u'1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial'),
    (2, u'2 - Obrigado'),
)

CHOICES_S1005_ALTERACAO_CONTENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1005_ALTERACAO_CONTPCD = (
    (0, u'0 - Dispensado de acordo com a lei'),
    (1, u'1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial'),
    (2, u'2 - Com exigibilidade suspensa, mesmo que parcialmente em virtude de Termo de Compromisso firmado com o Ministério do Trabalho'),
    (9, u'9 - Obrigado'),
)

CHOICES_S1005_ALTERACAO_INDSUBSTPATROBRA = (
    (1, u'1 - Contribuição Patronal Substituída'),
    (2, u'2 - Contribuição Patronal Não Substituída'),
)

CHOICES_S1005_ALTERACAO_REGPT = (
    (0, u'0 - Não utiliza'),
    (1, u'1 - Manual'),
    (2, u'2 - Mecânico'),
    (3, u'3 - Eletrônico (portaria MTE 1.510/2009)'),
    (4, u'4 - Não eletrônico alternativo (art. 1° da Portaria MTE 373/2011)'),
    (5, u'5 - Eletrônico alternativo ( art. 2° da Portaria MTE 373/2011)'),
    (6, u'6 - Eletrônico - outros'),
)

CHOICES_S1005_ALTERACAO_TPCAEPF = (
    (1, u'1 - Contribuinte Individual'),
    (2, u'2 - Produtor Rural'),
    (3, u'3 - Segurado Especial'),
)

CHOICES_S1005_ALTERACAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1005_ALTERACAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (4, u'4 - Processo FAP'),
)

CHOICES_S1005_EXCLUSAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1005_INCLUSAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
)

CHOICES_S1005_INCLUSAO_CONTAPR = (
    (0, u'0 - Dispensado de acordo com a lei'),
    (1, u'1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial'),
    (2, u'2 - Obrigado'),
)

CHOICES_S1005_INCLUSAO_CONTENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1005_INCLUSAO_CONTPCD = (
    (0, u'0 - Dispensado de acordo com a lei'),
    (1, u'1 - Dispensado, mesmo que parcialmente, em virtude de processo judicial'),
    (2, u'2 - Com exigibilidade suspensa, mesmo que parcialmente em virtude de Termo de Compromisso firmado com o Ministério do Trabalho'),
    (9, u'9 - Obrigado'),
)

CHOICES_S1005_INCLUSAO_INDSUBSTPATROBRA = (
    (1, u'1 - Contribuição Patronal Substituída'),
    (2, u'2 - Contribuição Patronal Não Substituída'),
)

CHOICES_S1005_INCLUSAO_REGPT = (
    (0, u'0 - Não utiliza'),
    (1, u'1 - Manual'),
    (2, u'2 - Mecânico'),
    (3, u'3 - Eletrônico (portaria MTE 1.510/2009)'),
    (4, u'4 - Não eletrônico alternativo (art. 1° da Portaria MTE 373/2011)'),
    (5, u'5 - Eletrônico alternativo ( art. 2° da Portaria MTE 373/2011)'),
    (6, u'6 - Eletrônico - outros'),
)

CHOICES_S1005_INCLUSAO_TPCAEPF = (
    (1, u'1 - Contribuinte Individual'),
    (2, u'2 - Produtor Rural'),
    (3, u'3 - Segurado Especial'),
)

CHOICES_S1005_INCLUSAO_TPINSC = (
    (1, u'1 - CNPJ'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1005_INCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
    (4, u'4 - Processo FAP'),
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

class s1005alteracao(SoftDeletionModel):
    s1005_evttabestab = models.OneToOneField('esocial.s1005evtTabEstab',
        related_name='%(class)s_s1005_evttabestab')
    def evento(self): return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_TPINSC)
    nrinsc = models.CharField(max_length=15)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    cnaeprep = models.IntegerField()
    aliqrat = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    regpt = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_REGPT)
    contapr = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_CONTAPR)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    contented = models.CharField(choices=CHOICES_S1005_ALTERACAO_CONTENTED, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_evttabestab) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.cnaeprep) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.regpt) + ' - ' + unicode(self.contapr)
    #s1005_alteracao_custom#

    class Meta:
        db_table = r's1005_alteracao'       
        managed = True # s1005_alteracao #
        unique_together = (
            #custom_unique_together_s1005_alteracao#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao
            #index_together_s1005_alteracao
        )
        permissions = (
            ("can_view_s1005_alteracao", "Can view s1005_alteracao"),
            #custom_permissions_s1005_alteracao
        )
        ordering = ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid', 'cnaeprep', 'aliqrat', 'regpt', 'contapr']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    tpcaepf = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_TPCAEPF)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.tpcaepf)
    #s1005_alteracao_infocaepf_custom#

    class Meta:
        db_table = r's1005_alteracao_infocaepf'       
        managed = True # s1005_alteracao_infocaepf #
        unique_together = (
            #custom_unique_together_s1005_alteracao_infocaepf#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_infocaepf
            #index_together_s1005_alteracao_infocaepf
        )
        permissions = (
            ("can_view_s1005_alteracao_infocaepf", "Can view s1005_alteracao_infocaepf"),
            #custom_permissions_s1005_alteracao_infocaepf
        )
        ordering = ['s1005_alteracao', 'tpcaepf']



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
    s1005_alteracao = models.ForeignKey('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.nrinsc)
    #s1005_alteracao_infoenteduc_custom#

    class Meta:
        db_table = r's1005_alteracao_infoenteduc'       
        managed = True # s1005_alteracao_infoenteduc #
        unique_together = (
            #custom_unique_together_s1005_alteracao_infoenteduc#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_infoenteduc
            #index_together_s1005_alteracao_infoenteduc
        )
        permissions = (
            ("can_view_s1005_alteracao_infoenteduc", "Can view s1005_alteracao_infoenteduc"),
            #custom_permissions_s1005_alteracao_infoenteduc
        )
        ordering = ['s1005_alteracao', 'nrinsc']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_INDSUBSTPATROBRA)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.indsubstpatrobra)
    #s1005_alteracao_infoobra_custom#

    class Meta:
        db_table = r's1005_alteracao_infoobra'       
        managed = True # s1005_alteracao_infoobra #
        unique_together = (
            #custom_unique_together_s1005_alteracao_infoobra#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_infoobra
            #index_together_s1005_alteracao_infoobra
        )
        permissions = (
            ("can_view_s1005_alteracao_infoobra", "Can view s1005_alteracao_infoobra"),
            #custom_permissions_s1005_alteracao_infoobra
        )
        ordering = ['s1005_alteracao', 'indsubstpatrobra']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    contpcd = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_CONTPCD)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.contpcd)
    #s1005_alteracao_infopcd_custom#

    class Meta:
        db_table = r's1005_alteracao_infopcd'       
        managed = True # s1005_alteracao_infopcd #
        unique_together = (
            #custom_unique_together_s1005_alteracao_infopcd#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_infopcd
            #index_together_s1005_alteracao_infopcd
        )
        permissions = (
            ("can_view_s1005_alteracao_infopcd", "Can view s1005_alteracao_infopcd"),
            #custom_permissions_s1005_alteracao_infopcd
        )
        ordering = ['s1005_alteracao', 'contpcd']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
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
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.inivalid)
    #s1005_alteracao_novavalidade_custom#

    class Meta:
        db_table = r's1005_alteracao_novavalidade'       
        managed = True # s1005_alteracao_novavalidade #
        unique_together = (
            #custom_unique_together_s1005_alteracao_novavalidade#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_novavalidade
            #index_together_s1005_alteracao_novavalidade
        )
        permissions = (
            ("can_view_s1005_alteracao_novavalidade", "Can view s1005_alteracao_novavalidade"),
            #custom_permissions_s1005_alteracao_novavalidade
        )
        ordering = ['s1005_alteracao', 'inivalid']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1005_alteracao_procadmjudfap_custom#

    class Meta:
        db_table = r's1005_alteracao_procadmjudfap'       
        managed = True # s1005_alteracao_procadmjudfap #
        unique_together = (
            #custom_unique_together_s1005_alteracao_procadmjudfap#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_procadmjudfap
            #index_together_s1005_alteracao_procadmjudfap
        )
        permissions = (
            ("can_view_s1005_alteracao_procadmjudfap", "Can view s1005_alteracao_procadmjudfap"),
            #custom_permissions_s1005_alteracao_procadmjudfap
        )
        ordering = ['s1005_alteracao', 'tpproc', 'nrproc', 'codsusp']



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
    s1005_alteracao = models.OneToOneField('s1005alteracao',
        related_name='%(class)s_s1005_alteracao')
    def evento(self): return self.s1005_alteracao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_alteracao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1005_alteracao_procadmjudrat_custom#

    class Meta:
        db_table = r's1005_alteracao_procadmjudrat'       
        managed = True # s1005_alteracao_procadmjudrat #
        unique_together = (
            #custom_unique_together_s1005_alteracao_procadmjudrat#
            
        )
        index_together = (
            #custom_index_together_s1005_alteracao_procadmjudrat
            #index_together_s1005_alteracao_procadmjudrat
        )
        permissions = (
            ("can_view_s1005_alteracao_procadmjudrat", "Can view s1005_alteracao_procadmjudrat"),
            #custom_permissions_s1005_alteracao_procadmjudrat
        )
        ordering = ['s1005_alteracao', 'tpproc', 'nrproc', 'codsusp']



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
    s1005_evttabestab = models.OneToOneField('esocial.s1005evtTabEstab',
        related_name='%(class)s_s1005_evttabestab')
    def evento(self): return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_EXCLUSAO_TPINSC)
    nrinsc = models.CharField(max_length=15)
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
        return unicode(self.s1005_evttabestab) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.inivalid)
    #s1005_exclusao_custom#

    class Meta:
        db_table = r's1005_exclusao'       
        managed = True # s1005_exclusao #
        unique_together = (
            #custom_unique_together_s1005_exclusao#
            
        )
        index_together = (
            #custom_index_together_s1005_exclusao
            #index_together_s1005_exclusao
        )
        permissions = (
            ("can_view_s1005_exclusao", "Can view s1005_exclusao"),
            #custom_permissions_s1005_exclusao
        )
        ordering = ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid']



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
    s1005_evttabestab = models.OneToOneField('esocial.s1005evtTabEstab',
        related_name='%(class)s_s1005_evttabestab')
    def evento(self): return self.s1005_evttabestab.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_TPINSC)
    nrinsc = models.CharField(max_length=15)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    cnaeprep = models.IntegerField()
    aliqrat = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    regpt = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_REGPT)
    contapr = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_CONTAPR)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    contented = models.CharField(choices=CHOICES_S1005_INCLUSAO_CONTENTED, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_evttabestab) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.cnaeprep) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.regpt) + ' - ' + unicode(self.contapr)
    #s1005_inclusao_custom#

    class Meta:
        db_table = r's1005_inclusao'       
        managed = True # s1005_inclusao #
        unique_together = (
            #custom_unique_together_s1005_inclusao#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao
            #index_together_s1005_inclusao
        )
        permissions = (
            ("can_view_s1005_inclusao", "Can view s1005_inclusao"),
            #custom_permissions_s1005_inclusao
        )
        ordering = ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid', 'cnaeprep', 'aliqrat', 'regpt', 'contapr']



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
    s1005_inclusao = models.OneToOneField('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    tpcaepf = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_TPCAEPF)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.tpcaepf)
    #s1005_inclusao_infocaepf_custom#

    class Meta:
        db_table = r's1005_inclusao_infocaepf'       
        managed = True # s1005_inclusao_infocaepf #
        unique_together = (
            #custom_unique_together_s1005_inclusao_infocaepf#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_infocaepf
            #index_together_s1005_inclusao_infocaepf
        )
        permissions = (
            ("can_view_s1005_inclusao_infocaepf", "Can view s1005_inclusao_infocaepf"),
            #custom_permissions_s1005_inclusao_infocaepf
        )
        ordering = ['s1005_inclusao', 'tpcaepf']



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
    s1005_inclusao = models.ForeignKey('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.nrinsc)
    #s1005_inclusao_infoenteduc_custom#

    class Meta:
        db_table = r's1005_inclusao_infoenteduc'       
        managed = True # s1005_inclusao_infoenteduc #
        unique_together = (
            #custom_unique_together_s1005_inclusao_infoenteduc#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_infoenteduc
            #index_together_s1005_inclusao_infoenteduc
        )
        permissions = (
            ("can_view_s1005_inclusao_infoenteduc", "Can view s1005_inclusao_infoenteduc"),
            #custom_permissions_s1005_inclusao_infoenteduc
        )
        ordering = ['s1005_inclusao', 'nrinsc']



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
    s1005_inclusao = models.OneToOneField('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    indsubstpatrobra = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_INDSUBSTPATROBRA)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.indsubstpatrobra)
    #s1005_inclusao_infoobra_custom#

    class Meta:
        db_table = r's1005_inclusao_infoobra'       
        managed = True # s1005_inclusao_infoobra #
        unique_together = (
            #custom_unique_together_s1005_inclusao_infoobra#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_infoobra
            #index_together_s1005_inclusao_infoobra
        )
        permissions = (
            ("can_view_s1005_inclusao_infoobra", "Can view s1005_inclusao_infoobra"),
            #custom_permissions_s1005_inclusao_infoobra
        )
        ordering = ['s1005_inclusao', 'indsubstpatrobra']



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
    s1005_inclusao = models.OneToOneField('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    contpcd = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_CONTPCD)
    nrprocjud = models.CharField(max_length=20, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.contpcd)
    #s1005_inclusao_infopcd_custom#

    class Meta:
        db_table = r's1005_inclusao_infopcd'       
        managed = True # s1005_inclusao_infopcd #
        unique_together = (
            #custom_unique_together_s1005_inclusao_infopcd#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_infopcd
            #index_together_s1005_inclusao_infopcd
        )
        permissions = (
            ("can_view_s1005_inclusao_infopcd", "Can view s1005_inclusao_infopcd"),
            #custom_permissions_s1005_inclusao_infopcd
        )
        ordering = ['s1005_inclusao', 'contpcd']



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
    s1005_inclusao = models.OneToOneField('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1005_inclusao_procadmjudfap_custom#

    class Meta:
        db_table = r's1005_inclusao_procadmjudfap'       
        managed = True # s1005_inclusao_procadmjudfap #
        unique_together = (
            #custom_unique_together_s1005_inclusao_procadmjudfap#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_procadmjudfap
            #index_together_s1005_inclusao_procadmjudfap
        )
        permissions = (
            ("can_view_s1005_inclusao_procadmjudfap", "Can view s1005_inclusao_procadmjudfap"),
            #custom_permissions_s1005_inclusao_procadmjudfap
        )
        ordering = ['s1005_inclusao', 'tpproc', 'nrproc', 'codsusp']



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
    s1005_inclusao = models.OneToOneField('s1005inclusao',
        related_name='%(class)s_s1005_inclusao')
    def evento(self): return self.s1005_inclusao.evento()
    tpproc = models.IntegerField(choices=CHOICES_S1005_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField()
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1005_inclusao) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp)
    #s1005_inclusao_procadmjudrat_custom#

    class Meta:
        db_table = r's1005_inclusao_procadmjudrat'       
        managed = True # s1005_inclusao_procadmjudrat #
        unique_together = (
            #custom_unique_together_s1005_inclusao_procadmjudrat#
            
        )
        index_together = (
            #custom_index_together_s1005_inclusao_procadmjudrat
            #index_together_s1005_inclusao_procadmjudrat
        )
        permissions = (
            ("can_view_s1005_inclusao_procadmjudrat", "Can view s1005_inclusao_procadmjudrat"),
            #custom_permissions_s1005_inclusao_procadmjudrat
        )
        ordering = ['s1005_inclusao', 'tpproc', 'nrproc', 'codsusp']



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
            

#VIEWS_MODELS
