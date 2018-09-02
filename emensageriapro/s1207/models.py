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
from django.apps import apps
get_model = apps.get_model



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
    (24, u'24 - Aposentadoria Voluntária por Idade - Proventos Proporcionais calculados sobre a última remuneração do cargo: Art. 40, § 1º, Inciso III, alínea "b'),
    (25, u'25 - Aposentadoria Voluntária por Idade - Proventos pela Média proporcionais - Art. 40, § 1º, Inciso III, alínea "b'),
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


#VIEWS_MODELS
