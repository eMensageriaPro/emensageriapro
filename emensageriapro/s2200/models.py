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

CHOICES_S2200_CASADOBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_CATEGORIACNH = (
    ('A', u'A - A'),
    ('AB', u'AB - AB'),
    ('AC', u'AC - AC'),
    ('AD', u'AD - AD'),
    ('AE', u'AE - AE'),
    ('B', u'B - B'),
    ('C', u'C - C'),
    ('D', u'D - D'),
    ('E', u'E - E'),
)

CHOICES_S2200_CLASSTRABESTRANG = (
    (1, u'1 - Visto permanente'),
    (10, u'10 - Beneficiado pelo acordo entre países do Mercosul'),
    (11, u'11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil'),
    (12, u'12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa'),
    (2, u'2 - Visto temporário'),
    (3, u'3 - Asilado'),
    (4, u'4 - Refugiado'),
    (5, u'5 - Solicitante de Refúgio'),
    (6, u'6 - Residente em país fronteiriço ao Brasil'),
    (7, u'7 - Deficiente físico e com mais de 51 anos'),
    (8, u'8 - Com residência provisória e anistiado, em situação irregular'),
    (9, u'9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros'),
)

CHOICES_S2200_CODMOTAFAST = (
    ('01', u'01 - Acidente/Doença do trabalho'),
    ('03', u'03 - Acidente/Doença não relacionada ao trabalho'),
    ('05', u'05 - Afastamento/licença prevista em regime próprio (estatuto), sem remuneração'),
    ('06', u'06 - Aposentadoria por invalidez'),
    ('07', u'07 - Acompanhamento - Licença para acompanhamento de membro da família enfermo'),
    ('08', u'08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, §6º, Dec. 99.684/90 (Regulamento do FGTS)'),
    ('10', u'10 - Afastamento/licença prevista em regime próprio (estatuto), com remuneração'),
    ('11', u'11 - Cárcere'),
    ('12', u'12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25°, parágrafo único - Celetistas em geral'),
    ('13', u'13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1°, inciso II, alínea 1 - Servidor público, estatutário ou não, dos órgãos ou entidades da Administração Direta ou Indireta da União, dos Estados, do Distrito Federal, dos Muni (...)'),
    ('14', u'14 - Cessão / Requisição'),
    ('15', u'15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso'),
    ('16', u'16 - Licença remunerada - Lei, liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho'),
    ('17', u'17 - Licença Maternidade - 120 dias e suas prorrogações/antecipações, inclusive para o cônjuge sobrevivente'),
    ('18', u'18 - Licença Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente'),
    ('19', u'19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso'),
    ('20', u'20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança, inclusive para o cônjuge sobrevivente'),
    ('21', u'21 - Licença não remunerada ou Sem Vencimento'),
    ('22', u'22 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, sem remuneração'),
    ('23', u'23 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, com remuneração'),
    ('24', u'24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical'),
    ('25', u'25 - Mulher vítima de violência - Lei 11.340/2006 - art. 9º §2o, II - Lei Maria da Penha'),
    ('26', u'26 - Participação de empregado no Conselho Nacional de Previdência Social-CNPS (art. 3º, Lei 8.213/1991)'),
    ('27', u'27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT'),
    ('28', u'28 - Representante Sindical - Afastamento pelo tempo que se fizer necessário, quando, na qualidade de representante de entidade sindical, estiver participando de reunião oficial de organismo internacional do qual o Brasil seja membro'),
    ('29', u'29 - Serviço Militar - Afastamento temporário para prestar serviço militar obrigatório;'),
    ('30', u'30 - Suspensão disciplinar - CLT, art. 474'),
    ('31', u'31 - Servidor Público em Disponibilidade'),
    ('33', u'33 - Licença Maternidade - de 180 dias, Lei 13.301/2016.'),
    ('34', u'34 - Inatividade do trabalhador avulso (portuário ou não portuário) por período superior a 90 dias'),
)

CHOICES_S2200_DEFAUDITIVA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFFISICA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFINTELECTUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFMENTAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEFVISUAL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEPIRRF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DEPSF = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_DIA = (
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável'),
)

CHOICES_S2200_FILHOSBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_HIPLEG = (
    (1, u'1 - Necessidade de substituição transitória de pessoal permanente'),
    (2, u'2 - Demanda complementar de serviços'),
)

CHOICES_S2200_INCTRAB = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_INDADMISSAO = (
    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Ação Fiscal'),
    (3, u'3 - Decorrente de Decisão Judicial'),
)

CHOICES_S2200_INDPROVIM = (
    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Decisão Judicial'),
)

CHOICES_S2200_INFOCOTA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2200_OPCFGTS = (
    (1, u'1 - Optante'),
    (2, u'2 - Não Optante'),
)

CHOICES_S2200_PAISRESID = (
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

CHOICES_S2200_REABREADAP = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_TMPPARC = (
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais'),
)

CHOICES_S2200_TPADMISSAO = (
    (1, u'1 - Admissão'),
    (2, u'2 - Transferência de empresa do mesmo grupo econômico'),
    (3, u'3 - Transferência de empresa consorciada ou de consórcio'),
    (4, u'4 - Transferência por motivo de sucessão, incorporação, cisão ou fusão'),
    (5, u'5 - Transferência do empregado doméstico para outro representante da mesma unidade familiar'),
)

CHOICES_S2200_TPDEP = (
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

CHOICES_S2200_TPINCLCONTR = (
    (1, u'1 - Locais sem filiais'),
    (2, u'2 - Estudo de mercado'),
    (3, u'3 - Contratação superior a 3 meses'),
)

CHOICES_S2200_TPINSC = (
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2200_TPJORNADA = (
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada'),
)

CHOICES_S2200_TPLOGRAD = (
    ('A', u'A - Área'),
    ('A', u'A - Área'),
    ('A V', u'A V - Área Verde'),
    ('A V', u'A V - Área Verde'),
    ('AC', u'AC - Acesso'),
    ('AC', u'AC - Acesso'),
    ('ACA', u'ACA - Acampamento'),
    ('ACA', u'ACA - Acampamento'),
    ('ACL', u'ACL - Acesso Local'),
    ('ACL', u'ACL - Acesso Local'),
    ('AD', u'AD - Adro'),
    ('AD', u'AD - Adro'),
    ('AE', u'AE - Área Especial'),
    ('AE', u'AE - Área Especial'),
    ('AER', u'AER - Aeroporto'),
    ('AER', u'AER - Aeroporto'),
    ('AL', u'AL - Alameda'),
    ('AL', u'AL - Alameda'),
    ('AMD', u'AMD - Avenida Marginal Direita'),
    ('AMD', u'AMD - Avenida Marginal Direita'),
    ('AME', u'AME - Avenida Marginal Esquerda'),
    ('AME', u'AME - Avenida Marginal Esquerda'),
    ('AN', u'AN - Anel Viário'),
    ('AN', u'AN - Anel Viário'),
    ('ANT', u'ANT - Antiga Estrada'),
    ('ANT', u'ANT - Antiga Estrada'),
    ('ART', u'ART - Artéria'),
    ('ART', u'ART - Artéria'),
    ('AT', u'AT - Alto'),
    ('AT', u'AT - Alto'),
    ('ATL', u'ATL - Atalho'),
    ('ATL', u'ATL - Atalho'),
    ('AV', u'AV - Avenida'),
    ('AV', u'AV - Avenida'),
    ('AVC', u'AVC - Avenida Contorno'),
    ('AVC', u'AVC - Avenida Contorno'),
    ('AVM', u'AVM - Avenida Marginal'),
    ('AVM', u'AVM - Avenida Marginal'),
    ('AVV', u'AVV - Avenida Velha'),
    ('AVV', u'AVV - Avenida Velha'),
    ('BAL', u'BAL - Balneário'),
    ('BAL', u'BAL - Balneário'),
    ('BC', u'BC - Beco'),
    ('BC', u'BC - Beco'),
    ('BCO', u'BCO - Buraco'),
    ('BCO', u'BCO - Buraco'),
    ('BEL', u'BEL - Belvedere'),
    ('BEL', u'BEL - Belvedere'),
    ('BL', u'BL - Bloco'),
    ('BL', u'BL - Bloco'),
    ('BLO', u'BLO - Balão'),
    ('BLO', u'BLO - Balão'),
    ('BLS', u'BLS - Blocos'),
    ('BLS', u'BLS - Blocos'),
    ('BLV', u'BLV - Bulevar'),
    ('BLV', u'BLV - Bulevar'),
    ('BSQ', u'BSQ - Bosque'),
    ('BSQ', u'BSQ - Bosque'),
    ('BVD', u'BVD - Boulevard'),
    ('BVD', u'BVD - Boulevard'),
    ('BX', u'BX - Baixa'),
    ('BX', u'BX - Baixa'),
    ('C', u'C - Cais'),
    ('C', u'C - Cais'),
    ('CAL', u'CAL - Calçada'),
    ('CAL', u'CAL - Calçada'),
    ('CAM', u'CAM - Caminho'),
    ('CAM', u'CAM - Caminho'),
    ('CAN', u'CAN - Canal'),
    ('CAN', u'CAN - Canal'),
    ('CH', u'CH - Chácara'),
    ('CH', u'CH - Chácara'),
    ('CHA', u'CHA - Chapadão'),
    ('CHA', u'CHA - Chapadão'),
    ('CIC', u'CIC - Ciclovia'),
    ('CIC', u'CIC - Ciclovia'),
    ('CIR', u'CIR - Circular'),
    ('CIR', u'CIR - Circular'),
    ('CJ', u'CJ - Conjunto'),
    ('CJ', u'CJ - Conjunto'),
    ('CJM', u'CJM - Conjunto Mutirão'),
    ('CJM', u'CJM - Conjunto Mutirão'),
    ('CMP', u'CMP - Complexo Viário'),
    ('CMP', u'CMP - Complexo Viário'),
    ('COL', u'COL - Colônia'),
    ('COL', u'COL - Colônia'),
    ('COM', u'COM - Comunidade'),
    ('COM', u'COM - Comunidade'),
    ('CON', u'CON - Condomínio'),
    ('CON', u'CON - Condomínio'),
    ('COR', u'COR - Corredor'),
    ('COR', u'COR - Corredor'),
    ('CPO', u'CPO - Campo'),
    ('CPO', u'CPO - Campo'),
    ('CRG', u'CRG - Córrego'),
    ('CRG', u'CRG - Córrego'),
    ('CTN', u'CTN - Contorno'),
    ('CTN', u'CTN - Contorno'),
    ('DSC', u'DSC - Descida'),
    ('DSC', u'DSC - Descida'),
    ('DSV', u'DSV - Desvio'),
    ('DSV', u'DSV - Desvio'),
    ('DT', u'DT - Distrito'),
    ('DT', u'DT - Distrito'),
    ('EB', u'EB - Entre Bloco'),
    ('EB', u'EB - Entre Bloco'),
    ('EIM', u'EIM - Estrada Intermunicipal'),
    ('EIM', u'EIM - Estrada Intermunicipal'),
    ('ENS', u'ENS - Enseada'),
    ('ENS', u'ENS - Enseada'),
    ('ENT', u'ENT - Entrada Particular'),
    ('ENT', u'ENT - Entrada Particular'),
    ('EQ', u'EQ - Entre Quadra'),
    ('EQ', u'EQ - Entre Quadra'),
    ('ESC', u'ESC - Escada'),
    ('ESC', u'ESC - Escada'),
    ('ESD', u'ESD - Escadaria'),
    ('ESD', u'ESD - Escadaria'),
    ('ESE', u'ESE - Estrada Estadual'),
    ('ESE', u'ESE - Estrada Estadual'),
    ('ESI', u'ESI - Estrada Vicinal'),
    ('ESI', u'ESI - Estrada Vicinal'),
    ('ESL', u'ESL - Estrada de Ligação'),
    ('ESL', u'ESL - Estrada de Ligação'),
    ('ESM', u'ESM - Estrada Municipal'),
    ('ESM', u'ESM - Estrada Municipal'),
    ('ESP', u'ESP - Esplanada'),
    ('ESP', u'ESP - Esplanada'),
    ('ESS', u'ESS - Estrada de Servidão'),
    ('ESS', u'ESS - Estrada de Servidão'),
    ('EST', u'EST - Estrada'),
    ('EST', u'EST - Estrada'),
    ('ESV', u'ESV - Estrada Velha'),
    ('ESV', u'ESV - Estrada Velha'),
    ('ETA', u'ETA - Estrada Antiga'),
    ('ETA', u'ETA - Estrada Antiga'),
    ('ETC', u'ETC - Estação'),
    ('ETC', u'ETC - Estação'),
    ('ETD', u'ETD - Estádio'),
    ('ETD', u'ETD - Estádio'),
    ('ETN', u'ETN - Estância'),
    ('ETN', u'ETN - Estância'),
    ('ETP', u'ETP - Estrada Particular'),
    ('ETP', u'ETP - Estrada Particular'),
    ('ETT', u'ETT - Estacionamento'),
    ('ETT', u'ETT - Estacionamento'),
    ('EVA', u'EVA - Evangélica'),
    ('EVA', u'EVA - Evangélica'),
    ('EVD', u'EVD - Elevada'),
    ('EVD', u'EVD - Elevada'),
    ('EX', u'EX - Eixo Industrial'),
    ('EX', u'EX - Eixo Industrial'),
    ('FAV', u'FAV - Favela'),
    ('FAV', u'FAV - Favela'),
    ('FAZ', u'FAZ - Fazenda'),
    ('FAZ', u'FAZ - Fazenda'),
    ('FER', u'FER - Ferrovia'),
    ('FER', u'FER - Ferrovia'),
    ('FNT', u'FNT - Fonte'),
    ('FNT', u'FNT - Fonte'),
    ('FRA', u'FRA - Feira'),
    ('FRA', u'FRA - Feira'),
    ('FTE', u'FTE - Forte'),
    ('FTE', u'FTE - Forte'),
    ('GAL', u'GAL - Galeria'),
    ('GAL', u'GAL - Galeria'),
    ('GJA', u'GJA - Granja'),
    ('GJA', u'GJA - Granja'),
    ('HAB', u'HAB - Núcleo Habitacional'),
    ('HAB', u'HAB - Núcleo Habitacional'),
    ('IA', u'IA - Ilha'),
    ('IA', u'IA - Ilha'),
    ('IND', u'IND - Indeterminado'),
    ('IND', u'IND - Indeterminado'),
    ('IOA', u'IOA - Ilhota'),
    ('IOA', u'IOA - Ilhota'),
    ('JD', u'JD - Jardim'),
    ('JD', u'JD - Jardim'),
    ('JDE', u'JDE - Jardinete'),
    ('JDE', u'JDE - Jardinete'),
    ('LD', u'LD - Ladeira'),
    ('LD', u'LD - Ladeira'),
    ('LGA', u'LGA - Lagoa'),
    ('LGA', u'LGA - Lagoa'),
    ('LGO', u'LGO - Lago'),
    ('LGO', u'LGO - Lago'),
    ('LOT', u'LOT - Loteamento'),
    ('LOT', u'LOT - Loteamento'),
    ('LRG', u'LRG - Largo'),
    ('LRG', u'LRG - Largo'),
    ('LT', u'LT - Lote'),
    ('LT', u'LT - Lote'),
    ('MER', u'MER - Mercado'),
    ('MER', u'MER - Mercado'),
    ('MNA', u'MNA - Marina'),
    ('MNA', u'MNA - Marina'),
    ('MOD', u'MOD - Modulo'),
    ('MOD', u'MOD - Modulo'),
    ('MRG', u'MRG - Projeção'),
    ('MRG', u'MRG - Projeção'),
    ('MRO', u'MRO - Morro'),
    ('MRO', u'MRO - Morro'),
    ('MTE', u'MTE - Monte'),
    ('MTE', u'MTE - Monte'),
    ('NUC', u'NUC - Núcleo'),
    ('NUC', u'NUC - Núcleo'),
    ('NUR', u'NUR - Núcleo Rural'),
    ('NUR', u'NUR - Núcleo Rural'),
    ('OUT', u'OUT - Outeiro'),
    ('OUT', u'OUT - Outeiro'),
    ('PAR', u'PAR - Paralela'),
    ('PAR', u'PAR - Paralela'),
    ('PAS', u'PAS - Passeio'),
    ('PAS', u'PAS - Passeio'),
    ('PAT', u'PAT - Pátio'),
    ('PAT', u'PAT - Pátio'),
    ('PC', u'PC - Praça'),
    ('PC', u'PC - Praça'),
    ('PCE', u'PCE - Praça de Esportes'),
    ('PCE', u'PCE - Praça de Esportes'),
    ('PDA', u'PDA - Parada'),
    ('PDA', u'PDA - Parada'),
    ('PDO', u'PDO - Paradouro'),
    ('PDO', u'PDO - Paradouro'),
    ('PNT', u'PNT - Ponta'),
    ('PNT', u'PNT - Ponta'),
    ('PR', u'PR - Praia'),
    ('PR', u'PR - Praia'),
    ('PRL', u'PRL - Prolongamento'),
    ('PRL', u'PRL - Prolongamento'),
    ('PRM', u'PRM - Parque Municipal'),
    ('PRM', u'PRM - Parque Municipal'),
    ('PRQ', u'PRQ - Parque'),
    ('PRQ', u'PRQ - Parque'),
    ('PRR', u'PRR - Parque Residencial'),
    ('PRR', u'PRR - Parque Residencial'),
    ('PSA', u'PSA - Passarela'),
    ('PSA', u'PSA - Passarela'),
    ('PSG', u'PSG - Passagem'),
    ('PSG', u'PSG - Passagem'),
    ('PSP', u'PSP - Passagem de Pedestre'),
    ('PSP', u'PSP - Passagem de Pedestre'),
    ('PSS', u'PSS - Passagem Subterrânea'),
    ('PSS', u'PSS - Passagem Subterrânea'),
    ('PTE', u'PTE - Ponte'),
    ('PTE', u'PTE - Ponte'),
    ('PTO', u'PTO - Porto'),
    ('PTO', u'PTO - Porto'),
    ('Q', u'Q - Quadra'),
    ('Q', u'Q - Quadra'),
    ('QTA', u'QTA - Quinta'),
    ('QTA', u'QTA - Quinta'),
    ('QTS', u'QTS - Quintas'),
    ('QTS', u'QTS - Quintas'),
    ('R', u'R - Rua'),
    ('R', u'R - Rua'),
    ('R I', u'R I - Rua Integração'),
    ('R I', u'R I - Rua Integração'),
    ('R L', u'R L - Rua de Ligação'),
    ('R L', u'R L - Rua de Ligação'),
    ('R P', u'R P - Rua Particular'),
    ('R P', u'R P - Rua Particular'),
    ('R V', u'R V - Rua Velha'),
    ('R V', u'R V - Rua Velha'),
    ('RAM', u'RAM - Ramal'),
    ('RAM', u'RAM - Ramal'),
    ('RCR', u'RCR - Recreio'),
    ('RCR', u'RCR - Recreio'),
    ('REC', u'REC - Recanto'),
    ('REC', u'REC - Recanto'),
    ('RER', u'RER - Retiro'),
    ('RER', u'RER - Retiro'),
    ('RES', u'RES - Residencial'),
    ('RES', u'RES - Residencial'),
    ('RET', u'RET - Reta'),
    ('RET', u'RET - Reta'),
    ('RLA', u'RLA - Ruela'),
    ('RLA', u'RLA - Ruela'),
    ('RMP', u'RMP - Rampa'),
    ('RMP', u'RMP - Rampa'),
    ('ROA', u'ROA - Rodo Anel'),
    ('ROA', u'ROA - Rodo Anel'),
    ('ROD', u'ROD - Rodovia'),
    ('ROD', u'ROD - Rodovia'),
    ('ROT', u'ROT - Rotula'),
    ('ROT', u'ROT - Rotula'),
    ('RPE', u'RPE - Rua de Pedestre'),
    ('RPE', u'RPE - Rua de Pedestre'),
    ('RPR', u'RPR - Margem'),
    ('RPR', u'RPR - Margem'),
    ('RTN', u'RTN - Retorno'),
    ('RTN', u'RTN - Retorno'),
    ('RTT', u'RTT - Rotatória'),
    ('RTT', u'RTT - Rotatória'),
    ('SEG', u'SEG - Segunda Avenida'),
    ('SEG', u'SEG - Segunda Avenida'),
    ('SIT', u'SIT - Sitio'),
    ('SIT', u'SIT - Sitio'),
    ('SRV', u'SRV - Servidão'),
    ('SRV', u'SRV - Servidão'),
    ('ST', u'ST - Setor'),
    ('ST', u'ST - Setor'),
    ('SUB', u'SUB - Subida'),
    ('SUB', u'SUB - Subida'),
    ('TCH', u'TCH - Trincheira'),
    ('TCH', u'TCH - Trincheira'),
    ('TER', u'TER - Terminal'),
    ('TER', u'TER - Terminal'),
    ('TR', u'TR - Trecho'),
    ('TR', u'TR - Trecho'),
    ('TRV', u'TRV - Trevo'),
    ('TRV', u'TRV - Trevo'),
    ('TUN', u'TUN - Túnel'),
    ('TUN', u'TUN - Túnel'),
    ('TV', u'TV - Travessa'),
    ('TV', u'TV - Travessa'),
    ('TVP', u'TVP - Travessa Particular'),
    ('TVP', u'TVP - Travessa Particular'),
    ('TVV', u'TVV - Travessa Velha'),
    ('TVV', u'TVV - Travessa Velha'),
    ('UNI', u'UNI - Unidade'),
    ('UNI', u'UNI - Unidade'),
    ('V', u'V - Via'),
    ('V', u'V - Via'),
    ('V C', u'V C - Via Coletora'),
    ('V C', u'V C - Via Coletora'),
    ('V L', u'V L - Via Local'),
    ('V L', u'V L - Via Local'),
    ('V-E', u'V-E - Via Expressa'),
    ('V-E', u'V-E - Via Expressa'),
    ('VAC', u'VAC - Via de Acesso'),
    ('VAC', u'VAC - Via de Acesso'),
    ('VAL', u'VAL - Vala'),
    ('VAL', u'VAL - Vala'),
    ('VCO', u'VCO - Via Costeira'),
    ('VCO', u'VCO - Via Costeira'),
    ('VD', u'VD - Viaduto'),
    ('VD', u'VD - Viaduto'),
    ('VER', u'VER - Vereda'),
    ('VER', u'VER - Vereda'),
    ('VEV', u'VEV - Via Elevado'),
    ('VEV', u'VEV - Via Elevado'),
    ('VL', u'VL - Vila'),
    ('VL', u'VL - Vila'),
    ('VLA', u'VLA - Viela'),
    ('VLA', u'VLA - Viela'),
    ('VLE', u'VLE - Vale'),
    ('VLE', u'VLE - Vale'),
    ('VLT', u'VLT - Via Litorânea'),
    ('VLT', u'VLT - Via Litorânea'),
    ('VPE', u'VPE - Via de Pedestre'),
    ('VPE', u'VPE - Via de Pedestre'),
    ('VRT', u'VRT - Variante'),
    ('VRT', u'VRT - Variante'),
    ('ZIG', u'ZIG - Zigue-Zague'),
    ('ZIG', u'ZIG - Zigue-Zague'),
)

CHOICES_S2200_TPPLANRP = (
    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro'),
)

CHOICES_S2200_TPPROV = (
    (1, u'1 - Nomeação em cargo efetivo'),
    (2, u'2 - Nomeação em cargo em comissão'),
    (3, u'3 - Incorporação (militar)'),
    (4, u'4 - Matrícula (militar)'),
    (5, u'5 - Reinclusão (militar)'),
    (6, u'6 - Diplomação'),
    (99, u'99 - Outros não relacionados acima'),
)

CHOICES_S2200_TPREGJOR = (
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT'),
)

CHOICES_S2200_TRABAPOSENT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

class s2200CNH(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nrregcnh = models.CharField(max_length=12)
    dtexped = models.DateField(blank=True, null=True)
    ufcnh = models.CharField(choices=ESTADOS, max_length=2)
    dtvalid = models.DateField()
    dtprihab = models.DateField(blank=True, null=True)
    categoriacnh = models.CharField(choices=CHOICES_S2200_CATEGORIACNH, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nrregcnh) + ' - ' + unicode(self.dtexped) + ' - ' + unicode(self.ufcnh) + ' - ' + unicode(self.dtvalid) + ' - ' + unicode(self.dtprihab) + ' - ' + unicode(self.categoriacnh)
    #s2200_cnh_custom#
    #s2200_cnh_custom#
    class Meta:
        db_table = r's2200_cnh'
        managed = True
        ordering = ['s2200_documentos', 'nrregcnh', 'dtexped', 'ufcnh', 'dtvalid', 'dtprihab', 'categoriacnh']


class s2200CTPS(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nrctps = models.CharField(max_length=11)
    seriectps = models.CharField(max_length=5)
    ufctps = models.CharField(choices=ESTADOS, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nrctps) + ' - ' + unicode(self.seriectps) + ' - ' + unicode(self.ufctps)
    #s2200_ctps_custom#
    #s2200_ctps_custom#
    class Meta:
        db_table = r's2200_ctps'
        managed = True
        ordering = ['s2200_documentos', 'nrctps', 'seriectps', 'ufctps']


class s2200OC(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nroc = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    dtvalid = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nroc) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped) + ' - ' + unicode(self.dtvalid)
    #s2200_oc_custom#
    #s2200_oc_custom#
    class Meta:
        db_table = r's2200_oc'
        managed = True
        ordering = ['s2200_documentos', 'nroc', 'orgaoemissor', 'dtexped', 'dtvalid']


class s2200RG(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nrrg = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nrrg) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2200_rg_custom#
    #s2200_rg_custom#
    class Meta:
        db_table = r's2200_rg'
        managed = True
        ordering = ['s2200_documentos', 'nrrg', 'orgaoemissor', 'dtexped']


class s2200RIC(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nrric = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nrric) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2200_ric_custom#
    #s2200_ric_custom#
    class Meta:
        db_table = r's2200_ric'
        managed = True
        ordering = ['s2200_documentos', 'nrric', 'orgaoemissor', 'dtexped']


class s2200RNE(models.Model):
    s2200_documentos = models.OneToOneField('s2200documentos',
        related_name='%(class)s_s2200_documentos')
    def evento(self): return self.s2200_documentos.evento()
    nrrne = models.CharField(max_length=14)
    orgaoemissor = models.CharField(max_length=20)
    dtexped = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_documentos) + ' - ' + unicode(self.nrrne) + ' - ' + unicode(self.orgaoemissor) + ' - ' + unicode(self.dtexped)
    #s2200_rne_custom#
    #s2200_rne_custom#
    class Meta:
        db_table = r's2200_rne'
        managed = True
        ordering = ['s2200_documentos', 'nrrne', 'orgaoemissor', 'dtexped']


class s2200afastamento(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtiniafast = models.DateField()
    codmotafast = models.CharField(choices=CHOICES_S2200_CODMOTAFAST, max_length=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtiniafast) + ' - ' + unicode(self.codmotafast)
    #s2200_afastamento_custom#
    #s2200_afastamento_custom#
    class Meta:
        db_table = r's2200_afastamento'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtiniafast', 'codmotafast']


class s2200alvaraJudicial(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.nrprocjud)
    #s2200_alvarajudicial_custom#
    #s2200_alvarajudicial_custom#
    class Meta:
        db_table = r's2200_alvarajudicial'
        managed = True
        ordering = ['s2200_evtadmissao', 'nrprocjud']


class s2200aposentadoria(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    trabaposent = models.CharField(choices=CHOICES_S2200_TRABAPOSENT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.trabaposent)
    #s2200_aposentadoria_custom#
    #s2200_aposentadoria_custom#
    class Meta:
        db_table = r's2200_aposentadoria'
        managed = True
        ordering = ['s2200_evtadmissao', 'trabaposent']


class s2200aprend(models.Model):
    s2200_infoceletista = models.OneToOneField('s2200infoCeletista',
        related_name='%(class)s_s2200_infoceletista')
    def evento(self): return self.s2200_infoceletista.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoceletista) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_aprend_custom#
    #s2200_aprend_custom#
    class Meta:
        db_table = r's2200_aprend'
        managed = True
        ordering = ['s2200_infoceletista', 'tpinsc', 'nrinsc']


class s2200brasil(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tplograd = models.CharField(choices=CHOICES_S2200_TPLOGRAD, max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2200_brasil_custom#
    #s2200_brasil_custom#
    class Meta:
        db_table = r's2200_brasil'
        managed = True
        ordering = ['s2200_evtadmissao', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']


class s2200contato(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    foneprinc = models.CharField(max_length=13, blank=True, null=True)
    fonealternat = models.CharField(max_length=13, blank=True, null=True)
    emailprinc = models.CharField(max_length=60, blank=True, null=True)
    emailalternat = models.CharField(max_length=60, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.foneprinc) + ' - ' + unicode(self.fonealternat) + ' - ' + unicode(self.emailprinc) + ' - ' + unicode(self.emailalternat)
    #s2200_contato_custom#
    #s2200_contato_custom#
    class Meta:
        db_table = r's2200_contato'
        managed = True
        ordering = ['s2200_evtadmissao', 'foneprinc', 'fonealternat', 'emailprinc', 'emailalternat']


class s2200dependente(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tpdep = models.CharField(choices=CHOICES_S2200_TPDEP, max_length=2)
    nmdep = models.CharField(max_length=70)
    dtnascto = models.DateField()
    cpfdep = models.CharField(max_length=11, blank=True, null=True)
    depirrf = models.CharField(choices=CHOICES_S2200_DEPIRRF, max_length=1)
    depsf = models.CharField(choices=CHOICES_S2200_DEPSF, max_length=1)
    inctrab = models.CharField(choices=CHOICES_S2200_INCTRAB, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpdep) + ' - ' + unicode(self.nmdep) + ' - ' + unicode(self.dtnascto) + ' - ' + unicode(self.cpfdep) + ' - ' + unicode(self.depirrf) + ' - ' + unicode(self.depsf) + ' - ' + unicode(self.inctrab)
    #s2200_dependente_custom#
    #s2200_dependente_custom#
    class Meta:
        db_table = r's2200_dependente'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpdep', 'nmdep', 'dtnascto', 'cpfdep', 'depirrf', 'depsf', 'inctrab']


class s2200desligamento(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtdeslig = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtdeslig)
    #s2200_desligamento_custom#
    #s2200_desligamento_custom#
    class Meta:
        db_table = r's2200_desligamento'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtdeslig']


class s2200documentos(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao)
    #s2200_documentos_custom#
    #s2200_documentos_custom#
    class Meta:
        db_table = r's2200_documentos'
        managed = True
        ordering = ['s2200_evtadmissao']


class s2200exterior(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    paisresid = models.CharField(choices=CHOICES_S2200_PAISRESID, max_length=3)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.paisresid) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.nmcid) + ' - ' + unicode(self.codpostal)
    #s2200_exterior_custom#
    #s2200_exterior_custom#
    class Meta:
        db_table = r's2200_exterior'
        managed = True
        ordering = ['s2200_evtadmissao', 'paisresid', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'nmcid', 'codpostal']


class s2200filiacaoSindical(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cnpjsindtrab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cnpjsindtrab)
    #s2200_filiacaosindical_custom#
    #s2200_filiacaosindical_custom#
    class Meta:
        db_table = r's2200_filiacaosindical'
        managed = True
        ordering = ['s2200_evtadmissao', 'cnpjsindtrab']


class s2200horContratual(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, max_length=4, blank=True, null=True)
    tpjornada = models.IntegerField(choices=CHOICES_S2200_TPJORNADA)
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True)
    tmpparc = models.IntegerField(choices=CHOICES_S2200_TMPPARC)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.qtdhrssem) + ' - ' + unicode(self.tpjornada) + ' - ' + unicode(self.dsctpjorn) + ' - ' + unicode(self.tmpparc)
    #s2200_horcontratual_custom#
    #s2200_horcontratual_custom#
    class Meta:
        db_table = r's2200_horcontratual'
        managed = True
        ordering = ['s2200_evtadmissao', 'qtdhrssem', 'tpjornada', 'dsctpjorn', 'tmpparc']


class s2200horario(models.Model):
    s2200_horcontratual = models.ForeignKey('s2200horContratual',
        related_name='%(class)s_s2200_horcontratual')
    def evento(self): return self.s2200_horcontratual.evento()
    dia = models.IntegerField(choices=CHOICES_S2200_DIA)
    codhorcontrat = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_horcontratual) + ' - ' + unicode(self.dia) + ' - ' + unicode(self.codhorcontrat)
    #s2200_horario_custom#
    #s2200_horario_custom#
    class Meta:
        db_table = r's2200_horario'
        managed = True
        ordering = ['s2200_horcontratual', 'dia', 'codhorcontrat']


class s2200ideEstabVinc(models.Model):
    s2200_trabtemporario = models.OneToOneField('s2200trabTemporario',
        related_name='%(class)s_s2200_trabtemporario')
    def evento(self): return self.s2200_trabtemporario.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_trabtemporario) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_ideestabvinc_custom#
    #s2200_ideestabvinc_custom#
    class Meta:
        db_table = r's2200_ideestabvinc'
        managed = True
        ordering = ['s2200_trabtemporario', 'tpinsc', 'nrinsc']


class s2200ideTrabSubstituido(models.Model):
    s2200_trabtemporario = models.ForeignKey('s2200trabTemporario',
        related_name='%(class)s_s2200_trabtemporario')
    def evento(self): return self.s2200_trabtemporario.evento()
    cpftrabsubst = models.CharField(max_length=11)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_trabtemporario) + ' - ' + unicode(self.cpftrabsubst)
    #s2200_idetrabsubstituido_custom#
    #s2200_idetrabsubstituido_custom#
    class Meta:
        db_table = r's2200_idetrabsubstituido'
        managed = True
        ordering = ['s2200_trabtemporario', 'cpftrabsubst']


class s2200infoCeletista(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtadm = models.DateField()
    tpadmissao = models.IntegerField(choices=CHOICES_S2200_TPADMISSAO)
    indadmissao = models.IntegerField(choices=CHOICES_S2200_INDADMISSAO)
    tpregjor = models.IntegerField(choices=CHOICES_S2200_TPREGJOR)
    natatividade = models.IntegerField(choices=CHOICES_S2200_NATATIVIDADE)
    dtbase = models.IntegerField(blank=True, null=True)
    cnpjsindcategprof = models.CharField(max_length=14)
    opcfgts = models.IntegerField(choices=CHOICES_S2200_OPCFGTS)
    dtopcfgts = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtadm) + ' - ' + unicode(self.tpadmissao) + ' - ' + unicode(self.indadmissao) + ' - ' + unicode(self.tpregjor) + ' - ' + unicode(self.natatividade) + ' - ' + unicode(self.dtbase) + ' - ' + unicode(self.cnpjsindcategprof) + ' - ' + unicode(self.opcfgts) + ' - ' + unicode(self.dtopcfgts)
    #s2200_infoceletista_custom#
    #s2200_infoceletista_custom#
    class Meta:
        db_table = r's2200_infoceletista'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtadm', 'tpadmissao', 'indadmissao', 'tpregjor', 'natatividade', 'dtbase', 'cnpjsindcategprof', 'opcfgts', 'dtopcfgts']


class s2200infoDecJud(models.Model):
    s2200_infoestatutario = models.OneToOneField('s2200infoEstatutario',
        related_name='%(class)s_s2200_infoestatutario')
    def evento(self): return self.s2200_infoestatutario.evento()
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoestatutario) + ' - ' + unicode(self.nrprocjud)
    #s2200_infodecjud_custom#
    #s2200_infodecjud_custom#
    class Meta:
        db_table = r's2200_infodecjud'
        managed = True
        ordering = ['s2200_infoestatutario', 'nrprocjud']


class s2200infoDeficiencia(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    deffisica = models.CharField(choices=CHOICES_S2200_DEFFISICA, max_length=1)
    defvisual = models.CharField(choices=CHOICES_S2200_DEFVISUAL, max_length=1)
    defauditiva = models.CharField(choices=CHOICES_S2200_DEFAUDITIVA, max_length=1)
    defmental = models.CharField(choices=CHOICES_S2200_DEFMENTAL, max_length=1)
    defintelectual = models.CharField(choices=CHOICES_S2200_DEFINTELECTUAL, max_length=1)
    reabreadap = models.CharField(choices=CHOICES_S2200_REABREADAP, max_length=1)
    infocota = models.CharField(choices=CHOICES_S2200_INFOCOTA, max_length=1)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.deffisica) + ' - ' + unicode(self.defvisual) + ' - ' + unicode(self.defauditiva) + ' - ' + unicode(self.defmental) + ' - ' + unicode(self.defintelectual) + ' - ' + unicode(self.reabreadap) + ' - ' + unicode(self.infocota) + ' - ' + unicode(self.observacao)
    #s2200_infodeficiencia_custom#
    #s2200_infodeficiencia_custom#
    class Meta:
        db_table = r's2200_infodeficiencia'
        managed = True
        ordering = ['s2200_evtadmissao', 'deffisica', 'defvisual', 'defauditiva', 'defmental', 'defintelectual', 'reabreadap', 'infocota', 'observacao']


class s2200infoEstatutario(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    indprovim = models.IntegerField(choices=CHOICES_S2200_INDPROVIM)
    tpprov = models.IntegerField(choices=CHOICES_S2200_TPPROV)
    dtnomeacao = models.DateField()
    dtposse = models.DateField()
    dtexercicio = models.DateField()
    tpplanrp = models.IntegerField(choices=CHOICES_S2200_TPPLANRP, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.indprovim) + ' - ' + unicode(self.tpprov) + ' - ' + unicode(self.dtnomeacao) + ' - ' + unicode(self.dtposse) + ' - ' + unicode(self.dtexercicio) + ' - ' + unicode(self.tpplanrp)
    #s2200_infoestatutario_custom#
    #s2200_infoestatutario_custom#
    class Meta:
        db_table = r's2200_infoestatutario'
        managed = True
        ordering = ['s2200_evtadmissao', 'indprovim', 'tpprov', 'dtnomeacao', 'dtposse', 'dtexercicio', 'tpplanrp']


class s2200localTrabDom(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tplograd = models.CharField(choices=CHOICES_S2200_TPLOGRAD, max_length=4)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
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
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2200_localtrabdom_custom#
    #s2200_localtrabdom_custom#
    class Meta:
        db_table = r's2200_localtrabdom'
        managed = True
        ordering = ['s2200_evtadmissao', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']


class s2200localTrabGeral(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    desccomp = models.CharField(max_length=80, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.desccomp)
    #s2200_localtrabgeral_custom#
    #s2200_localtrabgeral_custom#
    class Meta:
        db_table = r's2200_localtrabgeral'
        managed = True
        ordering = ['s2200_evtadmissao', 'tpinsc', 'nrinsc', 'desccomp']


class s2200observacoes(models.Model):
    s2200_evtadmissao = models.ForeignKey('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.observacao)
    #s2200_observacoes_custom#
    #s2200_observacoes_custom#
    class Meta:
        db_table = r's2200_observacoes'
        managed = True
        ordering = ['s2200_evtadmissao', 'observacao']


class s2200sucessaoVinc(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cnpjempregant = models.CharField(max_length=14)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dttransf = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cnpjempregant) + ' - ' + unicode(self.matricant) + ' - ' + unicode(self.dttransf) + ' - ' + unicode(self.observacao)
    #s2200_sucessaovinc_custom#
    #s2200_sucessaovinc_custom#
    class Meta:
        db_table = r's2200_sucessaovinc'
        managed = True
        ordering = ['s2200_evtadmissao', 'cnpjempregant', 'matricant', 'dttransf', 'observacao']


class s2200trabEstrangeiro(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    dtchegada = models.DateField(blank=True, null=True)
    classtrabestrang = models.IntegerField(choices=CHOICES_S2200_CLASSTRABESTRANG)
    casadobr = models.CharField(choices=CHOICES_S2200_CASADOBR, max_length=1)
    filhosbr = models.CharField(choices=CHOICES_S2200_FILHOSBR, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.dtchegada) + ' - ' + unicode(self.classtrabestrang) + ' - ' + unicode(self.casadobr) + ' - ' + unicode(self.filhosbr)
    #s2200_trabestrangeiro_custom#
    #s2200_trabestrangeiro_custom#
    class Meta:
        db_table = r's2200_trabestrangeiro'
        managed = True
        ordering = ['s2200_evtadmissao', 'dtchegada', 'classtrabestrang', 'casadobr', 'filhosbr']


class s2200trabTemporario(models.Model):
    s2200_infoceletista = models.OneToOneField('s2200infoCeletista',
        related_name='%(class)s_s2200_infoceletista')
    def evento(self): return self.s2200_infoceletista.evento()
    hipleg = models.IntegerField(choices=CHOICES_S2200_HIPLEG)
    justcontr = models.CharField(max_length=999)
    tpinclcontr = models.IntegerField(choices=CHOICES_S2200_TPINCLCONTR)
    tpinsc = models.IntegerField(choices=CHOICES_S2200_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_infoceletista) + ' - ' + unicode(self.hipleg) + ' - ' + unicode(self.justcontr) + ' - ' + unicode(self.tpinclcontr) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2200_trabtemporario_custom#
    #s2200_trabtemporario_custom#
    class Meta:
        db_table = r's2200_trabtemporario'
        managed = True
        ordering = ['s2200_infoceletista', 'hipleg', 'justcontr', 'tpinclcontr', 'tpinsc', 'nrinsc']


class s2200transfDom(models.Model):
    s2200_evtadmissao = models.OneToOneField('esocial.s2200evtAdmissao',
        related_name='%(class)s_s2200_evtadmissao')
    def evento(self): return self.s2200_evtadmissao.evento()
    cpfsubstituido = models.CharField(max_length=11)
    matricant = models.CharField(max_length=30, blank=True, null=True)
    dttransf = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2200_evtadmissao) + ' - ' + unicode(self.cpfsubstituido) + ' - ' + unicode(self.matricant) + ' - ' + unicode(self.dttransf)
    #s2200_transfdom_custom#
    #s2200_transfdom_custom#
    class Meta:
        db_table = r's2200_transfdom'
        managed = True
        ordering = ['s2200_evtadmissao', 'cpfsubstituido', 'matricant', 'dttransf']


#VIEWS_MODELS
