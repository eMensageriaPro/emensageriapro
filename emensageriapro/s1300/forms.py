# coding: utf-8
from django import forms
from emensageriapro.s1300.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1300evtContrSindPatr 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1300_contribsind(forms.ModelForm):
    vlrcontribsind = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1300_contribsind,self ).__init__(*args,**kwargs)
        
        self.fields['vlrcontribsind'].widget.attrs['required'] = True
        
        self.fields['tpcontribsind'].widget.attrs['required'] = True
        
        self.fields['cnpjsindic'].widget.attrs['required'] = True
        self.fields['s1300_evtcontrsindpatr'].queryset = s1300evtContrSindPatr.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1300_evtcontrsindpatr'].widget.attrs['required'] = True

    class Meta:
        model = s1300contribSind
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

