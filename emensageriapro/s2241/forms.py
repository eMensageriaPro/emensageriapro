# coding: utf-8
from django import forms
from emensageriapro.s2241.models import * 
from emensageriapro.tabelas.models import eSocialFatoresRisco 
from emensageriapro.esocial.models import s2241evtInsApo 


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



class form_s2241_iniinsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_iniinsalperic'].queryset = s2241iniInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniinsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPericinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_iniinsalperic_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_iniinsalperic_infoamb'].queryset = s2241iniInsalPericinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniinsalperic_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPericfatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_iniinsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniinsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniInsalPeric
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_iniaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_iniaposentesp'].queryset = s2241iniAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEspinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_iniaposentesp_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_iniaposentesp_infoamb'].queryset = s2241iniAposentEspinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_iniaposentesp_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEspfatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_iniaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_iniaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241iniAposentEsp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_fiminsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fiminsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_fiminsalperic'].queryset = s2241fimInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_fiminsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimInsalPericinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_fiminsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fiminsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimInsalPeric
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_fimaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fimaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_fimaposentesp'].queryset = s2241fimAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_fimaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimAposentEspinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_fimaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_fimaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241fimAposentEsp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altinsalperic_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_altinsalperic'].queryset = s2241altInsalPeric.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altinsalperic'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPericinfoamb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altinsalperic_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_altinsalperic_infoamb'].queryset = s2241altInsalPericinfoamb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altinsalperic_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPericfatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altinsalperic(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altinsalperic,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241altInsalPeric
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altaposentesp_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2241_altaposentesp'].queryset = s2241altAposentEsp.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altaposentesp'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEspinfoamb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altaposentesp_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2241_altaposentesp_infoamb'].queryset = s2241altAposentEspinfoamb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2241_altaposentesp_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEspfatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2241_altaposentesp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2241_altaposentesp,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2241_evtinsapo'].widget.attrs['required'] = True

    class Meta:
        model = s2241altAposentEsp
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

