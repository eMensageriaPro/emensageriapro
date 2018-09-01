# coding: utf-8
from django import forms
from emensageriapro.s2240.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2240evtExpRisco 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2240_fimexprisco_respreg(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco_respreg,self ).__init__(*args,**kwargs)
        
        self.fields['nroc'].widget.attrs['required'] = True
        
        self.fields['nisresp'].widget.attrs['required'] = True
        
        self.fields['dtini'].widget.attrs['required'] = True
        self.fields['s2240_evtexprisco'].queryset = s2240evtExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRiscorespReg
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_fimexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_fimexprisco'].queryset = s2240fimExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_fimexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRiscoinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_fimexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_fimexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimcondicao'].widget.attrs['required'] = True
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240fimExpRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_altexprisco_epi(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_epi,self ).__init__(*args,**kwargs)
        
        self.fields['higienizacao'].widget.attrs['required'] = True
        
        self.fields['periodictroca'].widget.attrs['required'] = True
        
        self.fields['przvalid'].widget.attrs['required'] = True
        
        self.fields['condfuncto'].widget.attrs['required'] = True
        
        self.fields['medprotecao'].widget.attrs['required'] = True
        
        self.fields['eficepi'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_fatrisco'].queryset = s2240altExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoepi
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_altexprisco_epc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_epc,self ).__init__(*args,**kwargs)
        
        self.fields['dscepc'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_fatrisco'].queryset = s2240altExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoepc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_altexprisco_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['utilizepi'].widget.attrs['required'] = True
        
        self.fields['utilizepc'].widget.attrs['required'] = True
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco_infoamb'].queryset = s2240altExpRiscoinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscofatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_altexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['dscativdes'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_altexprisco'].queryset = s2240altExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_altexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRiscoinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_altexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_altexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dtaltcondicao'].widget.attrs['required'] = True
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240altExpRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_iniexprisco_epi(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_epi,self ).__init__(*args,**kwargs)
        
        self.fields['higienizacao'].widget.attrs['required'] = True
        
        self.fields['periodictroca'].widget.attrs['required'] = True
        
        self.fields['przvalid'].widget.attrs['required'] = True
        
        self.fields['condfuncto'].widget.attrs['required'] = True
        
        self.fields['medprotecao'].widget.attrs['required'] = True
        
        self.fields['eficepi'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco_fatrisco'].queryset = s2240iniExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoepi
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_iniexprisco_epc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_epc,self ).__init__(*args,**kwargs)
        
        self.fields['dscepc'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco_fatrisco'].queryset = s2240iniExpRiscofatRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco_fatrisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoepc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_iniexprisco_fatrisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_fatrisco,self ).__init__(*args,**kwargs)
        
        self.fields['utilizepi'].widget.attrs['required'] = True
        
        self.fields['utilizepc'].widget.attrs['required'] = True
        
        self.fields['codfatris'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco_infoamb'].queryset = s2240iniExpRiscoinfoAmb.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco_infoamb'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscofatRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_iniexprisco_infoamb(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco_infoamb,self ).__init__(*args,**kwargs)
        
        self.fields['dscativdes'].widget.attrs['required'] = True
        
        self.fields['codamb'].widget.attrs['required'] = True
        self.fields['s2240_iniexprisco'].queryset = s2240iniExpRisco.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2240_iniexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRiscoinfoAmb
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2240_iniexprisco(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2240_iniexprisco,self ).__init__(*args,**kwargs)
        
        self.fields['dtinicondicao'].widget.attrs['required'] = True
        
        self.fields['s2240_evtexprisco'].widget.attrs['required'] = True

    class Meta:
        model = s2240iniExpRisco
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]

