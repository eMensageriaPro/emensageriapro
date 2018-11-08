# coding: utf-8
from django import forms
from emensageriapro.s1295.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1295evtTotConting 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1295_iderespinf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1295_iderespinf,self ).__init__(*args,**kwargs)
        
        self.fields['telefone'].widget.attrs['required'] = True
        
        self.fields['cpfresp'].widget.attrs['required'] = True
        
        self.fields['nmresp'].widget.attrs['required'] = True
        
        self.fields['s1295_evttotconting'].widget.attrs['required'] = True

    class Meta:
        model = s1295ideRespInf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

