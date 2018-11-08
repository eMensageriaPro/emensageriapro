# coding: utf-8
from django import forms
from emensageriapro.s1299.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1299evtFechaEvPer 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1299_iderespinf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1299_iderespinf,self ).__init__(*args,**kwargs)
        
        self.fields['telefone'].widget.attrs['required'] = True
        
        self.fields['cpfresp'].widget.attrs['required'] = True
        
        self.fields['nmresp'].widget.attrs['required'] = True
        
        self.fields['s1299_evtfechaevper'].widget.attrs['required'] = True

    class Meta:
        model = s1299ideRespInf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

