#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_R2050_INDCOM = (
    (1, u'1 - Comercialização da Produção por Prod. Rural PJ/Agroindústria, exceto para entidades executoras do PAA'),
    (8, u'8 - Comercialização da Produção para Entidade do Programa de Aquisição de Alimentos - PAA'),
    (9, u'9 - Comercialização direta da Produção no Mercado Externo'),
)

CHOICES_R2050_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2050infoProc(models.Model):
    r2050_tipocom = models.ForeignKey('r2050tipoCom',
        related_name='%(class)s_r2050_tipocom')
    def evento(self): return self.r2050_tipocom.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2050_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrcpsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrratsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrsenarsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2050_tipocom) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vlrcpsusp) + ' - ' + unicode(self.vlrratsusp) + ' - ' + unicode(self.vlrsenarsusp)
    #r2050_infoproc_custom#
    #r2050_infoproc_custom#
    class Meta:
        db_table = r'r2050_infoproc'
        managed = True
        ordering = ['r2050_tipocom', 'tpproc', 'nrproc', 'codsusp', 'vlrcpsusp', 'vlrratsusp', 'vlrsenarsusp']



class r2050infoProcSerializer(ModelSerializer):
    class Meta:
        model = r2050infoProc
        fields = '__all__'
            

class r2050tipoCom(models.Model):
    r2050_evtcomprod = models.ForeignKey('efdreinf.r2050evtComProd',
        related_name='%(class)s_r2050_evtcomprod')
    def evento(self): return self.r2050_evtcomprod.evento()
    indcom = models.IntegerField(choices=CHOICES_R2050_INDCOM)
    vlrrecbruta = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2050_evtcomprod) + ' - ' + unicode(self.indcom) + ' - ' + unicode(self.vlrrecbruta)
    #r2050_tipocom_custom#
    #r2050_tipocom_custom#
    class Meta:
        db_table = r'r2050_tipocom'
        managed = True
        ordering = ['r2050_evtcomprod', 'indcom', 'vlrrecbruta']



class r2050tipoComSerializer(ModelSerializer):
    class Meta:
        model = r2050tipoCom
        fields = '__all__'
            

#VIEWS_MODELS
