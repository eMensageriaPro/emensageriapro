# coding: utf-8
from django import forms
from emensageriapro.r2060.models import * 
from emensageriapro.efdreinf.models import r2060evtCPRB 


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




class form_r2060_infoproc(forms.ModelForm):
    vlrcprbsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2060_infoproc, self).__init__(*args,**kwargs)
        
        self.fields['r2060_tipocod'].queryset = r2060tipoCod.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_tipocod'].widget.attrs['required'] = True        
        self.fields['tpproc'].widget.attrs['required'] = True        
        self.fields['nrproc'].widget.attrs['required'] = True        
        self.fields['vlrcprbsusp'].widget.attrs['required'] = True
        
    class Meta:
        model = r2060infoProc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r2060_tipoajuste(forms.ModelForm):
    vlrajuste = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2060_tipoajuste, self).__init__(*args,**kwargs)
        
        self.fields['r2060_tipocod'].queryset = r2060tipoCod.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_tipocod'].widget.attrs['required'] = True        
        self.fields['tpajuste'].widget.attrs['required'] = True        
        self.fields['codajuste'].widget.attrs['required'] = True        
        self.fields['vlrajuste'].widget.attrs['required'] = True        
        self.fields['descajuste'].widget.attrs['required'] = True        
        self.fields['dtajuste'].widget.attrs['required'] = True
        
    class Meta:
        model = r2060tipoAjuste
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_r2060_tipocod(forms.ModelForm):
    vlrrecbrutaativ = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrexcrecbruta = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlradicrecbruta = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbccprb = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcprbapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_r2060_tipocod, self).__init__(*args,**kwargs)
        
        self.fields['r2060_evtcprb'].queryset = r2060evtCPRB.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_evtcprb'].widget.attrs['required'] = True        
        self.fields['codativecon'].widget.attrs['required'] = True        
        self.fields['vlrrecbrutaativ'].widget.attrs['required'] = True        
        self.fields['vlrexcrecbruta'].widget.attrs['required'] = True        
        self.fields['vlradicrecbruta'].widget.attrs['required'] = True        
        self.fields['vlrbccprb'].widget.attrs['required'] = True
        
    class Meta:
        model = r2060tipoCod
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

