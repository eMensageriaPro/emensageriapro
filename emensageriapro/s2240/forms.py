# coding: utf-8
from django import forms
from emensageriapro.s2240.models import * 
from emensageriapro.tabelas.models import eSocialFatoresRisco 
from emensageriapro.esocial.models import s2240evtExpRisco 


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



class form_s2240_iniexprisco_respreg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_respreg,self ).__init__(*args,**kwargs)
        
        self.fields['ufoc'].widget.attrs['required'] = True
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['ideoc'].widget.attrs['required'] = True
        
        self.fields['nmresp'].widget.attrs['required'] = True
        
        self.fields['nisresp'].widget.attrs['required'] = True
        
        self.fields['cpfresp'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscorespReg
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_obs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_obs,self ).__init__(*args,**kwargs)
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoobs
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_fatrisco(forms.ModelForm):
    limtol = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    intconc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['utilizepi'].widget.attrs['required'] = True
        
        self.fields['utilizepc'].widget.attrs['required'] = True
        
        self.fields['tpaval'].widget.attrs['required'] = True
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscofatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_epi(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_epi,self ).__init__(*args,**kwargs)
        
        self.fields['higienizacao'].widget.attrs['required'] = True
        
        self.fields['periodictroca'].widget.attrs['required'] = True
        
        self.fields['przvalid'].widget.attrs['required'] = True
        
        self.fields['usoinint'].widget.attrs['required'] = True
        
        self.fields['condfuncto'].widget.attrs['required'] = True
        
        self.fields['medprotecao'].widget.attrs['required'] = True
        
        self.fields['eficepi'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco_fatrisco'].queryset = s2240iniExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoepi
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_epc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_epc,self ).__init__(*args,**kwargs)
        
        self.fields['dscepc'].widget.attrs['required'] = True
        
        self.fields['codep'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco_fatrisco'].queryset = s2240iniExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoepc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_iniexprisco_ativpericinsal(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_ativpericinsal,self ).__init__(*args,**kwargs)
        
        self.fields['codativ'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoativPericInsal
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_fimexprisco_respreg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco_respreg,self ).__init__(*args,**kwargs)
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['nisresp'].widget.attrs['required'] = True
        
        self.fields['dtini'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRiscorespReg
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_fimexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_fimexprisco'].queryset = s2240fimExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_fimexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRiscoinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_fimexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_altexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['dscativdes'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco'].queryset = s2240altExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoinfoAmb
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_altexprisco_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['utilizepi'].widget.attrs['required'] = True
        
        self.fields['utilizepc'].widget.attrs['required'] = True
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_infoamb'].queryset = s2240altExpRiscoinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscofatRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_altexprisco_epi(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_epi,self ).__init__(*args,**kwargs)
        
        self.fields['higienizacao'].widget.attrs['required'] = True
        
        self.fields['periodictroca'].widget.attrs['required'] = True
        
        self.fields['przvalid'].widget.attrs['required'] = True
        
        self.fields['condfuncto'].widget.attrs['required'] = True
        
        self.fields['medprotecao'].widget.attrs['required'] = True
        
        self.fields['eficepi'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_fatrisco'].queryset = s2240altExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoepi
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_altexprisco_epc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_epc,self ).__init__(*args,**kwargs)
        
        self.fields['dscepc'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_fatrisco'].queryset = s2240altExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoepc
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]


class form_s2240_altexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRisco
        exclude = [ 
            'criado_em', 'criado_por',
            'modificado_em', 'modificado_por',
            'excluido',
 
        ]

