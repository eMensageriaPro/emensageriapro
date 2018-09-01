# coding: utf-8
from django import forms
from emensageriapro.esocial.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.mensageiro.models import TransmissorLoteEsocial 
from emensageriapro.mensageiro.models import RetornosEventos 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s5012_evtirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5012_evtirrf,self ).__init__(*args,**kwargs)
        
        self.fields['indexistinfo'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s5012evtIrrf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s5011evtCS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s5002evtIrrfBenef
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s5001evtBasesTrab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s3000evtExclusao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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


class form_s2400_evtcdbenprrp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_evtcdbenprrp,self ).__init__(*args,**kwargs)
        
        self.fields['tpplanrp'].widget.attrs['required'] = True
        
        self.fields['paisnac'].widget.attrs['required'] = True
        
        self.fields['paisnascto'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2400evtCdBenPrRP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2399evtTSVTermino
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2306evtTSVAltContr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2300evtTSVInicio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2299evtDeslig
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2298evtReintegr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2260evtConvInterm
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2250evtAvPrevio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2241evtInsApo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2240evtExpRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2230evtAfastTemp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['nmmed'].widget.attrs['required'] = True
        
        self.fields['frmctt'].widget.attrs['required'] = True
        
        self.fields['resaso'].widget.attrs['required'] = True
        
        self.fields['tpaso'].widget.attrs['required'] = True
        
        self.fields['dtaso'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2220evtMonit
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['tplocal'].widget.attrs['required'] = True
        
        self.fields['iniciatcat'].widget.attrs['required'] = True
        
        self.fields['indcomunpolicia'].widget.attrs['required'] = True
        
        self.fields['indcatobito'].widget.attrs['required'] = True
        
        self.fields['tpcat'].widget.attrs['required'] = True
        
        self.fields['hrstrabantesacid'].widget.attrs['required'] = True
        
        self.fields['hracid'].widget.attrs['required'] = True
        
        self.fields['tpacid'].widget.attrs['required'] = True
        
        self.fields['dtacid'].widget.attrs['required'] = True
        
        self.fields['cpftrab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['tpregistrador'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2210evtCAT
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2206evtAltContratual
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2205evtAltCadastral
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2200evtAdmissao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s2190evtAdmPrelim
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1300evtContrSindPatr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indapuracao'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['evtcontratavnp'].widget.attrs['required'] = True
        
        self.fields['evtcomprod'].widget.attrs['required'] = True
        
        self.fields['evtaqprod'].widget.attrs['required'] = True
        
        self.fields['evtpgtos'].widget.attrs['required'] = True
        
        self.fields['evtremun'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1299evtFechaEvPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1298evtReabreEvPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1295evtTotConting
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1280evtInfoComplPer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1270evtContratAvNP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1260evtComProd
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1250evtAqProd
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1210evtPgtos
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1207evtBenPrRP
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1202evtRmnRPPS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1200evtRemun
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True

    class Meta:
        model = s1080evtTabOperPort
        exclude = [ 
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
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1070evtTabProcesso
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1060evtTabAmbiente
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1050evtTabHorTur
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1040evtTabFuncao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1035evtTabCarreira
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1030evtTabCargo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1020evtTabLotacao
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1010evtTabRubrica
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1005evtTabEstab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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
        
        self.fields['status'].widget.attrs['required'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['status'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['required'] = True
        self.fields['versao'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_esocial'].queryset = TransmissorLoteEsocial.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_esocial'].widget.attrs['readonly'] = True

    class Meta:
        model = s1000evtInfoEmpregador
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
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

