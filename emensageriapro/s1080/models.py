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

CHOICES_S1080_ALTERACAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
)

CHOICES_S1080_INCLUSAO_ALIQRAT = (
    (1, u'1 - 1'),
    (2, u'2 - 2'),
    (3, u'3 - 3'),
)

class s1080alteracao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    aliqrat = models.IntegerField(choices=CHOICES_S1080_ALTERACAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s1080_alteracao_custom#
    #s1080_alteracao_custom#
    class Meta:
        db_table = r's1080_alteracao'
        managed = True
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'fimvalid', 'aliqrat', 'fap', 'aliqratajust']


class s1080alteracaonovaValidade(models.Model):
    s1080_alteracao = models.OneToOneField('s1080alteracao',
        related_name='%(class)s_s1080_alteracao')
    def evento(self): return self.s1080_alteracao.evento()
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
        return unicode(self.s1080_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1080_alteracao_novavalidade_custom#
    #s1080_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1080_alteracao_novavalidade'
        managed = True
        ordering = ['s1080_alteracao', 'inivalid', 'fimvalid']


class s1080exclusao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
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
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1080_exclusao_custom#
    #s1080_exclusao_custom#
    class Meta:
        db_table = r's1080_exclusao'
        managed = True
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'fimvalid']


class s1080inclusao(models.Model):
    s1080_evttaboperport = models.OneToOneField('esocial.s1080evtTabOperPort',
        related_name='%(class)s_s1080_evttaboperport')
    def evento(self): return self.s1080_evttaboperport.evento()
    cnpjopportuario = models.CharField(max_length=14)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    aliqrat = models.IntegerField(choices=CHOICES_S1080_INCLUSAO_ALIQRAT)
    fap = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    aliqratajust = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1080_evttaboperport) + ' - ' + unicode(self.cnpjopportuario) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.aliqrat) + ' - ' + unicode(self.fap) + ' - ' + unicode(self.aliqratajust)
    #s1080_inclusao_custom#
    #s1080_inclusao_custom#
    class Meta:
        db_table = r's1080_inclusao'
        managed = True
        ordering = ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'fimvalid', 'aliqrat', 'fap', 'aliqratajust']


#VIEWS_MODELS
