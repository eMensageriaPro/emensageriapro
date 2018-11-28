# coding: utf-8
from django import forms
from emensageriapro.efdreinf.models import * 
from emensageriapro.mensageiro.models import TransmissorLoteEfdreinf 


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



class form_r9000_evtexclusao(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r9000_evtexclusao,self ).__init__(*args,**kwargs)
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['nrrecevt'].widget.attrs['required'] = True
        
        self.fields['tpevento'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r9000evtExclusao
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r5011_evttotalcontrib(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r5011_evttotalcontrib,self ).__init__(*args,**kwargs)
        
        self.fields['hash'].widget.attrs['required'] = True
        
        self.fields['idev'].widget.attrs['required'] = True
        
        self.fields['tpev'].widget.attrs['required'] = True
        
        self.fields['dhprocess'].widget.attrs['required'] = True
        
        self.fields['nrprotentr'].widget.attrs['required'] = True
        
        self.fields['descretorno'].widget.attrs['required'] = True
        
        self.fields['cdretorno'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r5011evtTotalContrib
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r5001_evttotal(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r5001_evttotal,self ).__init__(*args,**kwargs)
        
        self.fields['hash'].widget.attrs['required'] = True
        
        self.fields['idev'].widget.attrs['required'] = True
        
        self.fields['tpev'].widget.attrs['required'] = True
        
        self.fields['dhprocess'].widget.attrs['required'] = True
        
        self.fields['descretorno'].widget.attrs['required'] = True
        
        self.fields['cdretorno'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r5001evtTotal
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r3010_evtespdesportivo(forms.ModelForm):
    vlrretparc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrreceitaclubes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrreceitatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r3010_evtespdesportivo,self ).__init__(*args,**kwargs)
        
        self.fields['vlrretparc'].widget.attrs['required'] = True
        
        self.fields['vlrreceitaclubes'].widget.attrs['required'] = True
        
        self.fields['vlrcp'].widget.attrs['required'] = True
        
        self.fields['vlrreceitatotal'].widget.attrs['required'] = True
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['dtapuracao'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r3010evtEspDesportivo
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2099_evtfechaevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2099_evtfechaevper,self ).__init__(*args,**kwargs)
        
        self.fields['evtcprb'].widget.attrs['required'] = True
        
        self.fields['evtcomprod'].widget.attrs['required'] = True
        
        self.fields['evtassdesprep'].widget.attrs['required'] = True
        
        self.fields['evtassdesprec'].widget.attrs['required'] = True
        
        self.fields['evtservpr'].widget.attrs['required'] = True
        
        self.fields['evtservtm'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2099evtFechaEvPer
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2098_evtreabreevper(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2098_evtreabreevper,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2098evtReabreEvPer
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2070_evtpgtosdivs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2070_evtpgtosdivs,self ).__init__(*args,**kwargs)
        
        self.fields['nmrazaobenef'].widget.attrs['required'] = True
        
        self.fields['codpgto'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2070evtPgtosDivs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2060_evtcprb(forms.ModelForm):
    vlrcprbsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpapurtotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrrecbrutatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2060_evtcprb,self ).__init__(*args,**kwargs)
        
        self.fields['vlrcpapurtotal'].widget.attrs['required'] = True
        
        self.fields['vlrrecbrutatotal'].widget.attrs['required'] = True
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2060evtCPRB
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2050_evtcomprod(forms.ModelForm):
    vlrsenarsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrratsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusptotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrsenarapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrratapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrrecbrutatotal = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2050_evtcomprod,self ).__init__(*args,**kwargs)
        
        self.fields['vlrsenarapur'].widget.attrs['required'] = True
        
        self.fields['vlrratapur'].widget.attrs['required'] = True
        
        self.fields['vlrcpapur'].widget.attrs['required'] = True
        
        self.fields['vlrrecbrutatotal'].widget.attrs['required'] = True
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2050evtComProd
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2040_evtassocdesprep(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2040_evtassocdesprep,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2040evtAssocDespRep
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2030_evtassocdesprec(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2030_evtassocdesprec,self ).__init__(*args,**kwargs)
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2030evtAssocDespRec
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2020_evtservprest(forms.ModelForm):
    vlrtotalnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_evtservprest,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotalretprinc'].widget.attrs['required'] = True
        
        self.fields['vlrtotalbaseret'].widget.attrs['required'] = True
        
        self.fields['vlrtotalbruto'].widget.attrs['required'] = True
        
        self.fields['indobra'].widget.attrs['required'] = True
        
        self.fields['nrinsctomador'].widget.attrs['required'] = True
        
        self.fields['tpinsctomador'].widget.attrs['required'] = True
        
        self.fields['nrinscestabprest'].widget.attrs['required'] = True
        
        self.fields['tpinscestabprest'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2020evtServPrest
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r2010_evtservtom(forms.ModelForm):
    vlrtotalnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrtotalbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2010_evtservtom,self ).__init__(*args,**kwargs)
        
        self.fields['indcprb'].widget.attrs['required'] = True
        
        self.fields['vlrtotalretprinc'].widget.attrs['required'] = True
        
        self.fields['vlrtotalbaseret'].widget.attrs['required'] = True
        
        self.fields['vlrtotalbruto'].widget.attrs['required'] = True
        
        self.fields['cnpjprestador'].widget.attrs['required'] = True
        
        self.fields['indobra'].widget.attrs['required'] = True
        
        self.fields['nrinscestab'].widget.attrs['required'] = True
        
        self.fields['tpinscestab'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['perapur'].widget.attrs['required'] = True
        
        self.fields['indretif'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r2010evtServTom
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r1070_evttabprocesso(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1070_evttabprocesso,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r1070evtTabProcesso
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]


class form_r1000_evtinfocontri(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r1000_evtinfocontri,self ).__init__(*args,**kwargs)
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        
        self.fields['verproc'].widget.attrs['required'] = True
        
        self.fields['procemi'].widget.attrs['required'] = True
        
        self.fields['tpamb'].widget.attrs['required'] = True
        
        self.fields['identidade'].widget.attrs['readonly'] = True
        
        self.fields['operacao'].widget.attrs['required'] = True
        
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['transmissor_lote_efdreinf'].queryset = TransmissorLoteEfdreinf.objects.using( slug ).filter(excluido=False).all()
        self.fields['transmissor_lote_efdreinf'].widget.attrs['readonly'] = True
        
        self.fields['versao'].widget.attrs['readonly'] = True

    class Meta:
        model = r1000evtInfoContri
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
            'dhprocess',
            'descretorno',
            'cdretorno',
            'arquivo',
            'arquivo_original',
            'validacoes',
            'validacao_precedencia',
            'ocorrencias',
            'retornos_evttotalcontrib',
            'retornos_evttotal',
 
        ]

