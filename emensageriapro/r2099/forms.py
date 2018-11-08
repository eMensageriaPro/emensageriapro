# coding: utf-8
from django import forms
from emensageriapro.r2099.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2099evtFechaEvPer 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2099_iderespinf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2099_iderespinf,self ).__init__(*args,**kwargs)
        
        self.fields['cpfresp'].widget.attrs['required'] = True
        
        self.fields['nmresp'].widget.attrs['required'] = True
        
        self.fields['r2099_evtfechaevper'].widget.attrs['required'] = True

    class Meta:
        model = r2099ideRespInf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

