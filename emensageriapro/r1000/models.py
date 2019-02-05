#coding: utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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



CHOICES_R1000_ALTERACAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_R1000_ALTERACAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_R1000_ALTERACAO_INDDESONERACAO = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos termos da Lei 12.546/2011 e alterações'),
)

CHOICES_R1000_ALTERACAO_INDESCRITURACAO = (
    (0, u'0 - Empresa Não obrigada à ECD'),
    (1, u'1 - Empresa obrigada à ECD'),
)

CHOICES_R1000_ALTERACAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
)

CHOICES_R1000_INCLUSAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_R1000_INCLUSAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_R1000_INCLUSAO_INDDESONERACAO = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos termos da Lei 12.546/2011 e alterações'),
)

CHOICES_R1000_INCLUSAO_INDESCRITURACAO = (
    (0, u'0 - Empresa Não obrigada à ECD'),
    (1, u'1 - Empresa obrigada à ECD'),
)

CHOICES_R1000_INCLUSAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
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

class r1000alteracao(SoftDeletionModel):
    r1000_evtinfocontri = models.OneToOneField('efdreinf.r1000evtInfoContri',
        related_name='%(class)s_r1000_evtinfocontri')
    def evento(self): return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    classtrib = models.CharField(max_length=2)
    indescrituracao = models.IntegerField(choices=CHOICES_R1000_ALTERACAO_INDESCRITURACAO)
    inddesoneracao = models.IntegerField(choices=CHOICES_R1000_ALTERACAO_INDDESONERACAO)
    indacordoisenmulta = models.IntegerField(choices=CHOICES_R1000_ALTERACAO_INDACORDOISENMULTA)
    indsitpj = models.IntegerField(choices=CHOICES_R1000_ALTERACAO_INDSITPJ, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_evtinfocontri) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.indescrituracao) + ' - ' + unicode(self.inddesoneracao) + ' - ' + unicode(self.indacordoisenmulta) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)
    #r1000_alteracao_custom#

    class Meta:
        db_table = r'r1000_alteracao'       
        managed = True # r1000_alteracao #
        permissions = (
            ("can_view_r1000_alteracao", "Can view r1000_alteracao"),
            #custom_permissions_r1000_alteracao
        )
        ordering = ['r1000_evtinfocontri', 'inivalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'nmctt', 'cpfctt']



class r1000alteracaoSerializer(ModelSerializer):
    class Meta:
        model = r1000alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000alteracaoinfoEFR(SoftDeletionModel):
    r1000_alteracao = models.OneToOneField('r1000alteracao',
        related_name='%(class)s_r1000_alteracao')
    def evento(self): return self.r1000_alteracao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_ALTERACAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_alteracao) + ' - ' + unicode(self.ideefr)
    #r1000_alteracao_infoefr_custom#

    class Meta:
        db_table = r'r1000_alteracao_infoefr'       
        managed = True # r1000_alteracao_infoefr #
        permissions = (
            ("can_view_r1000_alteracao_infoefr", "Can view r1000_alteracao_infoefr"),
            #custom_permissions_r1000_alteracao_infoefr
        )
        ordering = ['r1000_alteracao', 'ideefr']



class r1000alteracaoinfoEFRSerializer(ModelSerializer):
    class Meta:
        model = r1000alteracaoinfoEFR
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000alteracaonovaValidade(SoftDeletionModel):
    r1000_alteracao = models.OneToOneField('r1000alteracao',
        related_name='%(class)s_r1000_alteracao')
    def evento(self): return self.r1000_alteracao.evento()
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
        return unicode(self.r1000_alteracao) + ' - ' + unicode(self.inivalid)
    #r1000_alteracao_novavalidade_custom#

    class Meta:
        db_table = r'r1000_alteracao_novavalidade'       
        managed = True # r1000_alteracao_novavalidade #
        permissions = (
            ("can_view_r1000_alteracao_novavalidade", "Can view r1000_alteracao_novavalidade"),
            #custom_permissions_r1000_alteracao_novavalidade
        )
        ordering = ['r1000_alteracao', 'inivalid']



class r1000alteracaonovaValidadeSerializer(ModelSerializer):
    class Meta:
        model = r1000alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000alteracaosoftHouse(SoftDeletionModel):
    r1000_alteracao = models.ForeignKey('r1000alteracao',
        related_name='%(class)s_r1000_alteracao')
    def evento(self): return self.r1000_alteracao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=115)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_alteracao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont)
    #r1000_alteracao_softhouse_custom#

    class Meta:
        db_table = r'r1000_alteracao_softhouse'       
        managed = True # r1000_alteracao_softhouse #
        permissions = (
            ("can_view_r1000_alteracao_softhouse", "Can view r1000_alteracao_softhouse"),
            #custom_permissions_r1000_alteracao_softhouse
        )
        ordering = ['r1000_alteracao', 'cnpjsofthouse', 'nmrazao', 'nmcont']



class r1000alteracaosoftHouseSerializer(ModelSerializer):
    class Meta:
        model = r1000alteracaosoftHouse
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000exclusao(SoftDeletionModel):
    r1000_evtinfocontri = models.OneToOneField('efdreinf.r1000evtInfoContri',
        related_name='%(class)s_r1000_evtinfocontri')
    def evento(self): return self.r1000_evtinfocontri.evento()
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
        return unicode(self.r1000_evtinfocontri) + ' - ' + unicode(self.inivalid)
    #r1000_exclusao_custom#

    class Meta:
        db_table = r'r1000_exclusao'       
        managed = True # r1000_exclusao #
        permissions = (
            ("can_view_r1000_exclusao", "Can view r1000_exclusao"),
            #custom_permissions_r1000_exclusao
        )
        ordering = ['r1000_evtinfocontri', 'inivalid']



class r1000exclusaoSerializer(ModelSerializer):
    class Meta:
        model = r1000exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000inclusao(SoftDeletionModel):
    r1000_evtinfocontri = models.OneToOneField('efdreinf.r1000evtInfoContri',
        related_name='%(class)s_r1000_evtinfocontri')
    def evento(self): return self.r1000_evtinfocontri.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    classtrib = models.CharField(max_length=2)
    indescrituracao = models.IntegerField(choices=CHOICES_R1000_INCLUSAO_INDESCRITURACAO)
    inddesoneracao = models.IntegerField(choices=CHOICES_R1000_INCLUSAO_INDDESONERACAO)
    indacordoisenmulta = models.IntegerField(choices=CHOICES_R1000_INCLUSAO_INDACORDOISENMULTA)
    indsitpj = models.IntegerField(choices=CHOICES_R1000_INCLUSAO_INDSITPJ, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_evtinfocontri) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.indescrituracao) + ' - ' + unicode(self.inddesoneracao) + ' - ' + unicode(self.indacordoisenmulta) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt)
    #r1000_inclusao_custom#

    class Meta:
        db_table = r'r1000_inclusao'       
        managed = True # r1000_inclusao #
        permissions = (
            ("can_view_r1000_inclusao", "Can view r1000_inclusao"),
            #custom_permissions_r1000_inclusao
        )
        ordering = ['r1000_evtinfocontri', 'inivalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'nmctt', 'cpfctt']



class r1000inclusaoSerializer(ModelSerializer):
    class Meta:
        model = r1000inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000inclusaoinfoEFR(SoftDeletionModel):
    r1000_inclusao = models.OneToOneField('r1000inclusao',
        related_name='%(class)s_r1000_inclusao')
    def evento(self): return self.r1000_inclusao.evento()
    ideefr = models.CharField(choices=CHOICES_R1000_INCLUSAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_inclusao) + ' - ' + unicode(self.ideefr)
    #r1000_inclusao_infoefr_custom#

    class Meta:
        db_table = r'r1000_inclusao_infoefr'       
        managed = True # r1000_inclusao_infoefr #
        permissions = (
            ("can_view_r1000_inclusao_infoefr", "Can view r1000_inclusao_infoefr"),
            #custom_permissions_r1000_inclusao_infoefr
        )
        ordering = ['r1000_inclusao', 'ideefr']



class r1000inclusaoinfoEFRSerializer(ModelSerializer):
    class Meta:
        model = r1000inclusaoinfoEFR
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class r1000inclusaosoftHouse(SoftDeletionModel):
    r1000_inclusao = models.ForeignKey('r1000inclusao',
        related_name='%(class)s_r1000_inclusao')
    def evento(self): return self.r1000_inclusao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=115)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.r1000_inclusao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont)
    #r1000_inclusao_softhouse_custom#

    class Meta:
        db_table = r'r1000_inclusao_softhouse'       
        managed = True # r1000_inclusao_softhouse #
        permissions = (
            ("can_view_r1000_inclusao_softhouse", "Can view r1000_inclusao_softhouse"),
            #custom_permissions_r1000_inclusao_softhouse
        )
        ordering = ['r1000_inclusao', 'cnpjsofthouse', 'nmrazao', 'nmcont']



class r1000inclusaosoftHouseSerializer(ModelSerializer):
    class Meta:
        model = r1000inclusaosoftHouse
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

#VIEWS_MODELS
