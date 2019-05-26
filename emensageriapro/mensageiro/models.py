#coding:utf-8
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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Arquivos'
        db_table = r'arquivos'       
        managed = True # arquivos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_arquivos", "Can view arquivos"),)
            
        ordering = []



class ArquivosSerializer(ModelSerializer):

    class Meta:
    
        model = Arquivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class Certificados(SoftDeletionModel):

    nome = models.CharField(max_length=300, )
    from django.core.files.storage import FileSystemStorage
    from emensageriapro.settings import BASE_DIR
    fs_certificado = FileSystemStorage(location=BASE_DIR+'/certificado/')
    certificado = models.FileField(storage=fs_certificado)
    senha = models.CharField(max_length=300, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.nome),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Certificados'
        db_table = r'certificados'       
        managed = True # certificados #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_certificados", "Can view certificados"), )
        
        ordering = [
            'nome',]
            
            
 
class CertificadosSerializer(ModelSerializer):

    class Meta:
    
        model = Certificados
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.arquivo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Importação de Arquivos'
        db_table = r'importacao_arquivos'       
        managed = True # importacao_arquivos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_importacao_arquivos", "Can view importacao_arquivos"),)
            
        ordering = [
            'arquivo',]



class ImportacaoArquivosSerializer(ModelSerializer):

    class Meta:
    
        model = ImportacaoArquivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.importacao_arquivos),
            unicode(self.arquivo),
            unicode(self.evento),
            unicode(self.versao),
            unicode(self.identidade_evento),
            unicode(self.identidade),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Eventos de Arquivos Importados'
        db_table = r'importacao_arquivos_eventos'       
        managed = True # importacao_arquivos_eventos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_importacao_arquivos_eventos", "Can view importacao_arquivos_eventos"),)
            
        ordering = [
            'importacao_arquivos',
            'arquivo',
            'evento',
            'versao',
            'identidade_evento',
            'identidade',]



class ImportacaoArquivosEventosSerializer(ModelSerializer):

    class Meta:
    
        model = ImportacaoArquivosEventos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.evento),
            unicode(self.versao),
            unicode(self.numero),
            unicode(self.registro_campo),
            unicode(self.registro_pai),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Regras de Validação'
        db_table = r'regras_validacao'       
        managed = True # regras_validacao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_regras_validacao", "Can view regras_validacao"),)
            
        ordering = []



class RegrasDeValidacaoSerializer(ModelSerializer):

    class Meta:
    
        model = RegrasDeValidacao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class Relatorios(SoftDeletionModel):

    titulo = models.CharField(max_length=500, )
    campos = models.CharField(max_length=500, )
    sql = models.TextField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Relatórios'
        db_table = r'relatorios'       
        managed = True # relatorios #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_relatorios", "Can view relatorios"),)
            
        ordering = []



class RelatoriosSerializer(ModelSerializer):

    class Meta:
    
        model = Relatorios
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class RetornosEventos(SoftDeletionModel):

    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', )
    identidade = models.CharField(max_length=36, blank=True, null=True, )
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True, )
    recepcao_data_hora = models.DateTimeField(blank=True, null=True, )
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True, )
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True, )
    processamento_codigo_resposta = models.CharField(max_length=10, blank=True, null=True, )
    processamento_descricao_resposta = models.TextField(blank=True, null=True, )
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True, )
    processamento_data_hora = models.DateTimeField(blank=True, null=True, )
    recibo_numero = models.CharField(max_length=100, blank=True, null=True, )
    recibo_hash = models.CharField(max_length=100, blank=True, null=True, )
    tpinsc = models.IntegerField(choices=CHOICES_TPINSC, blank=True, null=True, )
    empregador_tpinsc = models.IntegerField(choices=CHOICES_TPINSC, blank=True, null=True, )
    nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    empregador_nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    cpftrab = models.CharField(max_length=11, blank=True, null=True, )
    nistrab = models.CharField(max_length=11, blank=True, null=True, )
    nmtrab = models.CharField(max_length=70, blank=True, null=True, )
    infocota = models.CharField(choices=CHOICES_INFOCOTA, max_length=50, blank=True, null=True, )
    matricula = models.CharField(max_length=30, blank=True, null=True, )
    dtadm = models.DateField(blank=True, null=True, )
    tpregjor = models.IntegerField(choices=CHOICES_TPREGJOR, blank=True, null=True, )
    dtbase = models.IntegerField(blank=True, null=True, )
    cnpjsindcategprof = models.CharField(max_length=14, blank=True, null=True, )
    dtposse = models.DateField(blank=True, null=True, )
    dtexercicio = models.DateField(blank=True, null=True, )
    codcargo = models.CharField(max_length=30, blank=True, null=True, )
    nmcargo = models.CharField(max_length=100, blank=True, null=True, )
    codcbocargo = models.CharField(max_length=6, blank=True, null=True, )
    codfuncao = models.CharField(max_length=30, blank=True, null=True, )
    dscfuncao = models.CharField(max_length=100, blank=True, null=True, )
    codcbofuncao = models.CharField(max_length=6, blank=True, null=True, )
    codcateg = models.IntegerField(blank=True, null=True, )
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    undsalfixo = models.IntegerField(choices=CHOICES_UNDSALFIXO, blank=True, null=True, )
    dscsalvar = models.CharField(max_length=255, blank=True, null=True, )
    tpcontr = models.IntegerField(choices=CHOICES_TPCONTR, blank=True, null=True, )
    dtterm = models.DateField(blank=True, null=True, )
    clauasseg = models.CharField(max_length=50, blank=True, null=True, )
    local_tpinsc = models.IntegerField(choices=CHOICES_TPINSC, blank=True, null=True, )
    local_nrinsc = models.CharField(max_length=15, blank=True, null=True, )
    local_cnae = models.IntegerField(blank=True, null=True, )
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    tpjornada = models.IntegerField(choices=CHOICES_TPJORNADA, blank=True, null=True, )
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True, )
    tmpparc = models.IntegerField(choices=CHOICES_TMPPARC, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.transmissor_lote_esocial),
            unicode(self.identidade),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Retornos dos Eventos'
        db_table = r'retornos_eventos'       
        managed = True # retornos_eventos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_retornos_eventos", "Can view retornos_eventos"),)
            
        ordering = [
            'transmissor_lote_esocial',
            'identidade',]



class RetornosEventosSerializer(ModelSerializer):

    class Meta:
    
        model = RetornosEventos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class RetornosEventosHorarios(SoftDeletionModel):

    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True, )
    dia = models.IntegerField(choices=CHOICES_DIA, blank=True, null=True, )
    codhorcontrat = models.CharField(max_length=30, blank=True, null=True, )
    hrentr = models.CharField(max_length=50, blank=True, null=True, )
    hrsaida = models.CharField(max_length=50, blank=True, null=True, )
    durjornada = models.IntegerField(blank=True, null=True, )
    perhorflexivel = models.CharField(choices=CHOICES_PERHORFLEXIVEL, max_length=50, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Retornos dos Eventos - Horários'
        db_table = r'retornos_eventos_horarios'       
        managed = True # retornos_eventos_horarios #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_retornos_eventos_horarios", "Can view retornos_eventos_horarios"),)
            
        ordering = []



class RetornosEventosHorariosSerializer(ModelSerializer):

    class Meta:
    
        model = RetornosEventosHorarios
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class RetornosEventosIntervalos(SoftDeletionModel):

    retornos_eventos_horarios = models.ForeignKey('mensageiro.RetornosEventosHorarios',
        related_name='%(class)s_retornos_eventos_horarios', blank=True, null=True, )
    tpinterv = models.IntegerField(choices=CHOICES_TPINTERV, blank=True, null=True, )
    durinterv = models.IntegerField(blank=True, null=True, )
    iniinterv = models.CharField(max_length=50, blank=True, null=True, )
    terminterv = models.CharField(max_length=50, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Retornos dos Eventos - Intervalos'
        db_table = r'retornos_eventos_intervalos'       
        managed = True # retornos_eventos_intervalos #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_retornos_eventos_intervalos", "Can view retornos_eventos_intervalos"),)
            
        ordering = []



class RetornosEventosIntervalosSerializer(ModelSerializer):

    class Meta:
    
        model = RetornosEventosIntervalos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class RetornosEventosOcorrencias(SoftDeletionModel):

    retornos_eventos = models.ForeignKey('mensageiro.RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, )
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA, blank=True, )
    codigo = models.IntegerField(blank=True, )
    descricao = models.TextField(blank=True, )
    localizacao = models.TextField(blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Retornos dos Eventos - Ocorrencias'
        db_table = r'retornos_eventos_ocorrencias'       
        managed = True # retornos_eventos_ocorrencias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_retornos_eventos_ocorrencias", "Can view retornos_eventos_ocorrencias"),)
            
        ordering = []



class RetornosEventosOcorrenciasSerializer(ModelSerializer):

    class Meta:
    
        model = RetornosEventosOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class TransmissorLote(SoftDeletionModel):

    transmissor_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    transmissor_nrinsc = models.CharField(max_length=20, )
    nome_empresa = models.CharField(max_length=200, )
    data_abertura = models.DateField()
    validar_eventos = models.IntegerField(choices=SIM_NAO, )
    verificar_predecessao = models.IntegerField(choices=SIM_NAO, )
    envio_automatico = models.IntegerField(choices=SIM_NAO, )
    logotipo = models.FileField(upload_to="logotipo", blank=True, null=True, )
    endereco_completo = models.TextField()
    empregador_nrinsc = models.CharField(max_length=20, )
    empregador_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    esocial_lote_min = models.IntegerField()
    esocial_lote_max = models.IntegerField()
    esocial_timeout = models.DecimalField(max_digits=15, decimal_places=2, )
    esocial_intervalo = models.IntegerField()
    esocial_tempo_prox_envio = models.IntegerField(blank=True, null=True, )
    esocial_certificado = models.ForeignKey('mensageiro.Certificados',
        related_name='%(class)s_esocial_certificado', blank=True, null=True, )
    esocial_pasta = models.CharField(max_length=200, blank=True, null=True, )
    contribuinte_nrinsc = models.CharField(max_length=20, )
    contribuinte_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO, )
    efdreinf_lote_min = models.IntegerField()
    efdreinf_lote_max = models.IntegerField()
    efdreinf_timeout = models.DecimalField(max_digits=15, decimal_places=2, )
    efdreinf_intervalo = models.IntegerField()
    efdreinf_tempo_prox_envio = models.IntegerField(blank=True, null=True, )
    efdreinf_certificado = models.ForeignKey('mensageiro.Certificados',
        related_name='%(class)s_efdreinf_certificado', blank=True, null=True, )
    efdreinf_pasta = models.CharField(max_length=200, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.transmissor_nrinsc),
            unicode(self.nome_empresa),
            unicode(self.empregador_nrinsc),
            unicode(self.contribuinte_nrinsc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Transmissor'
        db_table = r'transmissores'       
        managed = True # transmissores #
        
        unique_together = (
            ('nome_empresa', 'excluido'),)
            
        index_together = ()
        
        permissions = (
            ("can_view_transmissores", "Can view transmissores"),)
            
        ordering = []



class TransmissorLoteSerializer(ModelSerializer):

    class Meta:
    
        model = TransmissorLote
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.transmissor),
            unicode(self.contribuinte_tpinsc),
            unicode(self.contribuinte_nrinsc),
            unicode(self.identidade_transmissor),
            unicode(self.codigo_status),
            unicode(self.retorno_descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Transmissor do EFD-Reinf'
        db_table = r'transmissor_lote_efdreinf'       
        managed = True # transmissor_lote_efdreinf #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_transmissor_lote_efdreinf", "Can view transmissor_lote_efdreinf"),)
            
        ordering = []



class TransmissorLoteEfdreinfSerializer(ModelSerializer):

    class Meta:
    
        model = TransmissorLoteEfdreinf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class TransmissorLoteEfdreinfOcorrencias(SoftDeletionModel):

    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', )
    resposta_codigo = models.CharField(max_length=50, )
    descricao = models.TextField()
    tipo = models.IntegerField(choices=EVENTOS_OCORRENCIAS_TIPO_EFDREINF, )
    localizacao = models.CharField(max_length=50, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Ocorrências do Transmissor de Lote do EFD-Reinf'
        db_table = r'transmissor_lote_efdreinf_ocorrencias'       
        managed = True # transmissor_lote_efdreinf_ocorrencias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_transmissor_lote_efdreinf_ocorrencias", "Can view transmissor_lote_efdreinf_ocorrencias"),)
            
        ordering = []



class TransmissorLoteEfdreinfOcorrenciasSerializer(ModelSerializer):

    class Meta:
    
        model = TransmissorLoteEfdreinfOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.transmissor),
            unicode(self.empregador_tpinsc),
            unicode(self.empregador_nrinsc),
            unicode(self.resposta_codigo),
            unicode(self.resposta_descricao),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Transmissor do eSocial'
        db_table = r'transmissor_lote_esocial'       
        managed = True # transmissor_lote_esocial #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_transmissor_lote_esocial", "Can view transmissor_lote_esocial"),)
            
        ordering = []



class TransmissorLoteEsocialSerializer(ModelSerializer):

    class Meta:
    
        model = TransmissorLoteEsocial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class TransmissorLoteEsocialOcorrencias(SoftDeletionModel):

    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', )
    resposta_codigo = models.CharField(max_length=50, )
    descricao = models.TextField()
    tipo = models.IntegerField(choices=EVENTOS_OCORRENCIAS_TIPO, )
    localizacao = models.CharField(max_length=50, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = []
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id

    class Meta:
    
        verbose_name = u'Ocorrências do Transmissor de Lote do eSocial'
        db_table = r'transmissor_lote_esocial_ocorrencias'       
        managed = True # transmissor_lote_esocial_ocorrencias #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_transmissor_lote_esocial_ocorrencias", "Can view transmissor_lote_esocial_ocorrencias"),)
            
        ordering = []



class TransmissorLoteEsocialOcorrenciasSerializer(ModelSerializer):

    class Meta:
    
        model = TransmissorLoteEsocialOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


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




class TransmissorEventosEsocial(models.Model):
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
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'
        
    class Meta:
        db_table = r'transmissor_eventos_esocial'
        managed = False


class TransmissorEventosEfdreinf(models.Model):
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
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    
    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True)
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True)
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True)
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True)
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True)
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True)
        
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_efdreinf'
        managed = False
        
        

class TransmissorEventosEsocialTotalizacoes(models.Model):
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
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_esocial_totalizacoes'
        managed = False


class TransmissorEventosEfdreinfTotalizacoes(models.Model):
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
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    
    # retornos_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
    #     related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    # retornos_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
    #     related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)

    retornos_r5001 = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_r5001', blank=True, null=True)
    retornos_r5011 = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_r5011', blank=True, null=True)
    retornos_r9001 = models.ForeignKey('efdreinf.r9001evtTotal',
        related_name='%(class)s_retornos_r9001', blank=True, null=True)
    retornos_r9002 = models.ForeignKey('efdreinf.r9002evtRet',
        related_name='%(class)s_retornos_r9002', blank=True, null=True)
    retornos_r9011 = models.ForeignKey('efdreinf.r9011evtTotalContrib',
        related_name='%(class)s_retornos_r9011', blank=True, null=True)
    retornos_r9012 = models.ForeignKey('efdreinf.r9012evtRetCons',
        related_name='%(class)s_retornos_r9012', blank=True, null=True)
        
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_efdreinf_totalizacoes'
        managed = False