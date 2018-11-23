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



CHOICES_R2060_CODAJUSTE = (
    (1, u'1 - Ajuste da CPRB: Adoção do Regime de Caixa'),
    (10, u'10 - O valor do aporte de recursos realizado nos termos do art 6 §3 inciso III da Lei 11.079/2004'),
    (11, u'11 - Demais ajustes oriundos da Legislação Tributária, estorno ou outras situações'),
    (2, u'2 - Ajuste da CPRB: Diferimento de Valores a recolher no período'),
    (3, u'3 - Adição de valores Diferidos em Período(s) Anteriores(es)'),
    (4, u'4 - Exportações diretas'),
    (5, u'5 - Transporte internacional de cargas'),
    (6, u'6 - Vendas canceladas e os descontos incondicionais concedidos'),
    (7, u'7 - IPI, se incluído na receita bruta'),
    (8, u'8 - ICMS, quando cobrado pelo vendedor dos bens ou prestador dos serviços na condição de substituto tributário'),
    (9, u'9 - Receita bruta reconhecida pela construção, recuperação, reforma, ampliação ou melhoramento da infraestrutura, cuja contrapartida seja ativo intangível representativo de direito de exploração, no caso de contratos de concessão de serviços públicos'),
)

CHOICES_R2060_TPAJUSTE = (
    (0, u'0 - Ajuste de redução'),
    (1, u'1 - Ajuste de acréscimo'),
)

CHOICES_R2060_TPPROC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2060infoProc(models.Model):
    r2060_tipocod = models.ForeignKey('r2060tipoCod',
        related_name='%(class)s_r2060_tipocod')
    def evento(self): return self.r2060_tipocod.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2060_TPPROC)
    nrproc = models.CharField(max_length=21)
    codsusp = models.IntegerField(blank=True, null=True)
    vlrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2060_tipocod) + ' - ' + unicode(self.tpproc) + ' - ' + unicode(self.nrproc) + ' - ' + unicode(self.vlrcprbsusp)
    #r2060_infoproc_custom#
    #r2060_infoproc_custom#
    class Meta:
        db_table = r'r2060_infoproc'
        managed = True
        ordering = ['r2060_tipocod', 'tpproc', 'nrproc', 'vlrcprbsusp']



class r2060infoProcSerializer(ModelSerializer):
    class Meta:
        model = r2060infoProc
        fields = '__all__'
            

class r2060tipoAjuste(models.Model):
    r2060_tipocod = models.ForeignKey('r2060tipoCod',
        related_name='%(class)s_r2060_tipocod')
    def evento(self): return self.r2060_tipocod.evento()
    tpajuste = models.IntegerField(choices=CHOICES_R2060_TPAJUSTE)
    codajuste = models.IntegerField(choices=CHOICES_R2060_CODAJUSTE)
    vlrajuste = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    descajuste = models.CharField(max_length=20)
    dtajuste = models.CharField(max_length=7)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2060_tipocod) + ' - ' + unicode(self.tpajuste) + ' - ' + unicode(self.codajuste) + ' - ' + unicode(self.vlrajuste) + ' - ' + unicode(self.descajuste) + ' - ' + unicode(self.dtajuste)
    #r2060_tipoajuste_custom#
    #r2060_tipoajuste_custom#
    class Meta:
        db_table = r'r2060_tipoajuste'
        managed = True
        ordering = ['r2060_tipocod', 'tpajuste', 'codajuste', 'vlrajuste', 'descajuste', 'dtajuste']



class r2060tipoAjusteSerializer(ModelSerializer):
    class Meta:
        model = r2060tipoAjuste
        fields = '__all__'
            

class r2060tipoCod(models.Model):
    r2060_evtcprb = models.ForeignKey('efdreinf.r2060evtCPRB',
        related_name='%(class)s_r2060_evtcprb')
    def evento(self): return self.r2060_evtcprb.evento()
    codativecon = models.CharField(max_length=8)
    vlrrecbrutaativ = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrexcrecbruta = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlradicrecbruta = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrbccprb = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrcprbapur = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2060_evtcprb) + ' - ' + unicode(self.codativecon) + ' - ' + unicode(self.vlrrecbrutaativ) + ' - ' + unicode(self.vlrexcrecbruta) + ' - ' + unicode(self.vlradicrecbruta) + ' - ' + unicode(self.vlrbccprb)
    #r2060_tipocod_custom#
    #r2060_tipocod_custom#
    class Meta:
        db_table = r'r2060_tipocod'
        managed = True
        ordering = ['r2060_evtcprb', 'codativecon', 'vlrrecbrutaativ', 'vlrexcrecbruta', 'vlradicrecbruta', 'vlrbccprb']



class r2060tipoCodSerializer(ModelSerializer):
    class Meta:
        model = r2060tipoCod
        fields = '__all__'
            

#VIEWS_MODELS
