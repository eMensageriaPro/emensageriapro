# coding: utf-8
from django import forms
from emensageriapro.r2020.models import * 
from emensageriapro.efdreinf.models import r2020evtServPrest 


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



class form_r2020_infoprocretad(forms.ModelForm):
    valoradic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infoprocretad,self ).__init__(*args,**kwargs)
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True
        
        self.fields['tpprocretadic'].widget.attrs['required'] = True
        
        self.fields['nrprocretadic'].widget.attrs['required'] = True
        
        self.fields['valoradic'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoProcRetAd
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r2020_infoprocretpr(forms.ModelForm):
    valorprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infoprocretpr,self ).__init__(*args,**kwargs)
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True
        
        self.fields['tpprocretprinc'].widget.attrs['required'] = True
        
        self.fields['nrprocretprinc'].widget.attrs['required'] = True
        
        self.fields['valorprinc'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoProcRetPr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r2020_infotpserv(forms.ModelForm):
    vlrbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretencao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretsub = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlradicional = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infotpserv,self ).__init__(*args,**kwargs)
        self.fields['r2020_nfs'].queryset = r2020nfs.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_nfs'].widget.attrs['required'] = True
        
        self.fields['tpservico'].widget.attrs['required'] = True
        
        self.fields['vlrbaseret'].widget.attrs['required'] = True
        
        self.fields['vlrretencao'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoTpServ
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_r2020_nfs(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_nfs,self ).__init__(*args,**kwargs)
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True
        
        self.fields['serie'].widget.attrs['required'] = True
        
        self.fields['numdocto'].widget.attrs['required'] = True
        
        self.fields['dtemissaonf'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True

    class Meta:
        model = r2020nfs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

