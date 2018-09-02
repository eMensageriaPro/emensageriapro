# coding: utf-8
from django import forms
from emensageriapro.s2400.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import Municipios 
from emensageriapro.esocial.models import s2400evtCdBenPrRP 


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



class form_s2400_fimbeneficio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_fimbeneficio,self ).__init__(*args,**kwargs)
        
        self.fields['mtvfim'].widget.attrs['required'] = True
        
        self.fields['dtfimbenef'].widget.attrs['required'] = True
        
        self.fields['nrbenefic'].widget.attrs['required'] = True
        
        self.fields['tpbenef'].widget.attrs['required'] = True
        
        self.fields['s2400_evtcdbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s2400fimBeneficio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_altbeneficio_infopenmorte(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_altbeneficio_infopenmorte,self ).__init__(*args,**kwargs)
        
        self.fields['cpfinst'].widget.attrs['required'] = True
        
        self.fields['idquota'].widget.attrs['required'] = True
        
        self.fields['s2400_altbeneficio'].widget.attrs['required'] = True

    class Meta:
        model = s2400altBeneficioinfoPenMorte
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_altbeneficio(forms.ModelForm):
    vrbenef = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_altbeneficio,self ).__init__(*args,**kwargs)
        
        self.fields['vrbenef'].widget.attrs['required'] = True
        
        self.fields['dtinibenef'].widget.attrs['required'] = True
        
        self.fields['nrbenefic'].widget.attrs['required'] = True
        
        self.fields['tpbenef'].widget.attrs['required'] = True
        
        self.fields['s2400_evtcdbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s2400altBeneficio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_inibeneficio_infopenmorte(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_inibeneficio_infopenmorte,self ).__init__(*args,**kwargs)
        
        self.fields['cpfinst'].widget.attrs['required'] = True
        
        self.fields['idquota'].widget.attrs['required'] = True
        
        self.fields['s2400_inibeneficio'].widget.attrs['required'] = True

    class Meta:
        model = s2400iniBeneficioinfoPenMorte
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_inibeneficio(forms.ModelForm):
    vrbenef = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_inibeneficio,self ).__init__(*args,**kwargs)
        
        self.fields['vrbenef'].widget.attrs['required'] = True
        
        self.fields['dtinibenef'].widget.attrs['required'] = True
        
        self.fields['nrbenefic'].widget.attrs['required'] = True
        
        self.fields['tpbenef'].widget.attrs['required'] = True
        
        self.fields['s2400_evtcdbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s2400iniBeneficio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_exterior(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_exterior,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['paisresid'].widget.attrs['required'] = True
        
        self.fields['s2400_evtcdbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s2400exterior
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2400_brasil(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2400_brasil,self ).__init__(*args,**kwargs)
        
        self.fields['uf'].widget.attrs['required'] = True
        
        self.fields['codmunic'].widget.attrs['required'] = True
        
        self.fields['cep'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['tplograd'].widget.attrs['required'] = True
        
        self.fields['s2400_evtcdbenprrp'].widget.attrs['required'] = True

    class Meta:
        model = s2400brasil
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

