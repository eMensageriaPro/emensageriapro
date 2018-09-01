# coding: utf-8
from django import forms
from emensageriapro.s1260.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1260evtComProd 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1260_infoprocjud(forms.ModelForm):
    vrsenarsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpsusp = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_infoprocjud,self ).__init__(*args,**kwargs)
        
        self.fields['codsusp'].widget.attrs['required'] = True
        
        self.fields['nrproc'].widget.attrs['required'] = True
        
        self.fields['tpproc'].widget.attrs['required'] = True
        self.fields['s1260_tpcomerc'].queryset = s1260tpComerc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_tpcomerc'].widget.attrs['required'] = True

    class Meta:
        model = s1260infoProcJud
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1260_nfs(forms.ModelForm):
    vrsenardesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrratdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrcpdescpr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vlrbruto = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_nfs,self ).__init__(*args,**kwargs)
        
        self.fields['vrsenardesc'].widget.attrs['required'] = True
        
        self.fields['vrratdescpr'].widget.attrs['required'] = True
        
        self.fields['vrcpdescpr'].widget.attrs['required'] = True
        
        self.fields['vlrbruto'].widget.attrs['required'] = True
        
        self.fields['dtemisnf'].widget.attrs['required'] = True
        
        self.fields['nrdocto'].widget.attrs['required'] = True
        self.fields['s1260_ideadquir'].queryset = s1260ideAdquir.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_ideadquir'].widget.attrs['required'] = True

    class Meta:
        model = s1260nfs
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1260_ideadquir(forms.ModelForm):
    vrcomerc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_ideadquir,self ).__init__(*args,**kwargs)
        
        self.fields['vrcomerc'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s1260_tpcomerc'].queryset = s1260tpComerc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_tpcomerc'].widget.attrs['required'] = True

    class Meta:
        model = s1260ideAdquir
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1260_tpcomerc(forms.ModelForm):
    vrtotcom = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1260_tpcomerc,self ).__init__(*args,**kwargs)
        
        self.fields['vrtotcom'].widget.attrs['required'] = True
        
        self.fields['indcomerc'].widget.attrs['required'] = True
        self.fields['s1260_evtcomprod'].queryset = s1260evtComProd.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1260_evtcomprod'].widget.attrs['required'] = True

    class Meta:
        model = s1260tpComerc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

