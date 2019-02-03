#coding: utf-8

"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from django.apps import apps
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S1210_DETPGTOANT_TPBCIRRF = (
    ('11', u'11 - Remuneração Mensal'),
    ('12', u'12 - 13o Salário'),
    ('13', u'13 - Férias'),
    ('14', u'14 - PLR'),
    ('15', u'15 - Rendimentos Recebidos Acumuladamente - RRA'),
    ('31', u'31 - Retenções do IRRF efetuadas sobre: Remuneração mensal'),
    ('32', u'32 - Retenções do IRRF efetuadas sobre: 13o Salário'),
    ('33', u'33 - Retenções do IRRF efetuadas sobre: Férias'),
    ('34', u'34 - Retenções do IRRF efetuadas sobre: PLR'),
    ('35', u'35 - Retenções do IRRF efetuadas sobre: RRA'),
    ('41', u'41 - Deduções da base de cálculo do IRRF: Previdência Social Oficial - PSO - Remuner. Mensal'),
    ('42', u'42 - Deduções da base de cálculo do IRRF: PSO - 13° salário'),
    ('43', u'43 - Deduções da base de cálculo do IRRF: PSO - Férias'),
    ('44', u'44 - Deduções da base de cálculo do IRRF: PSO - RRA'),
    ('46', u'46 - Deduções da base de cálculo do IRRF: Previdência Privada - salário mensal'),
    ('47', u'47 - Deduções da base de cálculo do IRRF: Previdência Privada - 13° salário'),
    ('51', u'51 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Remuneração Mensal'),
    ('52', u'52 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - 13° salário'),
    ('53', u'53 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - Férias'),
    ('54', u'54 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - PLR'),
    ('55', u'55 - Deduções da base de cálculo do IRRF: Pensão Alimentícia - RRA'),
    ('61', u'61 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - Remuneração Mensal'),
    ('62', u'62 - Deduções da base de cálculo do IRRF: Fundo de Aposentadoria Programada Individual - FAPI - 13° salário'),
    ('63', u'63 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - Remuneração Mensal'),
    ('64', u'64 - Deduções da base de cálculo do IRRF: Fundação de Previdência Complementar do Servidor Público - Funpresp - 13° salário'),
    ('70', u'70 - Isenções do IRRF: Parcela Isenta 65 anos - Remuneração Mensal'),
    ('71', u'71 - Isenções do IRRF: Parcela Isenta 65 anos - 13° salário'),
    ('72', u'72 - Isenções do IRRF: Diárias'),
    ('73', u'73 - Isenções do IRRF: Ajuda de Custo'),
    ('74', u'74 - Isenções do IRRF: Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho'),
    ('75', u'75 - Isenções do IRRF: Abono pecuniário'),
    ('76', u'76 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - Remuneração Mensal'),
    ('77', u'77 - Isenções do IRRF: Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço - 13° salário'),
    ('78', u'78 - Isenções do IRRF: Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e alugueis'),
    ('79', u'79 - Isenções do IRRF: Outras isenções (o nome da rubrica deve ser claro para identificação da natureza dos valores)'),
    ('81', u'81 - Demandas Judiciais: Depósito Judicial'),
    ('82', u'82 - Demandas Judiciais: Compensação Judicial do ano calendário'),
    ('83', u'83 - Demandas Judiciais: Compensação Judicial de anos anteriores'),
    ('91', u'91 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Remuneração Mensal'),
    ('92', u'92 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: 13o Salário'),
    ('93', u'93 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: Férias'),
    ('94', u'94 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: PLR'),
    ('95', u'95 - Incidência Suspensa decorrente de decisão judicial, relativas a base de cálculo do IRRF sobre: RRA'),
)

CHOICES_S1210_DETPGTOBENPR_INDPGTOTT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_DETPGTOFL_INDPGTOTT = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_IDEPGTOEXT_CODPAIS = (
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

CHOICES_S1210_IDEPGTOEXT_INDNIF = (
    (1, u'1 - Beneficiário com NIF'),
    (2, u'2 - Beneficiário dispensado do NIF'),
    (3, u'3 - País não exige NIF'),
)

CHOICES_S1210_INDRESBR = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1210_TPPGTO = (
    (1, u'1 - Pagamento de remuneração, conforme apurado em {dmDev} do S-1200'),
    (2, u'2 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2299'),
    (3, u'3 - Pagamento de verbas rescisórias conforme apurado em {dmDev} do S- 2399'),
    (5, u'5 - Pagamento de remuneração conforme apurado em {dmDev} do S-1202'),
    (6, u'6 - Pagamento de Benefícios Previdenciários, conforme apurado em {dmDev} do S-1207'),
    (7, u'7 - Recibo de férias'),
    (9, u'9 - Pagamento relativo a competências anteriores ao início de obrigatoriedade dos eventos periódicos para o contribuinte'),
)

class s1210deps(SoftDeletionModel):
    s1210_evtpgtos = models.OneToOneField('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos')
    def evento(self): return self.s1210_evtpgtos.evento()
    vrdeddep = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.vrdeddep)
    #s1210_deps_custom#
    class Meta:
        db_table = r's1210_deps'
        managed = True # s1210_deps #
        ordering = ['s1210_evtpgtos', 'vrdeddep']



class s1210depsSerializer(ModelSerializer):
    class Meta:
        model = s1210deps
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoAnt(SoftDeletionModel):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    def evento(self): return self.s1210_infopgto.evento()
    codcateg = models.TextField(max_length=3)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg)
    #s1210_detpgtoant_custom#
    class Meta:
        db_table = r's1210_detpgtoant'
        managed = True # s1210_detpgtoant #
        ordering = ['s1210_infopgto', 'codcateg']



class s1210detPgtoAntSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoAnt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoAntinfoPgtoAnt(SoftDeletionModel):
    s1210_detpgtoant = models.ForeignKey('s1210detPgtoAnt',
        related_name='%(class)s_s1210_detpgtoant')
    def evento(self): return self.s1210_detpgtoant.evento()
    tpbcirrf = models.CharField(choices=CHOICES_S1210_DETPGTOANT_TPBCIRRF, max_length=2)
    vrbcirrf = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtoant) + ' - ' + unicode(self.tpbcirrf) + ' - ' + unicode(self.vrbcirrf)
    #s1210_detpgtoant_infopgtoant_custom#
    class Meta:
        db_table = r's1210_detpgtoant_infopgtoant'
        managed = True # s1210_detpgtoant_infopgtoant #
        ordering = ['s1210_detpgtoant', 'tpbcirrf', 'vrbcirrf']



class s1210detPgtoAntinfoPgtoAntSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoAntinfoPgtoAnt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoBenPr(SoftDeletionModel):
    s1210_infopgto = models.OneToOneField('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    def evento(self): return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7)
    idedmdev = models.CharField(max_length=30)
    indpgtott = models.CharField(choices=CHOICES_S1210_DETPGTOBENPR_INDPGTOTT, max_length=1)
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.perref) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq)
    #s1210_detpgtobenpr_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr'
        managed = True # s1210_detpgtobenpr #
        ordering = ['s1210_infopgto', 'perref', 'idedmdev', 'indpgtott', 'vrliq']



class s1210detPgtoBenPrSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPr
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoBenPrinfoPgtoParc(SoftDeletionModel):
    s1210_detpgtobenpr = models.ForeignKey('s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr')
    def evento(self): return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtobenpr_infopgtoparc_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr_infopgtoparc'
        managed = True # s1210_detpgtobenpr_infopgtoparc #
        ordering = ['s1210_detpgtobenpr', 'codrubr', 'idetabrubr', 'vrrubr']



class s1210detPgtoBenPrinfoPgtoParcSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPrinfoPgtoParc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoBenPrretPgtoTot(SoftDeletionModel):
    s1210_detpgtobenpr = models.ForeignKey('s1210detPgtoBenPr',
        related_name='%(class)s_s1210_detpgtobenpr')
    def evento(self): return self.s1210_detpgtobenpr.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtobenpr) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtobenpr_retpgtotot_custom#
    class Meta:
        db_table = r's1210_detpgtobenpr_retpgtotot'
        managed = True # s1210_detpgtobenpr_retpgtotot #
        ordering = ['s1210_detpgtobenpr', 'codrubr', 'idetabrubr', 'vrrubr']



class s1210detPgtoBenPrretPgtoTotSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoBenPrretPgtoTot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFer(SoftDeletionModel):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    def evento(self): return self.s1210_infopgto.evento()
    codcateg = models.TextField(max_length=3)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    dtinigoz = models.DateField()
    qtdias = models.IntegerField()
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codcateg) + ' - ' + unicode(self.dtinigoz) + ' - ' + unicode(self.qtdias) + ' - ' + unicode(self.vrliq)
    #s1210_detpgtofer_custom#
    class Meta:
        db_table = r's1210_detpgtofer'
        managed = True # s1210_detpgtofer #
        ordering = ['s1210_infopgto', 'codcateg', 'dtinigoz', 'qtdias', 'vrliq']



class s1210detPgtoFerSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFerdetRubrFer(SoftDeletionModel):
    s1210_detpgtofer = models.ForeignKey('s1210detPgtoFer',
        related_name='%(class)s_s1210_detpgtofer')
    def evento(self): return self.s1210_detpgtofer.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofer) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofer_detrubrfer_custom#
    class Meta:
        db_table = r's1210_detpgtofer_detrubrfer'
        managed = True # s1210_detpgtofer_detrubrfer #
        ordering = ['s1210_detpgtofer', 'codrubr', 'idetabrubr', 'vrrubr']



class s1210detPgtoFerdetRubrFerSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFerdetRubrFer
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFerpenAlim(SoftDeletionModel):
    s1210_detpgtofer_detrubrfer = models.ForeignKey('s1210detPgtoFerdetRubrFer',
        related_name='%(class)s_s1210_detpgtofer_detrubrfer')
    def evento(self): return self.s1210_detpgtofer_detrubrfer.evento()
    cpfbenef = models.CharField(max_length=11)
    dtnasctobenef = models.DateField(blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofer_detrubrfer) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)
    #s1210_detpgtofer_penalim_custom#
    class Meta:
        db_table = r's1210_detpgtofer_penalim'
        managed = True # s1210_detpgtofer_penalim #
        ordering = ['s1210_detpgtofer_detrubrfer', 'cpfbenef', 'nmbenefic', 'vlrpensao']



class s1210detPgtoFerpenAlimSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFerpenAlim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFl(SoftDeletionModel):
    s1210_infopgto = models.ForeignKey('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    def evento(self): return self.s1210_infopgto.evento()
    perref = models.CharField(max_length=7, blank=True, null=True)
    idedmdev = models.CharField(max_length=30)
    indpgtott = models.CharField(choices=CHOICES_S1210_DETPGTOFL_INDPGTOTT, max_length=1)
    vrliq = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    nrrecarq = models.CharField(max_length=40, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.idedmdev) + ' - ' + unicode(self.indpgtott) + ' - ' + unicode(self.vrliq)
    #s1210_detpgtofl_custom#
    class Meta:
        db_table = r's1210_detpgtofl'
        managed = True # s1210_detpgtofl #
        ordering = ['s1210_infopgto', 'idedmdev', 'indpgtott', 'vrliq']



class s1210detPgtoFlSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFlinfoPgtoParc(SoftDeletionModel):
    s1210_detpgtofl = models.ForeignKey('s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl')
    def evento(self): return self.s1210_detpgtofl.evento()
    matricula = models.CharField(max_length=30, blank=True, null=True)
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofl_infopgtoparc_custom#
    class Meta:
        db_table = r's1210_detpgtofl_infopgtoparc'
        managed = True # s1210_detpgtofl_infopgtoparc #
        ordering = ['s1210_detpgtofl', 'codrubr', 'idetabrubr', 'vrrubr']



class s1210detPgtoFlinfoPgtoParcSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlinfoPgtoParc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFlpenAlim(SoftDeletionModel):
    s1210_detpgtofl_retpgtotot = models.ForeignKey('s1210detPgtoFlretPgtoTot',
        related_name='%(class)s_s1210_detpgtofl_retpgtotot')
    def evento(self): return self.s1210_detpgtofl_retpgtotot.evento()
    cpfbenef = models.CharField(max_length=11)
    dtnasctobenef = models.DateField(blank=True, null=True)
    nmbenefic = models.CharField(max_length=70)
    vlrpensao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl_retpgtotot) + ' - ' + unicode(self.cpfbenef) + ' - ' + unicode(self.nmbenefic) + ' - ' + unicode(self.vlrpensao)
    #s1210_detpgtofl_penalim_custom#
    class Meta:
        db_table = r's1210_detpgtofl_penalim'
        managed = True # s1210_detpgtofl_penalim #
        ordering = ['s1210_detpgtofl_retpgtotot', 'cpfbenef', 'nmbenefic', 'vlrpensao']



class s1210detPgtoFlpenAlimSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlpenAlim
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210detPgtoFlretPgtoTot(SoftDeletionModel):
    s1210_detpgtofl = models.ForeignKey('s1210detPgtoFl',
        related_name='%(class)s_s1210_detpgtofl')
    def evento(self): return self.s1210_detpgtofl.evento()
    codrubr = models.CharField(max_length=30)
    idetabrubr = models.CharField(max_length=8)
    qtdrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=6, blank=True, null=True)
    fatorrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=5, blank=True, null=True)
    vrunit = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vrrubr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_detpgtofl) + ' - ' + unicode(self.codrubr) + ' - ' + unicode(self.idetabrubr) + ' - ' + unicode(self.vrrubr)
    #s1210_detpgtofl_retpgtotot_custom#
    class Meta:
        db_table = r's1210_detpgtofl_retpgtotot'
        managed = True # s1210_detpgtofl_retpgtotot #
        ordering = ['s1210_detpgtofl', 'codrubr', 'idetabrubr', 'vrrubr']



class s1210detPgtoFlretPgtoTotSerializer(ModelSerializer):
    class Meta:
        model = s1210detPgtoFlretPgtoTot
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210idePgtoExt(SoftDeletionModel):
    s1210_infopgto = models.OneToOneField('s1210infoPgto',
        related_name='%(class)s_s1210_infopgto')
    def evento(self): return self.s1210_infopgto.evento()
    codpais = models.CharField(choices=CHOICES_S1210_IDEPGTOEXT_CODPAIS, max_length=3)
    indnif = models.IntegerField(choices=CHOICES_S1210_IDEPGTOEXT_INDNIF)
    nifbenef = models.CharField(max_length=20, blank=True, null=True)
    dsclograd = models.CharField(max_length=100)
    nrlograd = models.CharField(max_length=10, blank=True, null=True)
    complem = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=90, blank=True, null=True)
    nmcid = models.CharField(max_length=50)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_infopgto) + ' - ' + unicode(self.codpais) + ' - ' + unicode(self.indnif) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nmcid)
    #s1210_idepgtoext_custom#
    class Meta:
        db_table = r's1210_idepgtoext'
        managed = True # s1210_idepgtoext #
        ordering = ['s1210_infopgto', 'codpais', 'indnif', 'dsclograd', 'nmcid']



class s1210idePgtoExtSerializer(ModelSerializer):
    class Meta:
        model = s1210idePgtoExt
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

class s1210infoPgto(SoftDeletionModel):
    s1210_evtpgtos = models.ForeignKey('esocial.s1210evtPgtos',
        related_name='%(class)s_s1210_evtpgtos')
    def evento(self): return self.s1210_evtpgtos.evento()
    dtpgto = models.DateField()
    tppgto = models.IntegerField(choices=CHOICES_S1210_TPPGTO)
    indresbr = models.CharField(choices=CHOICES_S1210_INDRESBR, max_length=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.s1210_evtpgtos) + ' - ' + unicode(self.dtpgto) + ' - ' + unicode(self.tppgto) + ' - ' + unicode(self.indresbr)
    #s1210_infopgto_custom#
    class Meta:
        db_table = r's1210_infopgto'
        managed = True # s1210_infopgto #
        ordering = ['s1210_evtpgtos', 'dtpgto', 'tppgto', 'indresbr']



class s1210infoPgtoSerializer(ModelSerializer):
    class Meta:
        model = s1210infoPgto
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not criado_por:
            criado_por = CurrentUserDefault()
            criado_em = timezone.now()
        modificado_por = CurrentUserDefault()
        modificado_em = timezone.now()
            

#VIEWS_MODELS
