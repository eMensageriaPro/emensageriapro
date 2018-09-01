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

CHOICES_S1000_ALTERACAO_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S1000_ALTERACAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_S1000_ALTERACAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_S1000_ALTERACAO_INDCONSTR = (
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora'),
)

CHOICES_S1000_ALTERACAO_INDCOOP = (
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas'),
)

CHOICES_S1000_ALTERACAO_INDDESFOLHA = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011'),
)

CHOICES_S1000_ALTERACAO_INDENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_INDETT = (
    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário'),
)

CHOICES_S1000_ALTERACAO_INDOPTREGELETRON = (
    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados'),
)

CHOICES_S1000_ALTERACAO_INDRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_ALTERACAO_INDSITPF = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente'),
)

CHOICES_S1000_ALTERACAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
)

CHOICES_S1000_ALTERACAO_NATJURID = (
    ('1015', u'1015 - Órgão Público do Poder Executivo Federal'),
    ('1023', u'1023 - Órgão Público do Poder Executivo Estadual ou do Distrito Federal'),
    ('1031', u'1031 - Órgão Público do Poder Executivo Municipal'),
    ('1040', u'1040 - Órgão Público do Poder Legislativo Federal'),
    ('1058', u'1058 - Órgão Público do Poder Legislativo Estadual ou do Distrito Federal'),
    ('1066', u'1066 - Órgão Público do Poder Legislativo Municipal'),
    ('1074', u'1074 - Órgão Público do Poder Judiciário Federal'),
    ('1082', u'1082 - Órgão Público do Poder Judiciário Estadual'),
    ('1104', u'1104 - Autarquia Federal'),
    ('1112', u'1112 - Autarquia Estadual ou do Distrito Federal'),
    ('1120', u'1120 - Autarquia Municipal'),
    ('1139', u'1139 - Fundação Pública de Direito Público Federal'),
    ('1147', u'1147 - Fundação Pública de Direito Público Estadual ou do Distrito Federal'),
    ('1155', u'1155 - Fundação Pública de Direito Público Municipal'),
    ('1163', u'1163 - Órgão Público Autônomo Federal'),
    ('1171', u'1171 - Órgão Público Autônomo Estadual ou do Distrito Federal'),
    ('1180', u'1180 - Órgão Público Autônomo Municipal'),
    ('1198', u'1198 - Comissão Polinacional'),
    ('1201', u'1201 - Fundo Público'),
    ('1210', u'1210 - Consórcio Público de Direito Público (Associação Pública)'),
    ('1228', u'1228 - Consórcio Público de Direito Privado'),
    ('1236', u'1236 - Estado ou Distrito Federal'),
    ('1244', u'1244 - Município'),
    ('1252', u'1252 - Fundação Pública de Direito Privado Federal'),
    ('1260', u'1260 - Fundação Pública de Direito Privado Estadual ou do Distrito Federal'),
    ('1279', u'1279 - Fundação Pública de Direito Privado Municipal'),
    ('2011', u'2011 - Empresa Pública'),
    ('2038', u'2038 - Sociedade de Economia Mista'),
    ('2046', u'2046 - Sociedade Anônima Aberta'),
    ('2054', u'2054 - Sociedade Anônima Fechada'),
    ('2062', u'2062 - Sociedade Empresária Limitada'),
    ('2070', u'2070 - Sociedade Empresária em Nome Coletivo'),
    ('2089', u'2089 - Sociedade Empresária em Comandita Simples'),
    ('2097', u'2097 - Sociedade Empresária em Comandita por Ações'),
    ('2127', u'2127 - Sociedade em Conta de Participação'),
    ('2135', u'2135 - Empresário (Individual)'),
    ('2143', u'2143 - Cooperativa'),
    ('2151', u'2151 - Consórcio de Sociedades'),
    ('2160', u'2160 - Grupo de Sociedades'),
    ('2178', u'2178 - Estabelecimento, no Brasil, de Sociedade Estrangeira'),
    ('2194', u'2194 - Estabelecimento, no Brasil, de Empresa Binacional Argentino-Brasileira'),
    ('2216', u'2216 - Empresa Domiciliada no Exterior'),
    ('2224', u'2224 - Clube/Fundo de Investimento'),
    ('2232', u'2232 - Sociedade Simples Pura'),
    ('2240', u'2240 - Sociedade Simples Limitada'),
    ('2259', u'2259 - Sociedade Simples em Nome Coletivo'),
    ('2267', u'2267 - Sociedade Simples em Comandita Simples'),
    ('2275', u'2275 - Empresa Binacional'),
    ('2283', u'2283 - Consórcio de Empregadores'),
    ('2291', u'2291 - Consórcio Simples'),
    ('2305', u'2305 - Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)'),
    ('2313', u'2313 - Empresa Individual de Responsabilidade Limitada (de Natureza Simples)'),
    ('2321', u'2321 - Sociedade Unipessoal de Advogados'),
    ('2330', u'2330 - Cooperativas de Consumo'),
    ('3034', u'3034 - Serviço Notarial e Registral (Cartório)'),
    ('3069', u'3069 - Fundação Privada'),
    ('3077', u'3077 - Serviço Social Autônomo'),
    ('3085', u'3085 - Condomínio Edilício'),
    ('3107', u'3107 - Comissão de Conciliação Prévia'),
    ('3115', u'3115 - Entidade de Mediação e Arbitragem'),
    ('3131', u'3131 - Entidade Sindical'),
    ('3204', u'3204 - Estabelecimento, no Brasil, de Fundação ou Associação Estrangeiras'),
    ('3212', u'3212 - Fundação ou Associação Domiciliada no Exterior'),
    ('3220', u'3220 - Organização Religiosa'),
    ('3239', u'3239 - Comunidade Indígena'),
    ('3247', u'3247 - Fundo Privado'),
    ('3255', u'3255 - Órgão de Direção Nacional de Partido Político'),
    ('3263', u'3263 - Órgão de Direção Regional de Partido Político'),
    ('3271', u'3271 - Órgão de Direção Local de Partido Político'),
    ('3280', u'3280 - Comitê Financeiro de Partido Político'),
    ('3298', u'3298 - Frente Plebiscitária ou Referendária'),
    ('3306', u'3306 - Organização Social (OS)'),
    ('3310', u'3310 - Demais Condomínios'),
    ('3999', u'3999 - Associação Privada'),
    ('4014', u'4014 - Empresa Individual Imobiliária'),
    ('4022', u'4022 - Segurado Especial'),
    ('4081', u'4081 - Contribuinte individual'),
    ('4090', u'4090 - Candidato a Cargo Político Eletivo'),
    ('4111', u'4111 - Leiloeiro'),
    ('4124', u'4124 - Produtor Rural (Pessoa Física)'),
    ('5010', u'5010 - Organização Internacional'),
    ('5029', u'5029 - Representação Diplomática Estrangeira'),
    ('5037', u'5037 - Outras Instituições Extraterritoriais'),
)

CHOICES_S1000_ALTERACAO_SUBTETO = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes'),
)

CHOICES_S1000_INCLUSAO_CLASSTRIB = (
    ('01', u'01 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
)

CHOICES_S1000_INCLUSAO_IDEEFR = (
    ('N', u'N - Não é EFR'),
    ('S', u'S - É EFR'),
)

CHOICES_S1000_INCLUSAO_INDACORDOISENMULTA = (
    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo'),
)

CHOICES_S1000_INCLUSAO_INDCONSTR = (
    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora'),
)

CHOICES_S1000_INCLUSAO_INDCOOP = (
    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas'),
)

CHOICES_S1000_INCLUSAO_INDDESFOLHA = (
    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011'),
)

CHOICES_S1000_INCLUSAO_INDENTED = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_INDETT = (
    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário'),
)

CHOICES_S1000_INCLUSAO_INDOPTREGELETRON = (
    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados'),
)

CHOICES_S1000_INCLUSAO_INDRPPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1000_INCLUSAO_INDSITPF = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente'),
)

CHOICES_S1000_INCLUSAO_INDSITPJ = (
    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação'),
)

CHOICES_S1000_INCLUSAO_SUBTETO = (
    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes'),
)

class s1000alteracao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    classtrib = models.CharField(choices=CHOICES_S1000_ALTERACAO_CLASSTRIB, max_length=2)
    natjurid = models.CharField(choices=CHOICES_S1000_ALTERACAO_NATJURID, max_length=4, blank=True, null=True)
    indcoop = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDCOOP, blank=True, null=True)
    indconstr = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDCONSTR, blank=True, null=True)
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDDESFOLHA)
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDOPTREGELETRON)
    indented = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDENTED, max_length=1, blank=True, null=True)
    indett = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDETT, max_length=1)
    nrregett = models.CharField(max_length=30, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.natjurid) + ' - ' + unicode(self.indcoop) + ' - ' + unicode(self.indconstr) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.indented) + ' - ' + unicode(self.indett) + ' - ' + unicode(self.nrregett) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt) + ' - ' + unicode(self.fonefixo) + ' - ' + unicode(self.fonecel) + ' - ' + unicode(self.email)
    #s1000_alteracao_custom#
    #s1000_alteracao_custom#
    class Meta:
        db_table = r's1000_alteracao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid', 'fimvalid', 'nmrazao', 'classtrib', 'natjurid', 'indcoop', 'indconstr', 'inddesfolha', 'indoptregeletron', 'indented', 'indett', 'nrregett', 'nmctt', 'cpfctt', 'fonefixo', 'fonecel', 'email']


class s1000alteracaodadosIsencao(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    ideminlei = models.CharField(max_length=70)
    nrcertif = models.CharField(max_length=40)
    dtemiscertif = models.DateField()
    dtvenccertif = models.DateField()
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True)
    dtprotrenov = models.DateField(blank=True, null=True)
    dtdou = models.DateField(blank=True, null=True)
    pagdou = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif) + ' - ' + unicode(self.nrprotrenov) + ' - ' + unicode(self.dtprotrenov) + ' - ' + unicode(self.dtdou) + ' - ' + unicode(self.pagdou)
    #s1000_alteracao_dadosisencao_custom#
    #s1000_alteracao_dadosisencao_custom#
    class Meta:
        db_table = r's1000_alteracao_dadosisencao'
        managed = True
        ordering = ['s1000_alteracao', 'ideminlei', 'nrcertif', 'dtemiscertif', 'dtvenccertif', 'nrprotrenov', 'dtprotrenov', 'dtdou', 'pagdou']


class s1000alteracaoinfoEFR(models.Model):
    s1000_alteracao_infoop = models.OneToOneField('s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop')
    def evento(self): return self.s1000_alteracao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_ALTERACAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.cnpjefr)
    #s1000_alteracao_infoefr_custom#
    #s1000_alteracao_infoefr_custom#
    class Meta:
        db_table = r's1000_alteracao_infoefr'
        managed = True
        ordering = ['s1000_alteracao_infoop', 'ideefr', 'cnpjefr']


class s1000alteracaoinfoEnte(models.Model):
    s1000_alteracao_infoop = models.OneToOneField('s1000alteracaoinfoOP',
        related_name='%(class)s_s1000_alteracao_infoop')
    def evento(self): return self.s1000_alteracao_infoop.evento()
    nmente = models.CharField(max_length=100)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_ALTERACAO_INDRPPS, max_length=1)
    subteto = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_SUBTETO)
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)
    #s1000_alteracao_infoente_custom#
    #s1000_alteracao_infoente_custom#
    class Meta:
        db_table = r's1000_alteracao_infoente'
        managed = True
        ordering = ['s1000_alteracao_infoop', 'nmente', 'uf', 'codmunic', 'indrpps', 'subteto', 'vrsubteto']


class s1000alteracaoinfoOP(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    nrsiafi = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.nrsiafi)
    #s1000_alteracao_infoop_custom#
    #s1000_alteracao_infoop_custom#
    class Meta:
        db_table = r's1000_alteracao_infoop'
        managed = True
        ordering = ['s1000_alteracao', 'nrsiafi']


class s1000alteracaoinfoOrgInternacional(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDACORDOISENMULTA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indacordoisenmulta)
    #s1000_alteracao_infoorginternacional_custom#
    #s1000_alteracao_infoorginternacional_custom#
    class Meta:
        db_table = r's1000_alteracao_infoorginternacional'
        managed = True
        ordering = ['s1000_alteracao', 'indacordoisenmulta']


class s1000alteracaonovaValidade(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
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
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1000_alteracao_novavalidade_custom#
    #s1000_alteracao_novavalidade_custom#
    class Meta:
        db_table = r's1000_alteracao_novavalidade'
        managed = True
        ordering = ['s1000_alteracao', 'inivalid', 'fimvalid']


class s1000alteracaosituacaoPF(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDSITPF)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpf)
    #s1000_alteracao_situacaopf_custom#
    #s1000_alteracao_situacaopf_custom#
    class Meta:
        db_table = r's1000_alteracao_situacaopf'
        managed = True
        ordering = ['s1000_alteracao', 'indsitpf']


class s1000alteracaosituacaoPJ(models.Model):
    s1000_alteracao = models.OneToOneField('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_ALTERACAO_INDSITPJ)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.indsitpj)
    #s1000_alteracao_situacaopj_custom#
    #s1000_alteracao_situacaopj_custom#
    class Meta:
        db_table = r's1000_alteracao_situacaopj'
        managed = True
        ordering = ['s1000_alteracao', 'indsitpj']


class s1000alteracaosoftwareHouse(models.Model):
    s1000_alteracao = models.ForeignKey('s1000alteracao',
        related_name='%(class)s_s1000_alteracao')
    def evento(self): return self.s1000_alteracao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_alteracao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone) + ' - ' + unicode(self.email)
    #s1000_alteracao_softwarehouse_custom#
    #s1000_alteracao_softwarehouse_custom#
    class Meta:
        db_table = r's1000_alteracao_softwarehouse'
        managed = True
        ordering = ['s1000_alteracao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone', 'email']


class s1000exclusao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
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
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid)
    #s1000_exclusao_custom#
    #s1000_exclusao_custom#
    class Meta:
        db_table = r's1000_exclusao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid', 'fimvalid']


class s1000inclusao(models.Model):
    s1000_evtinfoempregador = models.OneToOneField('esocial.s1000evtInfoEmpregador',
        related_name='%(class)s_s1000_evtinfoempregador')
    def evento(self): return self.s1000_evtinfoempregador.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7)
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True)
    nmrazao = models.CharField(max_length=100)
    classtrib = models.CharField(choices=CHOICES_S1000_INCLUSAO_CLASSTRIB, max_length=2)
    natjurid = models.CharField(max_length=4, blank=True, null=True)
    indcoop = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDCOOP, blank=True, null=True)
    indconstr = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDCONSTR, blank=True, null=True)
    inddesfolha = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDDESFOLHA)
    indoptregeletron = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDOPTREGELETRON)
    indented = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDENTED, max_length=1, blank=True, null=True)
    indett = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDETT, max_length=1)
    nrregett = models.CharField(max_length=30, blank=True, null=True)
    nmctt = models.CharField(max_length=70)
    cpfctt = models.CharField(max_length=11)
    fonefixo = models.CharField(max_length=13, blank=True, null=True)
    fonecel = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_evtinfoempregador) + ' - ' + unicode(self.inivalid) + ' - ' + unicode(self.fimvalid) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.classtrib) + ' - ' + unicode(self.natjurid) + ' - ' + unicode(self.indcoop) + ' - ' + unicode(self.indconstr) + ' - ' + unicode(self.inddesfolha) + ' - ' + unicode(self.indoptregeletron) + ' - ' + unicode(self.indented) + ' - ' + unicode(self.indett) + ' - ' + unicode(self.nrregett) + ' - ' + unicode(self.nmctt) + ' - ' + unicode(self.cpfctt) + ' - ' + unicode(self.fonefixo) + ' - ' + unicode(self.fonecel) + ' - ' + unicode(self.email)
    #s1000_inclusao_custom#
    #s1000_inclusao_custom#
    class Meta:
        db_table = r's1000_inclusao'
        managed = True
        ordering = ['s1000_evtinfoempregador', 'inivalid', 'fimvalid', 'nmrazao', 'classtrib', 'natjurid', 'indcoop', 'indconstr', 'inddesfolha', 'indoptregeletron', 'indented', 'indett', 'nrregett', 'nmctt', 'cpfctt', 'fonefixo', 'fonecel', 'email']


class s1000inclusaodadosIsencao(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    ideminlei = models.CharField(max_length=70)
    nrcertif = models.CharField(max_length=40)
    dtemiscertif = models.DateField()
    dtvenccertif = models.DateField()
    nrprotrenov = models.CharField(max_length=40, blank=True, null=True)
    dtprotrenov = models.DateField(blank=True, null=True)
    dtdou = models.DateField(blank=True, null=True)
    pagdou = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.ideminlei) + ' - ' + unicode(self.nrcertif) + ' - ' + unicode(self.dtemiscertif) + ' - ' + unicode(self.dtvenccertif) + ' - ' + unicode(self.nrprotrenov) + ' - ' + unicode(self.dtprotrenov) + ' - ' + unicode(self.dtdou) + ' - ' + unicode(self.pagdou)
    #s1000_inclusao_dadosisencao_custom#
    #s1000_inclusao_dadosisencao_custom#
    class Meta:
        db_table = r's1000_inclusao_dadosisencao'
        managed = True
        ordering = ['s1000_inclusao', 'ideminlei', 'nrcertif', 'dtemiscertif', 'dtvenccertif', 'nrprotrenov', 'dtprotrenov', 'dtdou', 'pagdou']


class s1000inclusaoinfoEFR(models.Model):
    s1000_inclusao_infoop = models.OneToOneField('s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop')
    def evento(self): return self.s1000_inclusao_infoop.evento()
    ideefr = models.CharField(choices=CHOICES_S1000_INCLUSAO_IDEEFR, max_length=1)
    cnpjefr = models.CharField(max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.ideefr) + ' - ' + unicode(self.cnpjefr)
    #s1000_inclusao_infoefr_custom#
    #s1000_inclusao_infoefr_custom#
    class Meta:
        db_table = r's1000_inclusao_infoefr'
        managed = True
        ordering = ['s1000_inclusao_infoop', 'ideefr', 'cnpjefr']


class s1000inclusaoinfoEnte(models.Model):
    s1000_inclusao_infoop = models.OneToOneField('s1000inclusaoinfoOP',
        related_name='%(class)s_s1000_inclusao_infoop')
    def evento(self): return self.s1000_inclusao_infoop.evento()
    nmente = models.CharField(max_length=100)
    uf = models.CharField(choices=ESTADOS, max_length=2)
    codmunic = models.TextField(max_length=7, blank=True, null=True)
    indrpps = models.CharField(choices=CHOICES_S1000_INCLUSAO_INDRPPS, max_length=1)
    subteto = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_SUBTETO)
    vrsubteto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao_infoop) + ' - ' + unicode(self.nmente) + ' - ' + unicode(self.uf) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.indrpps) + ' - ' + unicode(self.subteto) + ' - ' + unicode(self.vrsubteto)
    #s1000_inclusao_infoente_custom#
    #s1000_inclusao_infoente_custom#
    class Meta:
        db_table = r's1000_inclusao_infoente'
        managed = True
        ordering = ['s1000_inclusao_infoop', 'nmente', 'uf', 'codmunic', 'indrpps', 'subteto', 'vrsubteto']


class s1000inclusaoinfoOP(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    nrsiafi = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.nrsiafi)
    #s1000_inclusao_infoop_custom#
    #s1000_inclusao_infoop_custom#
    class Meta:
        db_table = r's1000_inclusao_infoop'
        managed = True
        ordering = ['s1000_inclusao', 'nrsiafi']


class s1000inclusaoinfoOrgInternacional(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indacordoisenmulta = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDACORDOISENMULTA)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indacordoisenmulta)
    #s1000_inclusao_infoorginternacional_custom#
    #s1000_inclusao_infoorginternacional_custom#
    class Meta:
        db_table = r's1000_inclusao_infoorginternacional'
        managed = True
        ordering = ['s1000_inclusao', 'indacordoisenmulta']


class s1000inclusaosituacaoPF(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indsitpf = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDSITPF)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpf)
    #s1000_inclusao_situacaopf_custom#
    #s1000_inclusao_situacaopf_custom#
    class Meta:
        db_table = r's1000_inclusao_situacaopf'
        managed = True
        ordering = ['s1000_inclusao', 'indsitpf']


class s1000inclusaosituacaoPJ(models.Model):
    s1000_inclusao = models.OneToOneField('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    indsitpj = models.IntegerField(choices=CHOICES_S1000_INCLUSAO_INDSITPJ)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.indsitpj)
    #s1000_inclusao_situacaopj_custom#
    #s1000_inclusao_situacaopj_custom#
    class Meta:
        db_table = r's1000_inclusao_situacaopj'
        managed = True
        ordering = ['s1000_inclusao', 'indsitpj']


class s1000inclusaosoftwareHouse(models.Model):
    s1000_inclusao = models.ForeignKey('s1000inclusao',
        related_name='%(class)s_s1000_inclusao')
    def evento(self): return self.s1000_inclusao.evento()
    cnpjsofthouse = models.CharField(max_length=14)
    nmrazao = models.CharField(max_length=100)
    nmcont = models.CharField(max_length=70)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s1000_inclusao) + ' - ' + unicode(self.cnpjsofthouse) + ' - ' + unicode(self.nmrazao) + ' - ' + unicode(self.nmcont) + ' - ' + unicode(self.telefone) + ' - ' + unicode(self.email)
    #s1000_inclusao_softwarehouse_custom#
    #s1000_inclusao_softwarehouse_custom#
    class Meta:
        db_table = r's1000_inclusao_softwarehouse'
        managed = True
        ordering = ['s1000_inclusao', 'cnpjsofthouse', 'nmrazao', 'nmcont', 'telefone', 'email']


#VIEWS_MODELS
