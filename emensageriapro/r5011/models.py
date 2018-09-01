#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_R5011_INDEXISTINFO = (
    (1, u'1 - Há informações de bases e/ou de tributos'),
    (2, u'2 - Há movimento, porém não há informações de bases ou de tributos'),
    (3, u'3 - Não há movimento na competência'),
)

CHOICES_R5011_TPINSCTOMADOR = (
    (1, u'1 - CNPJ'),
    (4, u'4 - CNO'),
)

CHOICES_R5011_TPOCORR = (
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
)

class r5011RCPRB(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
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
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcprb) + ' - ' + unicode(self.vlrcrcprb) + ' - ' + unicode(self.vlrcrcprbsusp)
    #r5011_rcprb_custom#
    #r5011_rcprb_custom#
    class Meta:
        db_table = r'r5011_rcprb'
        managed = True
        ordering = ['r5011_infototalcontrib', 'crcprb', 'vlrcrcprb', 'vlrcrcprbsusp']


class r5011RComl(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
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
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.crcoml) + ' - ' + unicode(self.vlrcrcoml) + ' - ' + unicode(self.vlrcrcomlsusp)
    #r5011_rcoml_custom#
    #r5011_rcoml_custom#
    class Meta:
        db_table = r'r5011_rcoml'
        managed = True
        ordering = ['r5011_infototalcontrib', 'crcoml', 'vlrcrcoml', 'vlrcrcomlsusp']


class r5011RPrest(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
    tpinsctomador = models.IntegerField(choices=CHOICES_R5011_TPINSCTOMADOR)
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
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.tpinsctomador) + ' - ' + unicode(self.nrinsctomador) + ' - ' + unicode(self.vlrtotalbaseret) + ' - ' + unicode(self.vlrtotalretprinc) + ' - ' + unicode(self.vlrtotalretadic) + ' - ' + unicode(self.vlrtotalnretprinc) + ' - ' + unicode(self.vlrtotalnretadic)
    #r5011_rprest_custom#
    #r5011_rprest_custom#
    class Meta:
        db_table = r'r5011_rprest'
        managed = True
        ordering = ['r5011_infototalcontrib', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc', 'vlrtotalretadic', 'vlrtotalnretprinc', 'vlrtotalnretadic']


class r5011RRecRepAD(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
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
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjassocdesp) + ' - ' + unicode(self.vlrtotalrep) + ' - ' + unicode(self.crrecrepad) + ' - ' + unicode(self.vlrcrrecrepad) + ' - ' + unicode(self.vlrcrrecrepadsusp)
    #r5011_rrecrepad_custom#
    #r5011_rrecrepad_custom#
    class Meta:
        db_table = r'r5011_rrecrepad'
        managed = True
        ordering = ['r5011_infototalcontrib', 'cnpjassocdesp', 'vlrtotalrep', 'crrecrepad', 'vlrcrrecrepad', 'vlrcrrecrepadsusp']


class r5011RTom(models.Model):
    r5011_infototalcontrib = models.ForeignKey('r5011infoTotalContrib',
        related_name='%(class)s_r5011_infototalcontrib')
    def evento(self): return self.r5011_infototalcontrib.evento()
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
        return unicode(self.r5011_infototalcontrib) + ' - ' + unicode(self.cnpjprestador) + ' - ' + unicode(self.vlrtotalbaseret)
    #r5011_rtom_custom#
    #r5011_rtom_custom#
    class Meta:
        db_table = r'r5011_rtom'
        managed = True
        ordering = ['r5011_infototalcontrib', 'cnpjprestador', 'vlrtotalbaseret']


class r5011infoCRTom(models.Model):
    r5011_rtom = models.ForeignKey('r5011RTom',
        related_name='%(class)s_r5011_rtom')
    def evento(self): return self.r5011_rtom.evento()
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
        return unicode(self.r5011_rtom) + ' - ' + unicode(self.crtom) + ' - ' + unicode(self.vlrcrtom) + ' - ' + unicode(self.vlrcrtomsusp)
    #r5011_infocrtom_custom#
    #r5011_infocrtom_custom#
    class Meta:
        db_table = r'r5011_infocrtom'
        managed = True
        ordering = ['r5011_rtom', 'crtom', 'vlrcrtom', 'vlrcrtomsusp']


class r5011infoTotalContrib(models.Model):
    r5011_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib')
    def evento(self): return self.r5011_evttotalcontrib.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True)
    indexistinfo = models.IntegerField(choices=CHOICES_R5011_INDEXISTINFO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.nrrecarqbase) + ' - ' + unicode(self.indexistinfo)
    #r5011_infototalcontrib_custom#
    #r5011_infototalcontrib_custom#
    class Meta:
        db_table = r'r5011_infototalcontrib'
        managed = True
        ordering = ['r5011_evttotalcontrib', 'nrrecarqbase', 'indexistinfo']


class r5011regOcorrs(models.Model):
    r5011_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_r5011_evttotalcontrib')
    def evento(self): return self.r5011_evttotalcontrib.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R5011_TPOCORR)
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
        return unicode(self.r5011_evttotalcontrib) + ' - ' + unicode(self.tpocorr) + ' - ' + unicode(self.localerroaviso) + ' - ' + unicode(self.codresp) + ' - ' + unicode(self.dscresp)
    #r5011_regocorrs_custom#
    #r5011_regocorrs_custom#
    class Meta:
        db_table = r'r5011_regocorrs'
        managed = True
        ordering = ['r5011_evttotalcontrib', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp']


#VIEWS_MODELS
