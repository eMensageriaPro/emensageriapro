#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



PERIODOS = (
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
)

class s1040alteracao(models.Model):
    s1040_evttabfuncao = models.OneToOneField('esocial.s1040evtTabFuncao',
        related_name='%(class)s_s1040_evttabfuncao')
    def evento(self): return self.s1040_evttabfuncao.evento()
    codfuncao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscfuncao = models.CharField(max_length=100)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1040_evttabfuncao) + ' - ' + unicode(self.codfuncao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dscfuncao) + ' - ' + unicode(self.codcbo)
    #s1040_alteracao_custom#
    #s1040_alteracao_custom#
    class Meta:
        db_table = r's1040_alteracao'
        managed = True
        ordering = ['s1040_evttabfuncao', 'codfuncao', 'inivalid', 'fimvalid', 'dscfuncao', 'codcbo']


class s1040alteracaonovaValidade(models.Model):
    s1040_alteracao = models.OneToOneField('s1040alteracao',
        related_name='%(class)s_s1040_alteracao')
    def evento(self): return self.s1040_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1040_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1040_alteracao_novavalidade_custom#
    #s1040_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1040_alteracao_novavalidade'
        managed = True
        ordering = ['s1040_alteracao', 'inivalid', 'fimvalid']


class s1040exclusao(models.Model):
    s1040_evttabfuncao = models.OneToOneField('esocial.s1040evtTabFuncao',
        related_name='%(class)s_s1040_evttabfuncao')
    def evento(self): return self.s1040_evttabfuncao.evento()
    codfuncao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1040_evttabfuncao) + ' - ' + unicode(self.codfuncao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1040_exclusao_custom#
    #s1040_exclusao_custom#
    class Meta:
        db_table = r's1040_exclusao'
        managed = True
        ordering = ['s1040_evttabfuncao', 'codfuncao', 'inivalid', 'fimvalid']


class s1040inclusao(models.Model):
    s1040_evttabfuncao = models.OneToOneField('esocial.s1040evtTabFuncao',
        related_name='%(class)s_s1040_evttabfuncao')
    def evento(self): return self.s1040_evttabfuncao.evento()
    codfuncao = models.CharField(max_length=30)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    dscfuncao = models.CharField(max_length=100)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1040_evttabfuncao) + ' - ' + unicode(self.codfuncao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.dscfuncao) + ' - ' + unicode(self.codcbo)
    #s1040_inclusao_custom#
    #s1040_inclusao_custom#
    class Meta:
        db_table = r's1040_inclusao'
        managed = True
        ordering = ['s1040_evttabfuncao', 'codfuncao', 'inivalid', 'fimvalid', 'dscfuncao', 'codcbo']


#VIEWS_MODELS
