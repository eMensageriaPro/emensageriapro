# coding: utf-8
from django import forms
from emensageriapro.s1280.models import * 
from emensageriapro.esocial.models import s1280evtInfoComplPer 


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



class form_s1280_infoativconcom(forms.ModelForm):
    fatormes = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fator13 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infoativconcom,self ).__init__(*args,**kwargs)
        
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['fatormes'].widget.attrs['required'] = True
        
        self.fields['fator13'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoAtivConcom
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1280_infosubstpatr(forms.ModelForm):
    percredcontrib = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infosubstpatr,self ).__init__(*args,**kwargs)
        
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['indsubstpatr'].widget.attrs['required'] = True
        
        self.fields['percredcontrib'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoSubstPatr
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s1280_infosubstpatropport(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1280_infosubstpatropport,self ).__init__(*args,**kwargs)
        self.fields['s1280_evtinfocomplper'].queryset = s1280evtInfoComplPer.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1280_evtinfocomplper'].widget.attrs['required'] = True
        
        self.fields['cnpjopportuario'].widget.attrs['required'] = True

    class Meta:
        model = s1280infoSubstPatrOpPort
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

