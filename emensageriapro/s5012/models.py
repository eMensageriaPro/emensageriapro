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
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_S5012_TPCR = (
    (3533, u'3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pensão Pagos por Previdência Pública'),
    (356201, u'356201 - IRRF sobre Participação dos trabalhadores em Lucros ou Resultados (PLR).'),
    (47301, u'047301 - IRRF - Residentes Fiscais no Exterior'),
    (56107, u'056107 - IRRF Mensal, 13° salário e Férias sobre Trabalho Assalariado no país ou ausente no exterior a serviço do país, exceto se contratado por Empregador Doméstico ou por Segurado Especial sujeito a recolhimento unificado'),
    (56108, u'056108 - IRRF Mensal, 13° salário e Férias sobre Trabalho Assalariado no país ou ausente no exterior a serviço do país, Empregado Doméstico ou Trabalhador contratado por Segurado Especial sujeito a recolhimento unificado'),
    (56109, u'056109 - IRRF 13° salário na rescisão de contrato de trabalho relativo a empregador sujeito a recolhimento unificado'),
    (56110, u'056110 - IRRF - Empregado doméstico - 13º salário'),
    (56111, u'056111 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'),
    (56112, u'056112 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário'),
    (56113, u'056113 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13° salário rescisório'),
    (58806, u'058806 - IRRF sobre Rendimento do trabalho sem vínculo empregatício'),
    (61001, u'061001 - IRRF sobre Rendimentos relativos a prestação de serviços de transporte rodoviário internacional de carga, pagos a transportador autônomo PF residente no Paraguai'),
)

class s5012infoCRContrib(models.Model):
    s5012_evtirrf = models.ForeignKey('esocial.s5012evtIrrf',
        related_name='%(class)s_s5012_evtirrf')
    def evento(self): return self.s5012_evtirrf.evento()
    tpcr = models.IntegerField(choices=CHOICES_S5012_TPCR)
    vrcr = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s5012_evtirrf) + ' - ' + unicode(self.tpcr) + ' - ' + unicode(self.vrcr)
    #s5012_infocrcontrib_custom#
    #s5012_infocrcontrib_custom#
    class Meta:
        db_table = r's5012_infocrcontrib'
        managed = True
        ordering = ['s5012_evtirrf', 'tpcr', 'vrcr']



class s5012infoCRContribSerializer(ModelSerializer):
    class Meta:
        model = s5012infoCRContrib
        fields = '__all__'
            

#VIEWS_MODELS
