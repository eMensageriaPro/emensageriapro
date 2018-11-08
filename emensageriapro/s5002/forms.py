# coding: utf-8
from django import forms
from emensageriapro.s5002.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.tabelas.models import eSocialTrabalhadoresCategorias 
from emensageriapro.esocial.models import s5002evtIrrfBenef 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s5002_idepgtoext(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_idepgtoext,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['indnif'].widget.attrs['required'] = True
        
        self.fields['codpais'].widget.attrs['required'] = True
        
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002idePgtoExt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5002_irrf(forms.ModelForm):
    vrirrfdesc = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_irrf,self ).__init__(*args,**kwargs)
        
        self.fields['vrirrfdesc'].widget.attrs['required'] = True
        
        self.fields['tpcr'].widget.attrs['required'] = True
        self.fields['s5002_infoirrf'].queryset = s5002infoIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002irrf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5002_basesirrf(forms.ModelForm):
    valor = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_basesirrf,self ).__init__(*args,**kwargs)
        
        self.fields['valor'].widget.attrs['required'] = True
        
        self.fields['tpvalor'].widget.attrs['required'] = True
        self.fields['s5002_infoirrf'].queryset = s5002infoIrrf.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_infoirrf'].widget.attrs['required'] = True

    class Meta:
        model = s5002basesIrrf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5002_infoirrf(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_infoirrf,self ).__init__(*args,**kwargs)
        
        self.fields['indresbr'].widget.attrs['required'] = True
        self.fields['s5002_evtirrfbenef'].queryset = s5002evtIrrfBenef.objects.using( slug ).filter(excluido=False).all()
        self.fields['s5002_evtirrfbenef'].widget.attrs['required'] = True

    class Meta:
        model = s5002infoIrrf
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s5002_infodep(forms.ModelForm):
    vrdeddep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s5002_infodep,self ).__init__(*args,**kwargs)
        
        self.fields['vrdeddep'].widget.attrs['required'] = True
        
        self.fields['s5002_evtirrfbenef'].widget.attrs['required'] = True

    class Meta:
        model = s5002infoDep
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

