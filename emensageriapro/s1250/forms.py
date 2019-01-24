# coding: utf-8
from django import forms
from emensageriapro.s1250.models import * 
from emensageriapro.esocial.models import s1250evtAqProd 


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




class form_s1250_ideprodutor(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1250_ideprodutor, self).__init__(*args,**kwargs)
        
        self.fields['s1250_tpaquis'].queryset = s1250tpAquis.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_tpaquis'].widget.attrs['required'] = True        
        self.fields['tpinscprod'].widget.attrs['required'] = True        
        self.fields['nrinscprod'].widget.attrs['required'] = True        
        self.fields['vlrbruto'].widget.attrs['required'] = True        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True        
        self.fields['vrratdescpr'].widget.attrs['required'] = True        
        self.fields['vrsenardesc'].widget.attrs['required'] = True        
        self.fields['indopccp'].widget.attrs['required'] = True
        
    class Meta:
        model = s1250ideProdutor
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1250_infoprocj(forms.ModelForm):
    vrcpnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1250_infoprocj, self).__init__(*args,**kwargs)
        
        self.fields['s1250_tpaquis'].queryset = s1250tpAquis.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_tpaquis'].widget.attrs['required'] = True        
        self.fields['nrprocjud'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True        
        self.fields['vrcpnret'].widget.attrs['required'] = True        
        self.fields['vrratnret'].widget.attrs['required'] = True        
        self.fields['vrsenarnret'].widget.attrs['required'] = True
        
    class Meta:
        model = s1250infoProcJ
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1250_infoprocjud(forms.ModelForm):
    vrcpnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenarnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1250_infoprocjud, self).__init__(*args,**kwargs)
        
        self.fields['s1250_ideprodutor'].queryset = s1250ideProdutor.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_ideprodutor'].widget.attrs['required'] = True        
        self.fields['nrprocjud'].widget.attrs['required'] = True        
        self.fields['codsusp'].widget.attrs['required'] = True        
        self.fields['vrcpnret'].widget.attrs['required'] = True        
        self.fields['vrratnret'].widget.attrs['required'] = True        
        self.fields['vrsenarnret'].widget.attrs['required'] = True
        
    class Meta:
        model = s1250infoProcJud
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1250_nfs(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1250_nfs, self).__init__(*args,**kwargs)
        
        self.fields['s1250_ideprodutor'].queryset = s1250ideProdutor.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_ideprodutor'].widget.attrs['required'] = True        
        self.fields['nrdocto'].widget.attrs['required'] = True        
        self.fields['dtemisnf'].widget.attrs['required'] = True        
        self.fields['vlrbruto'].widget.attrs['required'] = True        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True        
        self.fields['vrratdescpr'].widget.attrs['required'] = True        
        self.fields['vrsenardesc'].widget.attrs['required'] = True
        
    class Meta:
        model = s1250nfs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]



class form_s1250_tpaquis(forms.ModelForm):
    vlrtotaquis = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super(form_s1250_tpaquis, self).__init__(*args,**kwargs)
        
        self.fields['s1250_evtaqprod'].queryset = s1250evtAqProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_evtaqprod'].widget.attrs['required'] = True        
        self.fields['indaquis'].widget.attrs['required'] = True        
        self.fields['vlrtotaquis'].widget.attrs['required'] = True
        
    class Meta:
        model = s1250tpAquis
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

