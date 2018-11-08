# coding: utf-8
from django import forms
from emensageriapro.s2410.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2410evtCdBenIn 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2410_homologtc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2410_homologtc,self ).__init__(*args,**kwargs)
        
        self.fields['nratolegal'].widget.attrs['required'] = True
        
        self.fields['dthomol'].widget.attrs['required'] = True
        
        self.fields['s2410_evtcdbenin'].widget.attrs['required'] = True

    class Meta:
        model = s2410homologTC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2410_instpenmorte(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2410_instpenmorte,self ).__init__(*args,**kwargs)
        
        self.fields['intaposentado'].widget.attrs['required'] = True
        
        self.fields['dtinst'].widget.attrs['required'] = True
        
        self.fields['cpfinst'].widget.attrs['required'] = True
        
        self.fields['s2410_infopenmorte'].widget.attrs['required'] = True

    class Meta:
        model = s2410instPenMorte
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2410_infopenmorte(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2410_infopenmorte,self ).__init__(*args,**kwargs)
        
        self.fields['tppenmorte'].widget.attrs['required'] = True
        
        self.fields['s2410_evtcdbenin'].widget.attrs['required'] = True

    class Meta:
        model = s2410infoPenMorte
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

