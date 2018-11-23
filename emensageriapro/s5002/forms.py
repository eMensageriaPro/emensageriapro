# coding: utf-8
from django import forms
from emensageriapro.s5002.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s5002evtIrrfBenef 


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



class form_s5002_irrf(forms.ModelForm):
    vrirrfdesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_irrf,self ).__init__(*args,**kwargs)
        
        self.fields['vrirrfdesc'].widget.attrs['required'] = True
        
        self.fields['tpcr'].widget.attrs['required'] = True
        self.fields['s5002_infoirrf'].queryset = s5002infoIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002irrf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5002_infoirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_infoirrf,self ).__init__(*args,**kwargs)
        
        self.fields['indresbr'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        self.fields['s5002_evtirrfbenef'].queryset = s5002evtIrrfBenef.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_evtirrfbenef'].widget.attrs['required'] = True

    class Meta:
        model = s5002infoIrrf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5002_infodep(forms.ModelForm):
    vrdeddep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_infodep,self ).__init__(*args,**kwargs)
        
        self.fields['vrdeddep'].widget.attrs['required'] = True
        
        self.fields['s5002_evtirrfbenef'].widget.attrs['required'] = True

    class Meta:
        model = s5002infoDep
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5002_idepgtoext(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_idepgtoext,self ).__init__(*args,**kwargs)
        
        self.fields['codpostal'].widget.attrs['required'] = True
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['bairro'].widget.attrs['required'] = True
        
        self.fields['complem'].widget.attrs['required'] = True
        
        self.fields['nrlograd'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['nifbenef'].widget.attrs['required'] = True
        
        self.fields['indnif'].widget.attrs['required'] = True
        
        self.fields['codpais'].widget.attrs['required'] = True
        
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002idePgtoExt
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5002_basesirrf(forms.ModelForm):
    valor = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_basesirrf,self ).__init__(*args,**kwargs)
        
        self.fields['valor'].widget.attrs['required'] = True
        
        self.fields['tpvalor'].widget.attrs['required'] = True
        self.fields['s5002_infoirrf'].queryset = s5002infoIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002basesIrrf
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

