#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.apps import apps
get_model = apps.get_model



CHOICES_S5002_CODCATEG = (
    (101, u'101 - Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT.'),
    (102, u'102 - Empregado - Trabalhador Rural por Pequeno Prazo da Lei 11.718/2008'),
    (103, u'103 - Empregado - Aprendiz'),
    (104, u'104 - Empregado - Doméstico'),
    (105, u'105 - Empregado - contrato a termo firmado nos termos da Lei 9601/98'),
    (106, u'106 - Trabalhador Temporário - contrato por prazo determinado nos termos da Lei 6019/74'),
    (111, u'111 - Empregado - contrato de trabalho intermitente'),
    (201, u'201 - Trabalhador Avulso Portuário'),
    (202, u'202 - Trabalhador Avulso Não Portuário'),
    (301, u'301 - Servidor Público Titular de Cargo Efetivo, Magistrado, Ministro de Tribunal de Contas, Conselheiro de Tribunal de Contas e Membro do Ministério Público'),
    (302, u'302 - Servidor Público Ocupante de Cargo exclusivo em comissão'),
    (303, u'303 - Agente Político'),
    (305, u'305 - Servidor Público indicado para conselho ou órgão deliberativo, na condição de representante do governo, órgão ou entidade da administração pública.'),
    (306, u'306 - Servidor Público Temporário, sujeito a regime administrativo especial definido em lei própria'),
    (307, u'307 - Militar efetivo'),
    (308, u'308 - Conscrito'),
    (309, u'309 - Agente Público - Outros'),
    (401, u'401 - Dirigente Sindical - informação prestada pelo Sindicato'),
    (410, u'410 - Trabalhador cedido - informação prestada pelo Cessionário'),
    (701, u'701 - Contribuinte individual - Autônomo em geral, exceto se enquadrado em uma das demais categorias de contribuinte individual'),
    (711, u'711 - Contribuinte individual - Transportador autônomo de passageiros'),
    (712, u'712 - Contribuinte individual - Transportador autônomo de carga'),
    (721, u'721 - Contribuinte individual - Diretor não empregado, com FGTS'),
    (722, u'722 - Contribuinte individual - Diretor não empregado, sem FGTS'),
    (723, u'723 - Contribuinte individual - empresários, sócios e membro de conselho de administração ou fiscal'),
    (731, u'731 - Contribuinte individual - Cooperado que presta serviços por intermédio de Cooperativa de Trabalho'),
    (734, u'734 - Contribuinte individual - Transportador Cooperado que presta serviços por intermédio de cooperativa de trabalho'),
    (738, u'738 - Contribuinte individual - Cooperado filiado a Cooperativa de Produção'),
    (741, u'741 - Contribuinte individual - Microempreendedor Individual'),
    (751, u'751 - Contribuinte individual - magistrado classista temporário da Justiça do Trabalho ou da Justiça Eleitoral que seja aposentado de qualquer regime previdenciário'),
    (761, u'761 - Contribuinte individual - Associado eleito para direção de Cooperativa, associação ou entidade de classe de qualquer natureza ou finalidade, bem como o síndico ou administrador eleito para exercer atividade de direção condominial, desde que recebam r (...)'),
    (771, u'771 - Contribuinte individual - Membro de conselho tutelar, nos termos da Lei nº 8.069, de 13 de julho de 1990'),
    (781, u'781 - Ministro de confissão religiosa ou membro de vida consagrada, de congregação ou de ordem religiosa'),
    (901, u'901 - Estagiário'),
    (902, u'902 - Médico Residente'),
    (903, u'903 - Bolsista, nos termos da lei 8958/1994'),
    (904, u'904 - Participante de curso de formação, como etapa de concurso público, sem vínculo de emprego/estatutário'),
    (905, u'905 - Atleta não profissional em formação que receba bolsa'),
)

CHOICES_S5002_CODPAIS = (
    ('008', u'008 - Abu Dhabi'),
    ('009', u'009 - Dirce'),
    ('013', u'013 - Afeganistao'),
    ('017', u'017 - Albania, Republica Da'),
    ('020', u'020 - Alboran-Perejil,Ilhas'),
    ('023', u'023 - Alemanha'),
    ('025', u'025 - Alemanha, Republica Democratica'),
    ('031', u'031 - Burkina Faso'),
    ('037', u'037 - Andorra'),
    ('040', u'040 - Angola'),
    ('041', u'041 - Anguilla'),
    ('043', u'043 - Antigua E Barbuda'),
    ('047', u'047 - Antilhas Holandesas'),
    ('053', u'053 - Arabia Saudita'),
    ('059', u'059 - Argelia'),
    ('063', u'063 - Argentina'),
    ('064', u'064 - Armenia, Republica Da'),
    ('065', u'065 - Aruba'),
    ('069', u'069 - Australia'),
    ('072', u'072 - Austria'),
    ('073', u'073 - Azerbaijao, Republica Do'),
    ('077', u'077 - Bahamas, Ilhas'),
    ('080', u'080 - Bahrein, Ilhas'),
    ('081', u'081 - Bangladesh'),
    ('083', u'083 - Barbados'),
    ('085', u'085 - Belarus, Republica Da'),
    ('087', u'087 - Belgica'),
    ('088', u'088 - Belize'),
    ('090', u'090 - Bermudas'),
    ('093', u'093 - Mianmar (BIRMANIA)'),
    ('097', u'097 - Bolivia, Estado Plurinacional Da'),
    ('098', u'098 - Bosnia-Herzegovina (REPUBLICA Da)'),
    ('100', u'100 - Int.Z.F.Manaus'),
    ('101', u'101 - Botsuana'),
    ('105', u'105 - Brasil'),
    ('106', u'106 - Fretado P/Brasil'),
    ('108', u'108 - Brunei'),
    ('111', u'111 - Bulgaria, Republica Da'),
    ('115', u'115 - Burundi'),
    ('119', u'119 - Butao'),
    ('127', u'127 - Cabo Verde, Republica De'),
    ('131', u'131 - Cachemira'),
    ('137', u'137 - Cayman, Ilhas'),
    ('141', u'141 - Camboja'),
    ('145', u'145 - Camaroes'),
    ('149', u'149 - Canada'),
    ('150', u'150 - Jersey, Ilha Do Canal'),
    ('151', u'151 - Canarias, Ilhas'),
    ('152', u'152 - Canal,Ilhas'),
    ('153', u'153 - Cazaquistao, Republica Do'),
    ('154', u'154 - Catar'),
    ('158', u'158 - Chile'),
    ('160', u'160 - China, Republica Popular'),
    ('161', u'161 - Formosa (TAIWAN)'),
    ('163', u'163 - Chipre'),
    ('165', u'165 - Cocos(Keeling),Ilhas'),
    ('169', u'169 - Colombia'),
    ('173', u'173 - Comores, Ilhas'),
    ('177', u'177 - Congo'),
    ('183', u'183 - Cook, Ilhas'),
    ('187', u'187 - Coreia (DO Norte), Rep.Pop.Democratica'),
    ('190', u'190 - Coreia (DO Sul), Republica Da'),
    ('193', u'193 - Costa Do Marfim'),
    ('195', u'195 - Croacia (REPUBLICA Da)'),
    ('196', u'196 - Costa Rica'),
    ('198', u'198 - Coveite'),
    ('199', u'199 - Cuba'),
    ('229', u'229 - Benin'),
    ('232', u'232 - Dinamarca'),
    ('235', u'235 - Dominica,Ilha'),
    ('237', u'237 - Dubai'),
    ('239', u'239 - Equador'),
    ('240', u'240 - Egito'),
    ('243', u'243 - Eritreia'),
    ('244', u'244 - Emirados Arabes Unidos'),
    ('245', u'245 - Espanha'),
    ('246', u'246 - Eslovenia, Republica Da'),
    ('247', u'247 - Eslovaca, Republica'),
    ('249', u'249 - Estados Unidos'),
    ('251', u'251 - Estonia, Republica Da'),
    ('253', u'253 - Etiopia'),
    ('255', u'255 - Falkland (ILHAS Malvinas)'),
    ('259', u'259 - Feroe, Ilhas'),
    ('263', u'263 - Fezzan'),
    ('267', u'267 - Filipinas'),
    ('271', u'271 - Finlandia'),
    ('275', u'275 - Franca'),
    ('281', u'281 - Gabao'),
    ('285', u'285 - Gambia'),
    ('289', u'289 - Gana'),
    ('291', u'291 - Georgia, Republica Da'),
    ('293', u'293 - Gibraltar'),
    ('297', u'297 - Granada'),
    ('301', u'301 - Grecia'),
    ('305', u'305 - Groenlandia'),
    ('309', u'309 - Guadalupe'),
    ('313', u'313 - Guam'),
    ('317', u'317 - Guatemala'),
    ('325', u'325 - Guiana Francesa'),
    ('329', u'329 - Guine'),
    ('331', u'331 - Guine-Equatorial'),
    ('334', u'334 - Guine-Bissau'),
    ('337', u'337 - Guiana'),
    ('341', u'341 - Haiti'),
    ('345', u'345 - Honduras'),
    ('351', u'351 - Hong Kong'),
    ('355', u'355 - Hungria, Republica Da'),
    ('357', u'357 - Iemen'),
    ('358', u'358 - Iemem Do Sul'),
    ('359', u'359 - Man, Ilha De'),
    ('361', u'361 - India'),
    ('365', u'365 - Indonesia'),
    ('367', u'367 - Inglaterra'),
    ('369', u'369 - Iraque'),
    ('372', u'372 - Ira, Republica Islamica Do'),
    ('375', u'375 - Irlanda'),
    ('379', u'379 - Islandia'),
    ('383', u'383 - Israel'),
    ('386', u'386 - Italia'),
    ('388', u'388 - Servia E Montenegro'),
    ('391', u'391 - Jamaica'),
    ('395', u'395 - Jammu'),
    ('396', u'396 - Johnston, Ilhas'),
    ('399', u'399 - Japao'),
    ('403', u'403 - Jordania'),
    ('411', u'411 - Kiribati'),
    ('420', u'420 - Laos, Rep.Pop.Democr.Do'),
    ('423', u'423 - Lebuan,Ilhas'),
    ('426', u'426 - Lesoto'),
    ('427', u'427 - Letonia, Republica Da'),
    ('431', u'431 - Libano'),
    ('434', u'434 - Liberia'),
    ('438', u'438 - Libia'),
    ('440', u'440 - Liechtenstein'),
    ('442', u'442 - Lituania, Republica Da'),
    ('445', u'445 - Luxemburgo'),
    ('447', u'447 - Macau'),
    ('449', u'449 - Macedonia, Ant.Rep.Iugoslava'),
    ('450', u'450 - Madagascar'),
    ('452', u'452 - Ilha Da Madeira'),
    ('455', u'455 - Malasia'),
    ('458', u'458 - Malavi'),
    ('461', u'461 - Maldivas'),
    ('464', u'464 - Mali'),
    ('467', u'467 - Malta'),
    ('472', u'472 - Marianas Do Norte'),
    ('474', u'474 - Marrocos'),
    ('476', u'476 - Marshall,Ilhas'),
    ('477', u'477 - Martinica'),
    ('485', u'485 - Mauricio'),
    ('488', u'488 - Mauritania'),
    ('490', u'490 - Midway, Ilhas'),
    ('493', u'493 - Mexico'),
    ('494', u'494 - Moldavia, Republica Da'),
    ('495', u'495 - Monaco'),
    ('497', u'497 - Mongolia'),
    ('499', u'499 - Micronesia'),
    ('501', u'501 - Montserrat,Ilhas'),
    ('505', u'505 - Mocambique'),
    ('507', u'507 - Namibia'),
    ('508', u'508 - Nauru'),
    ('511', u'511 - Christmas,Ilha (NAVIDAD)'),
    ('517', u'517 - Nepal'),
    ('521', u'521 - Nicaragua'),
    ('525', u'525 - Niger'),
    ('528', u'528 - Nigeria'),
    ('531', u'531 - Niue,Ilha'),
    ('535', u'535 - Norfolk,Ilha'),
    ('538', u'538 - Noruega'),
    ('542', u'542 - Nova Caledonia'),
    ('545', u'545 - Papua Nova Guine'),
    ('548', u'548 - Nova Zelandia'),
    ('551', u'551 - Vanuatu'),
    ('556', u'556 - Oma'),
    ('563', u'563 - Pacifico,Ilhas Do (ADMINISTRACAO Dos Eua)'),
    ('566', u'566 - Pacifico,Ilhas Do (POSSESSAO Dos Eua)'),
    ('569', u'569 - Pacifico,Ilhas Do (TERRITORIO Em Fideicomisso Dos'),
    ('573', u'573 - Paises Baixos (HOLANDA)'),
    ('575', u'575 - Palau'),
    ('576', u'576 - Paquistao'),
    ('578', u'578 - Palestina'),
    ('580', u'580 - Panama'),
    ('583', u'583 - Papua Nova Guiné'),
    ('586', u'586 - Paraguai'),
    ('589', u'589 - Peru'),
    ('593', u'593 - Pitcairn,Ilha'),
    ('599', u'599 - Polinesia Francesa'),
    ('603', u'603 - Polonia, Republica Da'),
    ('607', u'607 - Portugal'),
    ('611', u'611 - Porto Rico'),
    ('623', u'623 - Quenia'),
    ('625', u'625 - Quirguiz, Republica'),
    ('628', u'628 - Reino Unido'),
    ('640', u'640 - Republica Centro-Africana'),
    ('647', u'647 - Republica Dominicana'),
    ('660', u'660 - Reuniao, Ilha'),
    ('665', u'665 - Zimbabue'),
    ('670', u'670 - Romenia'),
    ('675', u'675 - Ruanda'),
    ('676', u'676 - Russia, Federacao Da'),
    ('677', u'677 - Salomao, Ilhas'),
    ('678', u'678 - Saint Kitts E Nevis'),
    ('685', u'685 - Saara Ocidental'),
    ('687', u'687 - El Salvador'),
    ('690', u'690 - Samoa'),
    ('691', u'691 - Samoa Americana'),
    ('695', u'695 - Sao Cristovao E Neves,Ilhas'),
    ('697', u'697 - San Marino'),
    ('700', u'700 - Sao Pedro E Miquelon'),
    ('705', u'705 - Sao Vicente E Granadinas'),
    ('710', u'710 - Santa Helena'),
    ('715', u'715 - Santa Lucia'),
    ('720', u'720 - Sao Tome E Principe, Ilhas'),
    ('728', u'728 - Senegal'),
    ('731', u'731 - Seychelles'),
    ('735', u'735 - Serra Leoa'),
    ('738', u'738 - Sikkim'),
    ('741', u'741 - Cingapura'),
    ('744', u'744 - Siria, Republica Arabe Da'),
    ('748', u'748 - Somalia'),
    ('750', u'750 - Sri Lanka'),
    ('754', u'754 - Suazilandia'),
    ('756', u'756 - Africa Do Sul'),
    ('759', u'759 - Sudao'),
    ('764', u'764 - Suecia'),
    ('767', u'767 - Suica'),
    ('770', u'770 - Suriname'),
    ('772', u'772 - Tadjiquistao, Republica Do'),
    ('776', u'776 - Tailandia'),
    ('780', u'780 - Tanzania, Rep.Unida Da'),
    ('782', u'782 - Territorio Brit.Oc.Indico'),
    ('783', u'783 - Djibuti'),
    ('785', u'785 - Territorio da Alta Comissao do Pacifico Ocidental'),
    ('788', u'788 - Chade'),
    ('790', u'790 - Tchecoslovaquia'),
    ('791', u'791 - Tcheca, Republica'),
    ('795', u'795 - Timor Leste'),
    ('800', u'800 - Togo'),
    ('805', u'805 - Toquelau,Ilhas'),
    ('810', u'810 - Tonga'),
    ('815', u'815 - Trinidad E Tobago'),
    ('820', u'820 - Tunisia'),
    ('823', u'823 - Turcas E Caicos,Ilhas'),
    ('824', u'824 - Turcomenistao, Republica Do'),
    ('827', u'827 - Turquia'),
    ('828', u'828 - Tuvalu'),
    ('831', u'831 - Ucrania'),
    ('833', u'833 - Uganda'),
    ('840', u'840 - Uniao Das Republicas Socialistas Sovieticas'),
    ('845', u'845 - Uruguai'),
    ('847', u'847 - Uzbequistao, Republica Do'),
    ('848', u'848 - Vaticano, Est.Da Cidade Do'),
    ('850', u'850 - Venezuela'),
    ('855', u'855 - Vietname Norte'),
    ('858', u'858 - Vietna'),
    ('863', u'863 - Virgens,Ilhas (BRITANICAS)'),
    ('866', u'866 - Virgens,Ilhas (E.U.A.)'),
    ('870', u'870 - Fiji'),
    ('873', u'873 - Wake, Ilha'),
    ('875', u'875 - Wallis E Futuna, Ilhas'),
    ('888', u'888 - Congo, Republica Democratica Do'),
    ('890', u'890 - Zambia'),
)

CHOICES_S5002_INDNIF = (
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF'),
)

CHOICES_S5002_INDRESBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S5002_TPCR = (
    (47301, u'047301 - Renda e Proventos de Qualquer Natureza'),
    (56107, u'056107 - IRRF - Rendimento do Trabalho Assalariado no País/Ausente no Exterior a Serviço do País'),
    (56108, u'056108 - IRRF - Empregado Doméstico'),
    (56109, u'056109 - IRRF - Empregado Doméstico - 13º Sal Rescisão'),
    (56110, u'056110 - IRRF - Empregado doméstico - 13º salário'),
    (56111, u'056111 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'),
    (56112, u'056112 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário'),
    (56113, u'056113 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário rescisório'),
    (58806, u'058806 - IRRF - Rendimento do trabalho sem vínculo empregatício'),
    (61001, u'061001 - IRRF - Rendimentos relativos a prestação de serviços de transporte rodoviário internacional de carga, pagos a transportador autônomo PF residente no Paraguai'),
    ('3280-06', u'3280-06 - IRRF - Serviços Prestados por associados de cooperativas de trabalho'),
    (3533, u'3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pensão Pagos por Previdência Pública'),
    (356201, u'356201 - IRRF - Participação dos trabalhadores em Lucros ou Resultados (PLR)'),
)

class s5002basesIrrf(models.Model):
    s5002_infoirrf = models.ForeignKey('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    def evento(self): return self.s5002_infoirrf.evento()
    tpvalor = models.IntegerField()
    valor = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.tpvalor) + ' - ' + unicode(self.valor)
    #s5002_basesirrf_custom#
    #s5002_basesirrf_custom#
    class Meta:
        db_table = r's5002_basesirrf'
        managed = True
        ordering = ['s5002_infoirrf', 'tpvalor', 'valor']


class s5002idePgtoExt(models.Model):
    s5002_infoirrf = models.OneToOneField('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    def evento(self): return self.s5002_infoirrf.evento()
    codpais = models.CharField(choices=CHOICES_S5002_CODPAIS, max_length=3)
    indnif = models.IntegerField(choices=CHOICES_S5002_INDNIF)
    nifbenef = models.CharField(max_length=20, blank=True, null=True)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    complem = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
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
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.codpais) + ' - ' + unicode(self.indnif) + ' - ' + unicode(self.nifbenef) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complem) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s5002_idepgtoext_custom#
    #s5002_idepgtoext_custom#
    class Meta:
        db_table = r's5002_idepgtoext'
        managed = True
        ordering = ['s5002_infoirrf', 'codpais', 'indnif', 'nifbenef', 'dsclograd', 'nrlograd', 'complem', 'bairro', 'nmcid', 'codpostal']


class s5002infoDep(models.Model):
    s5002_evtirrfbenef = models.OneToOneField('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef')
    def evento(self): return self.s5002_evtirrfbenef.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_evtirrfbenef) + ' - ' + unicode(self.vrdeddep)
    #s5002_infodep_custom#
    #s5002_infodep_custom#
    class Meta:
        db_table = r's5002_infodep'
        managed = True
        ordering = ['s5002_evtirrfbenef', 'vrdeddep']


class s5002infoIrrf(models.Model):
    s5002_evtirrfbenef = models.ForeignKey('esocial.s5002evtIrrfBenef',
        related_name='%(class)s_s5002_evtirrfbenef')
    def evento(self): return self.s5002_evtirrfbenef.evento()
    codcateg = models.IntegerField(choices=CHOICES_S5002_CODCATEG, blank=True, null=True)
    indresbr = models.CharField(choices=CHOICES_S5002_INDRESBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_evtirrfbenef) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.indresbr)
    #s5002_infoirrf_custom#
    #s5002_infoirrf_custom#
    class Meta:
        db_table = r's5002_infoirrf'
        managed = True
        ordering = ['s5002_evtirrfbenef', 'codcateg', 'indresbr']


class s5002irrf(models.Model):
    s5002_infoirrf = models.ForeignKey('s5002infoIrrf',
        related_name='%(class)s_s5002_infoirrf')
    def evento(self): return self.s5002_infoirrf.evento()
    tpcr = models.IntegerField(choices=CHOICES_S5002_TPCR)
    vrirrfdesc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5002_infoirrf) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrirrfdesc)
    #s5002_irrf_custom#
    #s5002_irrf_custom#
    class Meta:
        db_table = r's5002_irrf'
        managed = True
        ordering = ['s5002_infoirrf', 'tpcr', 'vrirrfdesc']


#VIEWS_MODELS
