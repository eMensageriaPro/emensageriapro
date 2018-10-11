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

CHOICES_S2206_DIA = (
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável'),
)

CHOICES_S2206_INDABONOPERM = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_INDPARCREMUN = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_INDTETORGPS = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2206_MTVALTER = (
    (1, u'1 - Promoção'),
    (2, u'2 - Readaptação'),
    (3, u'3 - Aproveitamento'),
    (8, u'8 - Outros'),
    (9, u'9 - Não alterado'),
)

CHOICES_S2206_NATATIVIDADE = (
    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural'),
)

CHOICES_S2206_TMPPARC = (
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais'),
)

CHOICES_S2206_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S2206_TPJORNADA = (
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada'),
)

CHOICES_S2206_TPPLANRP = (
    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro'),
)

CHOICES_S2206_TPREGJOR = (
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT'),
)

class s2206alvaraJudicial(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    nrprocjud = models.CharField(max_length=20)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.nrprocjud)
    #s2206_alvarajudicial_custom#
    #s2206_alvarajudicial_custom#
    class Meta:
        db_table = r's2206_alvarajudicial'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'nrprocjud']



class s2206alvaraJudicialSerializer(ModelSerializer):
    class Meta:
        model = s2206alvaraJudicial
        fields = '__all__'
            

class s2206aprend(models.Model):
    s2206_infoceletista = models.OneToOneField('s2206infoCeletista',
        related_name='%(class)s_s2206_infoceletista')
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
    nrinsc = models.CharField(max_length=15)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_infoceletista) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc)
    #s2206_aprend_custom#
    #s2206_aprend_custom#
    class Meta:
        db_table = r's2206_aprend'
        managed = True
        ordering = ['s2206_infoceletista', 'tpinsc', 'nrinsc']



class s2206aprendSerializer(ModelSerializer):
    class Meta:
        model = s2206aprend
        fields = '__all__'
            

class s2206filiacaoSindical(models.Model):
    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    cnpjsindtrab = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.cnpjsindtrab)
    #s2206_filiacaosindical_custom#
    #s2206_filiacaosindical_custom#
    class Meta:
        db_table = r's2206_filiacaosindical'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'cnpjsindtrab']



class s2206filiacaoSindicalSerializer(ModelSerializer):
    class Meta:
        model = s2206filiacaoSindical
        fields = '__all__'
            

class s2206horContratual(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, max_length=4, blank=True, null=True)
    tpjornada = models.IntegerField(choices=CHOICES_S2206_TPJORNADA)
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True)
    tmpparc = models.IntegerField(choices=CHOICES_S2206_TMPPARC)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.qtdhrssem) + ' - ' + unicode(self.tpjornada) + ' - ' + unicode(self.dsctpjorn) + ' - ' + unicode(self.tmpparc)
    #s2206_horcontratual_custom#
    #s2206_horcontratual_custom#
    class Meta:
        db_table = r's2206_horcontratual'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'qtdhrssem', 'tpjornada', 'dsctpjorn', 'tmpparc']



class s2206horContratualSerializer(ModelSerializer):
    class Meta:
        model = s2206horContratual
        fields = '__all__'
            

class s2206horario(models.Model):
    s2206_horcontratual = models.ForeignKey('s2206horContratual',
        related_name='%(class)s_s2206_horcontratual')
    dia = models.IntegerField(choices=CHOICES_S2206_DIA)
    codhorcontrat = models.CharField(max_length=30)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_horcontratual) + ' - ' + unicode(self.dia) + ' - ' + unicode(self.codhorcontrat)
    #s2206_horario_custom#
    #s2206_horario_custom#
    class Meta:
        db_table = r's2206_horario'
        managed = True
        ordering = ['s2206_horcontratual', 'dia', 'codhorcontrat']



class s2206horarioSerializer(ModelSerializer):
    class Meta:
        model = s2206horario
        fields = '__all__'
            

class s2206infoCeletista(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    tpregjor = models.IntegerField(choices=CHOICES_S2206_TPREGJOR)
    natatividade = models.IntegerField(choices=CHOICES_S2206_NATATIVIDADE)
    dtbase = models.IntegerField(blank=True, null=True)
    cnpjsindcategprof = models.CharField(max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpregjor) + ' - ' + unicode(self.natatividade) + ' - ' + unicode(self.dtbase) + ' - ' + unicode(self.cnpjsindcategprof)
    #s2206_infoceletista_custom#
    #s2206_infoceletista_custom#
    class Meta:
        db_table = r's2206_infoceletista'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'tpregjor', 'natatividade', 'dtbase', 'cnpjsindcategprof']



class s2206infoCeletistaSerializer(ModelSerializer):
    class Meta:
        model = s2206infoCeletista
        fields = '__all__'
            

class s2206infoEstatutario(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    tpplanrp = models.IntegerField(choices=CHOICES_S2206_TPPLANRP)
    indtetorgps = models.CharField(choices=CHOICES_S2206_INDTETORGPS, max_length=1, blank=True, null=True)
    indabonoperm = models.CharField(choices=CHOICES_S2206_INDABONOPERM, max_length=1, blank=True, null=True)
    indparcremun = models.CharField(choices=CHOICES_S2206_INDPARCREMUN, max_length=1, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpplanrp) + ' - ' + unicode(self.indtetorgps) + ' - ' + unicode(self.indabonoperm) + ' - ' + unicode(self.indparcremun)
    #s2206_infoestatutario_custom#
    #s2206_infoestatutario_custom#
    class Meta:
        db_table = r's2206_infoestatutario'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'tpplanrp', 'indtetorgps', 'indabonoperm', 'indparcremun']



class s2206infoEstatutarioSerializer(ModelSerializer):
    class Meta:
        model = s2206infoEstatutario
        fields = '__all__'
            

class s2206localTrabDom(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    tplograd = models.TextField(max_length=4)
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
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tplograd) + ' - ' + unicode(self.dsclograd) + ' - ' + unicode(self.nrlograd) + ' - ' + unicode(self.complemento) + ' - ' + unicode(self.bairro) + ' - ' + unicode(self.cep) + ' - ' + unicode(self.codmunic) + ' - ' + unicode(self.uf)
    #s2206_localtrabdom_custom#
    #s2206_localtrabdom_custom#
    class Meta:
        db_table = r's2206_localtrabdom'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'tplograd', 'dsclograd', 'nrlograd', 'complemento', 'bairro', 'cep', 'codmunic', 'uf']



class s2206localTrabDomSerializer(ModelSerializer):
    class Meta:
        model = s2206localTrabDom
        fields = '__all__'
            

class s2206localTrabGeral(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    tpinsc = models.IntegerField(choices=CHOICES_S2206_TPINSC)
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
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.tpinsc) + ' - ' + unicode(self.nrinsc) + ' - ' + unicode(self.desccomp)
    #s2206_localtrabgeral_custom#
    #s2206_localtrabgeral_custom#
    class Meta:
        db_table = r's2206_localtrabgeral'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'tpinsc', 'nrinsc', 'desccomp']



class s2206localTrabGeralSerializer(ModelSerializer):
    class Meta:
        model = s2206localTrabGeral
        fields = '__all__'
            

class s2206observacoes(models.Model):
    s2206_evtaltcontratual = models.ForeignKey('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    observacao = models.CharField(max_length=255)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.observacao)
    #s2206_observacoes_custom#
    #s2206_observacoes_custom#
    class Meta:
        db_table = r's2206_observacoes'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'observacao']



class s2206observacoesSerializer(ModelSerializer):
    class Meta:
        model = s2206observacoes
        fields = '__all__'
            

class s2206servPubl(models.Model):
    s2206_evtaltcontratual = models.OneToOneField('esocial.s2206evtAltContratual',
        related_name='%(class)s_s2206_evtaltcontratual')
    mtvalter = models.IntegerField(choices=CHOICES_S2206_MTVALTER)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_evtaltcontratual) + ' - ' + unicode(self.mtvalter)
    #s2206_servpubl_custom#
    #s2206_servpubl_custom#
    class Meta:
        db_table = r's2206_servpubl'
        managed = True
        ordering = ['s2206_evtaltcontratual', 'mtvalter']



class s2206servPublSerializer(ModelSerializer):
    class Meta:
        model = s2206servPubl
        fields = '__all__'
            

class s2206trabTemp(models.Model):
    s2206_infoceletista = models.OneToOneField('s2206infoCeletista',
        related_name='%(class)s_s2206_infoceletista')
    justprorr = models.CharField(max_length=999)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.s2206_infoceletista) + ' - ' + unicode(self.justprorr)
    #s2206_trabtemp_custom#
    #s2206_trabtemp_custom#
    class Meta:
        db_table = r's2206_trabtemp'
        managed = True
        ordering = ['s2206_infoceletista', 'justprorr']



class s2206trabTempSerializer(ModelSerializer):
    class Meta:
        model = s2206trabTemp
        fields = '__all__'
            

#VIEWS_MODELS
