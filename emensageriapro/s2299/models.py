#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S2299_INFOPERANT_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2299_INFOPERANT_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2299_INFOPERANT_TPACCONV = (
    ('A', u'A - Acordo Coletivo de Trabalho'),
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('C', u'C - Convenção Coletiva de Trabalho'),
    ('D', u'D - Sentença Normativa - Dissídio'),
    ('E', u'E - Conversão de Licença Saúde em Acidente de Trabalho'),
)

CHOICES_S2299_INFOPERANT_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOPERAPUR_GRAUEXP = (
    (1, u'1 - Não ensejador de aposentadoria especial'),
    (2, u'2 - Ensejador de Aposentadoria Especial - FAE15_12% (15 anos de contribuição e alíquota de 12%)'),
    (3, u'3 - Ensejador de Aposentadoria Especial - FAE20_09% (20 anos de contribuição e alíquota de 9%)'),
    (4, u'4 - Ensejador de Aposentadoria Especial - FAE25_06% (25 anos de contribuição e alíquota de 6%)'),
)

CHOICES_S2299_INFOPERAPUR_INDSIMPLES = (
    (1, u'1 - Contribuição Substituída Integralmente'),
    (2, u'2 - Contribuição não substituída'),
    (3, u'3 - Contribuição não substituída concomitante com contribuição substituída'),
)

CHOICES_S2299_INFOPERAPUR_TPDEP = (
    ('01', u'01 - Cônjuge'),
    ('02', u'02 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável'),
    ('03', u'03 - Filho(a) ou enteado(a)'),
    ('04', u'04 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau'),
    ('06', u'06 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'),
    ('07', u'07 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2° grau, do(a) qual detenha a guarda judicial'),
    ('09', u'09 - Pais, avós e bisavós'),
    ('10', u'10 - Menor pobre do qual detenha a guarda judicial'),
    ('11', u'11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'),
    ('12', u'12 - Ex-cônjuge'),
    ('99', u'99 - Agregado/Outros'),
)

CHOICES_S2299_INFOPERAPUR_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOTRABINTERM_INDMV = (
    (1, u'1 - O declarante aplica a alíquota de desconto do segurado sobre a remuneração por ele informada (o percentual da alíquota será obtido considerando a remuneração total do trabalhador)'),
    (2, u'2 - O declarante aplica a alíquota de desconto do segurado sobre a diferença entre o limite máximo do salário de contribuição e a remuneração de outra(s) empresa(s) para as quais o trabalhador informou que houve o desconto'),
    (3, u'3 - O declarante não realiza desconto do segurado, uma vez que houve desconto sobre o limite máximo de salário de contribuição em outra(s) empresa(s)'),
)

CHOICES_S2299_INFOTRABINTERM_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2299_INFOTRABINTERM_TPTRIB = (
    (2, u'2 - Contribuições sociais do trabalhador'),
    (3, u'3 - FGTS'),
    (3, u'3 - IRRF'),
    (4, u'4 - Contribuição sindical'),
)

class s2299dmDev(models.Model):
    s2299_verbasresc = models.ForeignKey('s2299verbasResc',
        related_name='%(class)s_s2299_verbasresc')
    def evento(self): return self.s2299_verbasresc.evento()
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_verbasresc) + ' - ' + unicode(self.idedmdev)
    #s2299_dmdev_custom#
    #s2299_dmdev_custom#
    class Meta:
        db_table = r's2299_dmdev'
        managed = True
        ordering = ['s2299_verbasresc', 'idedmdev']


class s2299infoPerAnt(models.Model):
    s2299_dmdev = models.OneToOneField('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_dmdev)
    #s2299_infoperant_custom#
    #s2299_infoperant_custom#
    class Meta:
        db_table = r's2299_infoperant'
        managed = True
        ordering = ['s2299_dmdev']


class s2299infoPerAntdetVerbas(models.Model):
    s2299_infoperant_ideestablot = models.ForeignKey('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperant_detverbas_custom#
    #s2299_infoperant_detverbas_custom#
    class Meta:
        db_table = r's2299_infoperant_detverbas'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']


class s2299infoPerAntideADC(models.Model):
    s2299_infoperant = models.ForeignKey('s2299infoPerAnt',
        related_name='%(class)s_s2299_infoperant')
    def evento(self): return self.s2299_infoperant.evento()
    dtacconv = models.DateField()
    tpacconv = models.CharField(choices=CHOICES_S2299_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField()
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant) + ' - ' + unicode(self.dtacconv) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.compacconv) + ' - ' + unicode(self.dtefacconv) + ' - ' + unicode(self.dsc)
    #s2299_infoperant_ideadc_custom#
    #s2299_infoperant_ideadc_custom#
    class Meta:
        db_table = r's2299_infoperant_ideadc'
        managed = True
        ordering = ['s2299_infoperant', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc']


class s2299infoPerAntideEstabLot(models.Model):
    s2299_infoperant_ideperiodo = models.ForeignKey('s2299infoPerAntidePeriodo',
        related_name='%(class)s_s2299_infoperant_ideperiodo')
    def evento(self): return self.s2299_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperant_ideestablot_custom#
    #s2299_infoperant_ideestablot_custom#
    class Meta:
        db_table = r's2299_infoperant_ideestablot'
        managed = True
        ordering = ['s2299_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao']


class s2299infoPerAntidePeriodo(models.Model):
    s2299_infoperant_ideadc = models.ForeignKey('s2299infoPerAntideADC',
        related_name='%(class)s_s2299_infoperant_ideadc')
    def evento(self): return self.s2299_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s2299_infoperant_ideperiodo_custom#
    #s2299_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's2299_infoperant_ideperiodo'
        managed = True
        ordering = ['s2299_infoperant_ideadc', 'perref']


class s2299infoPerAntinfoAgNocivo(models.Model):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperant_infoagnocivo_custom#
    #s2299_infoperant_infoagnocivo_custom#
    class Meta:
        db_table = r's2299_infoperant_infoagnocivo'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'grauexp']


class s2299infoPerAntinfoSimples(models.Model):
    s2299_infoperant_ideestablot = models.OneToOneField('s2299infoPerAntideEstabLot',
        related_name='%(class)s_s2299_infoperant_ideestablot')
    def evento(self): return self.s2299_infoperant_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERANT_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperant_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperant_infosimples_custom#
    #s2299_infoperant_infosimples_custom#
    class Meta:
        db_table = r's2299_infoperant_infosimples'
        managed = True
        ordering = ['s2299_infoperant_ideestablot', 'indsimples']


class s2299infoPerApur(models.Model):
    s2299_dmdev = models.OneToOneField('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_dmdev)
    #s2299_infoperapur_custom#
    #s2299_infoperapur_custom#
    class Meta:
        db_table = r's2299_infoperapur'
        managed = True
        ordering = ['s2299_dmdev']


class s2299infoPerApurdetOper(models.Model):
    s2299_infoperapur_infosaudecolet = models.ForeignKey('s2299infoPerApurinfoSaudeColet',
        related_name='%(class)s_s2299_infoperapur_infosaudecolet')
    def evento(self): return self.s2299_infoperapur_infosaudecolet.evento()
    cnpjoper = models.CharField(max_length=14)
    regans = models.CharField(max_length=6)
    vrpgtit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_infosaudecolet) + ' - ' + unicode(self.cnpjoper) + ' - ' + unicode(self.regans) + ' - ' + unicode(self.vrpgtit)
    #s2299_infoperapur_detoper_custom#
    #s2299_infoperapur_detoper_custom#
    class Meta:
        db_table = r's2299_infoperapur_detoper'
        managed = True
        ordering = ['s2299_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit']


class s2299infoPerApurdetPlano(models.Model):
    s2299_infoperapur_detoper = models.ForeignKey('s2299infoPerApurdetOper',
        related_name='%(class)s_s2299_infoperapur_detoper')
    def evento(self): return self.s2299_infoperapur_detoper.evento()
    tpdep = models.CharField(choices=CHOICES_S2299_INFOPERAPUR_TPDEP, max_length=2)
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    vlrpgdep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_detoper) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.vlrpgdep)
    #s2299_infoperapur_detplano_custom#
    #s2299_infoperapur_detplano_custom#
    class Meta:
        db_table = r's2299_infoperapur_detplano'
        managed = True
        ordering = ['s2299_infoperapur_detoper', 'tpdep', 'cpfdep', 'nmdep', 'dtnascto', 'vlrpgdep']


class s2299infoPerApurdetVerbas(models.Model):
    s2299_infoperapur_ideestablot = models.ForeignKey('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s2299_infoperapur_detverbas_custom#
    #s2299_infoperapur_detverbas_custom#
    class Meta:
        db_table = r's2299_infoperapur_detverbas'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']


class s2299infoPerApurideEstabLot(models.Model):
    s2299_infoperapur = models.ForeignKey('s2299infoPerApur',
        related_name='%(class)s_s2299_infoperapur')
    def evento(self): return self.s2299_infoperapur.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codlotacao = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codlotacao)
    #s2299_infoperapur_ideestablot_custom#
    #s2299_infoperapur_ideestablot_custom#
    class Meta:
        db_table = r's2299_infoperapur_ideestablot'
        managed = True
        ordering = ['s2299_infoperapur', 'tpinsc', 'nrinsc', 'codlotacao']


class s2299infoPerApurinfoAgNocivo(models.Model):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    grauexp = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_GRAUEXP)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.grauexp)
    #s2299_infoperapur_infoagnocivo_custom#
    #s2299_infoperapur_infoagnocivo_custom#
    class Meta:
        db_table = r's2299_infoperapur_infoagnocivo'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'grauexp']


class s2299infoPerApurinfoSaudeColet(models.Model):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot)
    #s2299_infoperapur_infosaudecolet_custom#
    #s2299_infoperapur_infosaudecolet_custom#
    class Meta:
        db_table = r's2299_infoperapur_infosaudecolet'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot']


class s2299infoPerApurinfoSimples(models.Model):
    s2299_infoperapur_ideestablot = models.OneToOneField('s2299infoPerApurideEstabLot',
        related_name='%(class)s_s2299_infoperapur_ideestablot')
    def evento(self): return self.s2299_infoperapur_ideestablot.evento()
    indsimples = models.IntegerField(choices=CHOICES_S2299_INFOPERAPUR_INDSIMPLES)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infoperapur_ideestablot) + ' - ' + unicode(self.indsimples)
    #s2299_infoperapur_infosimples_custom#
    #s2299_infoperapur_infosimples_custom#
    class Meta:
        db_table = r's2299_infoperapur_infosimples'
        managed = True
        ordering = ['s2299_infoperapur_ideestablot', 'indsimples']


class s2299infoTrabInterm(models.Model):
    s2299_dmdev = models.ForeignKey('s2299dmDev',
        related_name='%(class)s_s2299_dmdev')
    def evento(self): return self.s2299_dmdev.evento()
    codconv = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_dmdev) + ' - ' + unicode(self.codconv)
    #s2299_infotrabinterm_custom#
    #s2299_infotrabinterm_custom#
    class Meta:
        db_table = r's2299_infotrabinterm'
        managed = True
        ordering = ['s2299_dmdev', 'codconv']


class s2299infoTrabIntermconsigFGTS(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    insconsig = models.CharField(max_length=5)
    nrcontr = models.CharField(max_length=40)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.insconsig) + ' - ' + unicode(self.nrcontr)
    #s2299_infotrabinterm_consigfgts_custom#
    #s2299_infotrabinterm_consigfgts_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_consigfgts'
        managed = True
        ordering = ['s2299_evtdeslig', 'insconsig', 'nrcontr']


class s2299infoTrabInterminfoMV(models.Model):
    s2299_verbasresc = models.OneToOneField('s2299verbasResc',
        related_name='%(class)s_s2299_verbasresc')
    def evento(self): return self.s2299_verbasresc.evento()
    indmv = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_INDMV)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_verbasresc) + ' - ' + unicode(self.indmv)
    #s2299_infotrabinterm_infomv_custom#
    #s2299_infotrabinterm_infomv_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_infomv'
        managed = True
        ordering = ['s2299_verbasresc', 'indmv']


class s2299infoTrabIntermprocCS(models.Model):
    s2299_verbasresc = models.OneToOneField('s2299verbasResc',
        related_name='%(class)s_s2299_verbasresc')
    def evento(self): return self.s2299_verbasresc.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_verbasresc) + ' - ' + unicode(self.nrprocjud)
    #s2299_infotrabinterm_proccs_custom#
    #s2299_infotrabinterm_proccs_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_proccs'
        managed = True
        ordering = ['s2299_verbasresc', 'nrprocjud']


class s2299infoTrabIntermprocJudTrab(models.Model):
    s2299_verbasresc = models.ForeignKey('s2299verbasResc',
        related_name='%(class)s_s2299_verbasresc')
    def evento(self): return self.s2299_verbasresc.evento()
    tptrib = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPTRIB)
    nrprocjud = models.CharField(max_length=20)
    codsusp = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_verbasresc) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s2299_infotrabinterm_procjudtrab_custom#
    #s2299_infotrabinterm_procjudtrab_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_procjudtrab'
        managed = True
        ordering = ['s2299_verbasresc', 'tptrib', 'nrprocjud', 'codsusp']


class s2299infoTrabIntermquarentena(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    dtfimquar = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.dtfimquar)
    #s2299_infotrabinterm_quarentena_custom#
    #s2299_infotrabinterm_quarentena_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_quarentena'
        managed = True
        ordering = ['s2299_evtdeslig', 'dtfimquar']


class s2299infoTrabIntermremunOutrEmpr(models.Model):
    s2299_infotrabinterm_infomv = models.ForeignKey('s2299infoTrabInterminfoMV',
        related_name='%(class)s_s2299_infotrabinterm_infomv')
    def evento(self): return self.s2299_infotrabinterm_infomv.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2299_INFOTRABINTERM_TPINSC)
    nrinsc = models.CharField(max_length=15)
    codcateg = models.IntegerField()
    vlrremunoe = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_infotrabinterm_infomv) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.vlrremunoe)
    #s2299_infotrabinterm_remunoutrempr_custom#
    #s2299_infotrabinterm_remunoutrempr_custom#
    class Meta:
        db_table = r's2299_infotrabinterm_remunoutrempr'
        managed = True
        ordering = ['s2299_infotrabinterm_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe']


class s2299observacoes(models.Model):
    s2299_evtdeslig = models.ForeignKey('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.observacao)
    #s2299_observacoes_custom#
    #s2299_observacoes_custom#
    class Meta:
        db_table = r's2299_observacoes'
        managed = True
        ordering = ['s2299_evtdeslig', 'observacao']


class s2299sucessaoVinc(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    cnpjsucessora = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.cnpjsucessora)
    #s2299_sucessaovinc_custom#
    #s2299_sucessaovinc_custom#
    class Meta:
        db_table = r's2299_sucessaovinc'
        managed = True
        ordering = ['s2299_evtdeslig', 'cnpjsucessora']


class s2299transfTit(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    cpfsubstituto = models.CharField(max_length=11)
    dtnascto = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig) + ' - ' + unicode(self.cpfsubstituto) + ' - ' + unicode(self.dtnascto)
    #s2299_transftit_custom#
    #s2299_transftit_custom#
    class Meta:
        db_table = r's2299_transftit'
        managed = True
        ordering = ['s2299_evtdeslig', 'cpfsubstituto', 'dtnascto']


class s2299verbasResc(models.Model):
    s2299_evtdeslig = models.OneToOneField('esocial.s2299evtDeslig',
        related_name='%(class)s_s2299_evtdeslig')
    def evento(self): return self.s2299_evtdeslig.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2299_evtdeslig)
    #s2299_verbasresc_custom#
    #s2299_verbasresc_custom#
    class Meta:
        db_table = r's2299_verbasresc'
        managed = True
        ordering = ['s2299_evtdeslig']


#VIEWS_MODELS
