# coding: utf-8
from django import forms
from emensageriapro.s5013.models import * 
from emensageriapro.esocial.models import s5013evtFGTS 


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



class form_s5013_baseperante(forms.ModelForm):
    basefgtse = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_baseperante,self ).__init__(*args,**kwargs)
        self.fields['s5013_infobaseperante'].queryset = s5013infoBasePerAntE.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_infobaseperante'].widget.attrs['required'] = True
        
        self.fields['tpvalore'].widget.attrs['required'] = True
        
        self.fields['basefgtse'].widget.attrs['required'] = True

    class Meta:
        model = s5013basePerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5013_baseperapur(forms.ModelForm):
    basefgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_baseperapur,self ).__init__(*args,**kwargs)
        self.fields['s5013_evtfgts'].queryset = s5013evtFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_evtfgts'].widget.attrs['required'] = True
        
        self.fields['tpvalor'].widget.attrs['required'] = True
        
        self.fields['basefgts'].widget.attrs['required'] = True

    class Meta:
        model = s5013basePerApur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5013_dpsperante(forms.ModelForm):
    vrfgtse = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_dpsperante,self ).__init__(*args,**kwargs)
        self.fields['s5013_infodpsperante'].queryset = s5013infoDpsPerAntE.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_infodpsperante'].widget.attrs['required'] = True
        
        self.fields['tpdpse'].widget.attrs['required'] = True
        
        self.fields['vrfgtse'].widget.attrs['required'] = True

    class Meta:
        model = s5013dpsPerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5013_dpsperapur(forms.ModelForm):
    vrfgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_dpsperapur,self ).__init__(*args,**kwargs)
        self.fields['s5013_evtfgts'].queryset = s5013evtFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_evtfgts'].widget.attrs['required'] = True
        
        self.fields['tpdps'].widget.attrs['required'] = True
        
        self.fields['vrfgts'].widget.attrs['required'] = True

    class Meta:
        model = s5013dpsPerApur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5013_infobaseperante(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_infobaseperante,self ).__init__(*args,**kwargs)
        self.fields['s5013_evtfgts'].queryset = s5013evtFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_evtfgts'].widget.attrs['required'] = True
        
        self.fields['perref'].widget.attrs['required'] = True

    class Meta:
        model = s5013infoBasePerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5013_infodpsperante(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5013_infodpsperante,self ).__init__(*args,**kwargs)
        self.fields['s5013_evtfgts'].queryset = s5013evtFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5013_evtfgts'].widget.attrs['required'] = True
        
        self.fields['perref'].widget.attrs['required'] = True

    class Meta:
        model = s5013infoDpsPerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

