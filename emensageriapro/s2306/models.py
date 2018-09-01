#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
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

CHOICES_S2306_NATESTAGIO = (
    ('N', u'N - Não Obrigatório'),
    ('O', u'O - Obrigatório'),
)

CHOICES_S2306_NIVESTAGIO = (
    (1, u'1 - Fundamental'),
    (2, u'2 - Médio'),
    (3, u'3 - Formação Profissional'),
    (4, u'4 - Superior'),
    (8, u'8 - Especial'),
    (9, u'9 - Mãe social (Lei 7644, de 1987)'),
)

CHOICES_S2306_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

class s2306ageIntegracao(models.Model):
    s2306_infoestagiario = models.OneToOneField('s2306infoEstagiario',
        related_name='%(class)s_s2306_infoestagiario')
    def evento(self): return self.s2306_infoestagiario.evento()
    cnpjagntinteg = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_infoestagiario) + ' - ' + unicode(self.cnpjagntinteg) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2306_ageintegracao_custom#
    #s2306_ageintegracao_custom#
    class Meta:
        db_table = r's2306_ageintegracao'
        managed = True
        ordering = ['s2306_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'bairro', 'cep', 'codmunic', 'uf']


class s2306cargoFuncao(models.Model):
    s2306_infocomplementares = models.OneToOneField('s2306infoComplementares',
        related_name='%(class)s_s2306_infocomplementares')
    def evento(self): return self.s2306_infocomplementares.evento()
    codcargo = models.CharField(max_length=30)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_infocomplementares) + ' - ' + unicode(self.codcargo) + ' - ' + unicode(self.codfuncao)
    #s2306_cargofuncao_custom#
    #s2306_cargofuncao_custom#
    class Meta:
        db_table = r's2306_cargofuncao'
        managed = True
        ordering = ['s2306_infocomplementares', 'codcargo', 'codfuncao']


class s2306infoComplementares(models.Model):
    s2306_evttsvaltcontr = models.OneToOneField('esocial.s2306evtTSVAltContr',
        related_name='%(class)s_s2306_evttsvaltcontr')
    def evento(self): return self.s2306_evttsvaltcontr.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_evttsvaltcontr)
    #s2306_infocomplementares_custom#
    #s2306_infocomplementares_custom#
    class Meta:
        db_table = r's2306_infocomplementares'
        managed = True
        ordering = ['s2306_evttsvaltcontr']


class s2306infoEstagiario(models.Model):
    s2306_infocomplementares = models.OneToOneField('s2306infoComplementares',
        related_name='%(class)s_s2306_infocomplementares')
    def evento(self): return self.s2306_infocomplementares.evento()
    natestagio = models.CharField(choices=CHOICES_S2306_NATESTAGIO, max_length=1)
    nivestagio = models.IntegerField(choices=CHOICES_S2306_NIVESTAGIO)
    areaatuacao = models.CharField(max_length=50, blank=True, null=True)
    nrapol = models.CharField(max_length=30, blank=True, null=True)
    vlrbolsa = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    dtprevterm = models.DateField()
    cnpjinstensino = models.CharField(max_length=14, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    dsclograd = models.CharField(max_length=100, blank=True, null=True)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    uf = models.CharField(choices=ESTADOS, max_length=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_infocomplementares) + ' - ' + unicode(self.natestagio) + ' - ' + unicode(self.nivestagio) + ' - ' + unicode(self.areaatuacao) + ' - ' + unicode(self.nrapol) + ' - ' + unicode(self.vlrbolsa) + ' - ' + unicode(self.dtprevterm) + ' - ' + unicode(self.cnpjinstensino) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2306_infoestagiario_custom#
    #s2306_infoestagiario_custom#
    class Meta:
        db_table = r's2306_infoestagiario'
        managed = True
        ordering = ['s2306_infocomplementares', 'natestagio', 'nivestagio', 'areaatuacao', 'nrapol', 'vlrbolsa', 'dtprevterm', 'cnpjinstensino', 'nmrazao', 'dsclograd', 'nrlograd', 'bairro', 'cep', 'codmunic', 'uf']


class s2306remuneracao(models.Model):
    s2306_infocomplementares = models.OneToOneField('s2306infoComplementares',
        related_name='%(class)s_s2306_infocomplementares')
    def evento(self): return self.s2306_infocomplementares.evento()
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    undsalfixo = models.IntegerField(choices=CHOICES_S2306_UNDSALFIXO)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_infocomplementares) + ' - ' + unicode(self.vrsalfx) + ' - ' + unicode(self.undsalfixo) + ' - ' + unicode(self.dscsalvar)
    #s2306_remuneracao_custom#
    #s2306_remuneracao_custom#
    class Meta:
        db_table = r's2306_remuneracao'
        managed = True
        ordering = ['s2306_infocomplementares', 'vrsalfx', 'undsalfixo', 'dscsalvar']


class s2306supervisorEstagio(models.Model):
    s2306_infoestagiario = models.OneToOneField('s2306infoEstagiario',
        related_name='%(class)s_s2306_infoestagiario')
    def evento(self): return self.s2306_infoestagiario.evento()
    cpfsupervisor = models.CharField(max_length=11)
    nmsuperv = models.CharField(max_length=70)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2306_infoestagiario) + ' - ' + unicode(self.cpfsupervisor) + ' - ' + unicode(self.nmsuperv)
    #s2306_supervisorestagio_custom#
    #s2306_supervisorestagio_custom#
    class Meta:
        db_table = r's2306_supervisorestagio'
        managed = True
        ordering = ['s2306_infoestagiario', 'cpfsupervisor', 'nmsuperv']


#VIEWS_MODELS
