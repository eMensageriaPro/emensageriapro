#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



class r2099ideRespInf(models.Model):
    r2099_evtfechaevper = models.OneToOneField('efdreinf.r2099evtFechaEvPer',
        related_name='%(class)s_r2099_evtfechaevper')
    def evento(self): return self.r2099_evtfechaevper.evento()
    nmresp = models.CharField(max_length=70)
    cpfresp = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2099_evtfechaevper) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.telefone) + ' - ' + unicode(self.email)
    #r2099_iderespinf_custom#
    #r2099_iderespinf_custom#
    class Meta:
        db_table = r'r2099_iderespinf'
        managed = True
        ordering = ['r2099_evtfechaevper', 'nmresp', 'cpfresp', 'telefone', 'email']


#VIEWS_MODELS
