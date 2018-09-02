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

GRUPO_CODIGO_ATIV_PROD_SERV = (
    (1, u'I - Pessoas Jurídicas Prestadoras de Serviços -'),
    (2, u'II - Pessoas Jurídicas Comerciais - CR 2991-01'),
    (3, u'III - Pessoas Jurídicas Fabricantes - CR 2991-01'),
    (4, u'IV - Códigos Genéricos - Outras Receitas sujeitas à CPRB - CR 2991-01'),
)

GRUPO_PAGAMENTOS_CODIGOS = (
    (1, u'Beneficiários no Brasil'),
    (2, u'Beneficiários no Brasil e Justiça – RRA'),
    (3, u'Remessa Exterior'),
)

SIM_NAO_TXT = (
    ('N', u'Não'),
    ('S', u'Sim'),
)

CLASSIFICACAO_REGRAS_PAGAMENTOS_CODIGOS = (
    (1, u'Beneficiários'),
    (2, u'Beneficiários / Justiça – RRA'),
)

class AcidentesSituacoesGeradoras(models.Model):
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
    #acidentes_situacoes_geradoras_custom#
    #acidentes_situacoes_geradoras_custom#
    class Meta:
        db_table = r'acidentes_situacoes_geradoras'
        managed = True
        ordering = ['codigo', 'descricao']


class AfastamentosMotivos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao) + ' - ' + unicode(self.data_inicio) + ' - ' + unicode(self.data_termino)
    #afastamentos_motivos_custom#
    #afastamentos_motivos_custom#
    class Meta:
        db_table = r'afastamentos_motivos'
        managed = True
        ordering = ['codigo', 'descricao', 'data_inicio', 'data_termino']


class AgentesCausadoresAcidentesTrabalho(models.Model):
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
    #agentes_causadores_acidentes_trabalho_custom#
    #agentes_causadores_acidentes_trabalho_custom#
    class Meta:
        db_table = r'agentes_causadores_acidentes_trabalho'
        managed = True
        ordering = ['codigo', 'descricao']


class AgentesCausadoresDoencasProfissionais(models.Model):
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
    #agentes_causadores_doencas_profissionais_custom#
    #agentes_causadores_doencas_profissionais_custom#
    class Meta:
        db_table = r'agentes_causadores_doencas_profissionais'
        managed = True
        ordering = ['codigo', 'descricao']


class ArquivosEsocialTipos(models.Model):
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
    #arquivos_esocial_tipos_custom#
    #arquivos_esocial_tipos_custom#
    class Meta:
        db_table = r'arquivos_esocial_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


class AtividadesPericulosasInsalubresEspeciais(models.Model):
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
    #atividades_periculosas_insalubres_especiais_custom#
    #atividades_periculosas_insalubres_especiais_custom#
    class Meta:
        db_table = r'atividades_periculosas_insalubres_especiais'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']


class BeneficiosPrevidenciariosCessacaoMotivos(models.Model):
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
    #beneficios_previdenciarios_cessacao_motivos_custom#
    #beneficios_previdenciarios_cessacao_motivos_custom#
    class Meta:
        db_table = r'beneficios_previdenciarios_cessacao_motivos'
        managed = True
        ordering = ['codigo', 'descricao']


class BeneficiosPrevidenciariosTipos(models.Model):
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
    #beneficios_previdenciarios_tipos_custom#
    #beneficios_previdenciarios_tipos_custom#
    class Meta:
        db_table = r'beneficios_previdenciarios_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


class CBO(models.Model):
    codigo = models.CharField(max_length=4)
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


class ClassificacaoServicosPrestados(models.Model):
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
    #classificacao_servicos_prestados_custom#
    #classificacao_servicos_prestados_custom#
    class Meta:
        db_table = r'classificacao_servicos_prestados'
        managed = True
        ordering = ['codigo', 'descricao']


class ClassificacaoTributaria(models.Model):
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
    #classificacao_tributaria_custom#
    #classificacao_tributaria_custom#
    class Meta:
        db_table = r'classificacao_tributaria'
        managed = True
        ordering = ['codigo', 'descricao']


class ClassificacoesTributarias(models.Model):
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
    #classificacoes_tributarias_custom#
    #classificacoes_tributarias_custom#
    class Meta:
        db_table = r'classificacoes_tributarias'
        managed = True
        ordering = ['codigo', 'descricao']


class CodificacoesAcidenteTrabalho(models.Model):
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
    #codificacoes_acidente_trabalho_custom#
    #codificacoes_acidente_trabalho_custom#
    class Meta:
        db_table = r'codificacoes_acidente_trabalho'
        managed = True
        ordering = ['codigo', 'descricao']


class CodigoAliquotasFPASTerceiros(models.Model):
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
    #codigo_aliquotas_fpas_terceiros_custom#
    #codigo_aliquotas_fpas_terceiros_custom#
    class Meta:
        db_table = r'codigo_aliquotas_fpas_terceiros'
        managed = True
        ordering = ['codigo', 'descricao']


class CodigosAtividadesProdutosServicosCPRB(models.Model):
    codigo = models.CharField(max_length=4)
    grupo = models.IntegerField(choices=GRUPO_CODIGO_ATIV_PROD_SERV)
    aliquota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    inicio_escrituracao = models.DateField(blank=True, null=True)
    ncm = models.CharField(max_length=12, blank=True, null=True)
    cr = models.CharField(max_length=12, blank=True, null=True)
    incidencia = models.TextField(blank=True, null=True)
    descricao = models.TextField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.grupo) + ' - ' + unicode(self.aliquota) + ' - ' + unicode(self.inicio_escrituracao) + ' - ' + unicode(self.ncm) + ' - ' + unicode(self.cr) + ' - ' + unicode(self.incidencia) + ' - ' + unicode(self.descricao)
    #codigos_atividades_produtos_servicos_cprb_custom#
    #codigos_atividades_produtos_servicos_cprb_custom#
    class Meta:
        db_table = r'codigos_atividades_produtos_servicos_cprb'
        managed = True
        ordering = ['codigo', 'grupo', 'aliquota', 'inicio_escrituracao', 'ncm', 'cr', 'incidencia', 'descricao']


class CompatibilidadesCategoriasClassificacoesLotacoes(models.Model):
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
    #compatibilidades_categorias_classificacoes_lotacoes_custom#
    #compatibilidades_categorias_classificacoes_lotacoes_custom#
    class Meta:
        db_table = r'compatibilidades_categorias_classificacoes_lotacoes'
        managed = True
        ordering = ['codigo', 'classificacao_tributaria']


class CompatibilidadesFPASClassificacoesTributarias(models.Model):
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
    #compatibilidades_fpas_classificacoes_tributarias_custom#
    #compatibilidades_fpas_classificacoes_tributarias_custom#
    class Meta:
        db_table = r'compatibilidades_fpas_classificacoes_tributarias'
        managed = True
        ordering = ['codigo']


class CompatibilidadesLotacoesClassificacoes(models.Model):
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
    #compatibilidades_lotacoes_classificacoes_custom#
    #compatibilidades_lotacoes_classificacoes_custom#
    class Meta:
        db_table = r'compatibilidades_lotacoes_classificacoes'
        managed = True
        ordering = ['codigo']


class DependentesTipos(models.Model):
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
    #dependentes_tipos_custom#
    #dependentes_tipos_custom#
    class Meta:
        db_table = r'dependentes_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


class DesligamentosMotivos(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.codigo) + ' - ' + unicode(self.descricao) + ' - ' + unicode(self.data_inicio) + ' - ' + unicode(self.data_termino)
    #desligamentos_motivos_custom#
    #desligamentos_motivos_custom#
    class Meta:
        db_table = r'desligamentos_motivos'
        managed = True
        ordering = ['codigo', 'descricao', 'data_inicio', 'data_termino']


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


class FatoresRisco(models.Model):
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
    #fatores_risco_custom#
    #fatores_risco_custom#
    class Meta:
        db_table = r'fatores_risco'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']


class FinanciamentosAposentadoriasEspeciais(models.Model):
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
    #financiamentos_aposentadorias_especiais_custom#
    #financiamentos_aposentadorias_especiais_custom#
    class Meta:
        db_table = r'financiamentos_aposentadorias_especiais'
        managed = True
        ordering = ['codigo', 'descricao']


class InformacoesBeneficiariosExterior(models.Model):
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
    #informacoes_beneficiarios_exterior_custom#
    #informacoes_beneficiarios_exterior_custom#
    class Meta:
        db_table = r'informacoes_beneficiarios_exterior'
        managed = True
        ordering = ['codigo', 'descricao']


class InscricoesTipos(models.Model):
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
    #inscricoes_tipos_custom#
    #inscricoes_tipos_custom#
    class Meta:
        db_table = r'inscricoes_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


class LogradourosTipos(models.Model):
    codigo = models.CharField(max_length=3)
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
    #logradouros_tipos_custom#
    #logradouros_tipos_custom#
    class Meta:
        db_table = r'logradouros_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


class LotacoesTributariasTipos(models.Model):
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
    #lotacoes_tributarias_tipos_custom#
    #lotacoes_tributarias_tipos_custom#
    class Meta:
        db_table = r'lotacoes_tributarias_tipos'
        managed = True
        ordering = ['codigo', 'descricao']


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


class NaturezasJuridicas(models.Model):
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
    #naturezas_juridicas_custom#
    #naturezas_juridicas_custom#
    class Meta:
        db_table = r'naturezas_juridicas'
        managed = True


class NaturezasLesoes(models.Model):
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
    #naturezas_lesoes_custom#
    #naturezas_lesoes_custom#
    class Meta:
        db_table = r'naturezas_lesoes'
        managed = True
        ordering = ['codigo', 'descricao']


class NaturezasRubricas(models.Model):
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
    #naturezas_rubricas_custom#
    #naturezas_rubricas_custom#
    class Meta:
        db_table = r'naturezas_rubricas'
        managed = True
        ordering = ['codigo', 'titulo']


class PagamentosCodigos(models.Model):
    grupo = models.IntegerField(choices=GRUPO_PAGAMENTOS_CODIGOS)
    beneficiario_pf = models.CharField(choices=SIM_NAO_TXT, max_length=1)
    beneficiario_pj = models.CharField(choices=SIM_NAO_TXT, max_length=1)
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
        return unicode(self.grupo) + ' - ' + unicode(self.beneficiario_pf) + ' - ' + unicode(self.beneficiario_pj) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #pagamentos_codigos_custom#
    #pagamentos_codigos_custom#
    class Meta:
        db_table = r'pagamentos_codigos'
        managed = True
        ordering = ['grupo', 'beneficiario_pf', 'beneficiario_pj', 'codigo', 'descricao']


class Paises(models.Model):
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
        return unicode(self.codigo) + ' - ' + unicode(self.nome) + ' - ' + unicode(self.codigo) + ' - ' + unicode(self.descricao)
    #paises_custom#
    #paises_custom#
    class Meta:
        db_table = r'paises'
        managed = True
        ordering = ['codigo', 'nome', 'codigo', 'descricao']


class PartesCorpoAtingidas(models.Model):
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
    #partes_corpo_atingidas_custom#
    #partes_corpo_atingidas_custom#
    class Meta:
        db_table = r'partes_corpo_atingidas'
        managed = True
        ordering = ['codigo', 'descricao']


class ProcedimentosDiagnosticos(models.Model):
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
    #procedimentos_diagnosticos_custom#
    #procedimentos_diagnosticos_custom#
    class Meta:
        db_table = r'procedimentos_diagnosticos'
        managed = True
        ordering = ['codigo', 'descricao']


class ProgramasPlanosDocumentos(models.Model):
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
    #programas_planos_documentos_custom#
    #programas_planos_documentos_custom#
    class Meta:
        db_table = r'programas_planos_documentos'
        managed = True
        ordering = ['codigo', 'descricao']


class RegrasPagamentosCodigos(models.Model):
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
    #regras_pagamentos_codigos_custom#
    #regras_pagamentos_codigos_custom#
    class Meta:
        db_table = r'regras_pagamentos_codigos'
        managed = True
        ordering = ['classificacao', 'tributacao_com_exigibilidade_suspensa', 'compensacao_imposto_por_decisao_judicial', 'rendimentos_isentos', 'deducoes', 'decimo_terceiro', 'codigo', 'descricao']


class RendimentosBeneficiariosExterior(models.Model):
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
    #rendimentos_beneficiarios_exterior_custom#
    #rendimentos_beneficiarios_exterior_custom#
    class Meta:
        db_table = r'rendimentos_beneficiarios_exterior'
        managed = True
        ordering = ['codigo', 'descricao']


class RendimentosBeneficiariosExteriorTributacao(models.Model):
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
    #rendimentos_beneficiarios_exterior_tributacao_custom#
    #rendimentos_beneficiarios_exterior_tributacao_custom#
    class Meta:
        db_table = r'rendimentos_beneficiarios_exterior_tributacao'
        managed = True
        ordering = ['codigo', 'descricao']


class TrabalhadoresCategorias(models.Model):
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
    #trabalhadores_categorias_custom#
    #trabalhadores_categorias_custom#
    class Meta:
        db_table = r'trabalhadores_categorias'
        managed = True
        ordering = ['grupo', 'codigo', 'descricao']


class TreinamentosCapacitacoesExerciciosSimulados(models.Model):
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
    #treinamentos_capacitacoes_exercicios_simulados_custom#
    #treinamentos_capacitacoes_exercicios_simulados_custom#
    class Meta:
        db_table = r'treinamentos_capacitacoes_exercicios_simulados'
        managed = True
        ordering = ['codigo', 'descricao']


#VIEWS_MODELS
