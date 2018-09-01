#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_R2010_TPPROCRETADIC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2010_TPPROCRETPRINC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2010infoProcRetAd(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    tpprocretadic = models.IntegerField(choices=CHOICES_R2010_TPPROCRETADIC)
    nrprocretadic = models.CharField(max_length=21)
    codsuspadic = models.IntegerField(blank=True, null=True)
    valoradic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.tpprocretadic) + ' - ' + unicode(self.nrprocretadic) + ' - ' + unicode(self.codsuspadic) + ' - ' + unicode(self.valoradic)
    #r2010_infoprocretad_custom#
    #r2010_infoprocretad_custom#
    class Meta:
        db_table = r'r2010_infoprocretad'
        managed = True
        ordering = ['r2010_evtservtom', 'tpprocretadic', 'nrprocretadic', 'codsuspadic', 'valoradic']


class r2010infoProcRetPr(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    tpprocretprinc = models.IntegerField(choices=CHOICES_R2010_TPPROCRETPRINC)
    nrprocretprinc = models.CharField(max_length=21)
    codsuspprinc = models.IntegerField(blank=True, null=True)
    valorprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.tpprocretprinc) + ' - ' + unicode(self.nrprocretprinc) + ' - ' + unicode(self.codsuspprinc) + ' - ' + unicode(self.valorprinc)
    #r2010_infoprocretpr_custom#
    #r2010_infoprocretpr_custom#
    class Meta:
        db_table = r'r2010_infoprocretpr'
        managed = True
        ordering = ['r2010_evtservtom', 'tpprocretprinc', 'nrprocretprinc', 'codsuspprinc', 'valorprinc']


class r2010infoTpServ(models.Model):
    r2010_nfs = models.ForeignKey('r2010nfs',
        related_name='%(class)s_r2010_nfs')
    def evento(self): return self.r2010_nfs.evento()
    tpservico = models.IntegerField()
    vlrbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretencao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretsub = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlradicional = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_nfs) + ' - ' + unicode(self.tpservico) + ' - ' + unicode(self.vlrbaseret) + ' - ' + unicode(self.vlrretencao) + ' - ' + unicode(self.vlrretsub) + ' - ' + unicode(self.vlrnretprinc) + ' - ' + unicode(self.vlrservicos15) + ' - ' + unicode(self.vlrservicos20) + ' - ' + unicode(self.vlrservicos25) + ' - ' + unicode(self.vlradicional) + ' - ' + unicode(self.vlrnretadic)
    #r2010_infotpserv_custom#
    #r2010_infotpserv_custom#
    class Meta:
        db_table = r'r2010_infotpserv'
        managed = True
        ordering = ['r2010_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao', 'vlrretsub', 'vlrnretprinc', 'vlrservicos15', 'vlrservicos20', 'vlrservicos25', 'vlradicional', 'vlrnretadic']


class r2010nfs(models.Model):
    r2010_evtservtom = models.ForeignKey('efdreinf.r2010evtServTom',
        related_name='%(class)s_r2010_evtservtom')
    def evento(self): return self.r2010_evtservtom.evento()
    serie = models.CharField(max_length=5)
    numdocto = models.CharField(max_length=15)
    dtemissaonf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    obs = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2010_evtservtom) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.numdocto) + ' - ' + unicode(self.dtemissaonf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.obs)
    #r2010_nfs_custom#
    #r2010_nfs_custom#
    class Meta:
        db_table = r'r2010_nfs'
        managed = True
        ordering = ['r2010_evtservtom', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto', 'obs']


#VIEWS_MODELS
