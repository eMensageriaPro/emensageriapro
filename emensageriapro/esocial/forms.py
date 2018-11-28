# coding: utf-8
from django import forms
from emensageriapro.esocial.models import * 
from emensageriapro.mensageiro.models import TransmissorLoteEsocial 
from emensageriapro.mensageiro.models import RetornosEventos 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.tabelas.models import eSocialPaises 
from emensageriapro.tabelas.models import eSocialLogradourosTipos 


__author__ = 'marcelovasconcellos'

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

#custom_forms#



class form_s5013_evtfgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_evtfgts,self ).__init__(*args,**kwargs)
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5013evtFGTS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s5012_evtirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5012_evtirrf,self ).__init__(*args,**kwargs)
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5012evtIrrf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s5011_evtcs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5011_evtcs,self ).__init__(*args,**kwargs)
        
        self.fields['classtrib'].widget.attrs['required'] = True
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5011evtCS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s5003_evtbasesfgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_evtbasesfgts,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5003evtBasesFGTS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s5002_evtirrfbenef(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_evtirrfbenef,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5002evtIrrfBenef
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s5001_evtbasestrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5001_evtbasestrab,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['nrrecarqbase'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s5001evtBasesTrab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s3000_evtexclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s3000_evtexclusao,self ).__init__(*args,**kwargs)
        
        self.fields['nrrecevt'].widget.attrs['required'] = True
        
        self.fields['tpevento'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s3000evtExclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2420_evtcdbenterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2420_evtcdbenterm,self ).__init__(*args,**kwargs)
        
        self.fields['mtvtermino'].widget.attrs['required'] = True
        
        self.fields['dttermbeneficio'].widget.attrs['required'] = True
        
        self.fields['nrbeneficio'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2420evtCdBenTerm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2416_evtcdbenalt(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2416_evtcdbenalt,self ).__init__(*args,**kwargs)
        
        self.fields['indsuspensao'].widget.attrs['required'] = True
        
        self.fields['indhomologtc'].widget.attrs['required'] = True
        
        self.fields['inddecjud'].widget.attrs['required'] = True
        
        self.fields['tpplanrp'].widget.attrs['required'] = True
        
        self.fields['tpbeneficio'].widget.attrs['required'] = True
        
        self.fields['dtaltbeneficio'].widget.attrs['required'] = True
        
        self.fields['nrbeneficio'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2416evtCdBenAlt
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2410_evtcdbenin(forms.ModelForm):
    vrbeneficio = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2410_evtcdbenin,self ).__init__(*args,**kwargs)
        
        self.fields['indhomologtc'].widget.attrs['required'] = True
        
        self.fields['inddecjud'].widget.attrs['required'] = True
        
        self.fields['tpplanrp'].widget.attrs['required'] = True
        
        self.fields['vrbeneficio'].widget.attrs['required'] = True
        
        self.fields['tpbeneficio'].widget.attrs['required'] = True
        
        self.fields['dtinibeneficio'].widget.attrs['required'] = True
        
        self.fields['nrbeneficio'].widget.attrs['required'] = True
        
        self.fields['cadini'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2410evtCdBenIn
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2405_evtcdbenefalt(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2405_evtcdbenefalt,self ).__init__(*args,**kwargs)
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['incfismen'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2405evtCdBenefAlt
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2400_evtcdbenefin(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_evtcdbenefin,self ).__init__(*args,**kwargs)
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['incfismen'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2400evtCdBenefIn
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2399_evttsvtermino(forms.ModelForm):
    vralim = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    percaliment = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2399_evttsvtermino,self ).__init__(*args,**kwargs)
        
        self.fields['dtterm'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2399evtTSVTermino
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2306_evttsvaltcontr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2306_evttsvaltcontr,self ).__init__(*args,**kwargs)
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2306evtTSVAltContr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2300_evttsvinicio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2300_evttsvinicio,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cadini'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2300evtTSVInicio
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2299_evtdeslig(forms.ModelForm):
    vralim = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    percaliment = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_evtdeslig,self ).__init__(*args,**kwargs)
        
        self.fields['indcumprparc'].widget.attrs['required'] = True
        
        self.fields['pensalim'].widget.attrs['required'] = True
        
        self.fields['indpagtoapi'].widget.attrs['required'] = True
        
        self.fields['dtdeslig'].widget.attrs['required'] = True
        
        self.fields['mtvdeslig'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2299evtDeslig
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2298_evtreintegr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2298_evtreintegr,self ).__init__(*args,**kwargs)
        
        self.fields['indpagtojuizo'].widget.attrs['required'] = True
        
        self.fields['dtefeito'].widget.attrs['required'] = True
        
        self.fields['dtefetretorno'].widget.attrs['required'] = True
        
        self.fields['tpreint'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2298evtReintegr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2260_evtconvinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2260_evtconvinterm,self ).__init__(*args,**kwargs)
        
        self.fields['indlocal'].widget.attrs['required'] = True
        
        self.fields['dtprevpgto'].widget.attrs['required'] = True
        
        self.fields['dtfim'].widget.attrs['required'] = True
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['codconv'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2260evtConvInterm
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2250_evtavprevio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2250_evtavprevio,self ).__init__(*args,**kwargs)
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2250evtAvPrevio
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2245_evttreicap(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2245_evttreicap,self ).__init__(*args,**kwargs)
        
        self.fields['codtreicap'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2245evtTreiCap
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2241_evtinsapo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_evtinsapo,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2241evtInsApo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2240_evtexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_evtexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dscativdes'].widget.attrs['required'] = True
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2240evtExpRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2231_evtcessao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2231_evtcessao,self ).__init__(*args,**kwargs)
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True

    class Meta:
        model = s2231evtCessao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2230_evtafasttemp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2230_evtafasttemp,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2230evtAfastTemp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2221_evttoxic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2221_evttoxic,self ).__init__(*args,**kwargs)
        
        self.fields['indrecusa'].widget.attrs['required'] = True
        
        self.fields['dtexame'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2221evtToxic
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2220_evtmonit(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2220_evtmonit,self ).__init__(*args,**kwargs)
        
        self.fields['ufcrm'].widget.attrs['required'] = True
        
        self.fields['nrcrm'].widget.attrs['required'] = True
        
        self.fields['nmresp'].widget.attrs['required'] = True
        
        self.fields['nrconsclasse'].widget.attrs['required'] = True
        
        self.fields['nisresp'].widget.attrs['required'] = True
        
        self.fields['ufcrm'].widget.attrs['required'] = True
        
        self.fields['nrcrm'].widget.attrs['required'] = True
        
        self.fields['nmmed'].widget.attrs['required'] = True
        
        self.fields['resaso'].widget.attrs['required'] = True
        
        self.fields['tpaso'].widget.attrs['required'] = True
        
        self.fields['dtaso'].widget.attrs['required'] = True
        
        self.fields['tpexameocup'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2220evtMonit
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2210_evtcat(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2210_evtcat,self ).__init__(*args,**kwargs)
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['tplocal'].widget.attrs['required'] = True
        
        self.fields['iniciatcat'].widget.attrs['required'] = True
        
        self.fields['codsitgeradora'].widget.attrs['required'] = True
        
        self.fields['indcomunpolicia'].widget.attrs['required'] = True
        
        self.fields['indcatobito'].widget.attrs['required'] = True
        
        self.fields['tpcat'].widget.attrs['required'] = True
        
        self.fields['hrstrabantesacid'].widget.attrs['required'] = True
        
        self.fields['tpacid'].widget.attrs['required'] = True
        
        self.fields['dtacid'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2210evtCAT
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2206_evtaltcontratual(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2206_evtaltcontratual,self ).__init__(*args,**kwargs)
        
        self.fields['tpcontr'].widget.attrs['required'] = True
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['tpregprev'].widget.attrs['required'] = True
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2206evtAltContratual
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2205_evtaltcadastral(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2205_evtaltcadastral,self ).__init__(*args,**kwargs)
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['dtalteracao'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2205evtAltCadastral
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2200_evtadmissao(forms.ModelForm):
    vrsalfx = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2200_evtadmissao,self ).__init__(*args,**kwargs)
        
        self.fields['tpcontr'].widget.attrs['required'] = True
        
        self.fields['undsalfixo'].widget.attrs['required'] = True
        
        self.fields['vrsalfx'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['cadini'].widget.attrs['required'] = True
        
        self.fields['tpregprev'].widget.attrs['required'] = True
        
        self.fields['tpregtrab'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['grauinstr'].widget.attrs['required'] = True
        
        self.fields['racacor'].widget.attrs['required'] = True
        
        self.fields['sexo'].widget.attrs['required'] = True
        
        self.fields['nmtrab'].widget.attrs['required'] = True
        
        self.fields['nistrab'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2200evtAdmissao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s2190_evtadmprelim(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2190_evtadmprelim,self ).__init__(*args,**kwargs)
        
        self.fields['dtadm'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s2190evtAdmPrelim
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1300_evtcontrsindpatr(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1300_evtcontrsindpatr,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1300evtContrSindPatr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1299_evtfechaevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1299_evtfechaevper,self ).__init__(*args,**kwargs)
        
        self.fields['evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['evtcontratavnp'].widget.attrs['required'] = True
        
        self.fields['evtcomprod'].widget.attrs['required'] = True
        
        self.fields['evtaqprod'].widget.attrs['required'] = True
        
        self.fields['evtpgtos'].widget.attrs['required'] = True
        
        self.fields['evtremun'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1299evtFechaEvPer
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1298_evtreabreevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1298_evtreabreevper,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1298evtReabreEvPer
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1295_evttotconting(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1295_evttotconting,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1295evtTotConting
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1280_evtinfocomplper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_evtinfocomplper,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1280evtInfoComplPer
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1270_evtcontratavnp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1270_evtcontratavnp,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1270evtContratAvNP
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1260_evtcomprod(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_evtcomprod,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscestabrural'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1260evtComProd
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1250_evtaqprod(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_evtaqprod,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscadq'].widget.attrs['required'] = True
        
        self.fields['tpinscadq'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1250evtAqProd
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1210_evtpgtos(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_evtpgtos,self ).__init__(*args,**kwargs)
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1210evtPgtos
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1207_evtbenprrp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1207_evtbenprrp,self ).__init__(*args,**kwargs)
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1207evtBenPrRP
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1202_evtrmnrpps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1202_evtrmnrpps,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1202evtRmnRPPS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1200_evtremun(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1200_evtremun,self ).__init__(*args,**kwargs)
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1200evtRemun
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1080_evttaboperport(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1080_evttaboperport,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1080evtTabOperPort
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1070_evttabprocesso(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1070_evttabprocesso,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1070evtTabProcesso
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1060_evttabambiente(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1060_evttabambiente,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1060evtTabAmbiente
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1050_evttabhortur(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1050_evttabhortur,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1050evtTabHorTur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1040_evttabfuncao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1040_evttabfuncao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1040evtTabFuncao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1035_evttabcarreira(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1035_evttabcarreira,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1035evtTabCarreira
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1030_evttabcargo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1030_evttabcargo,self ).__init__(*args,**kwargs)
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1030evtTabCargo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1020_evttablotacao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1020_evttablotacao,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1020evtTabLotacao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1010_evttabrubrica(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1010_evttabrubrica,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1010evtTabRubrica
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1005_evttabestab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1005_evttabestab,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1005evtTabEstab
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]


class form_s1000_evtinfoempregador(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1000_evtinfoempregador,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = s1000evtInfoEmpregador
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'recibo_hash',
            'recibo_numero',
            'processamento_data_hora',
            'processamento_versao_app_processamento',
            'processamento_descricao_resposta',
            'processamento_codigo_resposta',
            'recepcao_protocolo_envio_lote',
            'recepcao_versao_app',
            'recepcao_data_hora',
            'recepcao_tp_amb',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_eventos',
 
        ]

