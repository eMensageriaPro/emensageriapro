#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S2416_MTVSUSPENSAO = (
    ('01', u'01 - Suspensão por não recadastramento'),
    ('99', u'99 - Outros motivos de suspensão'),
)

CHOICES_S2416_TPPENMORTE = (
    (1, u'1 - Vitalícia'),
    (2, u'2 - Temporária'),
)

class s2416homologTC(models.Model):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    nratolegal = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.nratolegal)
    #s2416_homologtc_custom#
    #s2416_homologtc_custom#
    class Meta:
        db_table = r's2416_homologtc'
        managed = True
        ordering = ['s2416_evtcdbenalt', 'nratolegal']



class s2416homologTCSerializer(ModelSerializer):
    class Meta:
        model = s2416homologTC
        fields = '__all__'
            

class s2416infoPenMorte(models.Model):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    tppenmorte = models.IntegerField(choices=CHOICES_S2416_TPPENMORTE)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.tppenmorte)
    #s2416_infopenmorte_custom#
    #s2416_infopenmorte_custom#
    class Meta:
        db_table = r's2416_infopenmorte'
        managed = True
        ordering = ['s2416_evtcdbenalt', 'tppenmorte']



class s2416infoPenMorteSerializer(ModelSerializer):
    class Meta:
        model = s2416infoPenMorte
        fields = '__all__'
            

class s2416suspensao(models.Model):
    s2416_evtcdbenalt = models.OneToOneField('esocial.s2416evtCdBenAlt',
        related_name='%(class)s_s2416_evtcdbenalt')
    def evento(self): return self.s2416_evtcdbenalt.evento()
    mtvsuspensao = models.CharField(choices=CHOICES_S2416_MTVSUSPENSAO, max_length=2)
    dscsuspensao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2416_evtcdbenalt) + ' - ' + unicode(self.mtvsuspensao) + ' - ' + unicode(self.dscsuspensao)
    #s2416_suspensao_custom#
    #s2416_suspensao_custom#
    class Meta:
        db_table = r's2416_suspensao'
        managed = True
        ordering = ['s2416_evtcdbenalt', 'mtvsuspensao', 'dscsuspensao']



class s2416suspensaoSerializer(ModelSerializer):
    class Meta:
        model = s2416suspensao
        fields = '__all__'
            

#VIEWS_MODELS
