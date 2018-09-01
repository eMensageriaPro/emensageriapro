#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_R2040_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2040_TPREPASSE = (
    (1, u'1 - Patrocínio'),
    (2, u'2 - Licenciamento de marcas e símbolos'),
    (3, u'3 - Publicidade'),
    (4, u'4 - Propaganda'),
    (5, u'5 - Transmissão de espetáculos'),
)

class r2040infoProc(models.Model):
    r2040_recursosrep = models.ForeignKey('r2040recursosRep',
        related_name='%(class)s_r2040_recursosrep')
    def evento(self): return self.r2040_recursosrep.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2040_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_recursosrep) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vlrnret)
    #r2040_infoproc_custom#
    #r2040_infoproc_custom#
    class Meta:
        db_table = r'r2040_infoproc'
        managed = True
        ordering = ['r2040_recursosrep', 'tpproc', 'nrproc', 'codsusp', 'vlrnret']


class r2040infoRecurso(models.Model):
    r2040_recursosrep = models.ForeignKey('r2040recursosRep',
        related_name='%(class)s_r2040_recursosrep')
    def evento(self): return self.r2040_recursosrep.evento()
    tprepasse = models.IntegerField(choices=CHOICES_R2040_TPREPASSE)
    descrecurso = models.CharField(max_length=20)
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_recursosrep) + ' - ' + unicode(self.tprepasse) + ' - ' + unicode(self.descrecurso) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vlrretapur)
    #r2040_inforecurso_custom#
    #r2040_inforecurso_custom#
    class Meta:
        db_table = r'r2040_inforecurso'
        managed = True
        ordering = ['r2040_recursosrep', 'tprepasse', 'descrecurso', 'vlrbruto', 'vlrretapur']


class r2040recursosRep(models.Model):
    r2040_evtassocdesprep = models.ForeignKey('efdreinf.r2040evtAssocDespRep',
        related_name='%(class)s_r2040_evtassocdesprep')
    def evento(self): return self.r2040_evtassocdesprep.evento()
    cnpjassocdesp = models.CharField(max_length=14)
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2040_evtassocdesprep) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.vlrtotalret) + ' - ' + unicode(self.vlrtotalnret)
    #r2040_recursosrep_custom#
    #r2040_recursosrep_custom#
    class Meta:
        db_table = r'r2040_recursosrep'
        managed = True
        ordering = ['r2040_evtassocdesprep', 'cnpjassocdesp', 'vlrtotalrep', 'vlrtotalret', 'vlrtotalnret']


#VIEWS_MODELS
