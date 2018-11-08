#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S1270_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class s1270remunAvNP(models.Model):
    s1270_evtcontratavnp = models.ForeignKey('esocial.s1270evtContratAvNP',
        related_name='%(class)s_s1270_evtcontratavnp')
    def evento(self): return self.s1270_evtcontratavnp.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S1270_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    vrbccp00 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbccp13 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrbcfgts = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrdesccp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1270_evtcontratavnp) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao) + ' - ' + unicode(self.vrbccp00) + ' - ' + unicode(self.vrbccp15) + ' - ' + unicode(self.vrbccp20) + ' - ' + unicode(self.vrbccp25) + ' - ' + unicode(self.vrbccp13) + ' - ' + unicode(self.vrbcfgts) + ' - ' + unicode(self.vrdesccp)
    #s1270_remunavnp_custom#
    #s1270_remunavnp_custom#
    class Meta:
        db_table = r's1270_remunavnp'
        managed = True
        ordering = ['s1270_evtcontratavnp', 'tpinsc', 'nrinsc', 'codlotacao', 'vrbccp00', 'vrbccp15', 'vrbccp20', 'vrbccp25', 'vrbccp13', 'vrbcfgts', 'vrdesccp']



class s1270remunAvNPSerializer(ModelSerializer):
    class Meta:
        model = s1270remunAvNP
        fields = '__all__'
            

#VIEWS_MODELS
