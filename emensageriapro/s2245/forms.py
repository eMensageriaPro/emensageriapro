# coding: utf-8
from django import forms
from emensageriapro.s2245.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2245evtTreiCap 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2245_ideprofresp(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2245_ideprofresp,self ).__init__(*args,**kwargs)
        
        self.fields['codcbo'].widget.attrs['required'] = True
        
        self.fields['formprof'].widget.attrs['required'] = True
        
        self.fields['tpprof'].widget.attrs['required'] = True
        
        self.fields['nmprof'].widget.attrs['required'] = True
        
        self.fields['cpfprof'].widget.attrs['required'] = True
        self.fields['s2245_infocomplem'].queryset = s2245infoComplem.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2245_infocomplem'].widget.attrs['required'] = True

    class Meta:
        model = s2245ideProfResp
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2245_infocomplem(forms.ModelForm):
    durtreicap = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2245_infocomplem,self ).__init__(*args,**kwargs)
        
        self.fields['tptreicap'].widget.attrs['required'] = True
        
        self.fields['modtreicap'].widget.attrs['required'] = True
        
        self.fields['durtreicap'].widget.attrs['required'] = True
        
        self.fields['dttreicap'].widget.attrs['required'] = True
        
        self.fields['s2245_evttreicap'].widget.attrs['required'] = True

    class Meta:
        model = s2245infoComplem
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

