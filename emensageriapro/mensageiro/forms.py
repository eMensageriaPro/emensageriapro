# coding: utf-8
from django import forms
from django.utils import timezone
from emensageriapro.mensageiro.models import *


__author__ = 'marcelovasconcellos'


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






class form_arquivos(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_arquivos, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_arquivos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = Arquivos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_certificados(forms.ModelForm):

    from django.forms import ModelForm, PasswordInput
    senha = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
    
        super(form_certificados, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_certificados, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = Certificados
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'senha']


class form_importacao_arquivos(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_importacao_arquivos, self).__init__(*args, **kwargs)
        
        self.fields['arquivo'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True
        self.fields['data_hora'].widget.attrs['readonly'] = True
        self.fields['importado_por'].widget.attrs['readonly'] = True
        self.fields['importado_por'].widget.attrs['disabled'] = True
        self.fields['quant_total'].widget.attrs['readonly'] = True
        self.fields['quant_aguardando'].widget.attrs['readonly'] = True
        self.fields['quant_importado'].widget.attrs['readonly'] = True
        self.fields['quant_erros'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_importacao_arquivos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = ImportacaoArquivos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'quant_processado']


class form_importacao_arquivos_eventos(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_importacao_arquivos_eventos, self).__init__(*args, **kwargs)
        
        self.fields['importacao_arquivos'].widget.attrs['readonly'] = True
        self.fields['importacao_arquivos'].widget.attrs['disabled'] = True
        self.fields['arquivo'].widget.attrs['readonly'] = True
        self.fields['evento'].widget.attrs['readonly'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['identidade_evento'].widget.attrs['readonly'] = True
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True
        self.fields['data_hora'].widget.attrs['readonly'] = True
        self.fields['validacoes'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_importacao_arquivos_eventos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = ImportacaoArquivosEventos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_regras_validacao(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_regras_validacao, self).__init__(*args, **kwargs)
        
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['obrigatorio'].widget.attrs['readonly'] = True
        self.fields['obrigatorio'].widget.attrs['disabled'] = True
        self.fields['descricao'].widget.attrs['readonly'] = True
        self.fields['tabela'].widget.attrs['readonly'] = True
        self.fields['valores_validos'].widget.attrs['readonly'] = True
        self.fields['validacoes_precedencia'].widget.attrs['readonly'] = True
        self.fields['validacoes'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_regras_validacao, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = RegrasDeValidacao
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_relatorios(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_relatorios, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_relatorios, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = Relatorios
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_retornos_eventos(forms.ModelForm):

    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdhrssem = forms.DecimalField(max_digits=15, decimal_places=2, localize=True, required=False, )

    def __init__(self, *args, **kwargs):
    
        super(form_retornos_eventos, self).__init__(*args, **kwargs)
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        self.fields['recepcao_tp_amb'].widget.attrs['readonly'] = True
        self.fields['recepcao_tp_amb'].widget.attrs['disabled'] = True
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        self.fields['recepcao_versao_app'].widget.attrs['readonly'] = True
        self.fields['recepcao_protocolo_envio_lote'].widget.attrs['readonly'] = True
        self.fields['processamento_codigo_resposta'].widget.attrs['readonly'] = True
        self.fields['processamento_descricao_resposta'].widget.attrs['readonly'] = True
        self.fields['processamento_versao_app_processamento'].widget.attrs['readonly'] = True
        self.fields['processamento_data_hora'].widget.attrs['readonly'] = True
        self.fields['recibo_numero'].widget.attrs['readonly'] = True
        self.fields['recibo_hash'].widget.attrs['readonly'] = True
        self.fields['tpinsc'].widget.attrs['readonly'] = True
        self.fields['tpinsc'].widget.attrs['disabled'] = True
        self.fields['empregador_tpinsc'].widget.attrs['readonly'] = True
        self.fields['empregador_tpinsc'].widget.attrs['disabled'] = True
        self.fields['nrinsc'].widget.attrs['readonly'] = True
        self.fields['empregador_nrinsc'].widget.attrs['readonly'] = True
        self.fields['cpftrab'].widget.attrs['readonly'] = True
        self.fields['nistrab'].widget.attrs['readonly'] = True
        self.fields['nmtrab'].widget.attrs['readonly'] = True
        self.fields['infocota'].widget.attrs['readonly'] = True
        self.fields['infocota'].widget.attrs['disabled'] = True
        self.fields['matricula'].widget.attrs['readonly'] = True
        self.fields['dtadm'].widget.attrs['readonly'] = True
        self.fields['tpregjor'].widget.attrs['readonly'] = True
        self.fields['tpregjor'].widget.attrs['disabled'] = True
        self.fields['dtbase'].widget.attrs['readonly'] = True
        self.fields['cnpjsindcategprof'].widget.attrs['readonly'] = True
        self.fields['dtposse'].widget.attrs['readonly'] = True
        self.fields['dtexercicio'].widget.attrs['readonly'] = True
        self.fields['codcargo'].widget.attrs['readonly'] = True
        self.fields['nmcargo'].widget.attrs['readonly'] = True
        self.fields['codcbocargo'].widget.attrs['readonly'] = True
        self.fields['codfuncao'].widget.attrs['readonly'] = True
        self.fields['dscfuncao'].widget.attrs['readonly'] = True
        self.fields['codcbofuncao'].widget.attrs['readonly'] = True
        self.fields['codcateg'].widget.attrs['readonly'] = True
        self.fields['vrsalfx'].widget.attrs['readonly'] = True
        self.fields['undsalfixo'].widget.attrs['readonly'] = True
        self.fields['undsalfixo'].widget.attrs['disabled'] = True
        self.fields['dscsalvar'].widget.attrs['readonly'] = True
        self.fields['tpcontr'].widget.attrs['readonly'] = True
        self.fields['tpcontr'].widget.attrs['disabled'] = True
        self.fields['dtterm'].widget.attrs['readonly'] = True
        self.fields['clauasseg'].widget.attrs['readonly'] = True
        self.fields['local_tpinsc'].widget.attrs['readonly'] = True
        self.fields['local_tpinsc'].widget.attrs['disabled'] = True
        self.fields['local_nrinsc'].widget.attrs['readonly'] = True
        self.fields['local_cnae'].widget.attrs['readonly'] = True
        self.fields['qtdhrssem'].widget.attrs['readonly'] = True
        self.fields['tpjornada'].widget.attrs['readonly'] = True
        self.fields['tpjornada'].widget.attrs['disabled'] = True
        self.fields['dsctpjorn'].widget.attrs['readonly'] = True
        self.fields['tmpparc'].widget.attrs['readonly'] = True
        self.fields['tmpparc'].widget.attrs['disabled'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_retornos_eventos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = RetornosEventos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_retornos_eventos_horarios(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_retornos_eventos_horarios, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_retornos_eventos_horarios, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = RetornosEventosHorarios
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_retornos_eventos_intervalos(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_retornos_eventos_intervalos, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_retornos_eventos_intervalos, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = RetornosEventosIntervalos
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_retornos_eventos_ocorrencias(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_retornos_eventos_ocorrencias, self).__init__(*args, **kwargs)
        
        self.fields['retornos_eventos'].widget.attrs['readonly'] = True
        self.fields['retornos_eventos'].widget.attrs['disabled'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['tipo'].widget.attrs['disabled'] = True
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['localizacao'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_retornos_eventos_ocorrencias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = RetornosEventosOcorrencias
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'descricao']


class form_transmissores(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_transmissores, self).__init__(*args, **kwargs)
        

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_transmissores, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = TransmissorLote
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',]


class form_transmissor_lote_efdreinf(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_transmissor_lote_efdreinf, self).__init__(*args, **kwargs)
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True
        self.fields['identidade_transmissor'].widget.attrs['readonly'] = True
        self.fields['codigo_status'].widget.attrs['readonly'] = True
        self.fields['codigo_status'].widget.attrs['disabled'] = True
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        self.fields['recepcao_versao_aplicativo'].widget.attrs['readonly'] = True
        self.fields['protocolo'].widget.attrs['readonly'] = True
        self.fields['numero_protocolo_fechamento'].widget.attrs['readonly'] = True
        self.fields['processamento_versao_aplicativo'].widget.attrs['readonly'] = True
        self.fields['tempo_estimado_conclusao'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_transmissor_lote_efdreinf, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = TransmissorLoteEfdreinf
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'retorno_descricao'
            'arquivo_header'
            'arquivo_request'
            'arquivo_response']


class form_transmissor_lote_efdreinf_ocorrencias(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_transmissor_lote_efdreinf_ocorrencias, self).__init__(*args, **kwargs)
        
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['disabled'] = True
        self.fields['transmissor_lote_efdreinf'].widget.attrs['required'] = True
        self.fields['resposta_codigo'].widget.attrs['readonly'] = True
        self.fields['resposta_codigo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['tipo'].widget.attrs['disabled'] = True
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['localizacao'].widget.attrs['readonly'] = True
        self.fields['localizacao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_transmissor_lote_efdreinf_ocorrencias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = TransmissorLoteEfdreinfOcorrencias
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'descricao']


class form_transmissor_lote_esocial(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_transmissor_lote_esocial, self).__init__(*args, **kwargs)
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['disabled'] = True
        self.fields['resposta_codigo'].widget.attrs['readonly'] = True
        self.fields['resposta_codigo'].widget.attrs['disabled'] = True
        self.fields['recepcao_data_hora'].widget.attrs['readonly'] = True
        self.fields['recepcao_versao_aplicativo'].widget.attrs['readonly'] = True
        self.fields['protocolo'].widget.attrs['readonly'] = True
        self.fields['processamento_versao_aplicativo'].widget.attrs['readonly'] = True
        self.fields['tempo_estimado_conclusao'].widget.attrs['readonly'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_transmissor_lote_esocial, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = TransmissorLoteEsocial
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'resposta_descricao'
            'arquivo_header'
            'arquivo_request'
            'arquivo_response']


class form_transmissor_lote_esocial_ocorrencias(forms.ModelForm):


    def __init__(self, *args, **kwargs):
    
        super(form_transmissor_lote_esocial_ocorrencias, self).__init__(*args, **kwargs)
        
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['disabled'] = True
        self.fields['transmissor_lote_esocial'].widget.attrs['required'] = True
        self.fields['resposta_codigo'].widget.attrs['readonly'] = True
        self.fields['resposta_codigo'].widget.attrs['required'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True
        self.fields['tipo'].widget.attrs['disabled'] = True
        self.fields['tipo'].widget.attrs['required'] = True
        self.fields['localizacao'].widget.attrs['readonly'] = True
        self.fields['localizacao'].widget.attrs['required'] = True

    def save(self, commit=True, *args, **kwargs):
    
        request = None
        
        if kwargs.has_key('request'):
        
            request = kwargs.pop('request')
        
        m =  super(form_transmissor_lote_esocial_ocorrencias, self).save(commit=True, *args, **kwargs)

        if request is not None:

            if m.criado_por_id is None:
                m.criado_por_id = request.user.id
                m.criado_em = timezone.now()
            m.modificado_por_id = request.user.id
            m.modificado_em = timezone.now()
            m.ativo = True
            m.save()
        
        return m
        
    class Meta:
    
        model = TransmissorLoteEsocialOcorrencias
        exclude = [ 
            'criado_em', 
            'criado_por',
            'modificado_em', 
            'modificado_por',
            'desativado_em', 
            'desativado_por',
            'descricao']