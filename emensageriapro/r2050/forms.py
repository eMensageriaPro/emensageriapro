# coding: utf-8
from django import forms
from emensageriapro.r2050.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2050evtComProd 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2050_infoproc(forms.ModelForm):
    vlrsenarsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrratsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2050_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r2050_tipocom'].queryset = r2050tipoCom.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2050_tipocom'].widget.attrs['required'] = True

    class Meta:
        model = r2050infoProc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2050_tipocom(forms.ModelForm):
    vlrrecbruta = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2050_tipocom,self ).__init__(*args,**kwargs)
        
        self.fields['vlrrecbruta'].widget.attrs['required'] = True
        
        self.fields['indcom'].widget.attrs['required'] = True
        self.fields['r2050_evtcomprod'].queryset = r2050evtComProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2050_evtcomprod'].widget.attrs['required'] = True

    class Meta:
        model = r2050tipoCom
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

