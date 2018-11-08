#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S2250_MTVCANCAVPREVIO = (
    (1, u'1 - Reconsideração prevista no artigo 489 da CLT'),
    (2, u'2 - Determinação Judicial'),
    (3, u'3 - Cumprimento de norma legal'),
    (9, u'9 - Outros'),
)

CHOICES_S2250_TPAVPREVIO = (
    (1, u'1 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de duas horas diárias [caput do art. 488 da CLT]'),
    (2, u'2 - Aviso prévio trabalhado dado pelo empregador ao empregado, que optou pela redução de dias corridos [parágrafo único do art. 488 da CLT]'),
    (4, u'4 - Aviso prévio dado pelo empregado (pedido de demissão), não dispensado de seu cumprimento, sob pena de desconto, pelo empregador, dos salários correspondentes ao prazo respectivo (§2º do art. 487 da CLT)'),
    (5, u'5 - Aviso prévio trabalhado dado pelo empregador rural ao empregado, com redução de um dia por semana ( art. 15 da Lei nº 5889/73)'),
)

class s2250cancAvPrevio(models.Model):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    def evento(self): return self.s2250_evtavprevio.evento()
    dtcancavprv = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    mtvcancavprevio = models.IntegerField(choices=CHOICES_S2250_MTVCANCAVPREVIO)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtcancavprv) + ' - ' + unicode(self.observacao) + ' - ' + unicode(self.mtvcancavprevio)
    #s2250_cancavprevio_custom#
    #s2250_cancavprevio_custom#
    class Meta:
        db_table = r's2250_cancavprevio'
        managed = True
        ordering = ['s2250_evtavprevio', 'dtcancavprv', 'observacao', 'mtvcancavprevio']



class s2250cancAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250cancAvPrevio
        fields = '__all__'
            

class s2250detAvPrevio(models.Model):
    s2250_evtavprevio = models.OneToOneField('esocial.s2250evtAvPrevio',
        related_name='%(class)s_s2250_evtavprevio')
    def evento(self): return self.s2250_evtavprevio.evento()
    dtavprv = models.DateField()
    dtprevdeslig = models.DateField()
    tpavprevio = models.IntegerField(choices=CHOICES_S2250_TPAVPREVIO)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2250_evtavprevio) + ' - ' + unicode(self.dtavprv) + ' - ' + unicode(self.dtprevdeslig) + ' - ' + unicode(self.tpavprevio) + ' - ' + unicode(self.observacao)
    #s2250_detavprevio_custom#
    #s2250_detavprevio_custom#
    class Meta:
        db_table = r's2250_detavprevio'
        managed = True
        ordering = ['s2250_evtavprevio', 'dtavprv', 'dtprevdeslig', 'tpavprevio', 'observacao']



class s2250detAvPrevioSerializer(ModelSerializer):
    class Meta:
        model = s2250detAvPrevio
        fields = '__all__'
            

#VIEWS_MODELS
