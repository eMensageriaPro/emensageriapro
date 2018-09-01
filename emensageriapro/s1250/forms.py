# coding: utf-8
from django import forms
from emensageriapro.s1250.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1250evtAqProd 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1250_infoprocjud(forms.ModelForm):
    vrsenarnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpnret = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_infoprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['vrsenarnret'].widget.attrs['required'] = True
        
        self.fields['vrratnret'].widget.attrs['required'] = True
        
        self.fields['vrcpnret'].widget.attrs['required'] = True
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        self.fields['s1250_ideprodutor'].queryset = s1250ideProdutor.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_ideprodutor'].widget.attrs['required'] = True

    class Meta:
        model = s1250infoProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1250_nfs(forms.ModelForm):
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_nfs,self ).__init__(*args,**kwargs)
        
        self.fields['vrsenardesc'].widget.attrs['required'] = True
        
        self.fields['vrratdescpr'].widget.attrs['required'] = True
        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['dtemisnf'].widget.attrs['required'] = True
        
        self.fields['nrdocto'].widget.attrs['required'] = True
        self.fields['s1250_ideprodutor'].queryset = s1250ideProdutor.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_ideprodutor'].widget.attrs['required'] = True

    class Meta:
        model = s1250nfs
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1250_ideprodutor(forms.ModelForm):
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_ideprodutor,self ).__init__(*args,**kwargs)
        
        self.fields['vrsenardesc'].widget.attrs['required'] = True
        
        self.fields['vrratdescpr'].widget.attrs['required'] = True
        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['nrinscprod'].widget.attrs['required'] = True
        
        self.fields['tpinscprod'].widget.attrs['required'] = True
        self.fields['s1250_tpaquis'].queryset = s1250tpAquis.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_tpaquis'].widget.attrs['required'] = True

    class Meta:
        model = s1250ideProdutor
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1250_tpaquis(forms.ModelForm):
    vlrtotaquis = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1250_tpaquis,self ).__init__(*args,**kwargs)
        
        self.fields['vlrtotaquis'].widget.attrs['required'] = True
        
        self.fields['indaquis'].widget.attrs['required'] = True
        self.fields['s1250_evtaqprod'].queryset = s1250evtAqProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1250_evtaqprod'].widget.attrs['required'] = True

    class Meta:
        model = s1250tpAquis
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

