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



CHOICES_S2245_TPPROF = (
    (1, u'1 - Profissional empregado do declarante'),
    (2, u'2 - Profissional sem vínculo de emprego/estatutário com o declarante'),
)

class s2245ideProfResp(models.Model):
    s2245_evttreicap = models.ForeignKey('esocial.s2245evtTreiCap',
        related_name='%(class)s_s2245_evttreicap')
    cpfprof = models.CharField(max_length=11)
    nmprof = models.CharField(max_length=70)
    tpprof = models.IntegerField(choices=CHOICES_S2245_TPPROF)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    formprof = models.CharField(max_length=255)
    codcbo = models.CharField(max_length=6)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2245_evttreicap) + ' - ' + unicode(self.cpfprof) + ' - ' + unicode(self.nmprof) + ' - ' + unicode(self.tpprof) + ' - ' + unicode(self.matricula) + ' - ' + unicode(self.formprof) + ' - ' + unicode(self.codcbo)
    #s2245_ideprofresp_custom#
    #s2245_ideprofresp_custom#
    class Meta:
        db_table = r's2245_ideprofresp'
        managed = True
        ordering = ['s2245_evttreicap', 'cpfprof', 'nmprof', 'tpprof', 'matricula', 'formprof', 'codcbo']


#VIEWS_MODELS
