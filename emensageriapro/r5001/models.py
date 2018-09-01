#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_R5001_TPINSCTOMADOR = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R5001_TPOCORR = (
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
)

class r5001RCPRB(models.Model):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crcprb = models.IntegerField()
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crcprb) + ' - ' + unicode(self.vlrcrcprb) + ' - ' + unicode(self.vlrcrcprbsusp)
    #r5001_rcprb_custom#
    #r5001_rcprb_custom#
    class Meta:
        db_table = r'r5001_rcprb'
        managed = True
        ordering = ['r5001_infototal', 'crcprb', 'vlrcrcprb', 'vlrcrcprbsusp']


class r5001RComl(models.Model):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crcoml = models.IntegerField()
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crcoml) + ' - ' + unicode(self.vlrcrcoml) + ' - ' + unicode(self.vlrcrcomlsusp)
    #r5001_rcoml_custom#
    #r5001_rcoml_custom#
    class Meta:
        db_table = r'r5001_rcoml'
        managed = True
        ordering = ['r5001_infototal', 'crcoml', 'vlrcrcoml', 'vlrcrcomlsusp']


class r5001RPrest(models.Model):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    tpinsctomador = models.IntegerField(choices=CHOICES_R5001_TPINSCTOMADOR)
    nrinsctomador = models.CharField(max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc) + ' - ' + unicode(self.vlrtotalretadic) + ' - ' + unicode(self.vlrtotalnretprinc) + ' - ' + unicode(self.vlrtotalnretadic)
    #r5001_rprest_custom#
    #r5001_rprest_custom#
    class Meta:
        db_table = r'r5001_rprest'
        managed = True
        ordering = ['r5001_infototal', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic']


class r5001RRecEspetDesp(models.Model):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    crrecespetdesp = models.IntegerField()
    vlrreceitatotal = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecespetdesp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecespetdespsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.crrecespetdesp) + ' - ' + unicode(self.vlrreceitatotal) + ' - ' + unicode(self.vlrcrrecespetdesp) + ' - ' + unicode(self.vlrcrrecespetdespsusp)
    #r5001_rrecespetdesp_custom#
    #r5001_rrecespetdesp_custom#
    class Meta:
        db_table = r'r5001_rrecespetdesp'
        managed = True
        ordering = ['r5001_infototal', 'crrecespetdesp', 'vlrreceitatotal', 'vlrcrrecespetdesp', 'vlrcrrecespetdespsusp']


class r5001RRecRepAD(models.Model):
    r5001_infototal = models.ForeignKey('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    cnpjassocdesp = models.CharField(max_length=14)
    vlrtotalrep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    crrecrepad = models.IntegerField()
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.crrecrepad) + ' - ' + unicode(self.vlrcrrecrepad) + ' - ' + unicode(self.vlrcrrecrepadsusp)
    #r5001_rrecrepad_custom#
    #r5001_rrecrepad_custom#
    class Meta:
        db_table = r'r5001_rrecrepad'
        managed = True
        ordering = ['r5001_infototal', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad', 'vlrcrrecrepadsusp']


class r5001RTom(models.Model):
    r5001_infototal = models.OneToOneField('r5001infoTotal',
        related_name='%(class)s_r5001_infototal')
    def evento(self): return self.r5001_infototal.evento()
    cnpjprestador = models.CharField(max_length=14)
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_infototal) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbaseret)
    #r5001_rtom_custom#
    #r5001_rtom_custom#
    class Meta:
        db_table = r'r5001_rtom'
        managed = True
        ordering = ['r5001_infototal', 'cnpjprestador', 'vlrtotalbaseret']


class r5001infoCRTom(models.Model):
    r5001_rtom = models.ForeignKey('r5001RTom',
        related_name='%(class)s_r5001_rtom')
    def evento(self): return self.r5001_rtom.evento()
    crtom = models.IntegerField()
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_rtom) + ' - ' + unicode(self.crtom) + ' - ' + unicode(self.vlrcrtom) + ' - ' + unicode(self.vlrcrtomsusp)
    #r5001_infocrtom_custom#
    #r5001_infocrtom_custom#
    class Meta:
        db_table = r'r5001_infocrtom'
        managed = True
        ordering = ['r5001_rtom', 'crtom', 'vlrcrtom', 'vlrcrtomsusp']


class r5001infoTotal(models.Model):
    r5001_evttotal = models.OneToOneField('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal')
    def evento(self): return self.r5001_evttotal.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_evttotal) + ' - ' + unicode(self.nrrecarqbase)
    #r5001_infototal_custom#
    #r5001_infototal_custom#
    class Meta:
        db_table = r'r5001_infototal'
        managed = True
        ordering = ['r5001_evttotal', 'nrrecarqbase']


class r5001regOcorrs(models.Model):
    r5001_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_r5001_evttotal')
    def evento(self): return self.r5001_evttotal.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5001_TPOCORR)
    localerroaviso = models.CharField(max_length=100)
    codresp = models.CharField(max_length=6)
    dscresp = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5001_evttotal) + ' - ' + unicode(self.tpocorr) + ' - ' + unicode(self.localerroaviso) + ' - ' + unicode(self.codresp) + ' - ' + unicode(self.dscresp)
    #r5001_regocorrs_custom#
    #r5001_regocorrs_custom#
    class Meta:
        db_table = r'r5001_regocorrs'
        managed = True
        ordering = ['r5001_evttotal', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp']


#VIEWS_MODELS
