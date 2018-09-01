# coding: utf-8
from django import forms
from emensageriapro.s2250.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2250evtAvPrevio 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2250_cancavprevio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2250_cancavprevio,self ).__init__(*args,**kwargs)
        
        self.fields['mtvcancavprevio'].widget.attrs['required'] = True
        
        self.fields['dtcancavprv'].widget.attrs['required'] = True
        
        self.fields['s2250_evtavprevio'].widget.attrs['required'] = True

    class Meta:
        model = s2250cancAvPrevio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2250_detavprevio(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2250_detavprevio,self ).__init__(*args,**kwargs)
        
        self.fields['tpavprevio'].widget.attrs['required'] = True
        
        self.fields['dtprevdeslig'].widget.attrs['required'] = True
        
        self.fields['dtavprv'].widget.attrs['required'] = True
        
        self.fields['s2250_evtavprevio'].widget.attrs['required'] = True

    class Meta:
        model = s2250detAvPrevio
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

