# coding: utf-8
from django import forms
from emensageriapro.s5012.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s5012evtIrrf 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s5012_infocrcontrib(forms.ModelForm):
    vrcr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5012_infocrcontrib,self ).__init__(*args,**kwargs)
        
        self.fields['vrcr'].widget.attrs['required'] = True
        
        self.fields['tpcr'].widget.attrs['required'] = True
        self.fields['s5012_evtirrf'].queryset = s5012evtIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5012_evtirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5012infoCRContrib
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

