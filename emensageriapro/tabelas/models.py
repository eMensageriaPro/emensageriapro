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



ESOCIAL_BENEFICIOS_PREVIDENCIARIOS_TIPOS_GRUPOS = (
    (1, u'Grupo 01 - Aposentadoria por Idade e Tempo de Contribuição'),
    (10, u'Grupo 10 - Benefícios Especiais com Vínculo Previdenciário'),
    (11, u'Grupo 11 - Benefícios Especiais sem Vínculo Previdenciário'),
    (12, u'Grupo 12 – Parlamentares'),
    (2, u'Grupo 02 - Aposentadoria Especial'),
    (3, u'Grupo 03 - Aposentadoria por Invalidez'),
    (4, u'Grupo 04 - Militares (Reforma)'),
    (5, u'Grupo 05 - Militares (Reserva)'),
    (6, u'Grupo 06 - Pensão por Morte'),
    (7, u'Grupo 07 - Auxílios Previdenciários'),
    (8, u'Grupo 08 - Complementação do Benefício do Regime Geral de Previdência Social (RGPS)'),
    (9, u'Grupo 09 - Benefícios Concedidos Antes da Obrigatoriedade de Envio dos Eventos Não Periódicos para Entes Públicos no eSocial (Carga Inicial)'),
)

GRUPOS_FATORES_RISCOS = (
    (1, u'FÍSICOS'),
    (10, u'PERICULOSO'),
    (11, u'ASSOCIAÇÃO DE FATORES DE RISCO'),
    (12, u'OUTROS FATORES DE RISCO'),
    (13, u'AUSÊNCIA DE FATORES DE RISCO'),
    (2, u'QUÍMICOS'),
    (3, u'BIOLÓGICOS'),
    (4, u'ERGONÔMICOS - BIOMECÂNICOS'),
    (5, u'ERGONÔMICOS - MOBILIÁRIO E EQUIPAMENTOS'),
    (6, u'ERGONÔMICOS - ORGANIZACIONAIS'),
    (7, u'ERGONÔMICOS - AMBIENTAIS'),
    (8, u'ERGONÔMICOS - PSICOSSOCIAIS/COGNITIVOS'),
    (9, u'MECÂNICOS/ACIDENTES'),
)

GRUPO_ATIVIDADES_PERICULOSAS = (
    (1, u'ATIVIDADES COM EXPOSIÇÃO A RISCOS BIOLÓGICOS'),
    (10, u'OUTRAS ATIVIDADES'),
    (11, u'AUSÊNCIA DE CORRESPONDÊNCIA'),
    (2, u'ATIVIDADES COM EXPOSIÇÃO A RISCOS QUÍMICOS'),
    (3, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM EXPLOSIVOS'),
    (4, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM INFLAMÁVEIS'),
    (5, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM RADIAÇÕES IONIZANTES OU SUBSTÂNCIAS RADIOATIVAS'),
    (6, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM EXPOSIÇÃO A ROUBOS OU OUTRAS ESPÉCIES DE VIOLÊNCIA FÍSICA NAS ATIVIDADES PROFISSIONAIS DE SEGURANÇA PESSOAL OU PATRIMONIAL'),
    (7, u'ATIVIDADES E OPERAÇÕES PERIGOSAS COM ENERGIA ELÉTRICA'),
    (8, u'ATIVIDADES PERIGOSAS EM MOTOCICLETA'),
    (9, u'ATIVIDADES ESPECIAIS POR EXPOSIÇÃO A AGENTES FÍSICOS'),
)

TRABALHADORES_CATEGORIAS_GRUPO = (
    (1, u'Empregado e Trabalhador Temporário'),
    (2, u'Avulso'),
    (3, u'Agente Público'),
    (4, u'Cessão'),
    (5, u'Contribuinte Individual'),
    (6, u'Bolsistas'),
)

GRUPO_NATUREZAS_JURIDICAS = (
    (1, u'Administração Pública'),
    (2, u'Entidades Empresariais'),
    (3, u'Entidades sem Fins Lucrativos'),
    (4, u'Pessoas Físicas'),
    (5, u'Organizações Internacionais e Outras Instituições Extraterritoriais'),
)

SIM_NAO_TXT = (
    ('N', u'Não'),
    ('S', u'Sim'),
)

GRUPO_PAGAMENTOS_CODIGOS = (
    (1, u'Beneficiários no Brasil'),
    (2, u'Beneficiários no Brasil e Justiça – RRA'),
    (3, u'Remessa Exterior'),
)

CLASSIFICACAO_REGRAS_PAGAMENTOS_CODIGOS = (
    (1, u'Beneficiários'),
    (2, u'Beneficiários / Justiça – RRA'),
)

GRUPO_CODIGO_ATIV_PROD_SERV = (
    (1, u'I - Pessoas Jurídicas Prestadoras de Serviços -'),
    (2, u'II - Pessoas Jurídicas Comerciais - CR 2991-01'),
    (3, u'III - Pessoas Jurídicas Fabricantes - CR 2991-01'),
    (4, u'IV - Códigos Genéricos - Outras Receitas sujeitas à CPRB - CR 2991-01'),
)

class CBO(models.Model):
    codigo = models.CharField(max_length=6)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #cbo_custom#
    #cbo_custom#
    class Meta:
        db_table = r'cbo'
        managed = True
        ordering = ['codigo', 'descricao']



class CBOSerializer(ModelSerializer):
    class Meta:
        model = CBO
        fields = '__all__'
            

class CID(models.Model):
    codigo = models.CharField(max_length=6)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    descricao_resumida = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #cid_custom#
    #cid_custom#
    class Meta:
        db_table = r'cid'
        managed = True
        ordering = ['codigo', 'descricao']



class CIDSerializer(ModelSerializer):
    class Meta:
        model = CID
        fields = '__all__'
            

class CNAE(models.Model):
    codigo = models.CharField(max_length=7)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    aliquota = models.DecimalField(max_digits=15, decimal_places=2)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #cnae_custom#
    #cnae_custom#
    class Meta:
        db_table = r'cnae'
        managed = True
        ordering = ['codigo', 'descricao']



class CNAESerializer(ModelSerializer):
    class Meta:
        model = CNAE
        fields = '__all__'
            

class EFDReinfClassificacaoServicosPrestados(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_classificacao_servicos_prestados_custom#
    #efdreinf_classificacao_servicos_prestados_custom#
    class Meta:
        db_table = r'efdreinf_classificacao_servicos_prestados'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfClassificacaoServicosPrestadosSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfClassificacaoServicosPrestados
        fields = '__all__'
            

class EFDReinfClassificacaoTributaria(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_classificacao_tributaria_custom#
    #efdreinf_classificacao_tributaria_custom#
    class Meta:
        db_table = r'efdreinf_classificacao_tributaria'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfClassificacaoTributariaSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfClassificacaoTributaria
        fields = '__all__'
            

class EFDReinfCodigosAtividadesProdutosServicosCPRB(models.Model):
    codigo = models.CharField(max_length=4)
    grupo = models.IntegerField(choices=GRUPO_CODIGO_ATIV_PROD_SERV)
    ncm = models.CharField(max_length=12, blank=True, null=True)
    cr = models.CharField(max_length=12, blank=True, null=True)
    inicio_escrituracao = models.DateField(blank=True, null=True)
    descricao = models.TextField()
    incidencia = models.TextField(blank=True, null=True)
    aliquota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.grupo) + ' - ' + unicode(self.ncm) + ' - ' + unicode(self.cr) + ' - ' + unicode(self.inicio_escrituracao) + ' - ' + unicode(self.descricao) + ' - ' + unicode(self.incidencia) + ' - ' + unicode(self.aliquota)
    #efdreinf_codigos_atividades_produtos_servicos_cprb_custom#
    #efdreinf_codigos_atividades_produtos_servicos_cprb_custom#
    class Meta:
        db_table = r'efdreinf_codigos_atividades_produtos_servicos_cprb'
        managed = True
        ordering = ['codigo', 'grupo', 'ncm', 'cr', 'inicio_escrituracao', 'descricao', 'incidencia', 'aliquota']



class EFDReinfCodigosAtividadesProdutosServicosCPRBSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfCodigosAtividadesProdutosServicosCPRB
        fields = '__all__'
            

class EFDReinfEventos(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_eventos_custom#
    #efdreinf_eventos_custom#
    class Meta:
        db_table = r'efdreinf_eventos'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfEventosSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfEventos
        fields = '__all__'
            

class EFDReinfInformacoesBeneficiariosExterior(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_informacoes_beneficiarios_exterior_custom#
    #efdreinf_informacoes_beneficiarios_exterior_custom#
    class Meta:
        db_table = r'efdreinf_informacoes_beneficiarios_exterior'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfInformacoesBeneficiariosExteriorSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfInformacoesBeneficiariosExterior
        fields = '__all__'
            

class EFDReinfPagamentosCodigos(models.Model):
    beneficiario_pf = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    beneficiario_pj = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    codigo = models.CharField(max_length=4)
    grupo = models.IntegerField(choices=GRUPO_PAGAMENTOS_CODIGOS)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.beneficiario_pf) + ' - ' + unicode(self.beneficiario_pj) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.grupo) + ' - ' + unicode(self.descricao)
    #efdreinf_pagamentos_codigos_custom#
    #efdreinf_pagamentos_codigos_custom#
    class Meta:
        db_table = r'efdreinf_pagamentos_codigos'
        managed = True
        ordering = ['beneficiario_pf', 'beneficiario_pj', 'codigo', 'grupo', 'descricao']



class EFDReinfPagamentosCodigosSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfPagamentosCodigos
        fields = '__all__'
            

class EFDReinfPaises(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_paises_custom#
    #efdreinf_paises_custom#
    class Meta:
        db_table = r'efdreinf_paises'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfPaisesSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfPaises
        fields = '__all__'
            

class EFDReinfRegrasPagamentosCodigos(models.Model):
    classificacao = models.IntegerField(choices=CLASSIFICACAO_REGRAS_PAGAMENTOS_CODIGOS)
    tributacao_com_exigibilidade_suspensa = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True)
    compensacao_imposto_por_decisao_judicial = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True)
    rendimentos_isentos = models.CharField(max_length=10, blank=True, null=True)
    deducoes = models.CharField(max_length=10, blank=True, null=True)
    decimo_terceiro = models.CharField(choices=SIM_NAO_TXT, max_length=1, blank=True, null=True)
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.classificacao) + ' - ' + unicode(self.tributacao_com_exigibilidade_suspensa) + ' - ' + unicode(self.compensacao_imposto_por_decisao_judicial) + ' - ' + unicode(self.rendimentos_isentos) + ' - ' + unicode(self.deducoes) + ' - ' + unicode(self.decimo_terceiro) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_regras_pagamentos_codigos_custom#
    #efdreinf_regras_pagamentos_codigos_custom#
    class Meta:
        db_table = r'efdreinf_regras_pagamentos_codigos'
        managed = True
        ordering = ['classificacao', 'tributacao_com_exigibilidade_suspensa', 'compensacao_imposto_por_decisao_judicial', 'rendimentos_isentos', 'deducoes', 'decimo_terceiro', 'codigo', 'descricao']



class EFDReinfRegrasPagamentosCodigosSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfRegrasPagamentosCodigos
        fields = '__all__'
            

class EFDReinfRendimentosBeneficiariosExterior(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_rendimentos_beneficiarios_exterior_custom#
    #efdreinf_rendimentos_beneficiarios_exterior_custom#
    class Meta:
        db_table = r'efdreinf_rendimentos_beneficiarios_exterior'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfRendimentosBeneficiariosExteriorSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfRendimentosBeneficiariosExterior
        fields = '__all__'
            

class EFDReinfRendimentosBeneficiariosExteriorTributacao(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #efdreinf_rendimentos_beneficiarios_exterior_tributacao_custom#
    #efdreinf_rendimentos_beneficiarios_exterior_tributacao_custom#
    class Meta:
        db_table = r'efdreinf_rendimentos_beneficiarios_exterior_tributacao'
        managed = True
        ordering = ['codigo', 'descricao']



class EFDReinfRendimentosBeneficiariosExteriorTributacaoSerializer(ModelSerializer):
    class Meta:
        model = EFDReinfRendimentosBeneficiariosExteriorTributacao
        fields = '__all__'
            

class Municipios(models.Model):
    codigo = models.CharField(max_length=7)
    titulo = models.CharField(max_length=300)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.titulo)
    #municipios_custom#
    #municipios_custom#
    class Meta:
        db_table = r'municipios'
        managed = True
        ordering = ['titulo']



class MunicipiosSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'
            

class eSocialAcidentesSituacoesGeradoras(models.Model):
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_acidentes_situacoes_geradoras_custom#
    #esocial_acidentes_situacoes_geradoras_custom#
    class Meta:
        db_table = r'esocial_acidentes_situacoes_geradoras'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialAcidentesSituacoesGeradorasSerializer(ModelSerializer):
    class Meta:
        model = eSocialAcidentesSituacoesGeradoras
        fields = '__all__'
            

class eSocialAfastamentosMotivos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao) + ' - ' + unicode(self.data_inicio) + ' - ' + unicode(self.data_termino)
    #esocial_afastamentos_motivos_custom#
    #esocial_afastamentos_motivos_custom#
    class Meta:
        db_table = r'esocial_afastamentos_motivos'
        managed = True
        ordering = ['codigo', 'descricao', 'data_inicio', 'data_termino']



class eSocialAfastamentosMotivosSerializer(ModelSerializer):
    class Meta:
        model = eSocialAfastamentosMotivos
        fields = '__all__'
            

class eSocialAgentesCausadoresAcidentesTrabalho(models.Model):
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_agentes_causadores_acidentes_trabalho_custom#
    #esocial_agentes_causadores_acidentes_trabalho_custom#
    class Meta:
        db_table = r'esocial_agentes_causadores_acidentes_trabalho'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialAgentesCausadoresAcidentesTrabalhoSerializer(ModelSerializer):
    class Meta:
        model = eSocialAgentesCausadoresAcidentesTrabalho
        fields = '__all__'
            

class eSocialAgentesCausadoresDoencasProfissionais(models.Model):
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_agentes_causadores_doencas_profissionais_custom#
    #esocial_agentes_causadores_doencas_profissionais_custom#
    class Meta:
        db_table = r'esocial_agentes_causadores_doencas_profissionais'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialAgentesCausadoresDoencasProfissionaisSerializer(ModelSerializer):
    class Meta:
        model = eSocialAgentesCausadoresDoencasProfissionais
        fields = '__all__'
            

class eSocialArquivosEsocialTipos(models.Model):
    codigo = models.CharField(max_length=6)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_arquivos_esocial_tipos_custom#
    #esocial_arquivos_esocial_tipos_custom#
    class Meta:
        db_table = r'esocial_arquivos_esocial_tipos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialArquivosEsocialTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialArquivosEsocialTipos
        fields = '__all__'
            

class eSocialAtividadesPericulosasInsalubresEspeciais(models.Model):
    grupo = models.IntegerField(choices=GRUPO_ATIVIDADES_PERICULOSAS)
    codigo = models.CharField(max_length=6)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.grupo) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_atividades_periculosas_insalubres_especiais_custom#
    #esocial_atividades_periculosas_insalubres_especiais_custom#
    class Meta:
        db_table = r'esocial_atividades_periculosas_insalubres_especiais'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']



class eSocialAtividadesPericulosasInsalubresEspeciaisSerializer(ModelSerializer):
    class Meta:
        model = eSocialAtividadesPericulosasInsalubresEspeciais
        fields = '__all__'
            

class eSocialBeneficiosPrevidenciariosCessacaoMotivos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_beneficios_previdenciarios_cessacao_motivos_custom#
    #esocial_beneficios_previdenciarios_cessacao_motivos_custom#
    class Meta:
        db_table = r'esocial_beneficios_previdenciarios_cessacao_motivos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialBeneficiosPrevidenciariosCessacaoMotivosSerializer(ModelSerializer):
    class Meta:
        model = eSocialBeneficiosPrevidenciariosCessacaoMotivos
        fields = '__all__'
            

class eSocialBeneficiosPrevidenciariosTipos(models.Model):
    grupo = models.IntegerField(choices=ESOCIAL_BENEFICIOS_PREVIDENCIARIOS_TIPOS_GRUPOS)
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.grupo) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_beneficios_previdenciarios_tipos_custom#
    #esocial_beneficios_previdenciarios_tipos_custom#
    class Meta:
        db_table = r'esocial_beneficios_previdenciarios_tipos'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']



class eSocialBeneficiosPrevidenciariosTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialBeneficiosPrevidenciariosTipos
        fields = '__all__'
            

class eSocialClassificacoesTributarias(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_classificacoes_tributarias_custom#
    #esocial_classificacoes_tributarias_custom#
    class Meta:
        db_table = r'esocial_classificacoes_tributarias'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialClassificacoesTributariasSerializer(ModelSerializer):
    class Meta:
        model = eSocialClassificacoesTributarias
        fields = '__all__'
            

class eSocialCodificacoesAcidenteTrabalho(models.Model):
    codigo = models.CharField(max_length=6)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_codificacoes_acidente_trabalho_custom#
    #esocial_codificacoes_acidente_trabalho_custom#
    class Meta:
        db_table = r'esocial_codificacoes_acidente_trabalho'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialCodificacoesAcidenteTrabalhoSerializer(ModelSerializer):
    class Meta:
        model = eSocialCodificacoesAcidenteTrabalho
        fields = '__all__'
            

class eSocialCodigoAliquotasFPASTerceiros(models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.TextField()
    tipo_empresa = models.CharField(max_length=20)
    base_calculo = models.CharField(max_length=50)
    terceiros = models.CharField(max_length=20)
    codigo_terceiro = models.CharField(max_length=4)
    aliquota = models.DecimalField(max_digits=15, decimal_places=2)
    ind_total = models.IntegerField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_codigo_aliquotas_fpas_terceiros_custom#
    #esocial_codigo_aliquotas_fpas_terceiros_custom#
    class Meta:
        db_table = r'esocial_codigo_aliquotas_fpas_terceiros'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialCodigoAliquotasFPASTerceirosSerializer(ModelSerializer):
    class Meta:
        model = eSocialCodigoAliquotasFPASTerceiros
        fields = '__all__'
            

class eSocialCompatibilidadesCategoriasClassificacoesLotacoes(models.Model):
    codigo = models.CharField(max_length=3)
    classificacao_tributaria = models.TextField()
    tipo_lotacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_05 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_24 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_90 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_lotacao_tributaria_91 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.classificacao_tributaria)
    #esocial_compatibilidades_categorias_classificacoes_lotacoes_custom#
    #esocial_compatibilidades_categorias_classificacoes_lotacoes_custom#
    class Meta:
        db_table = r'esocial_compatibilidades_categorias_classificacoes_lotacoes'
        managed = True
        ordering = ['codigo', 'classificacao_tributaria']



class eSocialCompatibilidadesCategoriasClassificacoesLotacoesSerializer(ModelSerializer):
    class Meta:
        model = eSocialCompatibilidadesCategoriasClassificacoesLotacoes
        fields = '__all__'
            

class eSocialCompatibilidadesFPASClassificacoesTributarias(models.Model):
    codigo = models.CharField(max_length=3)
    classificacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_11 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_13 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_14 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_22 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_60 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_70 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_80 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_85 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    classificacao_tributaria_99 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo)
    #esocial_compatibilidades_fpas_classificacoes_tributarias_custom#
    #esocial_compatibilidades_fpas_classificacoes_tributarias_custom#
    class Meta:
        db_table = r'esocial_compatibilidades_fpas_classificacoes_tributarias'
        managed = True
        ordering = ['codigo']



class eSocialCompatibilidadesFPASClassificacoesTributariasSerializer(ModelSerializer):
    class Meta:
        model = eSocialCompatibilidadesFPASClassificacoesTributarias
        fields = '__all__'
            

class eSocialCompatibilidadesLotacoesClassificacoes(models.Model):
    codigo = models.CharField(max_length=2)
    tipo_classificacao_tributaria_01 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_02 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_03 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_04 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_06 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_07 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_08 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_09 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_10 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_11 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_13 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_14 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_21 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_22 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_60 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_70 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_80 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_85 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    tipo_classificacao_tributaria_99 = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo)
    #esocial_compatibilidades_lotacoes_classificacoes_custom#
    #esocial_compatibilidades_lotacoes_classificacoes_custom#
    class Meta:
        db_table = r'esocial_compatibilidades_lotacoes_classificacoes'
        managed = True
        ordering = ['codigo']



class eSocialCompatibilidadesLotacoesClassificacoesSerializer(ModelSerializer):
    class Meta:
        model = eSocialCompatibilidadesLotacoesClassificacoes
        fields = '__all__'
            

class eSocialDependentesTipos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_dependentes_tipos_custom#
    #esocial_dependentes_tipos_custom#
    class Meta:
        db_table = r'esocial_dependentes_tipos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialDependentesTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialDependentesTipos
        fields = '__all__'
            

class eSocialDesligamentosMotivos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao) + ' - ' + unicode(self.data_inicio) + ' - ' + unicode(self.data_termino)
    #esocial_desligamentos_motivos_custom#
    #esocial_desligamentos_motivos_custom#
    class Meta:
        db_table = r'esocial_desligamentos_motivos'
        managed = True
        ordering = ['codigo', 'descricao', 'data_inicio', 'data_termino']



class eSocialDesligamentosMotivosSerializer(ModelSerializer):
    class Meta:
        model = eSocialDesligamentosMotivos
        fields = '__all__'
            

class eSocialFatoresRisco(models.Model):
    grupo = models.IntegerField(choices=GRUPOS_FATORES_RISCOS)
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.grupo) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_fatores_risco_custom#
    #esocial_fatores_risco_custom#
    class Meta:
        db_table = r'esocial_fatores_risco'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']



class eSocialFatoresRiscoSerializer(ModelSerializer):
    class Meta:
        model = eSocialFatoresRisco
        fields = '__all__'
            

class eSocialFinanciamentosAposentadoriasEspeciais(models.Model):
    codigo = models.CharField(max_length=14)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_financiamentos_aposentadorias_especiais_custom#
    #esocial_financiamentos_aposentadorias_especiais_custom#
    class Meta:
        db_table = r'esocial_financiamentos_aposentadorias_especiais'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialFinanciamentosAposentadoriasEspeciaisSerializer(ModelSerializer):
    class Meta:
        model = eSocialFinanciamentosAposentadoriasEspeciais
        fields = '__all__'
            

class eSocialInscricoesTipos(models.Model):
    codigo = models.CharField(max_length=14)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_inscricoes_tipos_custom#
    #esocial_inscricoes_tipos_custom#
    class Meta:
        db_table = r'esocial_inscricoes_tipos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialInscricoesTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialInscricoesTipos
        fields = '__all__'
            

class eSocialLogradourosTipos(models.Model):
    codigo = models.CharField(max_length=5)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_logradouros_tipos_custom#
    #esocial_logradouros_tipos_custom#
    class Meta:
        db_table = r'esocial_logradouros_tipos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialLogradourosTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialLogradourosTipos
        fields = '__all__'
            

class eSocialLotacoesTributariasTipos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    preenchimento_campo_nr_insc = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_lotacoes_tributarias_tipos_custom#
    #esocial_lotacoes_tributarias_tipos_custom#
    class Meta:
        db_table = r'esocial_lotacoes_tributarias_tipos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialLotacoesTributariasTiposSerializer(ModelSerializer):
    class Meta:
        model = eSocialLotacoesTributariasTipos
        fields = '__all__'
            

class eSocialNaturezasJuridicas(models.Model):
    grupo = models.IntegerField(choices=GRUPO_NATUREZAS_JURIDICAS)
    codigo = models.CharField(max_length=20)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_naturezas_juridicas_custom#
    #esocial_naturezas_juridicas_custom#
    class Meta:
        db_table = r'esocial_naturezas_juridicas'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialNaturezasJuridicasSerializer(ModelSerializer):
    class Meta:
        model = eSocialNaturezasJuridicas
        fields = '__all__'
            

class eSocialNaturezasLesoes(models.Model):
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_naturezas_lesoes_custom#
    #esocial_naturezas_lesoes_custom#
    class Meta:
        db_table = r'esocial_naturezas_lesoes'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialNaturezasLesoesSerializer(ModelSerializer):
    class Meta:
        model = eSocialNaturezasLesoes
        fields = '__all__'
            

class eSocialNaturezasRubricas(models.Model):
    codigo = models.CharField(max_length=14)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.titulo)
    #esocial_naturezas_rubricas_custom#
    #esocial_naturezas_rubricas_custom#
    class Meta:
        db_table = r'esocial_naturezas_rubricas'
        managed = True
        ordering = ['codigo', 'titulo']



class eSocialNaturezasRubricasSerializer(ModelSerializer):
    class Meta:
        model = eSocialNaturezasRubricas
        fields = '__all__'
            

class eSocialPaises(models.Model):
    codigo = models.CharField(max_length=14)
    nome = models.CharField(max_length=200)
    data_criacao = models.DateField(blank=True, null=True)
    data_extincao = models.DateField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.nome)
    #esocial_paises_custom#
    #esocial_paises_custom#
    class Meta:
        db_table = r'esocial_paises'
        managed = True
        ordering = ['codigo', 'nome']



class eSocialPaisesSerializer(ModelSerializer):
    class Meta:
        model = eSocialPaises
        fields = '__all__'
            

class eSocialPartesCorpoAtingidas(models.Model):
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_partes_corpo_atingidas_custom#
    #esocial_partes_corpo_atingidas_custom#
    class Meta:
        db_table = r'esocial_partes_corpo_atingidas'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialPartesCorpoAtingidasSerializer(ModelSerializer):
    class Meta:
        model = eSocialPartesCorpoAtingidas
        fields = '__all__'
            

class eSocialProcedimentosDiagnosticos(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_procedimentos_diagnosticos_custom#
    #esocial_procedimentos_diagnosticos_custom#
    class Meta:
        db_table = r'esocial_procedimentos_diagnosticos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialProcedimentosDiagnosticosSerializer(ModelSerializer):
    class Meta:
        model = eSocialProcedimentosDiagnosticos
        fields = '__all__'
            

class eSocialProgramasPlanosDocumentos(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_programas_planos_documentos_custom#
    #esocial_programas_planos_documentos_custom#
    class Meta:
        db_table = r'esocial_programas_planos_documentos'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialProgramasPlanosDocumentosSerializer(ModelSerializer):
    class Meta:
        model = eSocialProgramasPlanosDocumentos
        fields = '__all__'
            

class eSocialTrabalhadoresCategorias(models.Model):
    grupo = models.IntegerField(choices=TRABALHADORES_CATEGORIAS_GRUPO)
    codigo = models.CharField(max_length=14)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.grupo) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_trabalhadores_categorias_custom#
    #esocial_trabalhadores_categorias_custom#
    class Meta:
        db_table = r'esocial_trabalhadores_categorias'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']



class eSocialTrabalhadoresCategoriasSerializer(ModelSerializer):
    class Meta:
        model = eSocialTrabalhadoresCategorias
        fields = '__all__'
            

class eSocialTreinamentosCapacitacoesExerciciosSimulados(models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #esocial_treinamentos_capacitacoes_exercicios_simulados_custom#
    #esocial_treinamentos_capacitacoes_exercicios_simulados_custom#
    class Meta:
        db_table = r'esocial_treinamentos_capacitacoes_exercicios_simulados'
        managed = True
        ordering = ['codigo', 'descricao']



class eSocialTreinamentosCapacitacoesExerciciosSimuladosSerializer(ModelSerializer):
    class Meta:
        model = eSocialTreinamentosCapacitacoesExerciciosSimulados
        fields = '__all__'
            

#VIEWS_MODELS
