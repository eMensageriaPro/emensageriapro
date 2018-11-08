#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



class s1299ideRespInf(models.Model):
    s1299_evtfechaevper = models.OneToOneField('esocial.s1299evtFechaEvPer',
        related_name='%(class)s_s1299_evtfechaevper')
    def evento(self): return self.s1299_evtfechaevper.evento()
    nmresp = models.CharField(max_length=70)
    cpfresp = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1299_evtfechaevper) + ' - ' + unicode(self.nmresp) + ' - ' + unicode(self.cpfresp) + ' - ' + unicode(self.telefone) + ' - ' + unicode(self.email)
    #s1299_iderespinf_custom#
    #s1299_iderespinf_custom#
    class Meta:
        db_table = r's1299_iderespinf'
        managed = True
        ordering = ['s1299_evtfechaevper', 'nmresp', 'cpfresp', 'telefone', 'email']



class s1299ideRespInfSerializer(ModelSerializer):
    class Meta:
        model = s1299ideRespInf
        fields = '__all__'
            

#VIEWS_MODELS
