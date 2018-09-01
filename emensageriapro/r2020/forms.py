# coding: utf-8
from django import forms
from emensageriapro.r2020.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.efdreinf.models import r2020evtServPrest 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_r2020_infoprocretad(forms.ModelForm):
    valoradic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infoprocretad,self ).__init__(*args,**kwargs)
        
        self.fields['valoradic'].widget.attrs['required'] = True
        
        self.fields['nrprocretadic'].widget.attrs['required'] = True
        
        self.fields['tpprocretadic'].widget.attrs['required'] = True
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoProcRetAd
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2020_infoprocretpr(forms.ModelForm):
    valorprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infoprocretpr,self ).__init__(*args,**kwargs)
        
        self.fields['valorprinc'].widget.attrs['required'] = True
        
        self.fields['nrprocretprinc'].widget.attrs['required'] = True
        
        self.fields['tpprocretprinc'].widget.attrs['required'] = True
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoProcRetPr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2020_infotpserv(forms.ModelForm):
    vlrnretadic = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlradicional = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos25 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos20 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrservicos15 = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrnretprinc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretsub = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrretencao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbaseret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_infotpserv,self ).__init__(*args,**kwargs)
        
        self.fields['vlrretencao'].widget.attrs['required'] = True
        
        self.fields['vlrbaseret'].widget.attrs['required'] = True
        
        self.fields['tpservico'].widget.attrs['required'] = True
        self.fields['r2020_nfs'].queryset = r2020nfs.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_nfs'].widget.attrs['required'] = True

    class Meta:
        model = r2020infoTpServ
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_r2020_nfs(forms.ModelForm):
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_r2020_nfs,self ).__init__(*args,**kwargs)
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['dtemissaonf'].widget.attrs['required'] = True
        
        self.fields['numdocto'].widget.attrs['required'] = True
        
        self.fields['serie'].widget.attrs['required'] = True
        self.fields['r2020_evtservprest'].queryset = r2020evtServPrest.objects.using( slug ).filter(excluido=False).all()
        self.fields['r2020_evtservprest'].widget.attrs['required'] = True

    class Meta:
        model = r2020nfs
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

