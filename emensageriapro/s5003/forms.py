# coding: utf-8
from django import forms
from emensageriapro.s5003.models import * 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s5003evtBasesFGTS 


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



class form_s5003_infotrabfgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_infotrabfgts,self ).__init__(*args,**kwargs)
        
        self.fields['mtvdesligtsv'].widget.attrs['required'] = True
        
        self.fields['dtterm'].widget.attrs['required'] = True
        
        self.fields['mtvdeslig'].widget.attrs['required'] = True
        
        self.fields['dtinicio'].widget.attrs['required'] = True
        
        self.fields['dtdeslig'].widget.attrs['required'] = True
        
        self.fields['dtadm'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        self.fields['s5003_ideestablot'].queryset = s5003ideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s5003infoTrabFGTS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_infotrabdps(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_infotrabdps,self ).__init__(*args,**kwargs)
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['matricula'].widget.attrs['required'] = True
        self.fields['s5003_infofgts'].queryset = s5003infoFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infofgts'].widget.attrs['required'] = True

    class Meta:
        model = s5003infoTrabDps
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_infofgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_infofgts,self ).__init__(*args,**kwargs)
        
        self.fields['dtvenc'].widget.attrs['required'] = True
        
        self.fields['s5003_evtbasesfgts'].widget.attrs['required'] = True

    class Meta:
        model = s5003infoFGTS
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_infodpsperante(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_infodpsperante,self ).__init__(*args,**kwargs)
        
        self.fields['perref'].widget.attrs['required'] = True
        self.fields['s5003_infotrabdps'].queryset = s5003infoTrabDps.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infotrabdps'].widget.attrs['required'] = True

    class Meta:
        model = s5003infoDpsPerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_infobaseperante(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_infobaseperante,self ).__init__(*args,**kwargs)
        
        self.fields['perref'].widget.attrs['required'] = True
        self.fields['s5003_infotrabfgts'].queryset = s5003infoTrabFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infotrabfgts'].widget.attrs['required'] = True

    class Meta:
        model = s5003infoBasePerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s5003_infofgts'].queryset = s5003infoFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infofgts'].widget.attrs['required'] = True

    class Meta:
        model = s5003ideEstabLot
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_dpsperapur(forms.ModelForm):
    dpsfgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_dpsperapur,self ).__init__(*args,**kwargs)
        
        self.fields['dpsfgts'].widget.attrs['required'] = True
        
        self.fields['tpdps'].widget.attrs['required'] = True
        self.fields['s5003_infotrabdps'].queryset = s5003infoTrabDps.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infotrabdps'].widget.attrs['required'] = True

    class Meta:
        model = s5003dpsPerApur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_dpsperante(forms.ModelForm):
    dpsfgtse = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_dpsperante,self ).__init__(*args,**kwargs)
        
        self.fields['dpsfgtse'].widget.attrs['required'] = True
        
        self.fields['tpdpse'].widget.attrs['required'] = True
        self.fields['s5003_infodpsperante'].queryset = s5003infoDpsPerAntE.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infodpsperante'].widget.attrs['required'] = True

    class Meta:
        model = s5003dpsPerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_baseperapur(forms.ModelForm):
    remfgts = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_baseperapur,self ).__init__(*args,**kwargs)
        
        self.fields['remfgts'].widget.attrs['required'] = True
        
        self.fields['tpvalor'].widget.attrs['required'] = True
        self.fields['s5003_infotrabfgts'].queryset = s5003infoTrabFGTS.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infotrabfgts'].widget.attrs['required'] = True

    class Meta:
        model = s5003basePerApur
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s5003_baseperante(forms.ModelForm):
    remfgtse = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5003_baseperante,self ).__init__(*args,**kwargs)
        
        self.fields['remfgtse'].widget.attrs['required'] = True
        
        self.fields['tpvalore'].widget.attrs['required'] = True
        self.fields['s5003_infobaseperante'].queryset = s5003infoBasePerAntE.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5003_infobaseperante'].widget.attrs['required'] = True

    class Meta:
        model = s5003basePerAntE
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

