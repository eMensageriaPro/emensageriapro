#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S1280_INDSUBSTPATR = (
    (1, u'1 - Integralmente substituída'),
    (2, u'2 - Parcialmente substituída'),
)

class s1280infoAtivConcom(models.Model):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    fatormes = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    fator13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.fatormes) + ' - ' + unicode(self.fator13)
    #s1280_infoativconcom_custom#
    #s1280_infoativconcom_custom#
    class Meta:
        db_table = r's1280_infoativconcom'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'fatormes', 'fator13']


class s1280infoSubstPatr(models.Model):
    s1280_evtinfocomplper = models.OneToOneField('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    indsubstpatr = models.IntegerField(choices=CHOICES_S1280_INDSUBSTPATR)
    percredcontrib = models.DecimalField(max_digits=15, decimal_places=2, max_length=5)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.indsubstpatr) + ' - ' + unicode(self.percredcontrib)
    #s1280_infosubstpatr_custom#
    #s1280_infosubstpatr_custom#
    class Meta:
        db_table = r's1280_infosubstpatr'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'indsubstpatr', 'percredcontrib']


class s1280infoSubstPatrOpPort(models.Model):
    s1280_evtinfocomplper = models.ForeignKey('esocial.s1280evtInfoComplPer',
        related_name='%(class)s_s1280_evtinfocomplper')
    def evento(self): return self.s1280_evtinfocomplper.evento()
    cnpjopportuario = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1280_evtinfocomplper) + ' - ' + unicode(self.cnpjopportuario)
    #s1280_infosubstpatropport_custom#
    #s1280_infosubstpatropport_custom#
    class Meta:
        db_table = r's1280_infosubstpatropport'
        managed = True
        ordering = ['s1280_evtinfocomplper', 'cnpjopportuario']


#VIEWS_MODELS
