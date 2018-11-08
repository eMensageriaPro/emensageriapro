#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S2410_INTAPOSENTADO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2410_TPPENMORTE = (
    (1, u'1 - Vitalícia'),
    (2, u'2 - Temporária'),
)

class s2410homologTC(models.Model):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    dthomol = models.DateField()
    nratolegal = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.dthomol) + ' - ' + unicode(self.nratolegal)
    #s2410_homologtc_custom#
    #s2410_homologtc_custom#
    class Meta:
        db_table = r's2410_homologtc'
        managed = True
        ordering = ['s2410_evtcdbenin', 'dthomol', 'nratolegal']



class s2410homologTCSerializer(ModelSerializer):
    class Meta:
        model = s2410homologTC
        fields = '__all__'
            

class s2410infoPenMorte(models.Model):
    s2410_evtcdbenin = models.OneToOneField('esocial.s2410evtCdBenIn',
        related_name='%(class)s_s2410_evtcdbenin')
    def evento(self): return self.s2410_evtcdbenin.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2410_TPPENMORTE)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2410_evtcdbenin) + ' - ' + unicode(self.tppenmorte)
    #s2410_infopenmorte_custom#
    #s2410_infopenmorte_custom#
    class Meta:
        db_table = r's2410_infopenmorte'
        managed = True
        ordering = ['s2410_evtcdbenin', 'tppenmorte']



class s2410infoPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410infoPenMorte
        fields = '__all__'
            

class s2410instPenMorte(models.Model):
    s2410_infopenmorte = models.OneToOneField('s2410infoPenMorte',
        related_name='%(class)s_s2410_infopenmorte')
    def evento(self): return self.s2410_infopenmorte.evento()
    cpfinst = models.CharField(max_length=11)
    dtinst = models.DateField()
    intaposentado = models.CharField(choices=CHOICES_S2410_INTAPOSENTADO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2410_infopenmorte) + ' - ' + unicode(self.cpfinst) + ' - ' + unicode(self.dtinst) + ' - ' + unicode(self.intaposentado)
    #s2410_instpenmorte_custom#
    #s2410_instpenmorte_custom#
    class Meta:
        db_table = r's2410_instpenmorte'
        managed = True
        ordering = ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado']



class s2410instPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2410instPenMorte
        fields = '__all__'
            

#VIEWS_MODELS
