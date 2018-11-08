#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S2245_MODTREICAP = (
    (1, u'1 - Presencial'),
    (2, u'2 - Educação a Distância (EaD)'),
    (3, u'3 - Semipresencial'),
)

CHOICES_S2245_TPPROF = (
    (1, u'1 - Profissional empregado do declarante'),
    (2, u'2 - Profissional sem vínculo de emprego/estatutário com o declarante'),
)

CHOICES_S2245_TPTREICAP = (
    (1, u'1 - Inicial'),
    (2, u'2 - Periódico'),
    (3, u'3 - Reciclagem'),
    (4, u'4 - Eventual'),
    (5, u'5 - Outros'),
)

class s2245ideProfResp(models.Model):
    s2245_infocomplem = models.ForeignKey('s2245infoComplem',
        related_name='%(class)s_s2245_infocomplem')
    def evento(self): return self.s2245_infocomplem.evento()
    cpfprof = models.CharField(max_length=11)
    nmprof = models.CharField(max_length=70)
    tpprof = models.IntegerField(choices=CHOICES_S2245_TPPROF)
    formprof = models.CharField(max_length=255)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2245_infocomplem) + ' - ' + unicode(self.cpfprof) + ' - ' + unicode(self.nmprof) + ' - ' + unicode(self.tpprof) + ' - ' + unicode(self.formprof) + ' - ' + unicode(self.codcbo)
    #s2245_ideprofresp_custom#
    #s2245_ideprofresp_custom#
    class Meta:
        db_table = r's2245_ideprofresp'
        managed = True
        ordering = ['s2245_infocomplem', 'cpfprof', 'nmprof', 'tpprof', 'formprof', 'codcbo']



class s2245ideProfRespSerializer(ModelSerializer):
    class Meta:
        model = s2245ideProfResp
        fields = '__all__'
            

class s2245infoComplem(models.Model):
    s2245_evttreicap = models.OneToOneField('esocial.s2245evtTreiCap',
        related_name='%(class)s_s2245_evttreicap')
    def evento(self): return self.s2245_evttreicap.evento()
    dttreicap = models.DateField()
    durtreicap = models.DecimalField(max_digits=15, decimal_places=2, max_length=6)
    modtreicap = models.IntegerField(choices=CHOICES_S2245_MODTREICAP)
    tptreicap = models.IntegerField(choices=CHOICES_S2245_TPTREICAP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2245_evttreicap) + ' - ' + unicode(self.dttreicap) + ' - ' + unicode(self.durtreicap) + ' - ' + unicode(self.modtreicap) + ' - ' + unicode(self.tptreicap)
    #s2245_infocomplem_custom#
    #s2245_infocomplem_custom#
    class Meta:
        db_table = r's2245_infocomplem'
        managed = True
        ordering = ['s2245_evttreicap', 'dttreicap', 'durtreicap', 'modtreicap', 'tptreicap']



class s2245infoComplemSerializer(ModelSerializer):
    class Meta:
        model = s2245infoComplem
        fields = '__all__'
            

#VIEWS_MODELS
