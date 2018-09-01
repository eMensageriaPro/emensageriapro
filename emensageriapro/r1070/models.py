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

PERIODOS = (
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
)

CHOICES_R1070_ALTERACAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade ou empresa'),
)

CHOICES_R1070_ALTERACAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R1070_ALTERACAO_INDSUSP = (
    ('1', u'01 - Liminar em Mandado de Segurança'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('2', u'02 - Depósito Judicial do Montante Integral'),
    ('3', u'03 - Depósito Administrativo do Montante Integral'),
    ('4', u'04 - Antecipação de Tutela'),
    ('5', u'05 - Liminar em Medida Cautelar'),
    ('8', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('9', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_R1070_ALTERACAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R1070_EXCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R1070_INCLUSAO_INDAUTORIA = (
    (1, u'1 - Próprio contribuinte'),
    (2, u'2 - Outra entidade ou empresa'),
)

CHOICES_R1070_INCLUSAO_INDDEPOSITO = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_R1070_INCLUSAO_INDSUSP = (
    ('1', u'01 - Liminar em Mandado de Segurança'),
    ('10', u'10 - Acórdão do TRF Favorável ao Contribuinte'),
    ('11', u'11 - Acórdão do STJ em Recurso Especial Favorável ao Contribuinte'),
    ('12', u'12 - Acórdão do STF em Recurso Extraordinário Favorável ao Contribuinte'),
    ('13', u'13 - Sentença 1ª instância não transitada em julgado com efeito suspensivo'),
    ('2', u'02 - Depósito Judicial do Montante Integral'),
    ('3', u'03 - Depósito Administrativo do Montante Integral'),
    ('4', u'04 - Antecipação de Tutela'),
    ('5', u'05 - Liminar em Medida Cautelar'),
    ('8', u'08 - Sentença em Mandado de Segurança Favorável ao Contribuinte'),
    ('9', u'09 - Sentença em Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF'),
    ('90', u'90 - Decisão Definitiva a favor do contribuinte'),
    ('92', u'92 - Sem suspensão da exigibilidade'),
)

CHOICES_R1070_INCLUSAO_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r1070alteracao(models.Model):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_ALTERACAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_R1070_ALTERACAO_INDAUTORIA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.indautoria)
    #r1070_alteracao_custom#
    #r1070_alteracao_custom#
    class Meta:
        db_table = r'r1070_alteracao'
        managed = True
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria']


class r1070alteracaodadosProcJud(models.Model):
    r1070_alteracao = models.OneToOneField('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.CharField(max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #r1070_alteracao_dadosprocjud_custom#
    #r1070_alteracao_dadosprocjud_custom#
    class Meta:
        db_table = r'r1070_alteracao_dadosprocjud'
        managed = True
        ordering = ['r1070_alteracao', 'ufvara', 'codmunic', 'idvara']


class r1070alteracaoinfoSusp(models.Model):
    r1070_alteracao = models.ForeignKey('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    codsusp = models.IntegerField(blank=True, null=True)
    indsusp = models.CharField(choices=CHOICES_R1070_ALTERACAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_R1070_ALTERACAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #r1070_alteracao_infosusp_custom#
    #r1070_alteracao_infosusp_custom#
    class Meta:
        db_table = r'r1070_alteracao_infosusp'
        managed = True
        ordering = ['r1070_alteracao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito']


class r1070alteracaonovaValidade(models.Model):
    r1070_alteracao = models.OneToOneField('r1070alteracao',
        related_name='%(class)s_r1070_alteracao')
    def evento(self): return self.r1070_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #r1070_alteracao_novavalidade_custom#
    #r1070_alteracao_novavalidade_custom#
    class Meta:
        db_table = r'r1070_alteracao_novavalidade'
        managed = True
        ordering = ['r1070_alteracao', 'inivalid', 'fimvalid']


class r1070exclusao(models.Model):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_EXCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #r1070_exclusao_custom#
    #r1070_exclusao_custom#
    class Meta:
        db_table = r'r1070_exclusao'
        managed = True
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid']


class r1070inclusao(models.Model):
    r1070_evttabprocesso = models.OneToOneField('efdreinf.r1070evtTabProcesso',
        related_name='%(class)s_r1070_evttabprocesso')
    def evento(self): return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_INCLUSAO_TPPROC)
    nrproc = models.CharField(max_length=21)
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    indautoria = models.IntegerField(choices=CHOICES_R1070_INCLUSAO_INDAUTORIA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_evttabprocesso) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.indautoria)
    #r1070_inclusao_custom#
    #r1070_inclusao_custom#
    class Meta:
        db_table = r'r1070_inclusao'
        managed = True
        ordering = ['r1070_evttabprocesso', 'tpproc', 'nrproc', 'inivalid', 'fimvalid', 'indautoria']


class r1070inclusaodadosProcJud(models.Model):
    r1070_inclusao = models.OneToOneField('r1070inclusao',
        related_name='%(class)s_r1070_inclusao')
    def evento(self): return self.r1070_inclusao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7)
    idvara = models.CharField(max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_inclusao) + ' - ' + unicode(self.ufvara) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.idvara)
    #r1070_inclusao_dadosprocjud_custom#
    #r1070_inclusao_dadosprocjud_custom#
    class Meta:
        db_table = r'r1070_inclusao_dadosprocjud'
        managed = True
        ordering = ['r1070_inclusao', 'ufvara', 'codmunic', 'idvara']


class r1070inclusaoinfoSusp(models.Model):
    r1070_inclusao = models.ForeignKey('r1070inclusao',
        related_name='%(class)s_r1070_inclusao')
    def evento(self): return self.r1070_inclusao.evento()
    codsusp = models.IntegerField(blank=True, null=True)
    indsusp = models.CharField(choices=CHOICES_R1070_INCLUSAO_INDSUSP, max_length=2)
    dtdecisao = models.DateField()
    inddeposito = models.CharField(choices=CHOICES_R1070_INCLUSAO_INDDEPOSITO, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r1070_inclusao) + ' - ' + unicode(self.codsusp) + ' - ' + unicode(self.indsusp) + ' - ' + unicode(self.dtdecisao) + ' - ' + unicode(self.inddeposito)
    #r1070_inclusao_infosusp_custom#
    #r1070_inclusao_infosusp_custom#
    class Meta:
        db_table = r'r1070_inclusao_infosusp'
        managed = True
        ordering = ['r1070_inclusao', 'codsusp', 'indsusp', 'dtdecisao', 'inddeposito']


#VIEWS_MODELS
