#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S3000_INDAPURACAO = (
    (1, u'1 - Mensal'),
    (2, u'2 - Anual (13° salário)'),
)

class s3000ideFolhaPagto(models.Model):
    s3000_evtexclusao = models.OneToOneField('esocial.s3000evtExclusao',
        related_name='%(class)s_s3000_evtexclusao')
    def evento(self): return self.s3000_evtexclusao.evento()
    indapuracao = models.IntegerField(choices=CHOICES_S3000_INDAPURACAO)
    perapur = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s3000_evtexclusao) + ' - ' + unicode(self.indapuracao) + ' - ' + unicode(self.perapur)
    #s3000_idefolhapagto_custom#
    #s3000_idefolhapagto_custom#
    class Meta:
        db_table = r's3000_idefolhapagto'
        managed = True
        ordering = ['s3000_evtexclusao', 'indapuracao', 'perapur']


class s3000ideTrabalhador(models.Model):
    s3000_evtexclusao = models.OneToOneField('esocial.s3000evtExclusao',
        related_name='%(class)s_s3000_evtexclusao')
    def evento(self): return self.s3000_evtexclusao.evento()
    cpftrab = models.CharField(max_length=11)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s3000_evtexclusao) + ' - ' + unicode(self.cpftrab) + ' - ' + unicode(self.nistrab)
    #s3000_idetrabalhador_custom#
    #s3000_idetrabalhador_custom#
    class Meta:
        db_table = r's3000_idetrabalhador'
        managed = True
        ordering = ['s3000_evtexclusao', 'cpftrab', 'nistrab']


#VIEWS_MODELS
