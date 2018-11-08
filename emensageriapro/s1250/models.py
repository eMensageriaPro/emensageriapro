#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S1250_INDAQUIS = (
    (1, u'1 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral'),
    (2, u'2 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA'),
    (3, u'3 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA. Evento de origem (S- 1250)'),
    (4, u'4 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral - Produção Isenta (Lei 13.606/2018)'),
    (5, u'5 - Aquisição da produção de produtor rural pessoa física ou segurado especial em geral por Entidade do PAA - Produção Isenta (Lei 13.606/2018)'),
    (6, u'6 - Aquisição da produção de produtor rural pessoa jurídica por Entidade do PAA - Produção Isenta (Lei 13.606/2018)'),
)

CHOICES_S1250_TPINSCPROD = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

class s1250ideProdutor(models.Model):
    s1250_tpaquis = models.ForeignKey('s1250tpAquis',
        related_name='%(class)s_s1250_tpaquis')
    def evento(self): return self.s1250_tpaquis.evento()
    tpinscprod = models.IntegerField(choices=CHOICES_S1250_TPINSCPROD)
    nrinscprod = models.CharField(max_length=14)
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1250_tpaquis) + ' - ' + unicode(self.tpinscprod) + ' - ' + unicode(self.nrinscprod) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrsenardesc)
    #s1250_ideprodutor_custom#
    #s1250_ideprodutor_custom#
    class Meta:
        db_table = r's1250_ideprodutor'
        managed = True
        ordering = ['s1250_tpaquis', 'tpinscprod', 'nrinscprod', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc']



class s1250ideProdutorSerializer(ModelSerializer):
    class Meta:
        model = s1250ideProdutor
        fields = '__all__'
            

class s1250infoProcJud(models.Model):
    s1250_ideprodutor = models.ForeignKey('s1250ideProdutor',
        related_name='%(class)s_s1250_ideprodutor')
    def evento(self): return self.s1250_ideprodutor.evento()
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField()
    vrcpnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenarnret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1250_ideprodutor) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.vrcpnret) + ' - ' + unicode(self.vrratnret) + ' - ' + unicode(self.vrsenarnret)
    #s1250_infoprocjud_custom#
    #s1250_infoprocjud_custom#
    class Meta:
        db_table = r's1250_infoprocjud'
        managed = True
        ordering = ['s1250_ideprodutor', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret']



class s1250infoProcJudSerializer(ModelSerializer):
    class Meta:
        model = s1250infoProcJud
        fields = '__all__'
            

class s1250nfs(models.Model):
    s1250_ideprodutor = models.ForeignKey('s1250ideProdutor',
        related_name='%(class)s_s1250_ideprodutor')
    def evento(self): return self.s1250_ideprodutor.evento()
    serie = models.CharField(max_length=5, blank=True, null=True)
    nrdocto = models.CharField(max_length=20)
    dtemisnf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrcpdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrratdescpr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vrsenardesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1250_ideprodutor) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.nrdocto) + ' - ' + unicode(self.dtemisnf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.vrcpdescpr) + ' - ' + unicode(self.vrratdescpr) + ' - ' + unicode(self.vrsenardesc)
    #s1250_nfs_custom#
    #s1250_nfs_custom#
    class Meta:
        db_table = r's1250_nfs'
        managed = True
        ordering = ['s1250_ideprodutor', 'serie', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc']



class s1250nfsSerializer(ModelSerializer):
    class Meta:
        model = s1250nfs
        fields = '__all__'
            

class s1250tpAquis(models.Model):
    s1250_evtaqprod = models.ForeignKey('esocial.s1250evtAqProd',
        related_name='%(class)s_s1250_evtaqprod')
    def evento(self): return self.s1250_evtaqprod.evento()
    indaquis = models.IntegerField(choices=CHOICES_S1250_INDAQUIS)
    vlrtotaquis = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1250_evtaqprod) + ' - ' + unicode(self.indaquis) + ' - ' + unicode(self.vlrtotaquis)
    #s1250_tpaquis_custom#
    #s1250_tpaquis_custom#
    class Meta:
        db_table = r's1250_tpaquis'
        managed = True
        ordering = ['s1250_evtaqprod', 'indaquis', 'vlrtotaquis']



class s1250tpAquisSerializer(ModelSerializer):
    class Meta:
        model = s1250tpAquis
        fields = '__all__'
            

#VIEWS_MODELS
