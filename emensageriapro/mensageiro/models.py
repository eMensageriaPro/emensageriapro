# eMensageriaAI #
#coding:utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.mensageiro.choices import *
get_model = apps.get_model


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class Arquivos(SoftDeletionModel):

    arquivo = models.CharField(max_length=300, )
    data_criacao = models.DateField()
    permite_recuperacao = models.IntegerField(choices=SIM_NAO, )

    def __unicode__(self):
        return unicode(self.id)

    class Meta:

        verbose_name = u'Arquivos'
        verbose_name_plural = u'Arquivos'
        db_table = r'arquivos'
        managed = True # arquivos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_Arquivos", u"Pode ver listagem do modelo ARQUIVOS"),
            ("can_see_data_Arquivos", u"Pode visualizar o conteúdo do modelo ARQUIVOS"),
            ("can_see_menu_Arquivos", u"Pode visualizar no menu o modelo ARQUIVOS"),
            ("can_print_list_Arquivos", u"Pode imprimir listagem do modelo ARQUIVOS"),
            ("can_print_data_Arquivos", u"Pode imprimir o conteúdo do modelo ARQUIVOS"), )

        ordering = [ ]



class ArquivosSerializer(ModelSerializer):

    class Meta:

        model = Arquivos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class ImportacaoArquivos(SoftDeletionModel):

    arquivo = models.CharField(max_length=200, blank=True, )
    status = models.IntegerField(choices=IMPORTACAO_STATUS, blank=True, )
    data_hora = models.DateTimeField(blank=True, )
    importado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_importado_por', blank=True, null=True, )
    quant_total = models.IntegerField(blank=True, null=True, )
    quant_aguardando = models.IntegerField(blank=True, null=True, )
    quant_processado = models.IntegerField(blank=True, null=True, )
    quant_importado = models.IntegerField(blank=True, null=True, )
    quant_erros = models.IntegerField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.arquivo)

    class Meta:

        verbose_name = u'Importação de Arquivos'
        verbose_name_plural = u'Importação de Arquivos'
        db_table = r'importacao_arquivos'
        managed = True # importacao_arquivos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_ImportacaoArquivos", u"Pode ver listagem do modelo IMPORTACAOARQUIVOS"),
            ("can_see_data_ImportacaoArquivos", u"Pode visualizar o conteúdo do modelo IMPORTACAOARQUIVOS"),
            ("can_see_menu_ImportacaoArquivos", u"Pode visualizar no menu o modelo IMPORTACAOARQUIVOS"),
            ("can_print_list_ImportacaoArquivos", u"Pode imprimir listagem do modelo IMPORTACAOARQUIVOS"),
            ("can_print_data_ImportacaoArquivos", u"Pode imprimir o conteúdo do modelo IMPORTACAOARQUIVOS"), )

        ordering = [
            'arquivo', ]



class ImportacaoArquivosSerializer(ModelSerializer):

    class Meta:

        model = ImportacaoArquivos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class ImportacaoArquivosEventos(SoftDeletionModel):

    importacao_arquivos = models.ForeignKey('mensageiro.ImportacaoArquivos',
        related_name='%(class)s_importacao_arquivos', blank=True, )
    arquivo = models.CharField(max_length=200, blank=True, null=True, )
    evento = models.CharField(max_length=100, blank=True, null=True, )
    versao = models.CharField(max_length=30, blank=True, null=True, )
    identidade_evento = models.CharField(max_length=100, blank=True, null=True, )
    identidade = models.IntegerField(blank=True, null=True, )
    status = models.IntegerField(choices=IMPORTACAO_STATUS, blank=True, null=True, )
    data_hora = models.DateTimeField(blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.importacao_arquivos) + ' - ' + unicode(self.arquivo) + ' - ' + unicode(self.evento) + ' - ' + unicode(self.versao) + ' - ' + unicode(self.identidade_evento) + ' - ' + unicode(self.identidade)

    class Meta:

        verbose_name = u'Eventos de Arquivos Importados'
        verbose_name_plural = u'Eventos de Arquivos Importados'
        db_table = r'importacao_arquivos_eventos'
        managed = True # importacao_arquivos_eventos #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_ImportacaoArquivosEventos", u"Pode ver listagem do modelo IMPORTACAOARQUIVOSEVENTOS"),
            ("can_see_data_ImportacaoArquivosEventos", u"Pode visualizar o conteúdo do modelo IMPORTACAOARQUIVOSEVENTOS"),
            ("can_see_menu_ImportacaoArquivosEventos", u"Pode visualizar no menu o modelo IMPORTACAOARQUIVOSEVENTOS"),
            ("can_print_list_ImportacaoArquivosEventos", u"Pode imprimir listagem do modelo IMPORTACAOARQUIVOSEVENTOS"),
            ("can_print_data_ImportacaoArquivosEventos", u"Pode imprimir o conteúdo do modelo IMPORTACAOARQUIVOSEVENTOS"), )

        ordering = [
            'importacao_arquivos',
            'arquivo',
            'evento',
            'versao',
            'identidade_evento',
            'identidade', ]



class ImportacaoArquivosEventosSerializer(ModelSerializer):

    class Meta:

        model = ImportacaoArquivosEventos
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class RegrasDeValidacao(SoftDeletionModel):

    evento = models.CharField(max_length=5000, )
    versao = models.CharField(max_length=20, blank=True, )
    numero = models.IntegerField()
    registro_campo = models.CharField(max_length=100, )
    registro_pai = models.CharField(max_length=100, )
    elemento = models.CharField(max_length=2, )
    tipo = models.CharField(max_length=1, )
    ocorrencias = models.CharField(max_length=10, )
    tamanho = models.CharField(max_length=10, )
    casas_decimais = models.CharField(max_length=10, )
    obrigatorio = models.IntegerField(choices=SIM_NAO, blank=True, )
    descricao = models.TextField(blank=True, )
    tabela = models.CharField(max_length=200, blank=True, null=True, )
    valores_validos = models.TextField(blank=True, null=True, )
    validacoes_precedencia = models.TextField(blank=True, null=True, )
    validacoes = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.evento) + ' - ' + unicode(self.versao) + ' - ' + unicode(self.numero) + ' - ' + unicode(self.registro_campo) + ' - ' + unicode(self.registro_pai)

    class Meta:

        verbose_name = u'Regras de Validação'
        verbose_name_plural = u'Regras de Validação'
        db_table = r'regras_validacao'
        managed = True # regras_validacao #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_RegrasDeValidacao", u"Pode ver listagem do modelo REGRASDEVALIDACAO"),
            ("can_see_data_RegrasDeValidacao", u"Pode visualizar o conteúdo do modelo REGRASDEVALIDACAO"),
            ("can_see_menu_RegrasDeValidacao", u"Pode visualizar no menu o modelo REGRASDEVALIDACAO"),
            ("can_print_list_RegrasDeValidacao", u"Pode imprimir listagem do modelo REGRASDEVALIDACAO"),
            ("can_print_data_RegrasDeValidacao", u"Pode imprimir o conteúdo do modelo REGRASDEVALIDACAO"), )

        ordering = [ ]



class RegrasDeValidacaoSerializer(ModelSerializer):

    class Meta:

        model = RegrasDeValidacao
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class Relatorios(SoftDeletionModel):

    titulo = models.CharField(max_length=500, )
    campos = models.CharField(max_length=500, )
    sql = models.TextField(blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.id)

    class Meta:

        verbose_name = u'Relatórios'
        verbose_name_plural = u'Relatórios'
        db_table = r'relatorios'
        managed = True # relatorios #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_Relatorios", u"Pode ver listagem do modelo RELATORIOS"),
            ("can_see_data_Relatorios", u"Pode visualizar o conteúdo do modelo RELATORIOS"),
            ("can_see_menu_Relatorios", u"Pode visualizar no menu o modelo RELATORIOS"),
            ("can_print_list_Relatorios", u"Pode imprimir listagem do modelo RELATORIOS"),
            ("can_print_data_Relatorios", u"Pode imprimir o conteúdo do modelo RELATORIOS"), )

        ordering = [ ]



class RelatoriosSerializer(ModelSerializer):

    class Meta:

        model = Relatorios
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class TransmissorLote(SoftDeletionModel):

    transmissor_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    transmissor_nrinsc = models.CharField(max_length=15, )
    nome_empresa = models.CharField(max_length=200, )
    data_abertura = models.DateField()
    logotipo = models.FileField(upload_to="logotipo", blank=True, null=True, )
    endereco_completo = models.TextField()
    nrinsc = models.CharField(max_length=15, )
    tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    certificado = models.ForeignKey('mensageiro.Certificados',
        related_name='%(class)s_certificado', blank=True, null=True, )

    def __unicode__(self):
        return unicode(self.transmissor_nrinsc) + ' - ' + unicode(self.nome_empresa) + ' - ' + unicode(self.nrinsc)

    def save(self, **kwargs):
        from emensageriapro.mensageiro.functions.funcoes import retirar_pontuacao_cpf_cnpj
        self.transmissor_nrinsc = retirar_pontuacao_cpf_cnpj(self.transmissor_nrinsc)
        self.nrinsc = retirar_pontuacao_cpf_cnpj(self.nrinsc)
        super(TransmissorLote, self).save(**kwargs)

    class Meta:

        verbose_name = u'Transmissor'
        verbose_name_plural = u'Transmissor'
        db_table = r'transmissores'
        managed = True # transmissores #

        unique_together = (
            ('nome_empresa', 'ativo'), )

        index_together = ()

        permissions = (
            ("can_see_list_TransmissorLote", u"Pode ver listagem do modelo TRANSMISSORLOTE"),
            ("can_see_data_TransmissorLote", u"Pode visualizar o conteúdo do modelo TRANSMISSORLOTE"),
            ("can_see_menu_TransmissorLote", u"Pode visualizar no menu o modelo TRANSMISSORLOTE"),
            ("can_print_list_TransmissorLote", u"Pode imprimir listagem do modelo TRANSMISSORLOTE"),
            ("can_print_data_TransmissorLote", u"Pode imprimir o conteúdo do modelo TRANSMISSORLOTE"), )

        ordering = [ ]



class TransmissorLoteSerializer(ModelSerializer):

    class Meta:

        model = TransmissorLote
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class TransmissorLoteEfdreinf(SoftDeletionModel):

    transmissor = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor', blank=True, null=True, )
    contribuinte_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    contribuinte_nrinsc = models.CharField(max_length=15, )
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS, )
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, blank=True, default=0, )
    identidade_transmissor = models.CharField(max_length=20, blank=True, null=True, )
    codigo_status = models.IntegerField(choices=CODIGO_STATUS_EFDREINF, blank=True, null=True, )
    retorno_descricao = models.TextField(blank=True, null=True, )
    recepcao_data_hora = models.DateTimeField(blank=True, null=True, )
    recepcao_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True, )
    protocolo = models.CharField(max_length=50, blank=True, null=True, )
    numero_protocolo_fechamento = models.CharField(max_length=50, blank=True, null=True, )
    processamento_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True, )
    tempo_estimado_conclusao = models.IntegerField(blank=True, null=True, )
    arquivo_header = models.CharField(max_length=200, blank=True, null=True, )
    arquivo_request = models.CharField(max_length=200, blank=True, null=True, )
    arquivo_response = models.CharField(max_length=200, blank=True, null=True, )
    data_hora_envio = models.DateTimeField(blank=True, null=True, )
    data_hora_consulta = models.DateTimeField(blank=True, null=True, )
    retorno_envio_json = JSONField("retorno_envio_json", blank=True, null=True)
    retorno_consulta_json = JSONField("retorno_consulta_json", blank=True, null=True)
    ocorrencias_json = JSONField("ocorrencias_json", blank=True, null=True)

    def __unicode__(self):
        return unicode(self.transmissor) + ' - ' + unicode(self.contribuinte_tpinsc) + ' - ' + unicode(self.contribuinte_nrinsc) + ' - ' + unicode(self.identidade_transmissor) + ' - ' + unicode(self.codigo_status) + ' - ' + unicode(self.retorno_descricao)

    class Meta:

        verbose_name = u'Transmissor do EFD-Reinf'
        verbose_name_plural = u'Transmissor do EFD-Reinf'
        db_table = r'transmissor_lote_efdreinf'
        managed = True # transmissor_lote_efdreinf #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_TransmissorLoteEfdreinf", u"Pode ver listagem do modelo TRANSMISSORLOTEEFDREINF"),
            ("can_see_data_TransmissorLoteEfdreinf", u"Pode visualizar o conteúdo do modelo TRANSMISSORLOTEEFDREINF"),
            ("can_see_menu_TransmissorLoteEfdreinf", u"Pode visualizar no menu o modelo TRANSMISSORLOTEEFDREINF"),
            ("can_print_list_TransmissorLoteEfdreinf", u"Pode imprimir listagem do modelo TRANSMISSORLOTEEFDREINF"),
            ("can_print_data_TransmissorLoteEfdreinf", u"Pode imprimir o conteúdo do modelo TRANSMISSORLOTEEFDREINF"), )

        ordering = [ ]



class TransmissorLoteEfdreinfSerializer(ModelSerializer):

    class Meta:

        model = TransmissorLoteEfdreinf
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


class TransmissorLoteEsocial(SoftDeletionModel):

    transmissor = models.ForeignKey('mensageiro.TransmissorLote',
        related_name='%(class)s_transmissor', blank=True, null=True, )
    empregador_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    empregador_nrinsc = models.CharField(max_length=15, )
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS, )
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, blank=True, default=0, )
    resposta_codigo = models.IntegerField(choices=CODIGO_RESPOSTA, blank=True, null=True, )
    resposta_descricao = models.TextField(blank=True, null=True, )
    recepcao_data_hora = models.DateTimeField(blank=True, null=True, )
    recepcao_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True, )
    protocolo = models.CharField(max_length=50, blank=True, null=True, )
    processamento_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True, )
    tempo_estimado_conclusao = models.IntegerField(blank=True, null=True, )
    arquivo_header = models.CharField(max_length=200, blank=True, null=True, )
    arquivo_request = models.CharField(max_length=200, blank=True, null=True, )
    arquivo_response = models.CharField(max_length=200, blank=True, null=True, )
    data_hora_envio = models.DateTimeField(blank=True, null=True, )
    data_hora_consulta = models.DateTimeField(blank=True, null=True, )
    retorno_envio_json = JSONField("retorno_envio_json", blank=True, null=True)
    retorno_consulta_json = JSONField("retorno_consulta_json", blank=True, null=True)
    ocorrencias_json = JSONField("ocorrencias_json", blank=True, null=True)

    def __unicode__(self):
        return unicode(self.transmissor) + ' - ' + unicode(self.empregador_tpinsc) + ' - ' + unicode(self.empregador_nrinsc) + ' - ' + unicode(self.resposta_codigo) + ' - ' + unicode(self.resposta_descricao)

    class Meta:

        verbose_name = u'Transmissor do eSocial'
        verbose_name_plural = u'Transmissor do eSocial'
        db_table = r'transmissor_lote_esocial'
        managed = True # transmissor_lote_esocial #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_see_list_TransmissorLoteEsocial", u"Pode ver listagem do modelo TRANSMISSORLOTEESOCIAL"),
            ("can_see_data_TransmissorLoteEsocial", u"Pode visualizar o conteúdo do modelo TRANSMISSORLOTEESOCIAL"),
            ("can_see_menu_TransmissorLoteEsocial", u"Pode visualizar no menu o modelo TRANSMISSORLOTEESOCIAL"),
            ("can_print_list_TransmissorLoteEsocial", u"Pode imprimir listagem do modelo TRANSMISSORLOTEESOCIAL"),
            ("can_print_data_TransmissorLoteEsocial", u"Pode imprimir o conteúdo do modelo TRANSMISSORLOTEESOCIAL"), )

        ordering = [ ]



class TransmissorLoteEsocialSerializer(ModelSerializer):

    class Meta:

        model = TransmissorLoteEsocial
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')


TPINSC_TRANSMISSOR_EVENTOS = (
    ('1', u'1 - CNPJ'),
    ('2', u'2 - CPF'),
    ('3', u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    ('4', u'4 - CNO (Cadastro Nacional de Obra)'),
)

TIPO_TRANSMISSOR_EVENTOS = (
    ('esocial', u'eSocial'),
    ('efdreinf', u'EFD-Reinf'),
)




class TransmissorEventosEsocial(SoftDeletionModel):

    from emensageriapro.esocial.models import EVENTO_STATUS

    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    transmissor_lote_esocial_error = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial_error', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    data_hora_envio = models.DateTimeField(blank=True, null=True, )
    data_hora_consulta = models.DateTimeField(blank=True, null=True, )
    retorno_envio_json = JSONField("retorno_envio_json", blank=True, null=True)
    retorno_consulta_json = JSONField("retorno_consulta_json", blank=True, null=True)
    evento_json = JSONField("evento_json", blank=True, null=True)
    ocorrencias_json = JSONField("ocorrencias_json", blank=True, null=True)

    def tabela_desvincular_evento(self):
        return self.tabela + '_desvincular_evento'

    def tabela_validar_api(self):
        return self.tabela + '_validar_evento_api'

    def tabela_salvar_tab(self):
        return self.tabela + '_salvar_tab'

    def tabela_validar(self):
        return self.tabela + '_validar_evento'

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:

        db_table = r'vw_transmissor_eventos_esocial'
        managed = False


class TransmissorEventosEfdreinf(SoftDeletionModel):

    from emensageriapro.esocial.models import EVENTO_STATUS

    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    transmissor_lote_efdreinf_error = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf_error', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    data_hora_envio = models.DateTimeField(blank=True, null=True, )
    data_hora_consulta = models.DateTimeField(blank=True, null=True, )
    retorno_envio_json = JSONField("retorno_envio_json", blank=True, null=True)
    retorno_consulta_json = JSONField("retorno_consulta_json", blank=True, null=True)
    evento_json = JSONField("evento_json", blank=True, null=True)
    ocorrencias_json = JSONField("ocorrencias_json", blank=True, null=True)

    def tabela_desvincular_evento(self):
        return self.tabela + '_desvincular_evento'

    def tabela_validar_api(self):
        return self.tabela + '_validar_evento_api'

    def tabela_salvar_tab(self):
        return self.tabela + '_salvar_tab'

    def tabela_validar(self):
        return self.tabela + '_validar_evento'

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:

        db_table = r'vw_transmissor_eventos_efdreinf'
        managed = False



class TransmissorEventosEsocialTotalizacoes(SoftDeletionModel):

    from emensageriapro.esocial.models import EVENTO_STATUS

    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)

    def url_recibo(self):
        return None

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_salvar_tab(self):
        return self.tabela + '_salvar_tab'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:

        db_table = r'vw_transmissor_eventos_esocial_totalizacoes'
        managed = False


class TransmissorEventosEfdreinfTotalizacoes(SoftDeletionModel):

    from emensageriapro.esocial.models import EVENTO_STATUS

    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)

    def url_recibo(self):
        return None

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_salvar_tab(self):
        return self.tabela + '_salvar_tab'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:

        db_table = r'vw_transmissor_eventos_efdreinf_totalizacoes'
        managed = False


class Certificados(SoftDeletionModel):

    nome = models.CharField(max_length=300, )
    from django.core.files.storage import FileSystemStorage
    from emensageriapro.settings import BASE_DIR
    fs_certificado = FileSystemStorage(location=BASE_DIR+'/certificado/')
    certificado = models.FileField(storage=fs_certificado)
    senha = models.CharField(max_length=300, blank=True, null=True, )

    def __unicode__(self):

        lista = [
            unicode(self.nome),]

        if lista:
            return ' - '.join(lista)

        else:
            return self.id

    class Meta:

        verbose_name = u'Certificados'
        verbose_name_plural = u'Certificados'
        db_table = r'certificados'
        managed = True # certificados #

        unique_together = ( )

        index_together = ()

        permissions = (
            ("can_view_certificados", "Can view certificados"), )

        ordering = [
            'nome', ]



class CertificadosSerializer(ModelSerializer):

    class Meta:

        model = Certificados
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'criado_por',
                            'modificado_em', 'modificado_por',
                            'desativado_em', 'desativado_por', 'ativo')