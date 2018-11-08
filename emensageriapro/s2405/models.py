#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



ESTADOS = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),
)

CHOICES_S2405_DEPFINSPREV = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_INCFISMEN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2405_SEXODEP = (
    ('F', u'F - Feminino'),
    ('M', u'M - Masculino'),
)

class s2405brasil(models.Model):
    s2405_endereco = models.OneToOneField('s2405endereco',
        related_name='%(class)s_s2405_endereco')
    def evento(self): return self.s2405_endereco.evento()
    tplograd = models.TextField(max_length=4)
    dsclograd = models.CharField(max_length=80)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2405_endereco) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2405_brasil_custom#
    #s2405_brasil_custom#
    class Meta:
        db_table = r's2405_brasil'
        managed = True
        ordering = ['s2405_endereco', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']



class s2405brasilSerializer(ModelSerializer):
    class Meta:
        model = s2405brasil
        fields = '__all__'
            

class s2405dependente(models.Model):
    s2405_evtcdbenefalt = models.ForeignKey('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt')
    def evento(self): return self.s2405_evtcdbenefalt.evento()
    tpdep = models.CharField(max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    sexodep = models.CharField(choices=CHOICES_S2405_SEXODEP, max_length=1)
    depirrf = models.CharField(choices=CHOICES_S2405_DEPIRRF, max_length=1)
    incfismen = models.CharField(choices=CHOICES_S2405_INCFISMEN, max_length=1)
    depfinsprev = models.CharField(choices=CHOICES_S2405_DEPFINSPREV, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.sexodep) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.incfismen) + ' - ' + unicode(self.depfinsprev)
    #s2405_dependente_custom#
    #s2405_dependente_custom#
    class Meta:
        db_table = r's2405_dependente'
        managed = True
        ordering = ['s2405_evtcdbenefalt', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'sexodep', 'depirrf', 'incfismen', 'depfinsprev']



class s2405dependenteSerializer(ModelSerializer):
    class Meta:
        model = s2405dependente
        fields = '__all__'
            

class s2405endereco(models.Model):
    s2405_evtcdbenefalt = models.OneToOneField('esocial.s2405evtCdBenefAlt',
        related_name='%(class)s_s2405_evtcdbenefalt')
    def evento(self): return self.s2405_evtcdbenefalt.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2405_evtcdbenefalt)
    #s2405_endereco_custom#
    #s2405_endereco_custom#
    class Meta:
        db_table = r's2405_endereco'
        managed = True
        ordering = ['s2405_evtcdbenefalt']



class s2405enderecoSerializer(ModelSerializer):
    class Meta:
        model = s2405endereco
        fields = '__all__'
            

class s2405exterior(models.Model):
    s2405_endereco = models.OneToOneField('s2405endereco',
        related_name='%(class)s_s2405_endereco')
    def evento(self): return self.s2405_endereco.evento()
    paisresid = models.TextField(max_length=3)
    dsclograd = models.CharField(max_length=80)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2405_endereco) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s2405_exterior_custom#
    #s2405_exterior_custom#
    class Meta:
        db_table = r's2405_exterior'
        managed = True
        ordering = ['s2405_endereco', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal']



class s2405exteriorSerializer(ModelSerializer):
    class Meta:
        model = s2405exterior
        fields = '__all__'
            

#VIEWS_MODELS
