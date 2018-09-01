#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S1300_TPCONTRIBSIND = (
    (1, u'1 - Contribuição Sindical Compulsória'),
    (2, u'2 - Contribuição Associativa'),
    (3, u'3 - Contribuição Assistencial'),
    (4, u'4 - Contribuição Confederativa'),
)

class s1300contribSind(models.Model):
    s1300_evtcontrsindpatr = models.ForeignKey('esocial.s1300evtContrSindPatr',
        related_name='%(class)s_s1300_evtcontrsindpatr')
    def evento(self): return self.s1300_evtcontrsindpatr.evento()
    cnpjsindic = models.CharField(max_length=14)
    tpcontribsind = models.IntegerField(choices=CHOICES_S1300_TPCONTRIBSIND)
    vlrcontribsind = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1300_evtcontrsindpatr) + ' - ' + unicode(self.cnpjsindic) + ' - ' + unicode(self.tpcontribsind) + ' - ' + unicode(self.vlrcontribsind)
    #s1300_contribsind_custom#
    #s1300_contribsind_custom#
    class Meta:
        db_table = r's1300_contribsind'
        managed = True
        ordering = ['s1300_evtcontrsindpatr', 'cnpjsindic', 'tpcontribsind', 'vlrcontribsind']


#VIEWS_MODELS
