#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S1207_INFOPERANT_TPACCONV = (
    ('B', u'B - Legislação federal, estadual, municipal ou distrital'),
    ('G', u'G - Decisão administrativa'),
    ('H', u'H - Decisão judicial'),
)

CHOICES_S1207_TPBENEF = (
    (1, u'1 - Aposentadoria Voluntária por Idade e Tempo de Contribuição - Proventos Integrais: Art. 40, § 1º, III “a” da CF, Redação EC 20/98'),
    (10, u'10 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c LC 152/2015'),
    (11, u'11 - Aposentadoria - Magistrado, Membro do MP e TC - Proventos Integrais correspondentes à última remuneração: Regra de Transição do Art. 8º, da EC 20/98'),
    (12, u'12 - Aposentadoria - Proventos Integrais correspondentes à última remuneração - Regra de Transição do Art. 8º, da EC 20/98: Geral'),
    (13, u'13 - Aposentadoria Especial do Professor - Regra de Transição do Art. 8º, da EC 20/98: Proventos Integrais correspondentes à última remuneração.'),
    (14, u'14 - Aposentadoria com proventos proporcionais calculados sobre a última remuneraçãoRegra de Transição do Art. 8º, da EC20/98 - Geral'),
    (15, u'15 - Aposentadoria - Regra de Transição do Art. 3º, da EC 47/05: Proventos Integrais correspondentes à última remuneração'),
    (16, u'16 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (17, u'17 - Aposentadoria Especial de Professor - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (18, u'18 - Aposentadoria Magistrado, Membro do MP e TC (homem) - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação a partir de 01/01/2006)'),
    (19, u'19 - Aposentadoria Magistrado, Membro do MP e TC - Regra de Transição do Art. 2º, da EC41/03: Proventos pela Média com redutor (Implementação até 31/12/2005)'),
    (2, u'2 - Aposentadoria por Idade - Proventos proporcionais: Art. 40, III, c da CF redação original - Anterior à EC 20/1998'),
    (20, u'20 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média com redutor - Geral (Implementação a partir de 01/01/2006)'),
    (21, u'21 - Aposentadoria Voluntária - Regra de Transição do Art. 2º, da EC 41/03 - Proventos pela Média reduzida - Geral (Implementação até 31/12/2005)'),
    (22, u'22 - Aposentadoria Voluntária - Regra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes á ultima remuneração do cargo - Geral'),
    (23, u'23 - Aposentadoria Voluntária Professor Educação infantil, ensino fundamental e médioRegra de Transição do Art. 6º, da EC41/03: Proventos Integrais correspondentes à última remuneração do cargo'),
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b" CF, Redação EC 20/98'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b" CF, Redação EC 41/03'),
    (26, u'26 - Aposentadoria Voluntária por Idade e por Tempo de Contribuição - Proventos pela Média: Art. 40, § 1º, Inciso III, aliena "a", CF, Redação EC 41/03'),
    (27, u'27 - Aposentadoria Voluntária por Tempo de Contribuição - Especial do professor de q/q nível de ensino - Art. 40, III, alínea b, da CF- Red. Original até EC 20/1998'),
    (28, u'28 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial do professor ed. infantil, ensino fundamental e médio - Art. 40, § 1º, Inciso III, alínea a, c/c § 5º da CF red. da EC 20/1998 )'),
    (29, u'29 - Aposentadoria Voluntária por idade e Tempo de Contribuição - Especial de Professor - Proventos pela Média: Art. 40, § 1º, Inciso III, alínea "a", C/C § 5º da CF, Redação EC 41/2003'),
    (3, u'3 - Aposentadoria por Invalidez - Proventos integrais ou proporcionais: Art. 40, I da CF redação original - anterior à EC 20/1998'),
    (30, u'30 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas com base na última remuneração do cargo) - Art. 40, Inciso I, Redação Original, CF'),
    (31, u'31 - Aposentadoria por Invalidez (proporcionais ou integrais , calculadas com base na última remuneração do cargo) - Art. 40, § 1º, Inciso I da CF com Redação da EC 20/1998'),
    (32, u'32 - Aposentadoria por Invalidez (proporcionais ou integrais, calculadas pela média) - Art. 40, § 1º, Inciso I da CF com Redação da EC 41/2003'),
    (33, u'33 - Aposentadoria por Invalidez (proporcionais ou integrais calculadas com base na última remuneração do cargo) - Art. 40 º 1º, Inciso I da CF C/C combinado com Art. 6ª- A da EC 70/2012'),
    (34, u'34 - Reforma por invalidez'),
    (35, u'35 - Reserva Remunerada Compulsória'),
    (36, u'36 - Reserva Remunerada Integral'),
    (37, u'37 - Reserva Remunerada Proporcional'),
    (38, u'38 - Auxílio Doença - Conforme lei do Ente'),
    (39, u'39 - Auxílio Reclusão - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (4, u'4 - Aposentadoria Compulsória - Proventos proporcionais: Art. 40, II da CF redação original, anterior à EC 20/1998 *'),
    (40, u'40 - Pensão por Morte'),
    (41, u'41 - Salário Família - Art. 13 da EC 20/1998 c/c lei do Ente'),
    (42, u'42 - Salário Maternidade - Art. 7º, XVIII c/c art. 39, § 3º da Constituição Federal'),
    (43, u'43 - Complementação de Aposentadoria do Regime Geral de Previdência Social (RGPS)'),
    (44, u'44 - Complementação de Pensão por Morte do Regime Geral de Previdência Social (RGPS)'),
    (5, u'5 - Aposentadoria por Tempo de Serviço Integral - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (6, u'6 - Aposentadoria por Tempo de Serviço Proporcional - Art. 40, III, a da CF redação original - anterior à EC 20/1998 *'),
    (7, u'7 - Aposentadoria Compulsória Proporcional calculada sobre a última remuneração- Art. 40, § 1º, Inciso II da CF, Redação EC 20/1998'),
    (8, u'8 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03'),
    (9, u'9 - Aposentadoria Compulsória Proporcional calculada pela média - Art. 40, § 1º Inciso II da CF, Redação EC 41/03, c/c EC 88/2015'),
    (91, u'91 - Aposentadoria sem paridade concedida antes do início de vigência do eSocial'),
    (92, u'92 - Aposentadoria com paridade concedida antes do início de vigência do eSocial'),
    (93, u'93 - Aposentadoria por invalidez com paridade concedida antes do início de vigência do eSocial'),
    (94, u'94 - Aposentadoria por invalidez sem paridade concedida antes do início de vigência do eSocial'),
    (95, u'95 - Transferência para reserva concedida antes do início de vigência do eSocial'),
    (96, u'96 - Reforma concedida antes do início de vigência do eSocial'),
    (97, u'97 - Pensão por morte com paridade concedida antes do início de vigência do eSocial'),
    (98, u'98 - Pensão por morte sem paridade concedida antes do início de vigência do eSocial'),
    (99, u'99 - Outros Benefícios previdenciários concedidos antes do início de vigência do eSocial'),
)

CHOICES_S1207_TPTRIB = (
    (1, u'1 - IRRF'),
    (5, u'5 - Contribuição para o RPPS/regime militar'),
)

class s1207dmDev(models.Model):
    s1207_evtbenprrp = models.ForeignKey('esocial.s1207evtBenPrRP',
        related_name='%(class)s_s1207_evtbenprrp')
    def evento(self): return self.s1207_evtbenprrp.evento()
    tpbenef = models.IntegerField(choices=CHOICES_S1207_TPBENEF)
    nrbenefic = models.CharField(max_length=20)
    idedmdev = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_evtbenprrp) + ' - ' + unicode(self.tpbenef) + ' - ' + unicode(self.nrbenefic) + ' - ' + unicode(self.idedmdev)
    #s1207_dmdev_custom#
    #s1207_dmdev_custom#
    class Meta:
        db_table = r's1207_dmdev'
        managed = True
        ordering = ['s1207_evtbenprrp', 'tpbenef', 'nrbenefic', 'idedmdev']



class s1207dmDevSerializer(ModelSerializer):
    class Meta:
        model = s1207dmDev
        fields = '__all__'
            

class s1207infoPerAnt(models.Model):
    s1207_dmdev = models.OneToOneField('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_dmdev)
    #s1207_infoperant_custom#
    #s1207_infoperant_custom#
    class Meta:
        db_table = r's1207_infoperant'
        managed = True
        ordering = ['s1207_dmdev']



class s1207infoPerAntSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAnt
        fields = '__all__'
            

class s1207infoPerAntideADC(models.Model):
    s1207_infoperant = models.ForeignKey('s1207infoPerAnt',
        related_name='%(class)s_s1207_infoperant')
    def evento(self): return self.s1207_infoperant.evento()
    dtacconv = models.DateField(blank=True, null=True)
    tpacconv = models.CharField(choices=CHOICES_S1207_INFOPERANT_TPACCONV, max_length=1)
    compacconv = models.CharField(max_length=7, blank=True, null=True)
    dtefacconv = models.DateField(blank=True, null=True)
    dsc = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperant) + ' - ' + unicode(self.dtacconv) + ' - ' + unicode(self.tpacconv) + ' - ' + unicode(self.compacconv) + ' - ' + unicode(self.dtefacconv) + ' - ' + unicode(self.dsc)
    #s1207_infoperant_ideadc_custom#
    #s1207_infoperant_ideadc_custom#
    class Meta:
        db_table = r's1207_infoperant_ideadc'
        managed = True
        ordering = ['s1207_infoperant', 'dtacconv', 'tpacconv', 'compacconv', 'dtefacconv', 'dsc']



class s1207infoPerAntideADCSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntideADC
        fields = '__all__'
            

class s1207infoPerAntideEstab(models.Model):
    s1207_infoperant_ideperiodo = models.ForeignKey('s1207infoPerAntidePeriodo',
        related_name='%(class)s_s1207_infoperant_ideperiodo')
    def evento(self): return self.s1207_infoperant_ideperiodo.evento()
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideperiodo) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1207_infoperant_ideestab_custom#
    #s1207_infoperant_ideestab_custom#
    class Meta:
        db_table = r's1207_infoperant_ideestab'
        managed = True
        ordering = ['s1207_infoperant_ideperiodo', 'tpinsc', 'nrinsc']



class s1207infoPerAntideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntideEstab
        fields = '__all__'
            

class s1207infoPerAntidePeriodo(models.Model):
    s1207_infoperant_ideadc = models.ForeignKey('s1207infoPerAntideADC',
        related_name='%(class)s_s1207_infoperant_ideadc')
    def evento(self): return self.s1207_infoperant_ideadc.evento()
    perref = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideadc) + ' - ' + unicode(self.perref)
    #s1207_infoperant_ideperiodo_custom#
    #s1207_infoperant_ideperiodo_custom#
    class Meta:
        db_table = r's1207_infoperant_ideperiodo'
        managed = True
        ordering = ['s1207_infoperant_ideadc', 'perref']



class s1207infoPerAntidePeriodoSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntidePeriodo
        fields = '__all__'
            

class s1207infoPerAntitensRemun(models.Model):
    s1207_infoperant_remunperant = models.ForeignKey('s1207infoPerAntremunPerAnt',
        related_name='%(class)s_s1207_infoperant_remunperant')
    def evento(self): return self.s1207_infoperant_remunperant.evento()
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
        return unicode(self.s1207_infoperant_remunperant) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1207_infoperant_itensremun_custom#
    #s1207_infoperant_itensremun_custom#
    class Meta:
        db_table = r's1207_infoperant_itensremun'
        managed = True
        ordering = ['s1207_infoperant_remunperant', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1207infoPerAntitensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntitensRemun
        fields = '__all__'
            

class s1207infoPerAntremunPerAnt(models.Model):
    s1207_infoperant_ideestab = models.ForeignKey('s1207infoPerAntideEstab',
        related_name='%(class)s_s1207_infoperant_ideestab')
    def evento(self): return self.s1207_infoperant_ideestab.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperant_ideestab)
    #s1207_infoperant_remunperant_custom#
    #s1207_infoperant_remunperant_custom#
    class Meta:
        db_table = r's1207_infoperant_remunperant'
        managed = True
        ordering = ['s1207_infoperant_ideestab']



class s1207infoPerAntremunPerAntSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerAntremunPerAnt
        fields = '__all__'
            

class s1207infoPerApur(models.Model):
    s1207_dmdev = models.OneToOneField('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_dmdev)
    #s1207_infoperapur_custom#
    #s1207_infoperapur_custom#
    class Meta:
        db_table = r's1207_infoperapur'
        managed = True
        ordering = ['s1207_dmdev']



class s1207infoPerApurSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApur
        fields = '__all__'
            

class s1207infoPerApurideEstab(models.Model):
    s1207_infoperapur = models.ForeignKey('s1207infoPerApur',
        related_name='%(class)s_s1207_infoperapur')
    def evento(self): return self.s1207_infoperapur.evento()
    tpinsc = models.IntegerField()
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperapur) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s1207_infoperapur_ideestab_custom#
    #s1207_infoperapur_ideestab_custom#
    class Meta:
        db_table = r's1207_infoperapur_ideestab'
        managed = True
        ordering = ['s1207_infoperapur', 'tpinsc', 'nrinsc']



class s1207infoPerApurideEstabSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApurideEstab
        fields = '__all__'
            

class s1207infoPerApuritensRemun(models.Model):
    s1207_infoperapur_remunperapur = models.ForeignKey('s1207infoPerApurremunPerApur',
        related_name='%(class)s_s1207_infoperapur_remunperapur')
    def evento(self): return self.s1207_infoperapur_remunperapur.evento()
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
        return unicode(self.s1207_infoperapur_remunperapur) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.qtdrubr) + ' - ' + unicode(self.fatorrubr) + ' - ' + unicode(self.vrunit) + ' - ' + unicode(self.vrrubr)
    #s1207_infoperapur_itensremun_custom#
    #s1207_infoperapur_itensremun_custom#
    class Meta:
        db_table = r's1207_infoperapur_itensremun'
        managed = True
        ordering = ['s1207_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'qtdrubr', 'fatorrubr', 'vrunit', 'vrrubr']



class s1207infoPerApuritensRemunSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApuritensRemun
        fields = '__all__'
            

class s1207infoPerApurremunPerApur(models.Model):
    s1207_infoperapur_ideestab = models.ForeignKey('s1207infoPerApurideEstab',
        related_name='%(class)s_s1207_infoperapur_ideestab')
    def evento(self): return self.s1207_infoperapur_ideestab.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_infoperapur_ideestab)
    #s1207_infoperapur_remunperapur_custom#
    #s1207_infoperapur_remunperapur_custom#
    class Meta:
        db_table = r's1207_infoperapur_remunperapur'
        managed = True
        ordering = ['s1207_infoperapur_ideestab']



class s1207infoPerApurremunPerApurSerializer(ModelSerializer):
    class Meta:
        model = s1207infoPerApurremunPerApur
        fields = '__all__'
            

class s1207itens(models.Model):
    s1207_dmdev = models.ForeignKey('s1207dmDev',
        related_name='%(class)s_s1207_dmdev')
    def evento(self): return self.s1207_dmdev.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1207_dmdev) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1207_itens_custom#
    #s1207_itens_custom#
    class Meta:
        db_table = r's1207_itens'
        managed = True
        ordering = ['s1207_dmdev', 'codrubr', 'idetabrubr', 'vrrubr']



class s1207itensSerializer(ModelSerializer):
    class Meta:
        model = s1207itens
        fields = '__all__'
            

class s1207procJudTrab(models.Model):
    s1207_evtbenprrp = models.ForeignKey('esocial.s1207evtBenPrRP',
        related_name='%(class)s_s1207_evtbenprrp')
    def evento(self): return self.s1207_evtbenprrp.evento()
    tptrib = models.IntegerField(choices=CHOICES_S1207_TPTRIB)
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
        return unicode(self.s1207_evtbenprrp) + ' - ' + unicode(self.tptrib) + ' - ' + unicode(self.nrprocjud) + ' - ' + unicode(self.codsusp)
    #s1207_procjudtrab_custom#
    #s1207_procjudtrab_custom#
    class Meta:
        db_table = r's1207_procjudtrab'
        managed = True
        ordering = ['s1207_evtbenprrp', 'tptrib', 'nrprocjud', 'codsusp']



class s1207procJudTrabSerializer(ModelSerializer):
    class Meta:
        model = s1207procJudTrab
        fields = '__all__'
            

#VIEWS_MODELS
