# coding: utf-8
from django import forms
from emensageriapro.r2060.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2060evtCPRB 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2060_infoproc(forms.ModelForm):
    vlrcprbsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2060_infoproc,self ).__init__(*args,**kwargs)
        
        self.fields['vlrcprbsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['r2060_tipocod'].queryset = r2060tipoCod.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_tipocod'].widget.attrs['required'] = True

    class Meta:
        model = r2060infoProc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2060_tipoajuste(forms.ModelForm):
    vlrajuste = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2060_tipoajuste,self ).__init__(*args,**kwargs)
        
        self.fields['dtajuste'].widget.attrs['required'] = True
        
        self.fields['descajuste'].widget.attrs['required'] = True
        
        self.fields['vlrajuste'].widget.attrs['required'] = True
        
        self.fields['codajuste'].widget.attrs['required'] = True
        
        self.fields['tpajuste'].widget.attrs['required'] = True
        self.fields['r2060_tipocod'].queryset = r2060tipoCod.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_tipocod'].widget.attrs['required'] = True

    class Meta:
        model = r2060tipoAjuste
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2060_tipocod(forms.ModelForm):
    vlrcprbapur = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbccprb = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlradicrecbruta = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrexcrecbruta = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrrecbrutaativ = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2060_tipocod,self ).__init__(*args,**kwargs)
        
        self.fields['vlrbccprb'].widget.attrs['required'] = True
        
        self.fields['vlradicrecbruta'].widget.attrs['required'] = True
        
        self.fields['vlrexcrecbruta'].widget.attrs['required'] = True
        
        self.fields['vlrrecbrutaativ'].widget.attrs['required'] = True
        
        self.fields['codativecon'].widget.attrs['required'] = True
        self.fields['r2060_evtcprb'].queryset = r2060evtCPRB.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2060_evtcprb'].widget.attrs['required'] = True

    class Meta:
        model = r2060tipoCod
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

